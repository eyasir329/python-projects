import random
import ascii_art

print("Welcome to Rock Paper Scissors")
value_img = [ascii_art.rock, ascii_art.paper, ascii_art.scissor]
# 0-rock, 1-paper, 2-scissor

random_int = random.randint(0, 2)
input_key = input("Enter Rock as 'r', Paper as 'p', Scissor as 's' ")
if input_key != 'r' or input_key != 'p' or input_key != 's':
    print("You have to choose right input")
else:
    input_value = 0
    if input_key == 'r':
        input_value = 0
    elif input_key == 'p':
        input_value = 1
    else:
        input_value = 2
    print(random_int)
    # game on
    name = ""
    if input_value == 0:
        name = "Rock"
    elif input_value == 1:
        name = "Paper"
    else:
        name = "Scissor"

    print(f"You choose: {name}\n")
    print(value_img[input_value])

    if random_int == 0:
        name = "Rock"
    elif random_int == 1:
        name = "Paper"
    else:
        name = "Scissor"
    print(f"\nComputer choose: {name}\n")
    print(value_img[random_int])

    if (input_value == 0 and random_int == 2) or (input_value == 2 and random_int == 1) or (
            input_value == 2 and random_int == 1):
        print("You win ")
    elif input_value == random_int:
        print("Draw")
    else:
        print("You loose")
