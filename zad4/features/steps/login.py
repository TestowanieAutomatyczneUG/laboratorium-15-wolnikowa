from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that
use_step_matcher("parse")

@given('Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='./chromedriver')
    context.driver.implicitly_wait(10)

@given('Gmail login page')
def step_impl(context):
    context.driver.get(
        "https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=1209600&osid=1&continue"
        "=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail"
        "%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(2)

@when(u'we write login {login} and click login button')
def step_impl(context, login):
    context.driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(login)
    context.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(2)

@when(u'we write password {password} and click login button')
def step_impl(context, password):
    context.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    context.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)

@when('click login button on password page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    time.sleep(5)

@when('click login button on login page')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    time.sleep(5)

@then('we will login')
def step_impl(context):
    assert_that(context.driver.current_url).is_equal_to('https://mail.google.com/mail/u/0/#inbox')

@then('we will not login')
def step_impl(context):
    assert_that(context.driver.current_url).is_not_equal_to('https://mail.google.com/mail/u/0/#inbox')