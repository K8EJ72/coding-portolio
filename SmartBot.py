## PART A: First Contact

import random

BOT_NAME = "SmartBot" # Wrote a constant for SmartBot's phrases.

print( "=" * 27 )
print( "Welcome to SmartBot v1.0" )
print( "=" * 27 )
print()

# Define variables for greeting.

def main() :
    userName = input(BOT_NAME + ": Hi there! I'm SmartBot. What's your name?: ")
    userAge = int(input(BOT_NAME + ": And how old are you?: "))
    hobby = input(BOT_NAME + ": What is your favourite hobby?: ")
    
    print()

    # Final compiled message including age in 100 years.
    print(BOT_NAME + ": Nice to meet you," , userName + "." , "You are", userAge , "years old and you like" , hobby + ".")
    print(BOT_NAME + ": Did you know you will be 100 years old in" , str(100 - userAge) , "years!")
    print()

    
## PART D: Mood Tracker

    messageCounter = 0
    userMood = 0

    positiveMoods = ["happy", "good", "great", "ecstatic", "elated", "excited"]
    negativeMoods = ["sad", "bored", "upset", "boring", "awful", "bad"]

    # There is a formula after each input to check for these moods.
    # And yes, I regret adding multiple inputs. 


## PART B: Conversation Loop
        
    print(BOT_NAME + ": Let's chat,", userName + "!" , "Type quit to leave.")
    print()

    isChatting = True  # To continue the chat loop. isChatting becomes False to terminate the loop.

    while isChatting == True :
        
        userReply = input(userName + ": ").lower()
        messageCounter += 1

        for goodMood in positiveMoods :
            if goodMood in userReply :
                userMood += 1

        for badMood in negativeMoods :
            if badMood in userReply :
                userMood -= 1
                
        # Makes it easier to do this function rather than copy and paste the same bye message.
        
        def sayBye() : 
            print(BOT_NAME + ": Session summary!")
            print(BOT_NAME + ": You sent " + str(messageCounter) + " messages.")
            print(BOT_NAME + ": Your final mood score is " + str(userMood) + "(" + moodScale + ")" )
            print(BOT_NAME + ": See you soon! ")
            
        if "quit" in userReply or "bye" in userReply :
            sayBye()
            isChatting = False

        # Implemented the random hello phrases from Part C.
        
        elif "hello" in userReply or "hi" in userReply or "hey" in userReply :
            print(BOT_NAME + ": " + randomHello(userName))
            
            greetingsReply = input(userName + ": ").lower()
            messageCounter += 1

            for goodMood in positiveMoods :
                if goodMood in greetingsReply :
                    userMood += 1

            for badMood in negativeMoods :
                if badMood in greetingsReply :
                    userMood -= 1

    
            if "quit" in greetingsReply or "bye" in greetingsReply :
                sayBye()
                isChatting = False
        
            else:
                if "ok" in greetingsReply or "good" in greetingsReply or "great" in greetingsReply :
                    print(BOT_NAME + ": That's good to hear! Let me know if there's anything I can do to make your day better!")
                elif "sad" in greetingsReply :
                    print(BOT_NAME + ": I'm sorry to hear that. Is there anything I can do to help?")
                else:
                    print(BOT_NAME + ": I see! Thanks for telling me how you feel. If there's anything I can do to make your day better, let me know!")

                activityReply =   input(userName + ": ").lower()
                messageCounter += 1

                for goodMood in positiveMoods :
                    if goodMood in activityReply :
                        userMood += 1

                for badMood in negativeMoods :
                    if badMood in activityReply :
                        userMood -= 1
        
                if activityReply == "quit" or activityReply == "bye":
                    sayBye()
                    isChatting = False
            
                else:    
                    if "can you do" in activityReply :
                        print(BOT_NAME + ": I can sing, dance and tell a joke or I have some cool fun facts!")
                        print(BOT_NAME + ": Would you like to see one of these?")
                        print(BOT_NAME + ": I can also track your mood at the end of our conversation together.")
                        print(BOT_NAME + ": Once you've tested out my features, say 'mood'. ")

                        featureLoop = True
                        
                        while featureLoop == True :

                            botFeatures = input(userName + ": ").lower()
                            messageCounter += 1

                            for goodMood in positiveMoods :
                                if goodMood in botFeatures :
                                    userMood += 1

                            for badMood in negativeMoods :
                                if badMood in botFeatures :
                                    userMood -= 1
            
                            if "quit" in botFeatures or "bye" in botFeatures :
                                sayBye()
                                isChatting = False
                                featureLoop = False
                
                            elif "sing" in botFeatures :
                                print(BOT_NAME + ": I would love to sing you a song! Pick a genre: pop, rap, jazz or country. ")

                                songChoice = input(userName + ": ").lower()
                                messageCounter += 1

                                for goodMood in positiveMoods :
                                    if goodMood in songChoice :
                                        userMood += 1

                                for badMood in negativeMoods :
                                    if badMood in songChoice :
                                        userMood -= 1

                                        
                                # Mood rating scale for Part D: Mood Tracker.
    
                                if userMood == 0 :
                                    moodScale = "balanced"
                                elif userMood > 0 :
                                    moodScale = "positive"
                                elif userMood < 0 :
                                    moodScale = "negative"
                    
                                if "quit" in songChoice or "bye" in songChoice :
                                    sayBye()
                                    isChatting = False
                                    featureLoop = False
                
                                
                                elif "pop" in songChoice :
                                    print(BOT_NAME + ": Here is Levitating by Dua Lipa!")
                                    print(BOT_NAME + ": [┘∵]つ🎙️ ♫⋆｡♪ I got you, moonlight, you're my starlight,\n"
                                          "I need you all night, come on, dance with me,\n"
                                          "I'm levitating,\n"
                                          "You, moonlight, you're my starlight,\n"
                                          "I need you all night, come on, dance with me,\n"
                                          "I'm levitating ♫⋆｡♪ ")
        
                                elif "rap" in songChoice :
                                    print(BOT_NAME + ": Here is The Real Slim Shady by Eminem!")
                                    print(BOT_NAME + ": [┘∵]つ🎙 ♫⋆｡♪ I'm Slim Shady, yes, I'm the real Shady,\n"
                                        "All you other Slim Shadys are just imitating,\n"
                                        "So won't the real Slim Shady please stand up,\n"
                                        "Please stand up, please stand up?\n"
                                        "Cause I'm Slim Shady, yes, I'm the real Shady,\n"
                                        "All you other Slim Shadys are just imitating,\n"
                                        "So won't the real Slim Shady please stand up,\n"
                                        "Please stand up, please stand up? ♫⋆｡♪ " )

                                elif "jazz" in songChoice :
                                    print(BOT_NAME + ": Here is At Last by Etta James!")
                                    print(BOT_NAME + ": [┘∵]つ🎙️ ♫⋆｡♪ At laaaaaaast,\n"
                                        "My love has come along, \n"
                                        "My lonely days are over, \n"
                                        "And life is like a song, \n"
                                        "Oh, yeah, yeah,\n"
                                        "At last ♫⋆｡♪ ")

                                elif "country" in songChoice :
                                            print(BOT_NAME + ": Here is Ring of Fire by Johnny Cash. Yeehaw!")
                                            print(BOT_NAME + ": [┘∵]つ🎙️ ♫⋆｡♪ I fell into a burning ring of fire,\n"
                                        "I went down, down, down and the flames went higher,\n"
                                        "And it burns, burns, burns, the ring of fire, the ring of fire. ♫⋆｡♪")

                                else:
                                    print(BOT_NAME + ": Sorry, I don't know any songs from that genre.")
                                    

                            elif "dance" in botFeatures :
                                    print(BOT_NAME + ": └[∵┌] ♫⋆｡♪ Happy dance, happy dance. ♫⋆｡♪ [┐∵]┘")

                            elif "joke" in botFeatures :
                                    print(BOT_NAME + ": Why do divers fall backwards into the sea?")
                                    print(BOT_NAME + ": . . . " )
                                    print(BOT_NAME + ": Because if they fell forward, they'd still be in the boat!")
                                    
                            elif "fact" in botFeatures :
                                print(factsRoulette())

                            elif "mood" in botFeatures :
                                print(BOT_NAME + ": Your mood score is: " + str(userMood) + ". You seem rather " + moodScale + "!")
                            
                            else:
                                print(BOT_NAME + ": Sorry, I am currently unable to perform that action. Please choose either sing, dance or a joke!")
                            
        else:    
            print(BOT_NAME + ": Sorry, I didn't understand that. Try again later!")
            isChatting = False


## PART C: Random Responses


def randomHello(userName) :
    possibleGreetings = ["Hey there, " + userName + ". How are you today?",
                         "Hi, " + userName + "! How's things?",
                         "'Sup, " + userName + "! What's cookin'?",
                         "Greetings, " + userName + ". How art thou faring this fine morn?"]
    return random.choice(possibleGreetings)

def factsRoulette() :
    randomFacts = [BOT_NAME + ": Did you know that the bat cave in The Dark Knight Rises is actually in Wales? Henrhyd Falls.",
                   BOT_NAME + ": Did you know that Roald Dahl, the author, was born in Wales?",
                   BOT_NAME + ": Did you know there's more sheep than people in Wales? Yep, 8.75 million sheep. Baa.",
                   BOT_NAME + ": Did you know that St Patrick, patron saint of Ireland, was most likely Welsh? Not a shred of Irish in him!",
                   BOT_NAME + ": Did you know that there's 641 castles in the whole of Wales? We've always had immaculate taste in homes."]
    return random.choice(randomFacts)
    
main()
