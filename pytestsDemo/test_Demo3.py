import pytest



def test_firstProgram():
   msg = "hello"
   assert msg == "hi", "because string do not match"

@pytest.mark.smoke
def test_secodCreditCard():
   a = 2
   b = 3
   assert a + 1, "Addition do not match"


def test_crossBrowser(crossBrowser):
   print(crossBrowser)


def test_crossBrowser2(crossBrowser2):
   print(crossBrowser2)
   print(crossBrowser2[0])
   print(crossBrowser2[1])
