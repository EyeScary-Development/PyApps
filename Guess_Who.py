Paul = {
  "Age": "Young",
  "Hair": "Brown",
  "Eyes": "Blue",
  "Gender": "Male"
}

Paul_Hair = input("What is Paul's hair colour")
if Paul_Hair in Paul["Hair"]:
  print("Correct")
else:
  print("False")
