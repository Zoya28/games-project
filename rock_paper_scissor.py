# rules of the game-------
# rock beats scissor, scissor beats paper, paper beats rock
import random
def play():

    user=input("what is your choice?\
    \n'r'for rock, 's' for scissor, 'p' for paper\n")
    comp=random.choice(['r','s','p'])
    if (user=='s') or (user=='r') or (user=='p') :
        if comp==user:
            return ("its a tie....")
        elif win(user,comp):
            return ("you won!\U0001F929")
        else:
            return ("you lose!\N{upside-down face}")
    return ("not valid!")

def win(user,comp):
    if (user=='r' and comp=='s') or (user=='s' and comp=='p') \
    or (user=='p' and comp=='r'):
        return True
print(play())