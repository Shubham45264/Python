menu={
  'pizza':40,
  'burger':50,
  'fries':40,
  'coffee':70,
}
print("Welcome to our python restraunt")
print("pizza: Rs40\nburger: Rs50\nfries: Rs40\nCoffee: Rs70")
order_total = 0
item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
  order_total += menu[item_1]
  print(f"Your item {item_1} has been added to your order")
else:
  print(f"ordered item{item_1} is not available yet!")
another_order = input("do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
      order_total += menu[item_2]
      print(f"Item {item_2} has been added to order")
    else:
      print(f"Ordered item {item_2} is not available!")
more_order = input("do you want to add another item? (Yes/No)")
if more_order == "Yes":
    item_3 = input("Enter the name of the third item= ")
    if item_3 in menu:
      order_total += menu[item_3]
      print(f"Item {item_3} has been added to order")
    else:
      print(f"Ordered item {item_3} is not available!")
print(f"The total amount of items is {order_total}")
print("thanks for Visiting")
  