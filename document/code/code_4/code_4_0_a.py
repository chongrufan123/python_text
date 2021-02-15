import pickle

file_name = "boy1.txt"
file_da = open(file_name, 'rb')
lala = pickle.load(file_da)
for each in lala:
    print(each)
    
print("==================")
file_name = "boy2.txt"
file_da = open(file_name, 'rb')
lala = pickle.load(file_da)
for each in lala:
    print(each)


print("==================")
file_name ="boy3.txt"

file_da = open(file_name, 'rb')
lala = pickle.load(file_da)
for each in lala:
    print(each)


print("==================")
file_name = "gril1.txt"
file_da = open(file_name, 'rb')
lala = pickle.load(file_da)
for each in lala:
    print(each)


print("==================")
file_name = "gril2.txt"
file_da = open(file_name, 'rb')
lala = pickle.load(file_da)
for each in lala:
    print(each)


print("==================")
file_name = "gril3.txt"
file_da = open(file_name, 'rb')
lala = pickle.load(file_da)
for each in lala:
    print(each)

