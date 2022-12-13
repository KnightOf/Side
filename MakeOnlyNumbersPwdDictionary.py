import itertools as its
numbers = "0123456789"
r = its.product(numbers,repeat=8)
dic = open("NumbersPwd.txt","a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
