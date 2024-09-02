import pytest


'''
if you want to return the data to a
specific test, then you have to add parameter.
Earlier in the last lecture I told you need not add this if you declare.
Globally, right.
So if you don't want to receive any data from that specific fixture, then you can skip it.
This particular test will actually execute that independently at the beginning and then it will run
this test.
But here your scenario is different.
You want to actually return, you are returning something.
You are returning some data from your fixture.
In the previous topic.
We did not return anything so you can actually not required to pass as a parameter once you declare
globally.
But in this case you are returning something.
When you are returning, then it's mandatory to pass that fixture name into your method.
Okay, because you want to print something and this is where it works, right?
I hope you understand the exact difference between why we are using this and why we are not using this.
Um, this is one of the famous interview question as well.
If you just Google with Python test framework questions, you will know in what scenario you will be
forced to pass fixture name.

'''
@pytest.mark.usefixtures("dataLoad")
class Test_Example2:

    def edit_profile(self, dataLoad):
        print(dataLoad)
        print(dataLoad[0])
        print(dataLoad[1])

