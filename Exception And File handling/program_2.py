import random

def game():
    print ("Your are playing....!")
    score = random.randint(1,100)
    with open("highscore.txt") as f:
        hiscore = f.read()
        if hiscore !="":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    
    print(f"Congratulations! your score is {score}.")


    if (score>hiscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))

        hiscore = score
        print(f"New high score! Your score has been saved.{hiscore}")
    return hiscore
game()
# print ("hiscore =",hiscore)