import pytest



# def test_fixtureDdemo(setup):
#print("I will execute test steps in fixture demo method")

# fixture is used as setup and tear down method for test cases
# conf test file to generalize fixture and make it available to all test cases

'''
So that concept in Python we call it as a fixtures, but you can do a lot with this fixtures.
Not only that, but that's the base concept.
Okay, so let me go through that.
Firstly, I'll create one fixture in this class.
You can declare that fixture anywhere in the beginning or at the end.

now when you run this test right now, this test, do not have idea about this, Right.
Because how will this test know that it has to depend upon this fixture.
So you can give connection of the fixture to this method by simply passing
that method name as an argument in your test

Now, when you run this test, when this test is going to run it, and
when it comes across this setup,
it will check if there is any fixture defined with setup.
Yes, it is defined.
So it will first execute this complete method before it reaches this test.
So this is like pre request it ran and then it will run this.


So in selenium framework we use this fixtures for opening a browser or 
setting up some database instances
or creating some configuration properties, environment variables.
It's all like prerequisite stuff.
Like if you want to run in Chrome browser, you will make sure you have 
Chrome driver setup and invoke
browser in this setup and then you start actual test cases inside it.

But these methods, which are tests nothing but tests, 
do not have impact because we are not passing argument into them.
Only when you pass fixture as an argument, then only 
it will be tied up to the fixture.

'''

@pytest.mark.usefixtures("setup")
 
class TestExample:
    def test_fixtureDemo1(self):
        print("I will execute test steps in fixture demo1 method")

    def test_fixtureDemo2(self):
        print("I will execute test steps in fixture demo2 method")

    def test_fixtureDemo3(self):
        print("I will execute test steps in fixture demo3 method")

    def test_fixtureDemo4(self):
        print("I will execute test steps in fixture demo4 method")

    def test_fixtureDemo5(self):
        print("I will execute test steps in fixture demo5 method")

