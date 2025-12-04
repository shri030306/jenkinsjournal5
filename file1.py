import sys

if len(sys.argv) == 4:
    print("User provided input values:")
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    print("No input given - using default values:")
    principal = 1000      
    rate = 5              
    time = 2         

simple_interest = (principal * rate * time) / 100


print("Principal:", principal)
print("Rate of Interest:", rate)
print("Time:", time)
print("Simple Interest:", simple_interest)
