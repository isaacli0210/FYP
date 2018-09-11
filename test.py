testString = ["Master(A296)", "Pater(B346)", "Cat(C543)"]

id = ""
for data in testString:
    datas = data.split("(")
    name = datas[0]
    id = datas[1][0:4]
    print(id)