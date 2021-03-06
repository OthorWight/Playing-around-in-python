import random

def make_die(sides=20):
    die_dict  = {}
    for i in range(sides):
        die_dict[i+1] = 0

    set_die_side_chances(die_dict)

def set_die_side_chances(die_dict):
    total = 0
    for i in die_dict:
        die_dict[i] = random.randrange(0, 2)
        total = total + die_dict[i]
    if total == 0:
        #print("Error: all zeros  ", die_dict)
        set_die_side_chances(die_dict)

    #print(die_dict)
    pop_die_sides_with_zero(die_dict)

def pop_die_sides_with_zero(die_dict):
    for i in list(die_dict):
        if die_dict[i] == 0:
            die_dict.pop(i)
            if len(die_dict) == 1:
                die_print_result(die_dict)
    if len(die_dict) > 1:
        set_die_side_chances(die_dict)

def die_print_result(die_dict):
    for i in die_dict:
        print(i)

for i in range(10):
    make_die()
