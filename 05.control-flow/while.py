number = 23
running = True

while(running):
    guess = int (input("Enter an integer: "))

    if(guess == number):
        print("Congratulations, you guessed it!")
        running = False
        # break
    elif(guess < number):
        print("No, it is a little higher than that")
    else:
        print("No, it is a little lower than that")

else:
    # Sempre será executado ao final do laço,
    # a menos que seja usada uma clausula 'break' para interromper o laço
    print("The while loop is over")

print("Done!")