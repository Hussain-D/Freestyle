list_1 = [1,2,3,4,5]

double_list = list(map(lambda i:i*2,list_1))

print("Initial list: ", list_1)
print("List of doubled numbers: ",double_list)

filter_evens = list(filter(lambda i:i%2==0,list_1))

print("Initial list: ",list_1)
print("List of even numbers: ",filter_evens)

filter_odds = list(filter(lambda i:i%2!=0,list_1))

print("Initial list: ",list_1)
print("List of odd numbers: ",filter_odds)