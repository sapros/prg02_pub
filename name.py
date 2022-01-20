msg = 'I asKed "is tHis cirilyc?"'
print(msg)
print(msg.title())

print(msg.upper())
print(msg.lower())

first_name = 'ada   '
last_name = '                  wong'
full_name = f"{first_name} {last_name}"

print(full_name.title())

message = f"HEllo, beach {full_name.title()}!"
print(message)
print("\tfacking\nfacking\nfuck")

#message = "{} {}".format(first_name, last_name)
#print(message)
#full_name_clean = f"{first_name.rstrip()} {last_name.lstrip()}"
full_name_clean = f"{first_name.strip()} {last_name.strip()}"
print(full_name_clean.title())

print(full_name_clean)

print("set input below:")
#a = input()
#a = 'a var content'
output = f"hi! {a}"
print(output)

a = a.strip()
a = len(a)

if a > 2:
    print("ты ввел YES")
else:
    print("ты ввел NO!")
print(a)


