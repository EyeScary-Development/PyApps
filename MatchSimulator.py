import random

PremList = {
  "1": 84,
  "2": 76,
  "3": 57,
  "4": 66,
  "5": 72,
  "6": 34,
}
PremName = {
  "1": "Arsenal",
  "2": "Aston Villa",
  "3": "Bournemouth",
  "4": "Brentford",
  "5": "Brighton",
  "6": "Burnley"
}
Lower_Range = 45
Upper_Range = 55
print("What 2 teams do you want to simulate a match between? Type the number that is in brackets beside the team")
Team1 = input("Arsenal (1), Aston Villa (2), Bournemouth (3), Brentford (4), Brighton (5), Burnley (6)")
Team2 = input("Arsenal (1), Aston Villa (2), Bournemouth (3), Brentford (4), Brighton (5), Burnley (6)")
if Team1 == Team2:
  print("No, do not pick 2 teams of the same")
  exit()
else:
  pass

if Team1 in PremList and Team2 in PremList:
  if PremList[Team1] > PremList[Team2]:
    Thing = random.randint(1,100)
    if Thing < PremList[Team2]:
      print(PremName[Team2], " won")
    elif Thing < PremList[Team1] and Thing > PremList[Team2]:
      print(PremName[Team1]," won")
    elif Lower_Range <= Thing <= Upper_Range:
      print("The result was a draw")
    else:
      print("Broken Code")
  else:
    Thing = random.random.randint(1,100)
    if Thing > PremList[Team2]:
      print(PremName[Team2], " won")
    elif Thing > PremList[Team1] and Thing < PremList[Team2]:
      print(PremName[Team1]," won")
    elif Lower_Range >= Thing >= Upper_Range:
      print("The result was a draw")
    else:
      print("Broken Code")
