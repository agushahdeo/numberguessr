import random

class User():
    def __init__(self, limit:int):
        self.chances = 10
        self.number = random.randint(1,limit)
        if self.number > limit/2:
            print("The number is greater than half the limit.")
        else:
            print("The number is lesser or equal to than half the limit.")
        
        if (self.number % 2) == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

        flag = False

        if self.number == 1:
            print(self.number, "is not a prime number")
        elif self.number > 1:
            # check for factors
            for i in range(2, self.number):
                if (self.number % i) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break
            if flag:
                print("The number is not a prime number.")
            else:
                print("The number is a prime number.")
if __name__ == "__main__":
    limit = int(input("Enter a maximum limit: "))
    guessed = False
    tries = 0
    user = User(limit=limit)
    while guessed != True and tries < 10:
        guess = int(input("Enter a guess:"))
        if guess == user.number:
            print("You guessed it! The number was {}!".format(user.number))
            guessed=True
            exit()
        elif guess + 5 or guess - 5 == user.number:
            print("Not quite but you are close!")
            tries+=1
        else:
            print("Incorrect.")
            tries+=1
    if tries >= 10:
        print("You ran out of tries! The number was {}!".format(user.number))
        
