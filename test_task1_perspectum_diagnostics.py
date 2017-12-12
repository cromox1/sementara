input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
# input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'], ['j', 'ju', 'gh']]

### total number of strings & number of unique string
def all_unique_strings(file1):
    jj = len(file1)
    inputall=[]
    for j in range(jj):
        inputall = inputall + file1[j]
    return len(inputall), len(list(set(inputall))), inputall

### strings appearing in multi lists
def strings_multilist(file1):
    jj = len(file1)
    dict1 = {} ; count2 = {} ; multi = []
    # change lists to dictionary+lists
    for p in range(jj):
        count={}
        for word in file1[p]:
            if word not in count:
                count[word] = 1
            else:
                count[word] +=1
        dict1[p] = count
    # count string by list
    for word in list(set(all_unique_strings(file1)[2])):
        count2[word] = 0
    for p in range(jj):
        for word in list(set(all_unique_strings(file1)[2])):
            if word in dict1[p].keys():
                count2[word] += 1
    for ky,vl in count2.items():
        if vl > 1:
            multi = multi + [ky]
    return multi

multilist = strings_multilist(input1)
uniquestr = all_unique_strings(input1)[1]
totalstr = all_unique_strings(input1)[0]

print('Strings appearing in multiple lists : ',end=''); print(*multilist, sep=', ')
print('Number of unique strings : ' + str(uniquestr))
print('Total number of strings processed : ' + str(totalstr))


