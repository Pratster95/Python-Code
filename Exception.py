def get_ratios(L1,L2):
    ratios=[]
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad argument')
    return print (ratios)
    
L1=[1,2,3,4,5]
L2=[6,7,8,9,0]
get_ratios(L1,L2)
