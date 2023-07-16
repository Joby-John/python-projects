import math

angles = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2]
funcs = ['sin', 'cos', 'tan']

while True:
    angle = math.choice(angles) # choose a random angle from the list
    func = math.choice(funcs) # choose a random trigonometric function to ask for
    
    angle_str = ''
    if angle == 0:
        angle_str = '0'
    elif angle == math.pi/6:
        angle_str = 'pi/6'
    elif angle == math.pi/4:
        angle_str = 'pi/4'
    elif angle == math.pi/3:
        angle_str = 'pi/3'
    elif angle == math.pi/2:
        angle_str = 'pi/2'
    
    answer = input(f"What is {func}({angle_str})? (Type 'end' to stop) ")
    
    if answer == 'end':
        break
    
    if func == 'sin':
        correct_answer = math.sin(angle)
    elif func == 'cos':
        correct_answer = math.cos(angle)
    elif func == 'tan':
        correct_answer = math.tan(angle)
    
    if float(answer) == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
