# any pytest file should start with test_ or end with test_
# pytest method should be start with test
# any code should be wrapped in method only
# in py test you can not have multiple test name with same names
# if you have that then it overwrites the previous result in other
# testing report it will report but pytest it overwrites if you have same method name
# in pytest every method is treated as one test case


def test_firstprogram():
    print("hello")


def test_greet():
    print("Good Morning!")


def test_cross_browser(crossBrowser):
    print(crossBrowser)