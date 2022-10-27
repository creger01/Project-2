#Cadyn Reger
import time
import random
out = []
element = ""

def prt_list(list):
    for y in list:
        print(y, flush=True)
        if len(y) < 70:
            time.sleep(3)
        else:
            time.sleep(4)

def prt_single(sentence, num):
    print(sentence, flush=True)
    time.sleep(num)

# The initial story.
def intro():
    global element
    element = random.choice(["O'Neil house party", "Alumni House party", "Keenan House party"])
    story = [
    "I am so excited for tonight!", f"My friends and I are going out to {element}",
    "and it\'s gonna be such a good time.", "We heard there were a lot of people going",
    "so I\'m super excited but kind of nervous. I need your help to find Michael John.\n"
    ]
    prt_list(story)

#first choice
def choose_1():
    act = [
    "Enter 1 if I should check in the kitchen.",
    "Enter 2 if I should go outside to look."
    ]
    prt_list(act)
    response = str(input("Please enter 1 or 2.)\n"))
    return response

#if kitchen
def go_where():
    choice1 = [
        "I start to walk to the kitchen.",
        "As I am walking, I run into Michael John's best friend, Glenn.\n"
    ]
    choice2 = [
        "I think I am going to walk to the kitchen.",
        "I've already lost my best friends, I might as well keep looking for Michael John.\n"]
    if "message" in out:
        prt_list(choice2)
    else:
        prt_list(choice1)
    response1 = str(input("Should I (3) stop and talk to Glenn or (4) try to find my frineds?\n"))
    return response1

#if I go to the kitchen
def kitchen():
    response1 = go_where()
    if response1 == "3":
        choice3 = [
        "As I searched through the kitchen, I ran into Glenn so I decided to talk",
        "to him for a bit. I knew he was Michael John's best freind and maybe he could",
        "give me some information I was looking for.", "I say 'Hey Glenn! I am so happy to see you!'",
        "he told me he was happy to see me too. I decided to ask him the question I'd been wanting",
        "answered for awhile. 'Glenn', I said, 'What does Michael John think about me?'",
        "Glenns face was shocking but a smile soon appeared. He told me that Michael John has",
        "a huge crush on me and hes waiting for me outside!"
        ]
        choice4 = [
        "As I searched through the kitchen, I ran into Glenn so I decided to talk",
        "to him for a bit. I knew he was Michael John's best freind and maybe he could",
        "help me with a question I've had for a while. 'Hey Glenn, great to see you!' I",
        "shouted across the kitchen. 'Glenn', I said, 'Does Michael John like me?'",
        "Glenns face beams with a wide smile and said, 'He\'s waiting outside for you, why",
        "don\'t you go ask him!\n"]
        if "message" in out:
            prt_list(choice4)
            play_again()
        else:
            prt_list(choice3)
            play_again()
    elif response1 == "4":
        choice6 = [
        f"I shoved quickly through people as the {element} was so packed with people shoulder",
        "to shoulder. I was four steps away form the back door when someone grabbed my arm and yelled",
        "my name, 'Lizzy, oh my word I\'m so happy to see you here!'" "It was Gabe, a guy I knew",
        "that liked me but I didn't really feel the same. He tried making conversation with me but",
        "I really just wasn't feeling it. Unfortuneately it was too late, Gabe started confessing",
        "his love for me and their was no where to escape! The night ended with Gabe stuck to my hip",
        "and I didn't get a chance to talk to Michael John."
        ]
        if "message" in out:
            prt_single("I didn't get to see Michael John, I need to restart my night! Try again!", 2)
        else:
            prt_list(choice6)
            out.append("message")
            choose_1
    else:
        prt_sing("Please help me, I need to find out the truth!", 2)
        kitchen()

#if I go outside
def outside():
    prt_single("I think I'm going to look outside for Michael John", 2)
    choice5 = [
    "I go around the house to get to the backyard where I hear loud music",
    "and people conversing. As I look around I don't see anybody I know.",
    "I started to get extremely frusterated because all I wanted was to spend",
    "this night hanging out with Michael John. I continue to look around and I noticed",
    "someone in the corner of my eye up on patio. It was Michael John standing on the railing",
    "shouting my name, 'Lizzy! You finally made it!' He jumps down from the patio railing and runs",
    "to my feet and confesses his love for me. He told me that I'm all he thinks about and he wants",
    "me to his forever.\n"
    ]
    if "message" in out:
        prt_single(
        f"I am so excited that I came to the {element}"
        )
        prt_single("Idk")                   #I dont know what to put here
    else:
        prt_list(choice5)
        out.append("message")

def game():
    response = choose_1()
    if response == "1":
        kitchen()
    elif response == "2":
        outside()
    else:
        game()
    game()


def word_game():
    intro()
    game()
    play_again()

def play_again():
    global out
    prt_single("Would you like to play again?", 2)
    response2 = str(input("Please enter 'yes' for yes and 'no' for no.\n").lower())
    if response2 == "yes":
        out = []
        word_game()
    elif response2 == "no":
        exit()
    else:
        play_again()

word_game()
