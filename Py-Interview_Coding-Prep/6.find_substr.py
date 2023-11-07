"""
Find the position of the substring in the main string
*
This is possibly an example of classic sliding window
"""
s1 = 'abcd'
s2 = 'kjkeoldlabcdadfdabcdv'
ls1 = len(s1)
ls2 = len(s2)

if ls1>ls2:
    for i in range(ls1-ls2+1):
        if s1[i:i+ls2] == s2:
            print('At ',i,'Till',i+ls2-1)
else:
    for i in range(ls2-ls1+1):
        if s2[i:i+ls1] == s1:
            print('At ',i,'Till',i+ls1-1)