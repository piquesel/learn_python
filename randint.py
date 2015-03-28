import random

nb_tries = 0
while True:
    llimit = int(input("What is the lower limit?"))
    ulimit = int(input("What is the upper limit?"))
    if llimit < ulimit:
        break
    else:
        print("Wrong limit assignement!")

nb_to_guess  = random.randint(llimit,ulimit)
print(nb_to_guess)

while True:
    user_choice = int(input("What is your guess? "))
    nb_tries += 1
    if user_choice == nb_to_guess:
        print("Awesome! You won...")
        break
    elif user_choice > nb_to_guess:
        print("Too high")
        continue
    else:
        print("Too low")
        continue
        
print("You find the right answer: {} in {} of guesses.".format(user_choice, nb_tries))