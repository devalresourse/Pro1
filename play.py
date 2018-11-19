def f(x):
    return x + 1
z = f(4)
if z == 5:
    print("z is 5")
else:
    print("z is not 5")

    #data structure question 3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i for i in a if i%3 ==0]
print(b)


#question4
for x in range(2, 100):
    if (x % 2 == 0):
        print (x)
