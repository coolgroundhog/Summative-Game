import time #Allows the code to use real-life time in the code
realload = 0#used for lines 13, 14, and 15
score=10#the score for the 10 questions
def questions(ques,ans1,ans2,ans3,ans4,rightans):#parameters set for the question and the 4 answers for multiple choice
    while True:
        global score
        print("-----------------------\n",ques)#prints question
        answer = int(input(print("",ans1,"\n",ans2,"\n",ans3,"\n",ans4)))#prints out multiple answers
        if answer == 1 or answer == 2 or answer == 3 or answer == 4:#i used the number of the answer instead of the full answer because i didn't want the person to type the entire answer down
            if answer == rightans:#if user's input is the right answer
                break
            if answer != rightans:#if user's input isn't the same as 'rightans'
                score-=1
                break

        elif answer != 1 or 2 or 3 or 4:
                print("\nPlease type '1', '2', '3', or '4' for the question numbers.\n")




def blankquestions(blankques,rightblankans):
    while True:
        global score #for some reason it only works if I type "global score" in both question functions
        blankans = input(blankques)
        if str.lower(blankans) in rightblankans:
            break
        else:
            score -=1#if user's input isn't the same as 'rightblankans'
            break

def scores():
    scoreload = 0#just for the fancy game loading
    print("-----------------------\nAll done! Calculating score... beep boop beep boop beep boop...")
    while scoreload <=3:#just a fancy "game loading" simulator
                time.sleep(0.5)
                print("beep")
                time.sleep(0.5)
                print("boop")
                scoreload +=1
    print("Done! Here are your results...\n-----------------------\n| Name:",name,"\n| Date:",time.strftime("%m/%d/%Y"),"\n| Score:",score,"/ 10. ",score*10,"%")#time.strftime("%m/%d/%Y") is for printing the date
    if score == 10:
        print("Letter grade: A. Yay!\n-----------------------")#different outcomes for each grade
    elif score == 9:
        print("Letter grade: A-. Pretty ok!")#different outcomes for each grade
    elif score == 8:
        print("Letter grade: B-. You could've done worse... and better as well.\n-----------------------")#different outcomes for each grade
    elif score == 7:
        print("Letter grade: C. Meh?\n-----------------------")#different outcomes for each grade
    elif score == 6:
        print("Letter grade: D. Oof. You're lucky this wasn't a real test.\n-----------------------")#different outcomes for each grade
    else:#all F
        print("Letter grade: F. Oof. You're lucky this wasn't a real test.\n-----------------------")




def scoreboard():#Scoreboard for textfile
   f = open("scoreboard.txt","a+")
   f.write("\n |" + "Name:"+name+"|  Date:"+ str(time.strftime("%m/%d/%Y"))+"|  Score:"+str(score)+"/ 10. ")
   f.close()
   print("---SCOREBOARD---")
   f = open("scoreboard.txt","r")
   if f.mode == 'r':#if scoreboard.txt is in 'read' mode
       contents =f.read()
       print(contents)#prints out textfile and scoreboard








def again():#for after the first round if they want to play again
    global name
    global score
    while True:
        more = input("Do you still wanna play? (y/n)")
        if more == "y":#yes
            print("Great!")
            name = input("Please type your name again.")
            topics()
            break
        elif more == "n":#no
            print("Aww. Well, bye",name,"!")
            exit()
            break#just in case exit() doesn't work
        else:#if they don't type y/n
            print("Please type y/n.")




def topics():
            global score
            score = 10
            global realload
            global topic
            topic = int(input("\nThere are 4 topics for you to choose:\n1. Random Trivia,\n2. Trick Questions,\n3. Pop culture,\n4. Math & Science.\nWhat do you want to choose? Press the number of the option you want to choose (1,2,3, or 4)"))#gives options for user
            print("Great!\n You have 10 questions to answer.\n-----------------------\nHOW TO PLAY:\nWhen you see multiple answers, type the number of the answer you think is right.\nWhen you don't see any multiple answers but instead see a blank, type down the full answer.\nWe'll show the score at the end.")
            time.sleep(5)
            print("Loading questions...")
            while realload <=3:#just a fancy "game loading" simulator
                time.sleep(1)
                print(".")
                realload +=1
            print("Done! Here are your questions:")
            if topic == 1:#random trivia
                print(" _______  _______ _       ______  _______ _______   ________________ _________       _________ _______ ")#fancy ascii art
                time.sleep(0.2)#fancy "time delay"
                print("(  ____ )(  ___  ) (    /|  __  \(  ___  )       )  \__   __/  ____ )\__   __/\     /|__   __/(  ___  )")#fancy ascii art
                time.sleep(0.2)#fancy "time delay"
                print("| (    )|| (   ) |  \  ( | (  \  ) (   ) | () () |     ) (  | (    )|   ) (  | )   ( |  ) (   | (   ) |")#fancy ascii art
                time.sleep(0.2)#fancy "time delay"
                print("| (____)|| (___) |   \ | | |   ) | |   | | || || |     | |  | (____)|   | |  | |   | |  | |   | (___) |")#fancy ascii art
                time.sleep(0.2)#fancy "time delay"
                print("|     __)|  ___  | (\ \) | |   | | |   | | |(_)| |     | |  |     __)   | |  ( (   ) )  | |   |  ___  |")#fancy ascii art
                time.sleep(0.2)#etc
                print("| (\ (   | (   ) | | \   | |   ) | |   | | |   | |     | |  | (\ (      | |   \ \_/ /   | |   | (   ) |")#fancy ascii art
                time.sleep(0.2)
                print("| ) \ \__| )   ( | )  \  | (__/  ) (___) | )   ( |     | |  | ) \ \_____) (___ \   / ___) (___| )   ( |")#fancy ascii art
                time.sleep(0.2)
                print("|/   \__/|/     \|/    )_)______/(_______)/     \|     )_(  |/   \__/\_______/  \_/  \_______/|/     \|")#fancy ascii art
                time.sleep(1)
                questions("What's the largest freshwater lake in the world?", "1.Great Slave Lake","2.Lake Ontario", "3.Lake Superior","4. Caspian Sea (kind of classified as a lake)",4)
                blankquestions("What's the 3-letter airport code for Los Angeles? _ _ _ (e.g. Hong Kong = HKG)", "lax")
                questions("Is there an American state that begins with 'p'?", "1.Yes", "2.No", "3.There used to be, but the state's name got changed","4.I don't have Google Maps how am I supposed to know", 1)
                questions("What bird bone is known as the 'wishbone'?","1.Vertebrae","2.Humerus","3.Collarbone","4.Skull",3)
                questions("How much does the adult giraffe heart weigh?","1.20lbs","2.25lbs","3.10lbs","4.Jeez at least I'm a normal person that isn't even supposed to know things like this",2)
                questions("How many mother sauces are there in classical French cuisine?","1.2","2.5","3.6","4.7",2)
                questions("How many years are in a score?","1.10","2.20","3.40","4.what even is this question why would i ever need to know that in any scenario ever",2)
                questions("What was the first planet to be discovered by a telescope?","1.Venus","2.Mars","3.Jupiter","4.Uranus",4)
                blankquestions("According to Wikipedia, what is the most common word?____","the")
                blankquestions("What does the N in NATO stand for? _ _ _ _ _","north")#all the random trivia questions

            elif topic == 2:#trick questions
                print(" __ __|     _)        |          _ \                      |   _)                     ")#fancy ascii art
                time.sleep(0.2)
                print("    |   __|  |   __|  |  /      |   |  |   |   _ \   __|  __|  |   _ \   __ \    __| ")
                time.sleep(0.2)
                print("    |  |     |  (       <       |   |  |   |   __/ \__ \  |    |  (   |  |   | \__ \ ")
                time.sleep(0.2)
                print("   _| _|    _| \___| _|\_\     \__\_\ \__,_| \___| ____/ \__| _| \___/  _|  _| ____/ ")
                time.sleep(1)
                questions("If there are 3 apples on the table and you take 2, how many do you have?","1.1","2.2","3.3","4.4",3)
                questions("Divide 30 by a half and add 10. What do you have left? ___","1.A number","2.An answer","3.An integer","4.How is this even fair all of the answers are correct",5)#just to mess them up
                questions("How many months have 28 days?","1.1","2. Depends if it's a leap year or not","3.12","4.0",3)
                blankquestions("Mount ___ was the highest in the world before Mount Everest was discovered","everest")
                questions("Does England have a 4th of July?","1.Yes","2.No","Who's england","England is my city",1)
                questions("If a plane crashes on the border of the US. and Canada, where do the survivors get buried?","1.U.S.","2.Canada","3.Neither","4.In the sea",3)
                questions("Is 1+1 2??","1.It's a trick question so definitely","2.It's a trick question and you're using reverse psychology to trick me into choosing number 1, so no, 1+1 does not equal 2","3.You're trying to outsmart me into saying it's '2' because '2' sounds smarter, well guess what, i choose neither","4.what",1)
                questions("How many loaves of bread can you put into an empty shopping cart?____","1.1","2.200","3.300","4.4",1)
                questions("How many times can you subtract 10 from 100?","1.10","2.5","3.60","4.once",4)
                questions("If an electric train is traveling south, which way is the smoke going?","1.North","2.South","3.West","4.What smoke",4)
                scores()

            elif topic == 3:#pop culture
                print("__________               _________       .__   __                       ")#fancy ascii art
                time.sleep(0.2)
                print("\______   \____ ______   \_   ___ \ __ __|  |_/  |_ __ _________   ____ ")
                time.sleep(0.2)
                print(" |     ___/  _ \ \____ \ /    \  \/|  |  \  |\   __\  |  \_  __ \_/ __ \ ")
                time.sleep(0.2)
                print(" |    |  (  <_> )  |_> > \     \___|  |  /  |_|  | |  |  /|  | \/\  ___/")
                time.sleep(0.2)
                print(" |____|   \____/|   __/   \______  /____/|____/__| |____/ |__|    \___  >")
                time.sleep(0.2)
                print("                |__|             \/                                   \/ ")
                blankquestions("Name a grass starter in Pokemon (not evolved).", ["bulbasaur","chikorita","sceptile","turtwig","snivy","chespin","rowlet"])
                questions("Who is the oldest of the Kardashian siblings?","1.Khloe","2.Kim","3.Kourtney","Rob",3)
                blankquestions("Released in 2017, which teen drama TV series is based on characters by Archie Comics? _________","riverdale")
                questions("Besides Lala Land and All About Eve, which movie received the most oscar nominations (14)?","1.Gone with the wind","2.Mary Poppins","3.The Emoji Movie","4.Titanic",4)
                questions("Who is the 'King of Pop'?","1.Michael Jackson","2.David Bowie","3.Bruno Mars","Prince",1)
                questions("Who won the FIFA World Cup in 2014?","1.Brazil","2.France","3.Italy","4.Germany",4)
                questions("'Hasta la vista, baby' is said by who?","1.The T-800",'2.The T-100',"3.The T-X","4.The T-1000",1)
                questions("Who was responsible for inspiring Katy Perry's 'I Kissed a Girl?'","1.Angelina Jolie","2.Brigitte Bardot","3.Scarlett Johansson","4.Rihanna",3)
                blankquestions("'There's vomit on his sweater already, mom's _____'","spaghetti")
                blankquestions("'She said ___ I am not afraid to, die'","baby")
            elif topic == 4:#math and science
                print("┌┬┐┌─┐┌┬┐┬ ┬   ┬   ╔═╗┌─┐┬┌─┐┌┐┌┌─┐┌─┐")#fancy ascii art
                time.sleep(0.2)
                print("│││├─┤ │ ├─┤  ┌┼─  ╚═╗│  │├┤ ││││  ├┤ ")
                time.sleep(0.2)
                print("┴ ┴┴ ┴ ┴ ┴ ┴  └┘   ╚═╝└─┘┴└─┘┘└┘└─┘└─┘")
                time.sleep(1)
                questions("One day, a person went to a horse racing area. Instead of counting the number of humans an horses, he counted 74 heads and 196 legs. How many humans and horses were there?", "1.37 humans & 98 horses", "2.24 horses and 50 humans", "3.31 horses and 74 humans", "4.24 humans and 50 horses",2)
                questions("What is dehydration hydrolysis used for?","1. Breaking up disaccharides","2. Building polypeptides","3. Building polysaccharides","4. 'Dehydration hydrolysis' is made up",4)#4 is rightans
                questions("What's the only place in this world who's fahrenheit and celsius degrees can be equal?","1.Alaska at -50 degrees","2.Antarctica at -40 degrees","3.Hawaii at 100 degrees","4.Anywhere that exceeds freezing point",2)
                questions("The region of DNA in prokaryotes to which RNA polymerase binds most tightly is the:","1.Promoter","2.Poly C center","3.Enhancer","4.Operator site",1)
                questions("Name a transition metal.","1.Aluminum","2.Gallium","3.Xenon","4.Americium",4)
                questions("Is all radioactivity man-made?","1.Yes","2.No","3.Sometimes","4.Maybe sometimes not really no definitely yes maybe absolutely not no",2)
                questions("Which atom is considered stable with less than 8 electrons in their outer shell?","1.Lithium","2.Phosphorus","3.Boron","4.Fluorine",3)
                blankquestions("What 'ology' is the study of birds?","Ornithology")
                questions("What is the largest asteroid in the solar system?","1.Ceres","2.Vesta","3.Hermes","4.Juno",1)
                questions("What is 2+2?", "1.2","2.1","4.3","3.4",3)
            scores()
            scoreboard()#prints out scoreboard
            again()#asks if they want to do it again


while True:
    print("Hello! Do you wanna play...")
    time.sleep(1)
    print("  ____  _____  _____          _   _ _  _____ \n |  _ \|  __ \|_   _|   /\   | \ | ( )/ ____|\n | |_) | |__) | | |    /  \  |  \| |/| (___  \n |  _ <|  _  /  | |   / /\ \ | . ` |  \___ \ \n | |_) | | \ \ _| |_ / ____ \| |\  |  ____) |\n |____/|_|  \_\_____/_/    \_\_| \_| |_____/ ")#ascii art
    time.sleep(0.5)
    playquiz = input(" ____  _____            _____ _   _ _______ ______           _____ ______ _____   _____ \n|  _ \|  __ \     /\   |_   _| \ | |__   __|  ____|   /\    / ____|  ____|  __ \ / ____|\n| |_) | |__) |   /  \    | | |  \| |  | |  | |__     /  \  | (___ | |__  | |__) | (___  \n|  _ <|  _  /   / /\ \   | | | . ` |  | |  |  __|   / /\ \  \___ \|  __| |  _  / \___ \ \n| |_) | | \ \  / ____ \ _| |_| |\  |  | |  | |____ / ____ \ ____) | |____| | \ \ ____) |\n|____/|_|  \_\/_/    \_\_____|_| \_|  |_|  |______/_/    \_\_____/|______|_|  \_\_____/    ?\nType y / n") #Gives option if they want to play
    if str.lower(playquiz) == "y":
        while True:
            global name
            name = input("Ok, cool! What's your name?")
            print("Great,",name,"!")
            topics()
            break
        break

    elif playquiz == "n":#if they don't want to play
        print("Well, that sucks. Bye!")
        exit()#quits code
        break#just in case exit() doesn't work. breaking the loop is better than having the code loop back again
    else:
        print("Please type y / n.")
