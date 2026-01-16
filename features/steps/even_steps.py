from behave import given, when, then
from src import number_checker



@given('the number is {number}')
def step_given_number(context, number):
    context.number = int(number)



@when('I check the number')
def step_when_check_number(context):
    context.result = number_checker.check_number(context.number)


@then('the result should be "{expected}"')
def step_then_result(context, expected):
    assert context.result == expected
