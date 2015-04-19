for i in range(9,0,-1):
    for j in range(9,0,-1):
        if j<=i:
            print(i,"*",j,"=",i*j," ",'\t',end=' ')
    print(end='\n')
print('\nDone!')
