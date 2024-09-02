# any pytest file should start with test_ or end with test_
# pytest method should be start with test
# any code should be wrapped in method only
# in pytest every method is treated as one test case
# in pytest each method treated as one test casepy
# in py test you can not have multiple test name with same names
# if you have that then it overwrites the previous result in other
# testing report it will report but pytest it overwrites if you have same method name
# doing some assertions here
# just comparing two vales based upon true or false return
# notes
# -k stands for method names execution , -s logs in output
# -v stands for more infor metadata ,
# you can run specific file with py.test <file name>

import pytest
@pytest.mark.skip
def test_firstProgram():
   msg = "hello"
   assert msg == "hi", "because string do not match"


def test_secodTest():
   a = 2
   b = 3
   assert a + 1, "Addition do not match"

# what if you want to run tests based upon smoke or regression?
'''
# what if you want to run tests based upon smoke or regression?

For that in Py test, there is a concept called Mark where you can actually mark that test case with

one set of name and you can tell your command line terminal to run only that mark related test cases.

It's like tagging in cucumber.

If you have familiar with cucumber framework, we call it as tags.


'''


@pytest.mark.smoke

# to run smoke related test command is -- py.test -m smoke -v -s
def test_secodCreditCard():
   print ("so! here is your CreditCard")


# If your requirement is only to not show this failing test case in your report.
"""
you know that is a bug and that should not create false alarm in your test report.
That's why you are skipping.
But if you come across a problem where by skipping that particular test, if you think some pre-request
operations for further test cases is impacting, then you can still run this test.
But you can skip reporting that in your report file.

I want to xfail this.

Right.
So when you give this, this particular test will run.
But in output you won't see about pass or fail.
So this is like just running but not reporting.
So you want to use this in cases where you think this is required for further test cases to run, but
that should not come in reporting.
"""

@pytest.mark.xfail
def test_thirdProgram():
   msg = "hello"
   assert msg == "hi", "because string do not match"












