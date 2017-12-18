input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
# input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'], ['j', 'ju', 'gh'], ['x','gk']]
# input1 = [['g', 'gh', 'ghj', 'g']]
# input1 = [['g', 'gh', 'ghj', 'g', 'ghj'],['g']]
# input1 = ['g', 'gh', 'ghj', 'g']
# input1 = {'g', 'gh', 'ghj', 'g'}

import pandas as pd
import unittest
from itertools import zip_longest

def convert2df(inputlist):
    allcol = len(inputlist)
    inputtmp = list(map(list, zip_longest(*inputlist))) ## transform input/dataframe format - Transpose
    inputdf = pd.DataFrame(inputtmp, columns=['col'+str(x) for x in range(allcol)]) ## convert to DataFrame

    uniqnone = pd.unique(inputdf[list(inputdf)].values.ravel()).tolist()
    uniq = [ xx for xx in uniqnone if xx is not None ]
    outputlist = pd.DataFrame(uniq, columns=['uniq'])

    for x in range(allcol):
        colname = 'col'+str(x)
        outputlist = outputlist.join(pd.DataFrame(uniq, columns=[colname]).isin(list(inputdf[colname])))

    outputlist = outputlist.join(pd.DataFrame(list(outputlist.sum(axis=1)), columns=['TRUE']))

    return outputlist, inputdf, uniq, inputlist

def testing(inputlist):
    try:
        inputlist = inputlist + []
        # print('input = '+str(inputlist))
        if type(inputlist[0]) != list:
            inputlist = [inputlist]
        # print('') ; print(convert2df(inputlist)[1].fillna('')) ; print('')
        # print('uniq = '+ str(convert2df(inputlist)[2]))
        # print('') ; print(convert2df(inputlist)[0]) ; print('')
        multilist = list(convert2df(inputlist)[0]['uniq'].loc[convert2df(inputlist)[0]['TRUE']>1 ])
        print('Strings appearing in multiple lists : ', end=''); print(*multilist, sep=', ')
        print('Number of unique strings : '+str(len(convert2df(inputlist)[0]['uniq'].axes[0])))
        print('Total number of strings processed : '+str(int(convert2df(inputlist)[1].apply(pd.value_counts).fillna(0).sum().sum())))

    except TypeError:
        print('Error - input is not a list')
        print('input = ' + str(inputlist))

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

testing(input1)
