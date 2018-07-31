current_number, next_number = 0,1
for x in range (1, 10):
    print(current_number)
    current_number, next_number = next_number, current_number + next_number