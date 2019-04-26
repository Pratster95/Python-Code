def linear_search(L,e):
    print ("Element Not Found")
    for i in range(len(L)):
        if e==L[i]:
            print ("Element found at position {0}".format(i))
    
    
(linear_search([1,2,5,7,8],7))