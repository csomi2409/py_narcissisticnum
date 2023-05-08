def narcissistic(value):
    narc=0
    for i in (str(value)):
        num = int(i)**int(len(str(value)))
        narc = narc + num

    if narc == value:
        print("Your number is narcissistic.")       
    else:
        print("Your number is not narcissistic")

Input = int(input("Input a number and I will decide if it's narcissistic or not:\n"))

narcissistic(Input)