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

if __name__ == "__main__":
    testing(input1)
