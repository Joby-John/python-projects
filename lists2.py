numbers = list()

while True:
    inp = input("Enter any number(one at a time), when done enter done:")
    if inp == 'done':
        break
    value = float(inp)
    numbers.append(value)
try:    
    Average = sum(numbers)/len(numbers)
    print("Average: ", Average)
except:
    print("enter atleast one number!")