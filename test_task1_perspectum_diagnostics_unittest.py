import unittest
from testing import all_unique_strings,strings_multilist

class TestInputMultiList(unittest.TestCase):
    def setUp(self):
        self.inputtest1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']] # all = 9, uniq = 7
        self.inputtest2 = ['j', 'ju', 'gh', 'ju', 'j']
        self.inputtest3 = ('a', 'b', 'c')
        self.verificationErrors = []

    def testInputIsAList(self):
        try:
            self.assertEqual(type(all_unique_strings(self.inputtest1)[2]), list)
        except TypeError as e:
            return False
        return True

    def testInputIsNotList(self):
        try:
            self.assertEqual(type(all_unique_strings(self.inputtest3)), tuple)
            self.assertNotEqual(type(all_unique_strings(self.inputtest3)), list)
        except TypeError as e:
            return False
        return True

    def testSingleListWillGiveNoMultilist(self):
        try:
            testinput = self.inputtest2
            if type(testinput[0]) != list:
                testinput = [testinput]
            multilist = strings_multilist(self.inputtest2)
            self.assertEqual(multilist, [])
        except ValueError as e:
            return False
        return True

    def testInputMultiListAllStringUnique(self):
        try:
            uniqtest = all_unique_strings(self.inputtest1)[1]
            alltest = all_unique_strings(self.inputtest1)[0]
            self.assertEqual(uniqtest, 7)
            self.assertEqual(alltest, 9)
        except TypeError as e:
            return False
        return True

    def testInputMultiListOutput(self):
        try:
            multilist = strings_multilist(self.inputtest1)
            self.assertEqual(multilist, ['gh'])
        except TypeError as e:
            return False
        return True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
