# tsufood was made due to TSU Detectives inability to pick a common place of food.
# This application was made to simplify the food decision making process that takes up precious forensics/busy work that is required of TSU detectives. Please utilize this tool when your TSU partner or you do not know where to go eat.

import random

food = [
    "...Wabash",
    "...Chinese",
    "...Fast food like PDQ",
    "...Random Google and go",
    "...Ask the first person you see in the office and commit",
    "...Decide but workout tomorrow",
    "...Burger Joint",
    "...Mexican",
    "...Chipotle",
    "...Greek ",
    "...Saigon",
]

def tsufood():
  itfl = ("...is the final answer")
  
  while True:
    question = input("Where will the TSU detectives go eat?: (Type in a random restaurant and see if it will match up! Hit enter again to close bro): ")
    print (random.choice(food))
    if not question:
      return itfl
print (tsufood())
