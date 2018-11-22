qs = ["What is your Name?",
      "What is your fav. color?",
      "What is your best movie"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

for i in range(1,4):
    print(i)
    for letter in ["a","b","c"]:
        print(letter)
        for number in ["co","pin","cook"]:
            print(number)

