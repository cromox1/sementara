input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
# input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'], ['j', 'ju', 'gh'], ['x'],['x', 'y']]
# input1 = {'g', 'gh', 'ghj', 'g'}
# input1 = ['g', 'gh', 'ghj', 'g']

### total number of strings & number of unique string
def all_unique_strings(inputlist):
    inputall=[]
    # convert inputlist to multi list if input is one list input
    if type(inputlist[0]) != list:
        inputlist = [inputlist]
    jj = len(inputlist)
    for j in range(jj):
        inputall = inputall + inputlist[j]
    return len(inputall), len(list(set(inputall))), inputall, list(set(inputall))

### strings appearing in multi lists
def strings_multilist(inputlist):
    jj = len(inputlist)
    dict1 = {} ; count2 = {} ; multi = []
    # change lists to dictionary of lists
    for p in range(jj):
        count={}
        for word in inputlist[p]:
            if word not in count:
                count[word] = 1
            else:
                count[word] +=1
        dict1[p] = count
    # count string by list
    for word in list(set(all_unique_strings(inputlist)[2])):
        count2[word] = 0
    for p in range(jj):
        for word in list(set(all_unique_strings(inputlist)[2])):
            if word in dict1[p].keys():
                count2[word] += 1
    if type(inputlist[0]) == list:
        for ky,vl in count2.items():
            if vl > 1:
                multi = multi + [ky]
    return multi

def testing(inputlist):
    try:
        inputlist = inputlist + []
        uniquestr = all_unique_strings(inputlist)[1]
        totalstr = all_unique_strings(inputlist)[0]
        multilist = strings_multilist(inputlist)
        print('Strings appearing in multiple lists : ', end=''); print(*multilist, sep=', ')
        print('Number of unique strings : ' + str(uniquestr))
        print('Total number of strings processed : ' + str(totalstr))
    except:
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

testing(input1)
