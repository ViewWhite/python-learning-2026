meal = float(input("What is the meal cost? "))
tip = int(input("What is the tip percentage? "))
tip_amount = meal * tip / 100
total = meal + tip_amount
print(f"The total cost of the meal is ${total:.2f}.")