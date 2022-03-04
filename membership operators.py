#membership operators
a = ["Apple","Watermelon","Orange","Pear","Cherry","Strawberry","Nectarine","Grape"]
b = input("Enter Fruit name:")
if b in a:
  print(b in a)
else:
  print(b not in a)