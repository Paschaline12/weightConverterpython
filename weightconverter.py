#python weight converter
weight = float(input("Enter your weight: "))
Unit = input("Kilograms or Pounds? K or L: ")

if Unit == "K":
    weight = weight * 2.205
    Unit = "Lbs"
    print(f"Your weight is {weight} {Unit}")
elif Unit == "L":
    weight = weight/2.205
    Unit = "Kgs"
    print(f"Your weight is {weight} {Unit}")
else:
    print(f"{Unit} is not a valid entry")



