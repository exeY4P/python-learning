amount = float(input("Enter amount: "))
percent_of_tip = int(input("Enter percent of tip: "))

tip = amount * (percent_of_tip / 100)
outcome = tip + amount

print(f"The amount of the invoice: {amount}")
print(f"Tip percentage: {percent_of_tip}")
print(f"\nTip: {tip}")
print(f"Outcome: {outcome}")
