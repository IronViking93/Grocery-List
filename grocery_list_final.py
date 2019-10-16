#below is the empty grocery item dictionary and the empty grocery history list as place holders. stop is set equal to False for the while loop.
grocery_item = {}
grocery_history = []
stop = False

#the while loop asks for input from the user such as the item number, how many they are purchasing, and how much the item is individually. It will then ask the user to press c if they want to add another item or q if they do not.
while not stop:
  item_name = input("Item name:\n")
  quantity = input("Quantity purchased:\n")
  price = input("Price per item:\n")
  grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(price)}
  grocery_history.append(grocery_item)
  finihed = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")
  if finished == 'q':
    stop = True

# grand_total is set to 0 as a place holder for the for loop.
grand_total = 0

#the for loop will cycle through each item that was added to the list and provide a total for the amount they purchase and how much that item was worth. it will then print out how many they bought, the item name, the price per item and the total for total cost of the item that they purchased.
for item in grocery_history:
  item_total = item['number'] * item['price']
  grand_total += item_total
  print("%d %s @ $%.2f ea $%.2f" %((item['number']), (item['name']), (item['price']), item_total))
  item_total = 0

#this will print out the grand total of their whole grocery list.
print("Grand total:  $%.2f" % grand_total)
  
