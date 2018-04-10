pdefine player_name = ""

#Protagonist
define player = DynamicCharacter("player_name", color=(192,64,64,255))

#characters
define etsuko = Character("Etsuko", who_color="#e4a9c6") #Etsuko
define tavo = Character("Tavo", who_color="#2a42ba") #Tavo
define camila = Character("Camila", who_color="#00007f") #Camila
define ivy = Character("Ivy", who_color="#2DC8FD") #Ivy
define cancino = Character("Cancion", who_color="#CC3333") #Cancino
define hagane = Character("Hagane", who_color="#4AC7D8") #Hagane
define pablo = Character("Pablo", who_color="#C2D84A") #Pablo

define sex = True
define choose_tea = False

define etsuko_choices = 0
define hagane_choices = 0
define camila_choices = 0
define pablo_choices = 0

define told_etsuko = False

label start:

    label game_start:
        scene black

        "Welcome to 'A Shared Cup Of Tea's demo!"
        "Let's start by defining your character a little, okay?"

        "Do you prefer your character to be a boy or a girl?"
        menu:
            "Boy":
                pass
            "Girl":
                $ sex = True
        "Okay, now, we need a name!"
        label name_choose:
            $ player_name = renpy.input("Choose your name: ")
            $ player_name = player_name.strip()

        if player_name == "your name":
            "Good movie, bad joke."
            jump name_choose
        if player_name == "":
            "You can't go by without a name!"
            jump name_choose

        "Okay, we're ready, but first lemme remind you."
        "This is just a DEMO, as such it doesn't reflect the history or quality of the finished product."
        "If you have any opinions you'd like to give to the dev's, or any suggestions or anything like that, we're reachable at facebook.com/etsukogamesandcode/ !"
        "Now, I'll drop you off in the middle of a conversation, good luck!"

        stop music fadeout 3.0
        scene white
        with Dissolve(5)
        scene black
        with Dissolve(1)

    label scene_01:
        play music "na i sho.mp3" fadein 1
        $ renpy.pause(1.0)
        hagane "And then she sent an audio begging for help!"
        "hahahahaha!"
        $ renpy.pause(1.0)
        pablo "So, we all agree he's a furry, right?"
        etsuko "Noooooo!"
        $ renpy.pause(1.0)
        ivy "Wait, is %(player_name)s asleep?"
        if sex:
            camila "I think she is..."
        else:
            camila "I think he is..."
        $ renpy.pause(1.0)
        tavo "Heeeey... Wake up..."
        if sex:
            cancino "Shouldn't we let her sleep?"
        else:
            cancino "Shouldn't we let him sleep?"
        $ renpy.pause(1.0)
        if sex:
            hagane "For fuck's sake Etsuko! You're so boring she fell asleep!"
        else:
            hagane "For fuck's sake Etsuko! You're so boring he fell asleep!"
        etsuko "How is this my fault again?"
        $ renpy.pause(1.0)
        stop music fadeout 3
        scene white
        with Dissolve(3)
        scene bg etsuko room
        with Dissolve(1.5)
        play music "autumn breeze.mp3" fadein 1.5
        "I woke up on a bed, that I'm not sure I recognize..."
        "Wasn't I hanging up with the group?"
        "D-Did I fall asleep?"
        "I was on a bed with white, soft, mattresses and lots of pillows, in a light grey room that had the bed, some book shelves, a closet and some wooden chairs."
        "I exited the bed trying to not make a mess out of it and exited the room."
        scene black
        with Dissolve(0.75)
        scene bg etsuko kitchen
        with Dissolve(0.75)
        show etsuko at center
        with Dissolve(.5)
        etsuko "Look who woke up!"
        show etsuko at left
        show ivy at right
        with Dissolve(.5)
        show etsuko 1 1
        etsuko "Look who woke up!"
        "Etsuko was standing next to the door I came from, she was wearing a white apron with pink hearts print all over it."
        ivy "Finally!"
        "Ivy was sitting down on a sofa sorrounding a rectangular coffee table with the rest of the group."
        ivy "How did you end up asleep like that?"
        player "I'm sorry guys, college has been rough on me lately..."
        "As I said that I approached the group and sat down with them."
        etsuko "You made poor little Hagane carry you back here on his back."
        "I looked at Hagane who was taken back by Etsuko revealing that detail."
        menu:
            "You carried me back...?":
                hagane "Don't say more than you need Etsuko, for fuck's sake."
                "Hagane said that to Etsuko, all flustered, as Etsuko got away from him pulling her tounge out cutely."
                "Everybody laughed at the interaction."
            "Thanks Hagane, I owe you one.":
                hagane "I-It's no problem %(player_name)s."
                "He said that as he stroked his hair and looked away."
                hagane "I know you'd have done the same."
        etsuko "You need to fall asleep on us more often, his face while carrying you was GOLD!"
        hagane "Shut the heck up, star boy"
        "He stood on the start of his feet ready to jump in case Etsuko said something again."
        etsuko "That's honestly freaking adorable, I'm actually jealous."
        "Etsuko said as he hid rapidly behind me, knowing Hagane would probably stand and follow him."

        "It was a nice moment, Pablo was there laughing, Camila was shatting with Ivy, Cancino was trying to tease Hagane..."
        "Isn't someone missing?"

        tavo "ETSUKOOOO"
        "Someone yelled from the kitchen desperately, as scaredy-cat Etsuko jumped and pulled my shirt as she was scared out of her heart."
        etsuko "Holy shit, Tavo, don't scare me like that, what happened?"
        "Etsuko said letting my shirt go and walking towards a door and holding her chest with both hands."
        tavo "I can't get your coffee machine to woooork"
        "Tavo came out of the kitchen with a sad expression."
        tavo "oh.."
        tavo "Oh..."
        tavo "Look at who-"
        etsuko "You're too late for that"
        "Etsuko stopped Tavo mid sentence, he laughed and brushed it off."
        tavo "Anyway, come help me out!"
        etsuko "Okay, %(player_name)s, do you prefer tea or coffee?"

        menu:
            "Tea":
                $ etsuko_choices = etsuko_choices + 1
                $ camila_choices = camila_choices + 1
                $ choose_tea = True
            "Coffee":
                $ pablo_choices = pablo_choices + 1
                $ hagane_choices = hagane_choices + 1

        etsuko "Kay', wait right here, I'll bring you your drink in a bit"
        "After he said that, he went back into the kitchen with Tavo"

        camila "So, how was the nap?"
        menu:
            "Finely, slept like a baby.":
                camila "Good to know"
                "Camila said as she got a tin box of cookies closer."
                camila "You must be hungry, I saved some cookies for you!"
                "I took one out and tried them, I recognized some chai tea flavour, they're amazing!"
                player "Is that Chai Tea? Did you make these?"
                camila "I did actually"
                "Camila seemed pleased with the recongizement that came with the compliment."
                $ camila_choices = camila_choices + 1
                hagane "I still don't get how you could fall asleep like that"
            "Not well, I remember someone yelling, actually...":
                camila "I told you to watch your volume, Hagane!"
                "As she said that she quickly punched Hagane in the arm, he laughed it off"
                $ hagane_choices = hagane_choices + 1
                hagane "I still don't get how you could fall asleep like that"
                "Hagane was comforting his punched arm with his hand with a smile and a closed eye."
        etsuko "{i}You don't have any right to say that, Hagane!{/i}"
        "Etsuko yelled out from the kitchen"
        camila "Have your classes been {i}that rough{/i}?"
        player "I only remember doing the projects my teacher asks for and falling asleep while doing them."
        pablo "On... your work table...?"
        "Worry appeared slightly on everyone's faces."
        player "Yup."
        camila "That's not good, you need to take better care of yourself!"
        "Camila said while showing some more worry on her face."
        player "Maybe I need someone to take care of me, instead."
        "I laughed softly and relaxed my friends complexed faces."

        etsuko "And interrupting that awkard talk at record speeds, tea and coffee by Tavo and me~"
        "Etsuko and Tavo came out of the kitchen, both holding a lot of cups."
        tavo "Who asked for coffee?"
        if choose_tea:
            jump tea_drinker
        else:
            jump coffee_drinker

    label tea_drinker:
        pablo "Mateo, Cancino, Hagane and me, I think."
        "Tavo skillfully left the cups in front of each person as the names where mentioned."
        etsuko "So there's tea for Camila, Tavo, %(player_name)s and me."
        camila "What leaves did you use, Etsu?"
        "Camila asked while she was being served her cup anxiously."
        etsuko "I used Summer Rose Tea!"
        "Etsuko finished leaving everyone their cups and sitted down. \n Once she was sitting, she grabbed her own cup with the sleeves of her cardigan in order to not burn herself."
        camila "Weren't you saving that tea for a special moment?"
        "Camila sipped her cup."
        camila "Oh wow, this is amazing..."
        etsuko "I was, But I started thinking about how a moment like that might never come, so..."
        etsuko "Instead I guessed it was better to share it than drink it alone with sad music."
        "She said that with a soft smile, slowly turning into a expression of satisfaction as she drank."
        camila "You haven't been doing that... right?"
        etsuko "Just sometimes... It's a really good tea, okay? It goes well with music and rain."
        camila "That doesn't sound like something healthy to put oneself through, right %(player_name)s?"
        menu:
            "Yeah, that sounds really depressing...":
                $ camila_choices = camila_choices + 1
                camila "See? If you feel like that, call us, we'll give you company, in exchange of sweet sweet tea though"
                hagane "You need to take better care of yourself."
                "Everybody laughed as Etsuko brushed her hair while smilling slightly uncomfortably as she realized what she might have been doing."
                #How the fuck does one translate "cabro qliao" into a sfw tsundere attitude???
            "I actually feel like doing that now that I think about it.":
                $ etsuko_choices = etsuko_choices + 1
                etsuko "Hey, who'd knew!"
                "Etsuko raised her hand we high fived."
                "Sad Winter Aesthetic gets a point!"
                hagane "You're both going to end depressed as heck."
                "We all laughed."
        hagane "So, how's the tea, %(player_name)s, haven't seen you have a sip yet."
        "I breathed slowly and took a big sip."
        "My mouth got exposed slowly to a softly sweet and floral flavour, something you'd expect from smelling a flower, not drinking something."
        player "It's... sweet. \nYou can really tell there's flowers in here."
        "After I finished that sentence I inmediately took another sip."
        jump after_drink

    label coffee_drinker:
        pablo "Mateo, Cancino, %(player_name)s, Hagane and me."
        "Tavo skillfully left the cups in front of each person as the names where mentioned."
        etsuko "So there's tea for Camila, Tavo and me."
        "Etsuko left the cups in front of the tea drinkers of the group and sat down."
        "Pablo inhaled strongly the scent that was coming up from his cup."
        pablo "Ahh~ Is this your Golden Willow Etsuko?"
        etsuko "As perceptive as always, huh? \n But actually, this time it is Tavo's take on my recipe."
        "Pablo took a big sip and slowly swallowed it."
        pablo "I'm impressed, is Tavo gaining interest in preparing coffee?"
        tavo "Maybe, and thanks, after seeing Etsuko preparing tea and coffee so many times I kinda grabbed interest in it."
        etsuko "I'd like to think that between seeing me prepare that coffee so many times and tasting what my hands made captured his heart."
        "Etsuko said that while doing really expressive hand gestures."
        pablo "I think he just likes coffee."
        "Hagane laughed out of his life, and Etsuko pretended that she was deeply wounded."
        hagane "So, how's the coffee %(player_name)s, haven't seen you have a sip yet."
        "I breathed slowly and took a big sip."
        "My mouth got exposed slowly to a aromatic and spicy flavour, from what seems to be cinnamon. \n And a exponentially fast flavour of a mild roasted coffee."
        "It's really comfortable, the sweet and spice of the cinnamon is strong, but not overthrowing the soft bitterness of the coffee."
        "After I finished that sentence I inmediately took another sip."
        jump after_drink

    label after_drink:
        pablo "At least Etsuko's got good taste for something, right?"
        "Everybody laughed but Etsuko showed himself annoyed."
        etsuko "Hey!"
        pablo "You've gotta admit he's got no taste for videogames."
        menu:
            "I'm sorry, but he's right.":
                $ pablo_choices = pablo_choices + 1
                pablo "See? I'm telling you!"
            "That's not right!":
                $ etsuko_choices = etsuko_choices + 1
                etsuko "See? Don't tease me like that, Pablo."
        "I slowly left that side of the conversation and joined Hagane, Camila and Cancino who were talking about collectibles."
        hagane "I tell you, these local stores only try to over-charge you for stuff!"
        "Hagane, as always, was in the verge of yelling."
        camila "But, you still don't have to wait for shipping, wouldn't that be worth it"
        cancino "Also, you don't have to deal with customs."
        "The discussion was something fun to see, as Camila and Cancino remained calm, while Hagane yelled."
        hagane "Once you start importing stuff often, customs become nothing."
        hagane "Also, you've got mail in rebate sometimes!"
        cancino "What do you think, %(player_name)s?"
        menu:
            "Not wait, but pay more!":
                $ camila_choices = camila_choices + 1
                pablo "So you're the impatient kind of type, huh..."
                player "I cannot really stand the wait for shippings, I start checking the status of the package every 20 minutes."
                hagane "Well, If you get anxious about shipments, maybe you're not going through the wront route paying more, I guess..."
                "Hagane incredibly said that with a much calmer voice."
            "Wait for shipping, but pay less!":
                $ hagane_choices = hagane_choices + 1
                cancino "Are you patient enough for that?"
                player "I already paid for it, while it arrives, I'm fine, I guess..."
                hagane "You could waste all that money in something else while you wait!"
                camila "Wouldn't that defeat the purpose of everything?"
                "Everybody showed confusion at Hagane's point."
        player "Now that I think about it, weren't we going to an amusement park now?"
        cancino "I mean, we were, but we were also waiting for you to wake up first."
        "Cancino snatched one of the cookies from the tin."
        tavo "I think we never decided on a amusement park or an arcade, though."
        "I think everybody can tell Tavo wants to go to an arcade."
        hagane "We always go to arcades, I say we do something different for once!"
        etsuko "I... I don't do well on amusement parks, but it's true we always go to arcades."
        pablo "I wanna go to the amusement park too, sounds fun, and really out of place for what's common in our gatherings."
        cancino "I don't care either way, both sound fun."
        "He said that while he had his mouth full of cookies."
        etsuko "It sounds like a plan then! Is everybody sure?"
        tavo "I guess so..."
        tavo "There whill be other occasions for rhythm games..."
        "Everyone started finishing their drinks and getting their things."
        player "Wait a minute."
        "Once I said that everyone stopped on their tracks, maybe getting everyone's attention was not the best idea for this."
        player "Were at your house, Etsuko, right?"
        etsuko "Yeah, why?"
        player "Was I sleeping at your bed?"
        "Letting that phrase out was embarrasing, and after hearing it, Etsuko got really flustered too."
        etsuko "Eh?... Uh... I... Y-Yeah..."
        "Etsuko tried hiding her face using the long sleeves her cardigan had, as her face started burning up."
        menu:
            "I have to thank you, I had a nice nap.":
                etsuko "I-It's no problem."
                "Etsuko's hair got over her eyes, and she, while looking away, nerviously sweep it aside."
            "I loved your bed, it was soft and comfortable.":
                $ etsuko_choices = etsuko_choices + 1
                etsuko "It's... no problem."
                "Etsuko completely hid her face with her sleeves and hair."
                hagane "Ayyy, what's that?"
                "Hagane said playfully as he went closer to Etsuko and took her hair up, teasing her."
                hagane "Is little Etsuko flustered for some reason?"
                etsuko "Don't tease me!"
                "Everyone laughed, and started getting outside, Etsuko going last with Hagane."
        jump metro_scene

    label metro_scene:
        "We took an elevator and got outside Etsuko's apartment."
        player "Which way do we need to go?"
        hagane "Oh right, you don't know how we got here."
        pablo "We go straight from here and we'll find a subway station, then it's just following the map."
        "As Pablo explained we started walking on the direction he pointed."

        "The group walked into the subway and took a train, they got lucky and got an almost empty wagon."
        "Who should I sit next to...?"

        menu:
            "Hagane":
                "I followed Hagane and sat besides him."
                $ hagane_choices = hagane_choices + 1
                hagane "Hey %(player_name)s, don't you get dizzy on rides?"
                menu:
                    "Yeah":
                        $ hagane_choices = hagane_choices - 1
                        hagane "That's a shame, sorry we made you come..."
                        player "It's okay, there's still other kind of rides to go though."
                        hagane "I have some pills for dizziness if you need some, so I hope you accompany us to the rollercasters!"
                        player "I'll do my best!"
                    "Nah, I'll be good.":
                        $ hagane_choices = hagane_choices + 1
                        hagane "Nice! So..."
                        player "So...?"
                        "Hagane stood up as his eyes got as bright as stars."
                        hagane "We'll go to the biggest rollercoaster, right?"
                        player "{i}I didn't about taking it to that extreme{/i}, but, I'll try."
            "Etsuko":
                "I followed Etsuko and sat besides her."
                $ etsuko_choices = etsuko_choices + 1
                etsuko "So... do you like amusement parks?"
                menu:
                    "Yeah!":
                        etsuko "Really? I can't really go on rides myself, lemafully."
                        etsuko "I guess if I could maybe I'd like them more..."
                        player "Why you can't ride them?"
                        etsuko "Lamefully, I have motion sickness, even riding cars gets me really dizzy and sick, unless I am the one driving."
                        player "I guess that makes this a pretty difficult time to have, then, I'm sorry we made you come."
                        etsuko "It's not a worry, coming here as a group sounds like a good time, I like seeing everyone smile."
                        "Etsuko looked at the rest of the group blissfully as she saw the rest of the group deciding what ride to get on first."
                    "Not really, but going as a group sounds fun!":
                        $ etsuko_choices = etsuko_choices + 1
                        $ told_etsuko = True
                        etsuko "Really? It's the same for me! I have a pretty bad time with amusement parks actually."
                        player "Why is that?"
                        etsuko "I have motion sickness, even cards are a little too much for me, unless I'm the one driving."
                        player "I guess that makes this a pretty difficult time to have, then, I'm sorry we made you come."
                        etsuko "It's not a problem, coming here as a group sounds like a good time, I like seeing everyone smiling."
                        "Etsuko looked at the rest of the group blissfully as she saw the rest of the group deciding what ride to get on first."
                        etsuko "Maybe..."
                        player "Huh?"
                        etsuko "If you'd accompany me into something more peaceful, like a cute, or scary ride, which I can go on, I'd be delighted."
                        player "Okay, we'll do that."
                        "Etsuko gave me a big smile and she let her head fall on my shoulder, I gave her a soft pat on the head."
            "Camila":
                "I followed Camila into the train and sat besides her."
                $ camila_choices = camila_choices + 1
                camila "It's been a pretty fun day, huh?"
                "Camila was sitting down as was calmly looking at the rest of the group."
                player "It has."
                camila "I'm really that the whole group can have fun together..."
                "Something in her voice wasn't right..."
                player "Is... Is something bothering you?"
                "Camila looked back to me, with a expression full of melancholy."
                camila "Do you think this will stay like this for long?"
                "Hearing that made me worry."
                player "W-What do you mean?"
                camila "I mean, people change, interests change, and friendships go away..."
                camila "I'm worried the same will happen with us..."
                menu:
                    "Don't worry, that won't happen.":
                        $ camila_choices = camila_choices + 1
                        "Camila looked straight into my eyes, she had the eyes of a lost puppy."
                        camila "You promise?"
                        player "I do."
                        "I patted Camila's head, as I tried to calm her down."
                        player "We have gone through hard stuff, but we have stayed together through all of it."
                        camila "T... Thanks %(player_name)s..."
                        "Camila smiled sweetly and put her view on the group, where everyone was trying to decide on which rides they would ride first."
                    "The group won't break apart.":
                        camila "I'm not so sure myself... We have gone through rough stuff, and I don't know if the group will sustain more of that."
                        player "I wouldn't worry about that, if we have gotten through that stuff, it means we can still hold up."
                        camila "I hope so..."
                        "Camila looked up to their friends, who were discussing which ride they would get up first."
            "Pablo":
                $ pablo_choices = pablo_choices + 1
                pablo "So, what do you plan on riding?"
                player "I still don't know, I don't know the place yet anyway."
                pablo "You can always ride this one."
                "I tried to not notice the awful tone that the joke gave."
                pablo "But, seriously, how has the city been treating you?"
                menu:
                    "It's nice, I feel like I'm slowly blending in.":
                        pablo "That's nice to know.\n If you do have any difficulties you know you can ask any of us, right?"
                        player "Right."
                        player "It's still pretty weird to wake up to a house that houses just me and Ivy though."
                        pablo "That sounds like something hard to get accustomed to."
                        player "I mean, 18 years living with your parents and suddenly you share a home alone with a friend."
                        pablo "You have to admit that's pretty sweet."
                        player "Yeah, it is actually really comfortable."
                        "We both looked at our friends who were all talking about what rides to go on first."
                    "Actually, It's pretty hard.":
                        pablo "Yeah, I get that... It's hard to notice that sometimes you're alone, huh..."
                        player "Even while having Ivy a bedroom away, it sometimes feels lonely..."
                        pablo "Yeah, not having your family at hand... Having to watch everything for yourself..."
                        pablo "You also need to be a role model for Ivy."
                        player "I think he's actually being a role model for me though!"
                        "We both laughed."
                        pablo "Well, all said, I get you, I passed through the same, we almost all did, and if you ever need some company to crack some jokes for you, just say the word."
                        pablo "Thanks Pablo..."
                        "We both looked at our friends who were all talking about what rides to go on first."

        "We traveled through 8 stations and finally got off."
        "Etsuko and Hagane were chatting and laughing, Pablo cracked some jokes for Ivy, Camila was searching which exit was the one we needed with the help of Tavo."

        camila "I think this is the one..."
        "Camila pointed at a mechanical escalator while looking at her phone and we followed her instructions."

        "We got outside and we saw a gigantic amusement park, with big rollercoasters, fun water themed rides and fun and spooky ones."
        "We paid our fees and got into the park."

        camila "So...\n Where are we going first?"
        menu:
            "A big rollecoaster!":
                $ hagane_choices = hagane_choices + 1
                jump demo_rollercoaster_big
            "A small rollercoaster!":
                $ camila_choices = camila_choices + 1
                jump demo_rollercoaster_small
            "A water ride!":
                $ pablo_choices = pablo_choices + 1
                jump demo_water_ride
            "The Haunted House!":
                $ etsuko_choices = etsuko_choices + 1
                jump demo_haunted_house

    label demo_rollercoaster_big:
        camila "Okay, does that sound good to everyone?"
        etsuko "I'm actually going to skip this one."
        hagane "Are you sure?"
        etsuko "Yeah, that for me sounds like a plain bad idea."
        etsuko "I'll be sitting over here, you all just go have your fun!"
        player "We don't really have to go to this big one first, are you..."
        etsuko "Oh, don't worry, go and have fun, I'll have my fun later."
        "Etsuko pulled some headphones from her pocket and went searching in the direction she said before."
        hagane "Okay now! Let's go!"

        $ renpy.pause(3.0)

        hagane "I feel REALLY sick..."
        "Behind Hagane came Pablo who was carrying Ivy's lifeless body."
        pablo "Maybe it wasn't that good of an idea, but it sure was fun!"
        "Camila was holding her stomach with one hand and holding her glasses in place with the other."
        camila "No one dare puke..."
        tavo "Don't worry, we wont."
        "Tavo came out looking like he didn't even go on the rollercoaster."
        "Etsuko came to get us and saw the state we were at."
        etsuko "I think I did a good job skipping this one."
        menu:
            "Yeah, I feel like I'm dying...":
                $ camila_choices = camila_choices + 1
                $ etsuko_choices = etsuko_choices + 1
                if dizzy:
                    etsuko "I'm not surprised at all."
                    "Etsuko laughed it off."
                    player "It wasn't a good idea at all."
                    if told_etsuko:
                        etsuko "I know, why did you go on it knowing you would get dizzy? It's almost as if you had a death wish!"
                        "I laughed slightly to try to get Etsuko to calm down a little, as she was slightly mad."
                else:
                    camila "Let's not do that ever again..."
                    etsuko "Guess I did a good job skipping this one."
                    "Etsuko was walking in our direction while pulling headphones out of her ears."
                    player "Yeah, you did, it wasn't a good idea at all..."
                    if told_etsuko:
                        etsuko "Yeah, no joke, I don't know how I would have ended if I had rode that."
            "I feel GREAT!":
                $ pablo_choices = pablo_choices + 1
                $ hagane_choices = hagane_choices + 1
                if dizzy:
                    hagane "You didn't even need the pills! You're amazing! Let's get onto another one!"
                else:
                    hagane "That's my guy!"
                    "Hagane was cheerfully jumping."
                    hagane "Let's go into another one!"
                etsuko "Ey, we've got more rides to go than just rollercoasters!"
                "Etsuko was walking in our direction while pulling headphones out of her ears."
                pablo "Can we rest a little before that? Ivy's COMPLETELY out..."
                "Pablo was, in fact, carrying Ivy's lifeless body on his back."
                "Etsuko, after seeing Ivy, ran to help Pablo carry him."




        pass

    label demo_rollercoaster_small:
        pass

    label demo_water_ride:
        pass

    label demo_haunted_house:
        pass





        if hagane_choices > etsuko_choices and hagane_choices > camila_choices and hagane_choices > pablo_choices:
            "Scene with Hagane."
        if etsuko_choices > hagane_choices and etsuko_choices > camila_choices and etsuko_choices > pablo_choices:
            "Scene with Etsuko."
        if camila_choices > hagane_choices and camila_choices > etsuko_choices and camila_choices > pablo_choices:
            "Scene with Camila."
        if pablo_choices > hagane_choices and pablo_choices > etsuko_choices and pablo_choices > camila_choices:
            "Scene with Pablo."













    return
