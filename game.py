import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print('The number must be less than!')
    elif predict_number < number:
        print('The number must be greater than!')
    else:
        print(f'You guess the number! This is = {number}, in {count} attemts')
        break
        