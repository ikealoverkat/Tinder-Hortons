define j = Character("Jerry")
define t = Character("Tammy")
define b = Character("Bentley")
define m = Character("Monica")
define tb = Character("Boss")
default wage = 10
image bg_bedroom = "images/background_bedroom.png"
image bg_bus_morning = "images/background_busstop.png"
image bg_bus_evening = "images/background_busstopsunset.png"
image bg_interior = "images/background_tinderhortonsinterior.png"
image bg_exterior = "images/background_tinderhortonsexterior.png" 

#import chars
#boss
image boss = "chars_images/boss.png"
#sierra
image sierra = "chars_images/sierra.png"
#jerry
image j = im.Scale("chars_images/jerry.png", 750, 750)
image jm = im.Scale("chars_images/jerry_mad.png", 750, 750)
image js = im.Scale("chars_images/jerry_sad.png", 750, 750)

#tammy
image t = im.Scale("chars_images/tammy.png", 750, 750)
image th = im.Scale("chars_images/tammy_happy.png", 750, 750)
image ts = im.Scale("chars_images/tammy_sad.png", 750, 750)

#bentley
image b = im.Scale("chars_images/bentley.png", 750, 750)
image bh = im.Scale("chars_images/bentley_happy.png", 750, 750)
image bm = im.Scale("chars_images/bentley_mad.png", 750, 750)

#monica
image m = im.Scale("chars_images/monica.png", 750, 750)
image mo = im.Scale("chars_images/monica_ominous.png", 750, 750)
image mh = im.Scale("chars_images/monica_happy.png", 750, 750)
image mho = im.Scale("chars_images/monica_happy_ominous.png", 750, 750)


label start:
    $ wage = 10
    if wage < 5:
        jump badending
    hide boss
    hide sierra
    hide j
    hide js
    hide jm 
    hide t
    hide th
    hide ts
    hide b 
    hide bh 
    hide bm 
    hide m 
    hide mo
    hide mh 
    hide mho

    # intro
    stop music
    play music "audio/mainmusic.mp3" loop fadein 0.5
    scene bg_bedroom
    play sound "audio/alarmsfx.mp3" noloop
    "It’s 10:00 in the morning."
    "Slamming your alarm clock, you realise you were 4 hours late for work."
    stop sound
    "You quickly change and throw on a coat, checking your phone for the next available times for the bus you take to work as you sprint to the station."
    scene bg_bus_morning
    "Luckily for you, the bus comes as you arrive and you board."
    scene bg_exterior
    "You arrive at your workplace, the nearby Tim Hortons, and push open the door."
    scene bg_interior
    "You can’t believe what you see - four raccoons wreaking havoc inside and your boss trying to attack them with a broom! He looks up and notices you."
    show boss at center
    "Boss" "YOU'RE. LATE."

    "Me" "My apologies, sir! It won’t happen again. I depend on these wages to live! I only get paid $10!"

    "Boss" "YOU HAVE ONE LAST CHANCE. KEEP THESE RACCOONS BUSY OR YOU’LL GET. DEDUCTED. PAY."
    
    "Me" "Absolutely sir, I will not let you down."

    "Boss" "YOU BETTER NOT!!!"
    hide boss with dissolve
    "You look around the store and notice your best employee-friend, Sierra. She signals to you and you sneak to her side."
    show sierra at center
    "Sierra" "The boss really hates you, huh?"

    "You nod your head."

    "Sierra" "I figured some things about the raccoons while you were gone, you know, to help you with your assignment..."

    "Me" "What do you mean? What assignment...?"
    
    "Sierra" "How do you not get it?"

    "Me" "If I was smart would I really be working here?"

    "Sierra" "Fair point. He wants you to speed date the raccoons…"

    "You’re shocked. Speed date? Raccoons? RACCOONS?"

    "Me" "You’re kidding, right? He wants me to date animals!"

    "Sierra shakes her head."

    "Me" "Alright, let’s hear your observations..."

    "Sierra" "You see that obese raccoon over there? That’s Jerry, the first racoon."

    "Sierra" "Jerry lost his family in a freak garbage can accident, when 42 pounds of trash landed on Jerry’s mom and his siblings."

    "Sierra" "He still has trauma to this day. He needs a partner who can understand and heal him slowly, without leaving him like his dad did and giving up on him when he believes he’s close."

    "Me" "How do you know all of this?"

    "Sierra" "Don’t question it."

    "Sierra" "The raccoon with a bow is Tammy. She has always been spoiled by her family; collecting the scraps from the finest restaurant trash cans in the world." 

    "Sierra" "She believes that this way of life is normal, and doesn’t believe that raccoons can’t live luxuriously."

    "Sierra" "The raccoon with the wide anime eyes is Bentley. Bentley believes he’s the king of the world and acts accordingly, showing off and competing with the other raccoons."
    
    "Sierra" "He has the battle scars from defeating the local raccoon mafia and never passes up the opportunity to yap about each scar. No wonder he can’t get any girls."

    "Sierra" "The last raccoon, the one with the pink fur, is Monica. She seems really sweet, but I always have this feeling that she could be hiding something... something ominous..."

    # meeting jerry

label jerry:
    hide sierra with dissolve
    stop music
    play music "audio/jerrymusic.mp3" loop fadein 0.5
    "You walk up to Jerry carefully, trying not to scare him. You know nothing about dating other people, let alone savage animals, but you do know how to listen."
    "You sit down at a table close to him, not close enough to scare him, but not far enough for him not to notice you."
    "He notices you staring at him and stares back, his eyes filled with rage (defensive) and fear."

    "Me" "Hey, Jerry... right?"
    show jm  at center
    "Jerry" "What’s it to you?"
    hide jm with dissolve

    menu:
        "Nothing much, I just... lost my parents in an accident this morning.":
            show j at center
            "Me" "I didn’t even have time to grieve before I was kicked to work…"
            hide j
            show js at center
            "There was a small flicker of change in Jerry’s eyes. Sincere, understanding, and guilty." 
            hide js
            show j at center
            "Jerry" "Why should I care?"
            
            "He rolled his eyes, but the sympathy in his eyes was obvious. You could tell he was hurting."
            
            "Your wage increased by $2."

            $ wage = wage + 2
 
            "Your current wage is $[wage]."
            hide j with dissolve
            menu:
                "I’m telling you this because I know what you’re going through.":
                    "Me" "I heard about the accident. The same trash can that killed your family killed mine too."
                    show js at center
                    "Jerry" "Your family got killed by a trash can too! Freaking trash cans..."
                    
                    "He starts to sob uncontrollably." 
                    
                    "In a desperate attempt to end this speed date and make him fall in love with you, you are forced to walk close and hug his furry, smelly body to comfort him."
                    hide js with dissolve 
                    "You gain two dollars." 

                    $ wage = wage + 2

                    "Your current wage is $[wage]."
    

                "Because they were killed by a trash can. A TRASH CAN! Are you serious? That’s hilarious!":
                    show jm at center
                    "Hearing your laughter over his trauma, all the sympathy disappeared. His eyes fill with anger and he pulls out his secret weapon; a shiny silver gun he had found in a trash can loaded with rocks."
                    play sound "audio/explosionsfx.mp3" noloop
                    "He shoots it everywhere, causing more things to break and your boss to crash out."

                    "Me" "Well, that didn’t go well… and now he’s destroying the place… great. Hopefully something good happens soon…"
                    hide jm with dissolve
                    "You lose three dollars."

                    $ wage = wage - 3
  
                    "Your current wage is $[wage]."

        "You’re looking real muscular today.":
            "It was an obvious lie. Eying him up and down, there wasn’t a single muscle in sight."
            show j at center
            "He scoffed. He clearly wasn’t amused."
            hide j
            show jm at center
            "Jerry" "Haha, very funny, now, if you don’t have anything better to do, get lost and stop staring."

            "Me" "Well, that didn’t go well… and now he’s destroying the place… great. Hopefully something good happens soon…"
            hide jm with dissolve
            "You lose two dollars."

            $ wage = wage - 2
  
            "Your current wage is $[wage]."
if wage < 5:
        jump badending
label tammy: 
    stop music
    play music "audio/tammymusic.mp3" loop fadein 0.5
    "After what happened with Jerry, you walk up to the next raccoon with a sigh, Tammy."
    "Me" "Hi, Tammy. I love your bow."
    show th at center
    "Tammy" "I know, isn't it lovely? Where’s yours?"
    hide th with dissolve
    menu:
        "Hey baby, are you a raccoon? Because I'm trash, but I still think you'll dig me.":
            show ts at center
            "Tammy" "Ew, me? Dig you? Who do you think I am? Unless you have chocolate truffles and A4 wagyu beef hidden under that hideous outfit, I don’t settle for anything less."
            "Me" "Um… well… I don’t… But I… do have something you could never find in fancy restaurants trash cans. Love and-"
            "Looking at Tammy, she seems to be losing interest and turning to stare in the reflection of the window instead."
            hide ts 
            show t at center
            "Tammy loses interest and continues causing mayhem around Tim Hortons. You end up getting a four hour screaming lecture from your boss."
            hide t with dissolve
            "You lose three dollars."
            
            $ wage = wage - 3
            "Your current wage is $[wage]."

        "Hey Tammy. Lookin’ good today girl. Love your hair, eyes, whiskers… That bow is magnificent, wanna see mine?":
            show th at center
            "Tammy" "I do amazing today, and every day. You should’ve seen me yesterday actually. My bow is gorgeous, brand new too. Where is your bow?"
            "Me" "Uhh…"
            
            "You needed to think of something to show Tammy fast but having no bow in sight that may be a problem. You quickly look around and your eyes land on a spare hairnet lying on the cashier table. You put on the hairnet quickly."
            hide th
            show t at center
            "Tammy" "…Is that… mesh?"
            
            "Me" "Imported mesh. From an exclusive industrial kitchen in Paris, Ontario."
            hide t
            show th at center
            "Tammy" "I adore it. You have taste. Questionable—but bold. We should collaborate."
            "Tammy ends up collabing with you on a brand new fashion line."
            hide th with dissolve
            "You gain four dollars."
            $ wage = wage + 4
            "Your current wage is $[wage]."
if wage < 5:
        jump badending
label bentley:
    stop music
    play music "audio/bentleymusic.mp3" loop fadein 0.5
    "You're already tired of talking to RACCOONS, but you have to keep on going... anything for the money!"
    show b at center
    "You walk up to the next raccoon, Bentley, excitedly, like a fan getting the one-in-a-lifetime chance to meet their idol, as he is in the process of swinging back and forth on a pendant light."
    hide b
    show bh at center
    "You sit down at a table next to him and hand him a notebook flipped to an empty page. He stops swinging and strikes a pose, a look of confidence and pride on his face."
    hide bh with dissolve
    menu:
        "Oh my gosh. Bentley?! I’m your biggest fan! You’re my idol!":
            "It pains you to say these words to anybody but your favourite singer, Joe-Jo Shewa. Sigh... too bad you never got to meet her before she went wack."
            show bh at center
            "Bentley" "You’ve heard of my heroic achievements?"

            "He points to the abundance of scars on his arm."

            "Bentley" "Have you ever heard the original story and not a retelling? So the raccoon mafia…:"
            
            "Me" "Here we go..."

            "He talks on and on about how he got each of his scars, but you tuned out after his third story. Safe to say he’s obsessed with you now."
            hide bh with dissolve
            "You gain two dollars."

            $ wage = wage + 2

            "Your current wage is $[wage]."

        "Can I have your signature here?":
            show bh at center
            "Bentley" "Of course, anything for a fan! I’ll have you know I have the most BEAUTIFUL handwriting ever recorded!"

            "You hand him a pen and he messily scribbles a raccoon mask."

            "Me" "Your signature..."

            "Bentley" "It’s beautiful right? It was inspired by the time I took down a Rushan raccoon mafia gang-:"

            "Me" "It’s really ugly."
            hide bh
            show b at center
            "You gag in disgust as Bentley stares at you in shock."
            hide b 
            show bm at center
            "Bentley" "...I’m sorry? What are you talking about? I have the finest penmanship in the world!"
            
            "Me" "Seriously, who writes like that? I have a feeling you might be over exaggerating about your so-called talents."

            "Bentley" "Me? Over exaggerating? Do you hear yourself?"

            "Me" "Loud and clear. You’re such an arrogant jerk and you write like a pig"

            "Bentley" "DID YOU JUST CALL ME A PIG??!!"

            "Turns out Bentley has trauma when it comes to pigs. He was forced to speak Pig Latin in his attempt to infiltrate and defeat the Rushan mafia. The word pig was his trigger word unfortunately." 
            
            "Bentley"  "****ay ouyay! Iay ophay ouyay ieday anay xcruciatingeay eathday!"
            play sound "audio/explosionsfx.mp3" noloop
            "You have no clue what he said, but he started attacking the employees, severely injuring Sierra and sending her to the hospital."
            hide bm with dissolve
            "You lose three dollars. Your actions caused Sierra, your best friend, to be taken to the ER. How could you!?"

            $ wage = wage - 3

            "Your current wage is $[wage]."
if wage < 5:
        jump badending
label monica:
    stop music
    play music "audio/monicamusic.mp3" loop fadein 0.5
    "At this point, you're completely sick of rizzing up raccoons."
    show m at center
    "You walk up to Monica, who was chewing on the wires of the OPEN sign hanging on the front window. She turns, noticing you and she smiles."
    hide m
    show mh at center
    "She seems to be the only raccoon there without the intention of destroying the restaurant. She seems so harmless. Maybe this raccoon will be easier to tame."

    "Monica" "Hello! Are you going to have a chat with me too, like the other raccoons?"
    hide mh with dissolve
    menu: 
        "Yeah! You seem very different from these other raccoons; you don’t seem to want to destroy this place!":
            show mh at center
            "Monica" "I know, I’m not crazy like the others. Don't you think so?"
            "Something feels unsettling about her. She seems too perfect..."
            hide mh
            show mho at center
            "You chat with Monica some more. With each sentence and topic change, her vibe became more and more sinister."
            hide mho 
            show mh at center
            "Monica" "So why are you single?"

            "Me" "I’m single because the only person who texts me first is my mom...and even she leaves me on read sometimes."
            hide mh
            show mho at center
            "A smile spreads across her face, not a gentle one, but a threatening one."

            "Monica" "I see. Who else treats you like you aren’t important? You know I’d do ANYTHING for you..."
            "Me" "What do you mean, anything?"
            "Monica" "Anything. Like... chew through your ex’s Wi-Fi cables. Or rearrange your enemy’s furniture slightly every night so they slowly go insane. I can even eat your math homework and make it look like an accident."
            
            "You laugh nervously."
            "Me" "Uhhh... thanks? That’s... really generous?"

            "Monica" "You’re welcome. I’ve already dug a small tunnel under your backyard so I can visit anytime. Isn’t that romantic?"

            "Me" "You know what, Monica? I think I just remembered I left my oven on. At home. In another province."
            
            "Monica giggles manically." 

            "Monica" "Silly! You don’t have an oven. Or a house. You live in a basement suite with your aunt Sharon and a cat named Meatball."

            "Me" "OKAY, HOW DO YOU KNOW THAT"

            "Monica ends up stalking you and forces you to rule the suburbs with her. You end up turning Timmy Hortons into a 24 hour garbage buffet and you're forced to marry her. Clearly your boss isn’t pleased."
            "You lose two dollars."
            hide mho with dissolve

            $ wage = wage - 2

            "Your current wage is $[wage]."

        "Actually, no, I was just leaving. You’re standing right at the exit.":
            stop music
            play music "audio/badendingmusic.mp3" loop fadein 0.5
            show mo at center
            "A look of anger flashes across her face, but it was quickly replaced by a smile." 
            hide mo
            show mh at center
            "Monica" "I’m sorry, but you can’t leave."
            "Me" "I’m tired, okay? I need to go to the spa next door and take a much-needed break."
            hide mh
            show mo at center
            "She looks you in the eyes, sending a chill down your spine."
            hide mo
            show m at center
            "Monica" "I can help. I learned how to massage humans."
            "Me" "There’s no need-"
            hide m
            show mo at center
            "Monica" "SIT. DOWN."

            "Her voice was piercing. You feel your legs go weak and you collapse onto the chair next to her." 

            "She hops down and reaches out towards your shoulders. You’re terrified. You don’t trust this raccoon at all. Your gut instinct tells you to run away from her, to not let her get anywhere near you at all, but you’re paralyzed."
            hide mo
            show mho at center
            "Her hands reach your shoulders. They’re cold and rugged. From this distance, you can smell human blood deep inside of her fur. She rubs your shoulders and with each movement her grip grows stronger and stronger, harsher and harsher. "
            play sound "audio/monicacracksfx.mp3" noloop
            "You can start to hear cracks. Not the relaxing cracks, but the uncomfortable ones. You try to shake her grip away, but she’s stronger than you, somehow." 
            play sound "audio/monicacracksfx.mp3" noloop
            "Your shoulders are hurting a lot now. You try to scream, but nothing comes out. You feel a cool liquid run across your back, maybe from the sweat. You blink, and you feel Monica’s grip slowly leave." 
            hide mho
            show mh at center
            "Monica" "Alright, byebye..."
            hide mh 
            show mo at center
            "She holds the door open for you and you walk out."
            hide mo with dissolve
            scene bg_exterior
            "You’re finally free from this place. Heading for the bus station, you didn’t look back. Not even once."
            "You lose five dollars."
            $ wage = wage - 5
            "Your current wage is $[wage]."
    if wage < 5:
        jump badending
    if wage >= 5:
        jump goodending
        
    
label goodending:
    stop music
    play music "audio/tammymusic.mp3" loop fadein 0.5
    scene bg_interior
    "The clock rings 6PM... Your shift is finally over, and you're done talking to all the raccoons. You check your wages: you're still making money."
    show boss at center
    "Boss" "Adequate work today. You could do better. Go home."
    
    "Me" "Thank you very much, boss!"
    
    "Boss" "GO. HOME."
    hide boss with dissolve
    scene bg_exterior
    "You breathe a sigh of relief, and head for the bus station. What a long day..."
    "--GOOD ENDING--"
    return

label badending: 
    stop music
    play music "audio/badendingmusic.mp3" loop fadein 0.5
    scene bg_interior
    "Suddenly, your boss barges in. You check your wages... NOW IT'S ZERO DOLLARS?! You break into a cold sweat."
    show boss at left
    "Me" "Oh no..."
    hide boss
    show boss at center
    "Boss" "YOU FAILURE! EVEN THE RACCOONS CAN DO BETTER THAN YOU. YOU’RE. FIRED!!!"
    "Me" "I'm so sorry sir... please... How else am I supposed to pay for rent??? I beg of you! Don't fire m-"
    "Boss" "I. DON’T. CARE. GET. OUT. OF. MY. STORE... NOW."
    "Boss" "GO. HOME. Oh wait... haha... you don't HAVE ONE ANYMORE!!"
    hide boss with dissolve
    "--BAD ENDING--"
    return

return