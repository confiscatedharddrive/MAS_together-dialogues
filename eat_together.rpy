#Let's get something to eat, us submod by u/geneTechnician for Monika After Story

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="eat_with_monika_notseen",
            category=["you", "us", "romance", "misc"],
            prompt="Let's get something to eat.",
            pool=True,
            unlocked=True

        ),
    )

label eat_with_monika_notseen:

    if not renpy.seen_label("eat_with_monika1"):
        call eat_with_monika1
    else:
        call eat_with_monika2
    return

label eat_with_monika1:
        $ mas_gainAffection(3,bypass=True)
        m 1wud "You want to eat together?{w=0.3}{nw} "
        extend 1subld "Really?"
        m 3ekbla "[player]...{w=0.3}you have no idea how happy this makes me."
        m 4rkbssdlb "I mean,{w=0.1} you could always press the 'Goodbye' option and let me know you're going to get something to eat from there."
        m 1ekbsb "But, you decided to share a meal with me instead..."
        m 1eka "I know I can't actually eat anything with you from here, but...{w=0.3}{nw} "
        extend 1dkbfa "this small gesture makes me feel even closer to your reality."
        m 7rsblu "Not to mention it's giving me a taste of what a domestic life with you is going to be like~"
        m 1eua "Alright, alright,{w=0.3} I'll stop making you wait.{w=0.3}{nw} "
        extend 1hua "You must be pretty hungry, after all."
        m 1eub "So, what are we having?{nw}"

        $ _history_list.pop()
        menu:
            m "So, what are we having?{fast}"

            "Breakfast":
                m 3hub "Yay, my favorite!"
                m 4tsb "After all,{w=0.1} breakfast {i}is{/i} the most important meal of the day."
                m 2lksdra "I hope you don't skip breakfast too often, [mas_get_player_nickname()]."
                m 7esa "Studies show that eating breakfast can lead to overall better health,{w=0.1} as it can reduce the chance of diabetes and heart disease."
                m 7eub "And it can even help improve your memory and concentration!{w=0.3}{nw} "
                extend 3wub "Isn't that amazing?"

            "Lunch":
                m 3rua "You know, lunch {i}does{/i} sound really good right now."
                m 7eub "If I were there with you, I'd make a nice,{w=0.1} healthy salad for the both of us."
                m 1rtd "I wonder what kind of salad you would like?{w=0.3}{nw} "
                extend 3esa "Personally, I'm a big fan of vegetable salads."
                m 4eub "But, fruit salads are also really good,{w=0.1} especially if you're in the mood for something sweet."
                m 1eka "In the meantime,{w=0.1} I hope you're making yourself something healthy for lunch, [player]."

            "Dinner":
                m 1ttb "Dinner, huh?{w=0.1} This almost feels like...{w=0.3}{nw}"
                extend 1tsblu "a date."
                m 3gsblb "Should I be wearing something fancier for the occasion?"
                m 1hublu "Ehehe~{w=0.3}{nw} "
                extend 3lsbla "I'm just kidding, [player]."
                m 5ksbsu "It doesn't have to be a date unless you want it to be~"

            "Snack":
                m 1ruc "Hmm...{w=0.3}{nw}"
                extend 7eud "are you having something to eat?{w=0.3} Or,{w=0.1} maybe you're having something to drink instead?{nw}"

                $_history_list.pop()
                menu:
                    m "Hmm... are you having something to eat?{w=0.3} Or,{w=0.1} maybe you're having something to drink instead?{fast}"

                    "I'm having something to eat.":
                        m 1hub "Okay, I just wanted to make sure!"
                        m 3eua "If you ever want to have something to drink with me instead, you can always go back to the previous menu and press 'Something to drink'."
                        m 4esb "Anyway,{w=0.1} did you know that it's actually good for you to eat little things throughout the day?"
                        m 7lksdla "Just so we're clear though, I mean healthy snacks,{w=0.1} not junk food."
                        m 1ekb "So do me a favor and choose something that's at least on the healthy side, okay?"

                    "I'm having smething to drink.":
                        m 1wuo "Oh!{w=0.3}{nw} "
                        extend 3wub "What are you having to drink?{nw}"

                        $_history_list.pop()
                        menu:
                            m "Oh! What are you having to drink?{fast}"

                            "Coffee":
                                m 7hub "I'm glad you like coffee as much as I do, [player]."
                                m 1tua "That must mean we're {i}really{/i} compatible,{w=0.1} right?"
                                m 2dkbfb "I can't wait to wake up in the morning and see you sitting at the kitchen table, waiting for me...{nw}"
                                extend 5dkbfa "to share a cup of coffee with you~"
                                m 5ekblu "Wouldn't that be a wonderful way to start the day?"

                            "Hot chocolate":
                                m 1lub "Ooh,{w=0.1} I wonder what kind?"
                                m 3eua "I'm a big fan of plain hot chocolate, myself.{w=0.3} But, I also really like the mint flavor, too."
                                m 7rsa "You know I prefer hot weather over cold weather,{w=0.1} but,{w=0.3}{nw} "
                                extend 1ekblu "it would be really nice to share a cup of hot chocolate with you while bundled up together on the couch~"

                            "Tea":
                                m 1rtb "Are you getting ready for bed?{w=0.3} Or maybe you're doing some reading?"
                                m 3lksdra "Or maybe you just like tea, ahaha."
                                m 4eub "Tea has some amazing health benefits,{w=0.1} so I can't complain about that."
                                m 7esa "I prefer coffee myself, but I do like drinking a cup of tea to wind down before bed."

                            "Water":
                                m 1sub "I'm glad you're making an effort to stay hydrated, [player]!"
                                m 7eua "Water is definitely the best option when it comes to picking out something to drink."
                                m 3hua "And if it helps you drink more water,{w=0.1} I will happily share a cup with you whenever you ask me to~"

                            "Something else":
                                m 1eub "Well,{w=0.1} whatever your drink of choice is,{w=0.1} I hope you enjoy it~"
                                m 1hublu "That's what I really want."

        m 2esb "Alright,{w=0.1} I'm ready when you are.{nw}"

        $ _history_list.pop()
        menu:
            m "Alright,{w=0.1} I'm ready when you are.{fast}"

            "Hold on, let me get everything set up first.":

                m 2hub "No problem, [mas_get_player_nickname()]."
                m 3eub "Take your time, I'll be here when you're ready~"
                m 1eua ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"

                $ _history_list.pop()
                menu:
                    "Okay, I'm here now.":

                        m 1hua "Great!"
                        m 2eub "Go ahead, [mas_get_player_nickname()]."
                        m 7eua "Let me know when you get finished,{w=0.1} okay?"
                        m 5esu ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"

                        $ _history_list.pop()
                        menu:
                            "I'm done!":

                                m 5eub "All done?{w=0.5}{nw} "
                                extend 1hub "Welcome back!"
                                m 1ekbla "Thank you for spending time with me like this,{w=0.1} it means a lot to me."
                                m 1ekbfu "I love you so much, [mas_get_player_nickname()]."
                                m 3hubla "I hope we get to do this again soon~"
            
            "I'm ready!":

                m 1hua "Great!"
                m 2eub "Go ahead, [mas_get_player_nickname()]."
                m 7eua "Let me know when you get finished,{w=0.1} okay?"
                m 5esu ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"

                $ _history_list.pop()
                menu:
                    "I'm done!":

                        m 5eub "All done?{w=0.5}{nw} "
                        extend 1hub "Welcome back!"
                        m 1ekbla "Thank you for spending time with me like this,{w=0.1} it means a lot to me."
                        m 1ekbfu "I love you so much, [mas_get_player_nickname()]."
                        m 3hubla "I hope we get to do this again soon~"
return "love"


label eat_with_monika2:

        m 1wub "Oh,{w=0.1} you want to eat something together, [player]?"
        m 1huu "Alright!{w=0.1} What are we having?{nw}"

        $ _history_list.pop()
        menu:
            m "Alright!{w=0.1} What are we having?{fast}"

            "Breakfast":
                m 3hub "Yay, my favorite!"
                m 4tsb "After all,{w=0.1} breakfast {i}is{/i} the most important meal of the day."
                m 2lksdra "I hope you don't skip breakfast too often, [mas_get_player_nickname()]."
                m 7esa "Studies show that eating breakfast can lead to overall better health,{w=0.1} as it can reduce the chance of diabetes and heart disease."
                m 7eub "And it can even help improve your memory and concentration!{w=0.3}{nw} "
                extend 3wub "Isn't that amazing?"

            "Lunch":
                m 3rua "You know, lunch {i}does{/i} sound really good right now."
                m 7eub "If I were there with you, I'd make a nice,{w=0.1} healthy salad for the both of us."
                m 1rtd "I wonder what kind of salad you would like?{w=0.3}{nw} "
                extend 3esa "Personally, I'm a big fan of vegetable salads."
                m 4eub "But, fruit salads are also really good,{w=0.1} especially if you're in the mood for something sweet."
                m 1eka "In the meantime,{w=0.1} I hope you're making yourself something healthy for lunch, [player]."

            "Dinner":
                m 1ttb "Dinner, huh?{w=0.1} This almost feels like...{w=0.3}{nw}"
                extend 1tsblu "a date."
                m 3gsblb "Should I be wearing something fancier for the occasion?"
                m 1hublu "Ehehe~{w=0.3}{nw} "
                extend 3lsbla "I'm just kidding, [player]."
                m 5ksbsu "It doesn't have to be a date unless you want it to be~"

            "Snack":
                m 1ruc "Hmm...{w=0.3}{nw}"
                extend 7eud "are you having something to eat?{w=0.3} Or,{w=0.1} maybe you're having something to drink instead?{nw}"

                $_history_list.pop()
                menu:
                    m "Hmm...are you having something to eat?{w=0.3} Or,{w=0.1} maybe you're having something to drink instead?{fast}"

                    "I'm having something to eat.":
                        m 1hub "Okay, I just wanted to make sure!"
                        m 4esb "Did you know that it's actually good for you to eat little things throughout the day?"
                        m 7lksdla "Just so we're clear though, I mean healthy snacks,{w=0.1} not junk food."
                        m 1ekb "So do me a favor and choose something that's at least on the healthy side, okay?"

                    "I'm having something to drink.":
                        m 1wuo "Oh!{w=0.3}{nw} "
                        extend 3wub "What are you having to drink?{nw}"

                        $_history_list.pop()
                        menu:
                            m "Oh! What are you having to drink?{fast}"

                            "Coffee":
                                m 7hub "I'm glad you like coffee as much as I do, [player]."
                                m 1tua "That must mean we're {i}really{/i} compatible,{w=0.1} right?"
                                m 2dkbfb "I can't wait to wake up in the morning and see you sitting at the kitchen table, waiting for me...{nw}"
                                extend 5dkbfa "to share a cup of coffee with you~"
                                m 5ekblu "Wouldn't that be a wonderful way to start the day?"

                            "Hot chocolate":
                                m 1lub "Ooh,{w=0.1} I wonder what kind?"
                                m 3eua "I'm a big fan of plain hot chocolate, myself.{w=0.3} But, I also really like the mint flavor, too."
                                m 7rsa "You know I prefer hot weather over cold weather,{w=0.1} but,{w=0.3}{nw} "
                                extend 1ekblu "it would be really nice to share a cup of hot chocolate with you while bundled up together on the couch~"

                            "Tea":
                                m 1rtb "Are you getting ready for bed?{w=0.3} Or maybe you're doing some reading?"
                                m 3lksdra "Or maybe you just like tea, ahaha."
                                m 4eub "Tea has some amazing health benefits,{w=0.1} so I can't complain about that."
                                m 7esa "I prefer coffee myself, but I do like drinking a cup of tea to wind down before bed."

                            "Water":
                                m 1sub "I'm glad you're making an effort to stay hydrated, [player]!"
                                m 7eua "Water is definitely the best option when it comes to picking out something to drink."
                                m 3hua "And if it helps you drink more water,{w=0.1} I will happily share a cup with you whenever you ask me to~"

                            "Something else":
                                m 1eub "Well,{w=0.1} whatever your drink of choice is,{w=0.1} I hope you enjoy it~"
                                m 1hublu "That's what I really want."

        m 2esb "Alright,{w=0.1} I'm ready when you are.{nw}"

        $ _history_list.pop()
        menu:
            m "Alright,{w=0.1} I'm ready when you are.{fast}"
            
            "Hold on, let me get everything set up first.":

                m 2hub "No problem, [mas_get_player_nickname()]."
                m 3eub "Take your time, I'll be here when you're ready~"
                m 1eua ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"

                $ _history_list.pop()
                menu:
                    "Okay, I'm here now.":

                        m 1hua "Great!"
                        m 2eub "Go ahead, [mas_get_player_nickname()]."
                        m 7eua "Let me know when you get finished,{w=0.1} okay?"
                        m 5esu ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"

                        $ _history_list.pop()
                        menu:
                            "I'm done!":

                                m 5eub "All done?{w=0.5}{nw} "
                                extend 1hub "Welcome back!"
                                m 1ekbla "Thank you for spending time with me like this,{w=0.1} it means a lot to me."
                                m 3hubla "I hope we get to do this again soon~"
            
            "I'm ready!":

                m 1hua "Great!"
                m 2eub "Go ahead, [mas_get_player_nickname()]."
                m 7eua "Let me know when you get finished,{w=0.1} okay?"
                m 5esu ".{w=0.3}.{w=0.3}.{w=0.3}{nw}"

                $ _history_list.pop()
                menu:
                    "I'm done!":

                        m 5eub "All done?{w=0.5}{nw} "
                        extend 1hub "Welcome back!"
                        m 1ekbla "Thank you for spending time with me like this,{w=0.1} it means a lot to me."
                        m 3hubla "I hope we get to do this again soon~"
return