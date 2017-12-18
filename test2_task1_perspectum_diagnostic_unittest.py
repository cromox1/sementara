import unittest
from test2_task1_perspectum_diagnostics import *

class TestInputMultiList(unittest.TestCase):
    def setUp(self):
        self.inputtest1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']] # all = 9, uniq = 7
        self.inputtest2 = ['j', 'ju', 'gh', 'ju', 'j']
        self.inputtest3 = ('a', 'b', 'c')
        self.verificationErrors = []

    def testInputIsAList(self):
        try:
            self.assertEqual(type(convert2df(self.inputtest1)[3]), list)
        except TypeError as e:
            return False
        return True

    def testInputIsNotList(self):
        try:
            self.assertEqual(type(convert2df(self.inputtest3)), tuple)
            self.assertNotEqual(type(convert2df(self.inputtest3)), list)
        except TypeError as e:
            return False
        return True

    def testSingleListWillGiveNoMultilist(self):
        try:
            testinput = self.inputtest2
            if type(testinput[0]) != list:
                testinput = [testinput]
            multilist = list(convert2df(testinput)[0]['uniq'].loc[convert2df(testinput)[0]['TRUE']>1 ])
            self.assertEqual(multilist, [])
        except ValueError as e:
            return False
        return True

    def testInputMultiListAllStringUnique(self):
        try:
            uniqtest = convert2df(self.inputtest1)[2]
            alltest = int(convert2df(self.inputtest1)[1].apply(pd.value_counts).fillna(0).sum().sum())
            self.assertEqual(len(uniqtest), 7)
            self.assertEqual(alltest, 9)
        except TypeError as e:
            return False
        return True

    def testInputMultiListOutput(self):
        try:
            multilist = list(convert2df(self.inputtest1)[0]['uniq'].loc[convert2df(self.inputtest1)[0]['TRUE']>1 ])
            self.assertEqual(multilist, ['gh'])
        except TypeError as e:
            return False
        return True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
