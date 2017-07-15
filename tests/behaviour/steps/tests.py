from behave import given, then, when


@given('we have behave installed')
def behave_installed(context):
    pass


@when('we implement a test')
def implement_test(context):
    assert context


@then('behave will test it for us!')
def test_it_for_us(context):
    assert context.failed is False
