msg = "hello, man"
print(msg)

msg = "Hello the second time!"
print(msg)

msg = "это кириллица?"
print(msg)

msg_sort = sorted(msg, reverse=True)
print(msg_sort)


msg_sort.remove('и')

print(msg_sort)

name =  "vala"
name2 = "vala2"
text = name + name2
print(f"{text}")

text = name * 5
print(f"{text}")

print("text " + str(name) + " " + str(name) + "!")

