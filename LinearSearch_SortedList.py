def search(L,e):
   
    for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
            
    return False
print (search([1,2,5,7,8],0))