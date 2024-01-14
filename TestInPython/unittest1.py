
#Here's one of implementatuon of  a unitest test case:
import unittest

def add(x,y):
    return x + y


#Each test case class contains one or more test methods
#which are regular Python methods whose names
#start with the word 'test'.

class TestAddition(unittest.TestCase):

    def test_add_positive_num(self):
        res = add(2,3)

        self.assertEqual(res, 5)


    def test_add_negative_num(self):
        res = add(-2, -3)

        self.assertEqual(res, -5)

#Call the main method
if __name__ == '__main__':
    unittest.main()


