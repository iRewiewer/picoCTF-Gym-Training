test = {0:"d", 29:"3", 4:"r", 2:"5", 23:"r", 3:"c", 17:"4", 1:"3", 7:"b", 10:"_", 5:"4", 9:"3", 11:"t", 15:"c", 8:"l", 12:"H", 20:"c", 14:"_", 6:"m", 24:"5", 18:"r", 13:"3", 19:"4", 21:"T", 16:"H", 27:"f", 30:"b", 25:"_", 22:"3", 28:"6", 26:"f", 31:"0"}

pwdSorted = dict(sorted(test.items()))

print("picoCTF{", end = "")

for i in pwdSorted.values():
    print(i, end = "")

print("}", end = "")