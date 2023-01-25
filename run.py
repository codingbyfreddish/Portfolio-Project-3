"""
Welcome to my adventure game.
Hope you will enjoy it!
To check out more visit www.github.com/codingbyfreddish
"""

# Introduction. User name and confirmation to start game
def start_game():
    print("Hey there! First things first, what is your name?")
    name = input("Name: ")
    print(f"{name}?? Well, i've heard worse i guess... who cares about names anyway, huh?\n")
    print(f"So {name} are you ready for an adventure? 'Yes' or 'No'")
    answer = input("Answer: ")
    if answer.lower().strip() == "yes":
        print(f"Buckle up {name}, you my friend are in for an epic adventure!\n")
        scene_one()
    else:
        print("Had a feeling you dident have what it takes. Welcome back when you do.")
        exit()


# Start of the adventure 
def scene_one():
    print("A little girl, named Petra, is wandering through the forest when she comes across a fork in the path.") 
    print("She must decide whether to take the path to the left or the path to the right.")
    answer = input("Will she go 'Left' or 'Right': ")
    if answer.lower().strip() == "left":
        print("Petra takes the left path. After walking for a while, she comes across a dark cave.")
        print("The cave looks scary and Petra gutfeeling says 'don't go in there.")
        print("But at the same time what if the cave contains a big, old tresure chest filled with gold and what not?")
        print("Petra stands infront of the cave not sure what to do, can you help her choose?")
        cave_or_not = input("'Go inside' or 'Continue': ")
        if cave_or_not.lower().strip() == "go inside":
            print("Petra goes inside the dark, scary cave... and is never seen again. ***Game Over***\n")
            game_over = input("Dont underestimate your gutfeeling. Want to play again? 'Yes or No': ")
            if game_over.lower().strip() == "yes":
                start_game()
            else:
                exit()
        else:
             print("Petra choose to trust her gut and wanders away from the cave.\n")
             scene_two()   

    else:
        print("Petra takes the right path. After walking for a while, she comes across a babbling brook.")
        print("She thinks for herself 'I am mighty thirsty, maybe i should drink alittle bit of water before continuing on my journey?'")
        drink_or_dont = input("'Drink' or 'Dont': ")
        if drink_or_dont.lower().strip() == "drink":
            print("Petra takes a couple sips of water and says to herself 'That sure was some quality H2O!'")
            print("Hydrated and feeling like a million bucks, she continues on her path.\n")
            scene_two()
        else:
            print("After a little while, Petra starts feeling weak and dizzy. She realize her adventure is coming to an end.")
            print("She hurrys home, and drinks close to a gallon of water. If only she had gotten some water in time... *** Game Over***\n")
            game_over = input("Stay hydrated friends.  Want to play again? 'Yes or No': ")
            if game_over.lower().strip() == "yes":
                start_game()
            else:
                exit()


# Start of scene two
def scene_two():
    print("After walking for a while, humming on Spice Girls 'Wannabe', she comes across a clearing with a large tree in the middle.")
    print("'Oh what a nice tree, i bet the view if great from up there! On the other hand, i am awfully tired, maybe its better to take a nap under it?' she says to herself.")
    print("What do you think Petra should do, 'Climb' or 'Nap'?")
    nap_or_die = input("Answer: ")
    if nap_or_die == "climb":
        print("Petra rushes to the tree and jumps up on the first branch she can see. With the speed of a skilled little monkey she flyes up branch after branch.")
        print("Well up at the highest point, she is mesmerized by the beautiful view. But when its time to climb down...")
        print("She freezes, only to remember how scared of heights she is. Who knows, maybe she's still up there? ***Game Over***\n")
        game_over = input("Never turn down a nap. Never. Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()
    else:
        print("Petra lays down under the tree. Within minutes, she falls asleep.")
        print("After twenty minutes or so, she wakes up... yawns once or twice, streaches abit and says to herself 'Thats what i call a perfect nap!'")
        print("She gets up, bruches of some grass and dirt and continues on her journey, filled with the magic powers a nap gives you.\n")
        scene_three()

# Start of scene three
def scene_three():
    print("After walking for a while, Petra comes across a berry bush. At this point of our adventure, her tummy was growling like a grizzly bear because she hadent eaten for hours.")
    print("She looked at the berries. Some of them she recognized, she remembered her kindergarden teacher showing them as berries you can eat.")
    print("But some of them she had never seen. 'What should i do now?' she asked herself")
    berries_or_be_burried = input("What do you think? Should she 'Eat all' berries, 'None' of them or only the ones she 'Recognize'? ")
    if berries_or_be_burried.lower().strip() == "recognize":
        print("'Nomnomnom those berries were sooo yummy!' She shouted quietly for herself. With some newfound energy she felt ready to embark on her adventure.\n")
        scene_four()
    elif berries_or_be_burried.lower().strip() == "eat all":
        print("After eating every berries she could see, her tummy started aiking so much she had to run straight home. Guess she should have only eaten the ones she recognized. *** Game Over***")
        game_over = input("The berries got the best of you, dident they? Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()
    elif berries_or_be_burried.lower().strip() == "none":
        print("Who does an adventure on a empty stomach? C'mon now, be serious for once. ***Game Over***\n")
        game_over = input("Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()
    else:
        print("Did you maybe misspell one of the choices? Lets replay it and this time choose 'Eat all', 'None' or 'Recognize'.\n")
        scene_three()

# Start of scene four
def scene_four():
    print("After walking for a while, Petra notices a big ol' snake laying across the road. Petra felt the fear raise in her body.")
    print("She thought 'Should i make a run for it or should i confront the snake?' She staired at the snake for a while, the snake staired back.")
    print("Petra was so afraid of the snake that she couldent move. It's up to you to help her out. ")
    snakes_on_a_path = input("Should she 'run' or 'confront'? ")
    if snakes_on_a_path == "confront":
        print("Petra saves up some curage and finally says 'hey there, how do you do? I have never meet a cobra before.'.")
        print("The snake replied 'Cobra? Bruh you serious? I am a python, little girl.'")
        print("Petra said quickly 'Oh im terribly sorry mr. Python, i guess i watch to much netflix and not enough nature channel.")
        print("The snake said 'Thats okay, guess that applies to most kids nowadays huh?'")
        print("The snake continued 'I can let you pass if you can answer my question correct, deal?'. Petra noded like she's never noded before.")
        print("'The question is: Tuples are immutable. True or False?' said the snake with a grin on his face.")
        tuple_me_this = input("Now it's your time to shine. What should Petra answer, 'True' or 'False'? ")
        if tuple_me_this.lower().strip() == 'true':
            print("'Well done little girl! I'll let you continue now, as promised.' exclaimed the snake joyfully.\n")
            scene_five()
        else:
            print("'Disappointed - yes, suprised - no' said the snake. Petra had no other choice than to go all the way back home. *** Game Over *** ")
            game_over = input("Shame on you...shame on you. Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()
    else:
        print("Petra started running, only to stamble and sprain her wrist. But her adventure was over. *** Game Over ***")
        game_over = input("Sometimes you just gotta face your fears. Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()
        

# Start of scene five
def scene_five():
    print("After walking for a while, Petra comes across a beautiful meadow, with a small pond in the middle.")
    print("All this walking has made her warm and a bath would surely cool her off. But what if there are dangerous animals in the water?")
    pond_pondering = input("Should she take a 'Bath' or 'Continue'? ")
    if pond_pondering.lower().strip() == 'bath':
        print("Petra dips her feet in the water, and she immediately feels something against her foot.")
        print("She twitches and she sees the big ol' snake from the road before in the water.")
        print("The snake looks as suprised as Petra and yells 'You again?'")
        print("The snake continues 'I havent eaten all day and a little girl like you will keep my tummy full for hours.'")
        print("'Please dont eat me, mr. Cob...i mean Python!' Petra shouted.")
        print("The snake replied 'Okay, okay, chill a bit. Snakes got ears too you know.")
        print("...'I tell you what, answer my question correct and i let you live' said the snake.")
        print("The snake thought for a moment and said 'Do you use square brackets or curly brackets for dictionarys?'")
        surly_curly = input("Do you know the answer? Is it '[]' or '{}' ")
        if surly_curly ==  "{}":
            print("'Well done again. I dont really care, i saw a fat toad on the other side, i can eat him.' said the snake and swam away.")
            print("Petra cooled off at the pond for a little while and continued her journey.\n")
            scene_six()
        else:
            print("'Well a deal is a deal' said the snake and swollowed Petra in just one bite. *** Game Over ***")
            game_over = input("Want to play again? 'Yes or No': ")
        if game_over.lower().strip() == "yes":
            start_game()
        else:
            exit()

    else:
        print("Petra thought about it for a sec but decided to continue on her adventure.")
        scene_six()


# Start of scene six
def scene_six():
    print(" ")







# Run all program functions
def main():
    start_game()
    scene_one()
    scene_two()
    scene_three()
    scene_four()
    scene_five()
    scene_six()


main()