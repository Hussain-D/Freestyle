list_1 = [1,2,3,4,5]

double_list = list(map(lambda i:i*2,list_1))

print(list_1)
print(double_list)

filter_evens = list(filter(lambda i:i%2==0,list_1))

print(list_1)
print(filter_evens)