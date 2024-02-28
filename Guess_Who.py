Paul = {
  "Age": "Young",
  "age": "young",
  "Hair": "Brown",
  "hair": "brown",
  "Eyes": "Blue",
  "eyes": "blue",
  "Gender": "Male",
  "gender": "male"
}

Paul_Hair = input("What is Paul's hair colour")
if Paul_Hair in Paul["Hair"] or Paul_Hair in Paul["hair"]:
  print("Correct")
else:
  print("False")
