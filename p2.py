print("This program shows all the odd numbers between 0 and any number of your choice...")
n = int(input("Enter your number: "))

arrayn = []
arrayodd = []
i = 0

while(i<(n+1)):
    arrayn.append(i)
    i+=1

for item in arrayn:
    if(item%2 != 0):
        arrayodd.append(item)
        print(item)