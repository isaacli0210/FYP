testString = ["Master(A296)", "Pater(B346)", "Cat(C543)"]
stringList = ["1", "2", "3"]

myString = "Hello, World"
for data in stringList:
    myString = myString + ", " + data
print(myString)

"""
id = ""
for data in testString:
    datas = data.split("(")
    name = datas[0]
    id = datas[1][0:4]
    print(id)
"""