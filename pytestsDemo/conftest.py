import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("i will be executing last")

# data driven fixture parameterizing concept
@pytest.fixture()
def dataLoad():
    # assume that you are building a user page and
    # you need to send first name last name and email
    print("user profile data is being created ")
    return ["Shubham", "tripathi", "rahulshettyacademy.com"]


@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser (request):
    return request.param


# in case of if you have multiple data


'''
inside.
You have to clearly tell that this fixture is now parameterized to tell 
that you have to pass params
like this.
'''
@pytest.fixture(params=[("chrome","shubham","tripathi"),("firefox","shubham"),"IE"])
def crossBrowser2 (request):
    return request.param

'''
You need to send it.
There is a instance which you have for fixture.
Okay.
That is a request.
Basically, whatever you declare in this level and each time one will be picked right, 
that will be
sent to this parameter called request.
'''


