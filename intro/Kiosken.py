print("Glass 20kr  varmkorv 15kr   läsk 15kr   godis 10kr")

item=input()

if item == "glass":
    print("hur många")
    amount=input()
    amount=int(amount)
    print(amount * 20)

elif item == "varmkorv":
    print("hur många")
    amount=input()
    amount=int(amount)
    print(amount * 15)

elif item == "läsk":
    print("hur många")
    amount=input()
    amount=int(amount)
    print(amount * 15)

elif item == "godis":
    print("hur många")
    amount=input()
    amount=int(amount)
    print(amount * 10)


