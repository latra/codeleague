from behave import *

use_step_matcher("parse")


@when(u'I register a submission in competition "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:detail', pk=comp.id))
    print(context.browser.html)
    context.browser.find_by_name('submit_resolution').first.click()
    assert context.browser.url == context.get_url('competition:submit-answer', pk=comp.id)
    for row in context.table:
        desc = row['description']
        github = row['github']
        form = context.browser.find_by_tag('form')
        print("FORM", form)
        frame = form.switch_to.frame("mytextarea_ifr")
        print("FRAME", frame)
        text_area = form.find_element_by_id("mytextarea_ifr")
        text_area.send_keys(desc)
        github_field = form.find_element_by_name("githuburl")
        github_field.type(github, slowly=True)
        context.browser.find_by_name('button_publish').first.click()


@step("there are {count:n} submissions")
def step_impl(context, count):
    """
    :type count: str
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And there are 1 submissions')


@when('I want to create a submission for a competition "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:submit-answer', pk=comp.pk))
