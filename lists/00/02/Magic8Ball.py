import random
import time
import sys

responses = [
     "It is certain.",
     "It is decidedly so.",
     "Without a doubt.",
     "Yes - definitely.",
     "You may rely on it.",

     "As I see it, yes.",
     "Most likely.",
     "Outlook good.",
     "Yes.",
     "Signs point to yes.",

     "Reply hazy, try again.",
     "Ask again later.",
     "Better not tell you now.",
     "Cannot predict now.",
     "Concentrate and ask again.",

     "Don't count on it.",
     "My reply is no.",
     "My sources say no.",
     "Outlook not so good.",
     "Very doubtful."
]

def userinput():
        question = 'Enter your question:'
        print(question)
        stuff = input("> ")

        print("\nThinking..\n")
        time.sleep(3)
        print(random.choice(responses))

        final()


def final():
        print("Would you like to ask another question?")
        user_reply = input('> ')
        while(input):
                if user_reply == "yes":
                        userinput()
                else:
                        print("Thanks for playing!")
                        sys.exit(0)


print("Welcome to the Magic 8 Ball!")
userinput()
