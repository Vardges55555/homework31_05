"""Try to write some variables that convert the pounds to centimeters.
Do not just type in the measurements. Work out the math in Python"""
# 1 pounds = 30.48 sm
user = float(input("Write pounds to Convert SM: "))
result = user * 30.48
print("The %d pounds is %.3fSM!" % (user, result))
