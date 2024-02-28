Paul = {
  "Age": "Young",
  "Hair": "Brown",
  "hair": "brown",
  "Eyes": "Blue",
  "Gender": "Male"
}

Paul_Hair = input("What is Paul's hair colour")
if Paul_Hair in Paul["Hair"] or Paul_Hair in Paul["hair"]:
  print("Correct")
else:
  print("False")
