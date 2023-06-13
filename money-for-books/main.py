books = int(input("How many books do you want to buy? "))
money = int(input("How much money do you have? "))

cost = books * 20

if money >= cost:
  print("You have enough money, go for it!")
else:
  difference = cost - money
  print("You need $" + str(difference) + " more to buy that number of books")