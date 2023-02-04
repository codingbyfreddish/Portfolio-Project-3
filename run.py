"""
Welcome to my adventure game.
Hope you will enjoy it!
"""

import time


def start_game():
    """
    Introduction. User name and confirmation to start game
    """
    print("Hey there! First things first, what is your name?")
    global name
    name = input("Name:\n")
    print(f"{name}?? Well, i've heard worse i guess... "
          "who cares about names anyway, huh?\n")
    print(f"So {name} are you ready for an adventure? 'Yes' or 'No'")
    answer = input("Answer:\n")
    if answer.lower().strip() == "yes":
        print(f"Buckle up {name}, you my friend are in for an epic "
              "adventure!\n")
        time.sleep(2)
        scene_one()
    elif answer.lower().strip() == "no":
        print("Had a feeling you dident have what it takes."
              "Welcome back when you do.")
        exit()
    else:
        print("Did you maybe misspell one of the choices? Lets try again..\n")
        time.sleep(1)
        start_game()


def scene_one():
    """
    Start of the adventure, scene one
    """
    print("A little girl, named Petra, is wandering through the forest when "
          "she comes across a fork in the path.")
    print("She must decide whether to take the path to the left or the path "
          "to the right.")
    answer = input("Will she go 'Left' or 'Right':\n")
    if answer.lower().strip() == "left":
        time.sleep(1)
        print("Petra takes the left path. After walking for a while, "
              "she comes across a dark cave.")
        print("The cave looks scary and Petra gutfeeling says "
              "'don't go in there'.")
        print("But at the same time what if the cave contains a big, "
              "old tresure chest filled with gold and what not?")
        print("Petra stands infront of the cave not sure what to do, "
              "can you help her choose?")
        cave_or_not = input("'Go inside' or 'Continue':\n")
        if cave_or_not.lower().strip() == "go inside":
            time.sleep(1)
            print("Petra goes inside the dark, scary cave... and was never "
                  "seen again. ***Game Over***\n")
            game_over = input("Dont underestimate your gutfeeling. Want to "
                              "play again? 'Yes or No':\n")
            if game_over.lower().strip() == "yes":
                print("\n")
                time.sleep(1)
                scene_one()
            elif game_over.lower().strip() == "no":
                exit()
            else:
                print("Did you maybe misspell one of the choices? Lets try "
                      "again...\n")
                time.sleep(1)
                scene_one()
        elif cave_or_not.lower().strip() == "continue":
            print("Petra choose to trust her gut and wanders away from "
                  "the cave.\n")
            time.sleep(1)
            scene_two()
        else:
            print("Did you maybe misspell one of the choices? Lets try "
                  "again...\n")
            time.sleep(1)
            scene_one()
    elif answer.lower().strip() == "right":
        print("Petra takes the right path. After walking for a while, she "
              "comes across a babbling brook.")
        print("She thinks for herself 'I am mighty thirsty, maybe i should "
              "drink alittle bit of water before continuing on my journey?'")
        drink_or_dont = input("'Drink' or 'Dont':\n")
        if drink_or_dont.lower().strip() == "drink":
            time.sleep(1)
            print("Petra takes a couple sips of water and says to herself "
                  "'That sure was some quality H2O!'")
            print("Hydrated and feeling like a million bucks, she continues "
                  "on her path.\n")
            time.sleep(1)
            scene_two()
        elif drink_or_dont.lower().strip() == "dont":
            time.sleep(1)
            print("After a little while, Petra starts feeling weak and dizzy. "
                  "She realize her adventure is coming to an end.")
            print("She hurrys home, and drinks close to a gallon of water. "
                  "If only she had gotten some water in time... "
                  "*** Game Over***\n")
            if game_over.lower().strip() == "yes":
                print("\n")
                time.sleep(1)
                scene_one()
            elif game_over.lower().strip() == "no":
                exit()
            else:
                print("Did you maybe misspell one of the choices? Lets try "
                      "again...\n")
                time.sleep(1)
                scene_one()

    else:
        print("Did you maybe misspell one of the choices? Lets try again...\n")
        time.sleep(1)
        scene_one()


def scene_two():
    """
    Start of scene two
    """
    print("After walking for a while, humming on Spice Girls 'Wannabe', "
          "she comes across a clearing with a large tree in the middle.")
    print("'Oh what a nice tree, i bet the view if great from up there! "
          "On the other hand, i am awfully tired, maybe its better to take "
          "a nap under it?' she said to herself.")
    print("What do you think Petra should do, 'Climb' or 'Nap'?")
    nap_or_die = input("Answer:\n")
    if nap_or_die.lower().strip() == "climb":
        time.sleep(1)
        print("Petra rushes to the tree and jumps up on the first branch "
              "she can see. With the speed of a skilled little monkey she "
              "flyes up branch after branch.")
        print("Well up at the highest point, she is mesmerized by the "
              "beautiful view. But when its time to climb down...")
        print("She freezes, only to remember how scared of heights she is. "
              "Who knows, maybe she's still up there? ***Game Over***\n")
        game_over = input("Never turn down a nap. Never. Want to play again? "
                          "'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            print("\n")
            time.sleep(1)
            scene_one()
        elif game_over.lower().strip() == "no":
            exit()
        else:
            print("Did you maybe misspell one of the choices? Lets try "
                  "again...\n")
            time.sleep(1)
            scene_two()
    elif nap_or_die.lower().strip() == "nap":
        print("Petra lays down under the tree. Within minutes, she falls "
              "asleep.")
        print("After twenty minutes or so, she wakes up... yawns once or "
              "twice, streaches abit and said to herself 'Thats what i call a "
              "perfect nap!'")
        print("She gets up, bruches of some grass and dirt and continues "
              "on her journey, filled with the magic powers a nap "
              "gives you.\n")
        time.sleep(1)
        scene_three()
    else:
        print("Did you maybe misspell one of the choices? Lets try again...\n")
        time.sleep(1)
        scene_two()


def scene_three():
    """
    Start of scene three
    """
    print("After walking for a while, Petra comes across a berry bush. "
          "At this point of our adventure, her tummy was growling like a "
          "grizzly bear because she hadent eaten for hours.")
    print("She looked at the berries. Some of them she recognized, she "
          "remembered her kindergarden teacher showing them as berries you "
          "can eat.")
    print("But some of them she had never seen. 'What should i do now?' "
          "she asked herself")
    berries_or_be_burried = input("What do you think? Should she 'Eat all' "
                                  "berries, 'None' of them or only the ones "
                                  "she 'Recognize'?\n")
    if berries_or_be_burried.lower().strip() == "recognize":
        time.sleep(1)
        print("'Nomnomnom those berries were sooo yummy!' She shouted quietly "
              "for herself. With some newfound energy she felt ready to "
              "embark on her adventure.\n")
        scene_four()
    elif berries_or_be_burried.lower().strip() == "eat all":
        time.sleep(1)
        print("After eating every berries she could see, her tummy started "
              "aiking so much she had to run straight home. Guess she should "
              "have only eaten the ones she recognized. *** Game Over***")
        game_over = input("The berries got the best of you, dident they? "
                          "Want to play again? 'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            time.sleep(1)
            scene_one()
        elif game_over.lower().strip() == "no":
            exit()
        else:
            print("Did you maybe misspell one of the choices? Lets try "
                  "again...\n")
            time.sleep(1)
            scene_three()
    elif berries_or_be_burried.lower().strip() == "none":
        print("Who does an adventure on a empty stomach? C'mon now, be "
              "serious for once. ***Game Over***\n")
        game_over = input("Want to play again? 'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            time.sleep(1)
            scene_one()
        elif game_over.lower().strip() == "no":
            exit()
        else:
            print("Did you maybe misspell one of the choices? Lets "
                  "try again...\n")
            time.sleep(1)
            scene_three()


def scene_four():
    """
    Start of scene four
    """
    print("After walking for a while, Petra notices a big ol' snake laying "
          "across the road. Petra felt the fear raise in her body.")
    print("She thought 'Should i make a run for it or should i confront the "
          "snake?' She staired at the snake for a while, the snake staired "
          "back.")
    print("Petra was so afraid of the snake that she couldent move. It's up "
          "to you to help her out. ")
    snakes_on_a_path = input("Should she 'run' or 'confront'?\n")
    if snakes_on_a_path == "confront":
        time.sleep(1)
        print("Petra saves up some curage and finally said 'hey there, how do "
              "you do? I have never meet a cobra before.'.")
        print("The snake replied 'Cobra? Bruh you serious? I am a python, "
              "little girl.'")
        print("Petra said quickly 'Oh im terribly sorry mr. Python, i guess "
              "i watch to much netflix and not enough nature channel.'")
        print("The snake said 'Thats okay, guess that applies to most kids "
              "nowadays huh?'")
        print("The snake continued 'I can let you pass if you can answer my "
              "question correct, deal?'. Petra noded like she's never noded "
              "before.")
        print("'The question is: Tuples are immutable. True or False?' said "
              "the snake with a grin on his face.")
        tuple_me_this = input("Now it's your time to shine. What should Petra "
                              "answer, 'True' or 'False'?\n")
        if tuple_me_this.lower().strip() == 'true':
            time.sleep(1)
            print("'Well done little girl! I'll let you continue now, as "
                  "promised.' exclaimed the snake joyfully.\n")
            time.sleep(1)
            scene_five()
        elif tuple_me_this.lower().strip() == 'false':
            print("'Disappointed - yes, suprised - no' said the snake. "
                  "Petra had no other choice than to go all the way back "
                  "home. *** Game Over *** ")
            game_over = input("Shame on you...shame on you. Want to play "
                              "again? 'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            time.sleep(1)
            scene_one()
        elif game_over.lower().strip() == "no":
            exit()
        else:
            print("Did you maybe misspell one of the choices? Lets "
                  "try again...\n")
        time.sleep(1)
        scene_four()
    elif snakes_on_a_path == "run":
        print("Petra started running, only to stamble and sprain her wrist. "
              "But her adventure was over. *** Game Over ***")
        game_over = input("Sometimes you just gotta face your fears. Want to "
                          "play again? 'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            time.sleep(1)
            scene_one()
        else:
            exit()
    else:
        print("Did you maybe misspell one of the choices? Lets try again...\n")
        time.sleep(1)
        scene_four()


def scene_five():
    """
    Start of scene five
    """
    print("After walking for a while, Petra comes across a beautiful meadow, "
          "with a small pond in the middle.")
    print("All this walking has made her warm and a bath would surely cool "
          "her off. But what if there are dangerous animals in the water?")
    pond_pondering = input("Should she take a 'Bath' or 'Continue'?\n")
    if pond_pondering.lower().strip() == 'bath':
        time.sleep(1)
        print("Petra dips her feet in the water, and she immediately felt "
              "something against her foot.")
        print("She twitches and she sees the big ol' snake from before"
              "in the water.")
        print("The snake looks as suprised as Petra and yells 'You again?'")
        print("The snake continues 'I havent eaten all day and a little girl "
              "like you will keep my tummy full for hours.'")
        print("'Please dont eat me, mr. Cob...i mean Python!' Petra shouted.")
        print("The snake replied 'Okay okay, chill a bit. Snakes got ears too "
              "you know.")
        print("...'I tell you what, answer my question correct and i let you "
              "live.' said the snake.")
        print("The snake thought for a moment and said 'Do you use square "
              "brackets or curly brackets for dictionarys?'")
        surly_curly = input("Do you know the answer? Is it '[]' or '{}'?\n")
        if surly_curly.lower().strip() == "{}":
            time.sleep(1)
            print("'Well done again. I dont really care, i saw a fat toad on "
                  "the other sideof the pond, i can eat him.' said the "
                  "snake and swam away.")
            print("Petra cooled off at the pond for a little while and then "
                  "continued her journey.\n")
            scene_six()
        elif surly_curly.lower().strip() == "[]":
            time.sleep(1)
            print("'Well a deal is a deal' said the snake and swollowed Petra "
                  "in just one bite. *** Game Over ***")
            game_over = input("Want to play again? 'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            time.sleep(1)
            scene_one()
        else:
            exit()

    elif pond_pondering.lower().strip() == 'continue':
        time.sleep(1)
        print("Petra thought about it for a second but decided to continue "
              "on her adventure, time is precious you know")
        time.sleep(1)
        scene_six()
    else:
        print("Did you maybe misspell one of the choices? Lets try again...\n")
        time.sleep(1)
        scene_five()


def scene_six():
    """
    End of the game, start of scene six
    """
    print("After walking for a while, Petra comes across a small cabin in the "
          "woods. It began to get pretty late and the sky was getting darker "
          "by the minute.")
    print("She thought for herself 'It's getting close to bedtime, maybe i "
          "should knock on this door and see if they can give me a ride home?")
    print("And then she thought: '...then again what adventure would that be? "
          "Maybe i'll just continue?")
    hardknock_life = input("Should Petra 'Knock' on the door or 'Continue'?\n")
    if hardknock_life.lower().strip() == "knock":
        time.sleep(1)
        print("Petra knocks on the door. After a couple of seconds a old man "
              "opens.. 'Who it is'? said a raspy, irritated voice.")
        print("Petra was a little restricted to strangers, as kids should be, "
              "said: 'Hey there mister, its getting late and im a long way "
              "from home...")
        print("'...could you give me a ride home?' she said with a somewhat "
              "squeaky voice.")
        print("The old man turned and yelled 'Hey Barbra, we got a little "
              "visitor!'")
        print("And from somewhere inside Petra could hear a ladys voice "
              "'Oh George what are you yelling about now?'")
        print("The old lady stepped up to Petra and said 'Now look at you, "
              "what a sweet little girl, are you hungry?'")
        print("And Petra was hungry, had been a while since she ate them "
              "berries. But eating dinner at strangers?")
        stranger_danger = input("Should Petra eat dinner at the strangers?"
                                " 'Yes' or 'No'\n")
        if stranger_danger.lower().strip() == "yes":
            time.sleep(1)
            print("'Yes mam, im hungry' said Petra. And the old lady reply "
                  "'Of course you are dear. Come in, we're having hot dogs'.")
            print("The old lady continued 'My name is Barbra and this is my "
                  "husband George. And after we have eating we can walk with "
                  "you home.")
            print("The hot dogs were delicous and Petra must have eating 10 "
                  "of them.")
            print("After dinner Petra and her new friends George and Barbra "
                  "took a walk home to Petras house, it only took about "
                  "10minutes.")
            print("Turns out Petras long adventure only took her to the end "
                  "of the street.")
            print("Guess the moral of the story is: You dont have to look "
                  "far for adventure, life is a big adventure in it self.")
            time.sleep(2)
            print("******* THE END *******")
            print(f"Well played {name}! Thanks to you Petra had a magic day "
                  "and got home safe and sound.")
            print("Thank you for playing my adventure game, you rock! TBH i "
                  "never thought you would make it.")
            print(f"One last thing, {name}... naa, nevermind. It wasent "
                  "anything important anyway.")
            game_over = input("Want to play again? 'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            time.sleep(2)
            scene_one()
        else:
            time.sleep(1)
            print("Once again, THANK YOU FOR PLAYING. Take care.")
            exit()

    elif hardknock_life.lower().strip() == "continue":
        print("'Hell no, stranger danger!' Petra said to herself and walked "
              "past the cabin.")
        print("After walking just a couple of minutes it had gotten even "
              "darker.")
        print("Every little adventurer needs to know when its time to call "
              "it quits.")
        print("Petra reached down her pocket and picked up her brand new "
              "cellphone.")
        print("'Mommy, daddy, can you come and pick me up! I'm just past the "
              "big old cabin down the road' Petra said.")
        print("'Of course, honey' her mom replied.")
        print("Soon Petra was home, safe and sound. Her dad gave her some hot "
              "dogs he just had made, they were delicous.")
        time.sleep(2)
        print("******* THE END *******")
        print("So you dident have the guts to knock on the cabindoor, did "
              f"you {name}?")
        print("But you did get Petra home safe and safe, which is all that "
              "matters!")
        print(f"So congrats {name}, you finished my adventure game like a "
              "champion! (Kinda)")
        game_over = input("Want to play again? 'Yes or No':\n")
        if game_over.lower().strip() == "yes":
            time.sleep(2)
            scene_one()
        else:
            time.sleep(1)
            print("Once again, THANK YOU FOR PLAYING. Take care.")
            exit()

    else:
        print("Did you maybe misspell one of the choices? "
              "Lets try again...\n")
        time.sleep(1)
        scene_six()


def main():
    """
    Run all program functions
    """
    start_game()
    scene_one()
    scene_two()
    scene_three()
    scene_four()
    scene_five()
    scene_six()


main()
