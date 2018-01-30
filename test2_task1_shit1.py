input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]
# input1 = [['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn'], ['j', 'ju', 'gh'], ['x','gk']]
# input1 = [['g', 'gh', 'ghj', 'g']]
# input1 = [['g', 'gh', 'ghj', 'g', 'ghj'],['g']]
# input1 = ['g', 'gh', 'ghj', 'g']
# input1 = {'g', 'gh', 'ghj', 'g'}

import pandas as pd
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

if __name__ == "__main__":
    testing(input1)
