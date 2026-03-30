# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c1 = Character("Lua")
define c2 = Character("Seren")
define c0 = Character("???")
default li_point = 0 #2 or grater is gossip. 0 or 1 is pushover
default li = ""
define y = Character("You")
init python:
    def check_char(li):
        # Comparison is case-sensitive by default
        if li == c1:
            return True
        else:
            return False  
default temp = ""
default temp2 ="" 
screen clickable_sprite_screen():
    imagebutton:
        idle "neutral.jpg"    # Normal image
        hover "close-neutral.png"  # Image when mouse is over it
        xalign 0.5 yalign 0.5      # Position on screen
        
        # Action to perform when clicked
        action Jump("monster") 

# The game starts here.
label check:
    if li_point>=2:
        $li = c2
    elif li_point<2:
        $li = c1

label start:
    play music "game/audio/LANDR-Nilix-The-Pain-of-Two-Warm-Low.mp3"
    scene black
    "Are you serious?"
    "I hate her. You know today, she...!"
    "You can't remember the last time you've been truly happy with your friends."
    "You get that people are imperfect. But you'd expect almost two decades old, you expect people to have SOME self awareness at the very least."
    "It's not your fault everyone in your school are flawed."
    "And who can blame you?"
    "Your 'best friend' [c1], has no backbone. She lets people walk all over her."
    "She never has a stance on {i}anything{/i}. Trying to gossip with her is like talking to ChatGPT. And you know he'll always agree with you."
    "\"She's so nice!\" Yeah, because she has the personality of a wet sponge."
    "You don't want a yes-woman. Her issues, anxiety, and lack of self-confidence isn't your problem anymore. ESPECIALLY after she never listens to your own problems."
    "And your other best friend [c2], isn't so terrible. But she would rather talk to anyone else than you."
    "It's like you've suddenly become the least interesting person in the world."
    "Woe is you!"
    "And with your ego bruised, you're not going to suck it up and spend your time chasing someone who's intent on hanging out with everyone but you."
    "So..."
    scene bg
    "You've been bed-rotting, doing a bit of self-reflection."
    "More about where your life has gone wrong than anything. Because you {i}know{/i} it's not your fault."
    "In your life, the type of people you hate the most are..."
    menu:
        "Gossips.":
            $li_point+=1
        "Yes-men.":
            $li_point+=0
    "Everyone does."
    "Think about the terrible, undeserved things you've endured in your life. Like eye-fucking that hottie in period three english and her not approaching you. Or your situationship not texting you back. Or all the women in your life being bitches."
    "If this is the best time of your life, you'd rather not think about how miserable adulthood will be."
    "When you need to vent, you go to..."
    menu:
        "Messages.":
            "You send paragraphs and paragraphs."
            "You're not messy, like {i}some people{/i}."
        "Instagram notes.":
            "You love your vague instagram notes."
            "Don't hmu. Only real ones know."
            "It's like a test to see if your friends still care about you everytime---like those cheating test videos, mostly scripted but nonetheless your guilty pleasure---And lately they don't."
            $li_point+=1
    "Self-relection is annoying and makes you feel like a loser."
    "You're honestly pissed at [c2]. The only way to get even is to get back at her. You have been..."
    menu:
        "Ignoring her.":
            $li_point+=0
        "Complaining to anyone who'll listen.":
            $li_point+=1
    "You can't stand her! Honestly..."
    if li_point>=2:
        $li = c2
    elif li_point<2:
        $li = c1
    jump phone
label phone:
    "It's three AM, witching hour."
    "It's time to get up to some mischief. You..."
    menu:
        "Check your phone.":
            jump act2
        "Go back to sleep.":
            "It's not worth thinking about anyway."
            "Good night."
            jump end
label act2:
    "You check your phone."
    "No messages. Of course."
    menu:
        "Check old messages.":
            "The last message you sent [c2] was last Thursday."
            "It's almost been a week."
            menu:
                "And she still doesn't remember me???":
                    "This is working you up. This is the opposite of sleep."
                    "Your message exchange has just been a series of asking her to hang out, and her apologizing for missing your messages because she was 'busy'."
                    "You see those instagram posts."
                    "It makes you feel a little pathetic..."
        "Go to sleep.":
            pass
    jump monster_meeting
label monster_meeting:
    "You have trouble falling asleep."
    "You do mange to sleep a litle. By the time you wake, it's still dark out."
    show neutral
    "Going to sleep isn't a option though, because there's something watching you."
    y "What the fuck."
    y "What is that?"
    call screen clickable_sprite_screen
label monster:
    show close-shock
    c0 "Hi."
    "That's like... definitely not human, right?"
    menu:
        "Scream.":
            "You scream. It doesn't do anything."
            "Does your mom not hear you?"
        "Punch it.":
            $temp = "limbs"
        "Run.":
            $temp = "limbs"
    "Your body won't move."
    if temp ="limbs":
        "You try to move your [temp], but they don't as much as twitch."
    menu:
        "Panic.":
            pass
        "Don't panic.":
            "You think carefully about what do."
            "..."
            "Fuck it. Your mind's going blank."
    y "What the fuck. What the fuck?"
    show close-neutral
    if check_char():
        c0 "Hi?"
    else:
        c0 "Hey."
    "Now, you've never been god-fearing, or the superstitious type. But you take back all the hours you've spent bullying those stick-up-their-ass stiffs who do."
    menu:
        "Who are you?":
            y "Who are you?"
        "What are you?":
            y "What are you?"
    if check_char():
        c0 "Hmm, guess?"
    else:
        c0 "You know who I am."
    "Like hell you do."
    "You must be..."
    menu:
        "My guilt.":
            y "A manifestation of my guilt."
        "Death.":
            "This is it."
            y "The grim reaper???"
        "...a friend?":
            y "My new bestie?"
            "Or better yet, a lover?"
    c0 "It's me, [c2]."
    y "This can't be real."
    y "You're not her. You don't even..."
    menu:
        "Have her beauty.":
            $ temp =="love"
        "Look like her.":
            $ temp == "like"
    if temp ="love":
        show close-shy
        "Beauty?"
        "You're lying."
    show close-shock
    c2 "You never call me beautiful to my face."
    "Why's she nitpicking? While she's literally a scary monster hovering above your bed, she's nitpicking you for not complimenting her enough."
    "This is just like her. It's always a weird power play gay chciken game with her. And..."
    menu:
        "You're gay.":
            "It's not your fault every guy in your school is ugly."
            "You never liked her boyfriend anyway. That's your justification."
            y "I'm telling you now."
            c2 "!!!"
            show close-neutral
            y "It's too late, anyway."
        "You're not gay.":
            y "Why does it even matter?"
            "You're not... one of {i}those{/i} poeple."
    y "You're disrupting my sleep."
    y "Just go away."
    c2 "I can't. You wanted me here."
    if temp == "love":
        c2 "You obviosuly feel something for me."
    "I can't go until you tell me how you really feel."
    menu:
        "I resent you.":
            $ temp = "I hate you."
            y "[temp]"
        "I hate you (love.)":
            $ temp = "I love you."
            $ temp2 = "You can't even see her face properly. But just the sight of her has your throat feeling tight, like someone had stuck your airway full of cotton balls. You want to gag on the words. She's beautiful. Even if you kind of hate her right now."
    "She doesn't even let you say it. She just assumes you love her."
    "She's super delusional. Self absorbed. Narcissistic. And every synonym in the book."
    "You wish she would spend more time with you. You need her."
    "And she doesn't need you."
    "She doesn't even care about you."
    "The only version you're getting of her is the one in your head."
    c2 "Then say it to my face."
    if temp = "I love you.":
        "[temp2]"
    y "I [temp]."
    c2 "No."
    y "Fuck you mean no???"
    c2 "Say it to my face."
    menu:
        "No.":
            pass
        "Okay.":
            pass
    y "What?"
    scene bg 
    with dissolve
    "When you look up again, you're alone. And you feel like you can breath again."
    "Your pajamas are damp and sticky under you. It feels different than it did just moments prior. Rougher, and more real."
    "You didn't realize how much you missed the feeling of being able to move."
    "You don't know if you just had a nightmare, or what...?"
    y "What the hell was that?"
    "That... thing. Whatever it was."
    menu:
        "It wasn't real.":
            "It doesn't matter."
            "It's your brain too bored now resorting to fucking with you for entertainment."
            "Like that experiment about people going schizo from staring at a mirror too long."
        "It was real.":
            "[c2] was here. Through that shadowy monster."
            "It's your reality."
    "It means you have to."
    "You..."
    menu:
        "Pick up the phone.":
            "You'll call her."
            y "It's her fault. All of this."
            "You'll let her know every detail of just how much she's hurt you."
            scene bg black with dissolve
            play sound "game/audio/freesound_community-hello-91045.mp3"
            c2 "Hello?"
            if temp == "I hate you.":
                "Ending 2A- Confrontation"
                return
            else:
                "Ending 2B- Confession"
                return
        "Go back to sleep.":
            "It doesn't matter."
            "None of this does."
            "After that whole fiasco, you hate her even more."
            "You just need to sleep it off. Like you do everytime."
            jump end

            
label end:
    scene black
    "Ending 1- sleep"
    return


    
    


        
    

    
    






#am i schizo. accepting im schizo and so depwerate for gossip listeners ill tlak to the monster in my head. 
#r u flriting w me. a little
#my name is c1/c2 to imply manifesrtation of friend

