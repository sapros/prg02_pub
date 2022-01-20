list1 = ['zero', 'one', 'two']
print(list1[2])

index = list1[-1]
print(index)

list1[-1] = 'noll'
print(list1)
list1 = list(list1)
list1.append('tree')
list1.append('four')
list1.append('five')
print(list1)


msg = "это кириллица?"
print(msg)
msg = ['а', 'v', 's', 'и', 'и', 'и', 'и', 'и', 'и', 'D']
msg_sort = sorted(msg, reverse=True)
print(msg_sort)

for val in msg_sort:
    msg_sort.remove('и')

print(msg_sort)

msg_indecec_count = len(msg_sort) - 1
a = 0
while a >= 0:
    msg_sort.remove('и')
    a = a - 1

print(msg_sort)

ages = [5, 12, 17, 18, 24, 32]


def myfunc(val):
    if val < 18:
        return False
    else:
        return True


adults = filter(myfunc, ages)


for x in adults:
    print(x)


ages = ages[0:3]
print(ages)

# beta_list = list(beta_list)
# for x in range(1, 4):
#        beta_list += ['fruit']
#
#
#    print(beta_list)

beta_list = ['apple', 'banana', 'orange']
beta_list_copy = beta_list.copy()
print(beta_list)

number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

for val in beta_list:
    print(val)


for val in range(1, 10):
    print(val)

range_in_list = list(range(1, 10))
print(range_in_list)

values = list(range(2, 11, 2))
print(values)


num_list = []
for val in range(1, 1000):
    num_list.append(val ** 2)


for val in num_list:
    print(f"|{val}|")


