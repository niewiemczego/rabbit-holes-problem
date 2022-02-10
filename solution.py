# Rabbit holes problem

# there are 100 holes in a line, and there is a rabbit hiding in one of the holes

# you can only look in one hole at a time, 
# and every time you look in a hole,
# the rabbit jumps to an adjacent hole 

# Task: find the rabbit


import random

pos = random.randint(0,99)

print(f"Rabbit pos - {pos}")

def rabbit_move():
    global pos
    old_pos = pos
    if pos == 0:
        pos += 1
    elif pos == 99:
        pos -+ 1
    else:
        if random.uniform(0,1) > 0.5:  # there is 50% chance for rabbit to move left/right if it's not on the edge
            pos += 1
        else:
            pos -= 1
    print(f"Rabbit jumped from {old_pos} to {pos}")

def solve():
    global pos
    if pos % 2 == 0:
        for i in range(100):
            if i == pos:
                print(f"Guessed rabbit hole - {i}")
                break
            else:
                rabbit_move()
    else:
        for i in range(99,-1,-1):
            if i == pos:
                print(f"Guessed rabbit hole - {i}")
                break
            else:
                rabbit_move()

if __name__ == "__main__":
    solve()
