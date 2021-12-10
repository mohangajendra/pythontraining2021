'''''''''Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)
Extras:
Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''''
import random
a=random.randint(1,9)
inputnum=0
count_num=0
while(inputnum!=a and inputnum!='exit'):
    inputnum = input("try entering a number again between 1 to 9, type exit to quit the game ")
    if inputnum=='exit':
        break
    inputnum=int(inputnum)
    count_num+=1
    if inputnum<a:
        print("your guessed low")
    elif inputnum>a:
        print("your guessed high")
    else:
        print("Hurray you guessed the number right, it is {}".format(a))
        print("you took {} attempts to guess it right".format(count_num))