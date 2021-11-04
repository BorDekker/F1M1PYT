from typing import Counter
Counter = 0

GroceryList = ["Milk", "Cheese", "Orange Juice", "Apples", "Bananas", "Grapes"]
for x in GroceryList:
    print(x)

print("")

ShoppingCart = ["Apples", "Apple Juice", "Bread", "Butter", "Cheese", "Orange Juice", "Milk", "Bananas", "Meat", "Peanut Butter"]
for item in ShoppingCart:
    print(item)

    for item2 in GroceryList:
        if item==item2:
            Counter += 1
    


if Counter == len(GroceryList):
    print("Finished Shopping")
else:
    print("continue")






#    if GroceryList == "Milk" "Cheese" "Orange Juice" "Apples" "Bananas" "Grapes":
 #       if GroceryList == ShoppingCart:
  #          print("Finished shopping")
    