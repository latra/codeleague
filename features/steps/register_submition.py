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
    context.browser.find_by_name('submit_resolution').first.click()
    assert context.browser.url == context.get_url('competition:submit-answer', pk=comp.id)
    for row in context.table:
        desc = row['description']
        github = row['github']
        form = context.browser.find_by_tag('form')
        print("FORM", form)
        with context.browser.get_iframe("mytextarea_ifr") as text_area:
            print("TEXT AREA", text_area)
            text_desc = text_area.find_by_tag('p')
            print("TEXT DESC", text_desc)
        github_field = context.browser.find_by_name('githuburl')
        print("GITHUB FIELD", github_field)
        print("GITHUB FIELD", github_field.first)
        context.browser.find_by_name('button_publish').first.click()





@when('I want to create a submission for a competition "{title}"')
def step_impl(context, title):
    """
    :type title: str
    :type context: behave.runner.Context
    """
    from apps.league.models import Competition
    comp = Competition.objects.get(title=title)
    context.browser.visit(context.get_url('competition:submit-answer', pk=comp.pk))

