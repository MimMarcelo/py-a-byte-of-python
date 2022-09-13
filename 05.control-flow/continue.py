while True:
    s = input("Enter something (q to quit): ")

    if s == "q":
        break
    if len(s) < 3:
        print("Too small")
        continue
    print("Input is of sufficient length")