my_list = []  # 선언

my_list.append('A')  # enqueue
my_list.append('B')
my_list.append('C')

# print(my_list)


print(my_list)

first = my_list.pop(0) # dequeue
print(my_list)

second = my_list.pop(0) # dequeue
print(my_list)

print(first, second)
