import os
import django
from behave.runner import Context
from django.shortcuts import resolve_url
from django.test.runner import DiscoverRunner
from selenium.webdriver.chrome.options import Options
from django.test.testcases import LiveServerTestCase
from splinter.browser import Browser

os.environ["DJANGO_SETTINGS_MODULE"] = "codeleague.settings"


class ExtendedContext(Context):
    def get_url(self, to=None, *args, **kwargs):
        return self.test.live_server_url + (
            resolve_url(to, *args, **kwargs) if to else '')


def before_all(context):
    chrome_options = Options()
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.browser = Browser('chrome', options=chrome_options)


def before_scenario(context, scenario):
    context.old_db_config = context.test_runner.setup_databases()
    object.__setattr__(context, '__class__', ExtendedContext)
    context.test = LiveServerTestCase
    context.test.setUpClass()


def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test
    context.test_runner.teardown_databases(context.old_db_config)


def after_all(context):
    context.test_runner.teardown_test_environment()
    context.browser.quit()
    context.browser = None
