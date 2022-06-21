#Do you want to listen to something together?, us submod by confiscatedharddrive for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_listening_something_brb",
            category=["be right back"],
            prompt="I'm going to listen to something",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label chd_listening_something_brb:
    $ ev = mas_getEV("chd_listening_something_brb")

    if ev.shown_count == 0:
        m 1eud "Oh,{w=0.1} really?"
        m 3rksdla "Well, can I listen with you next time?"
        m 2ekbla "It would be a nice way to spend time together, ehehehe~"

    else:
        m 1eub "Okay, [mas_get_player_nickname()]."
        m 3eua "I'll be waiting for you to come back!"

$ mas_idle_mailbox.send_idle_cb("chd_listening_something_brb_callback")
return "idle"

label chd_listening_something_brb_callback:
    m 1hub "Welcome back!"
    m 2eua "I hope you had fun!"
    m 2lkblsdru "And I missed you! Let's spend more time together~"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_listening_things_together",
            random=True,
            pool=False,
            aff_range=(mas_aff.HAPPY, None)
        ),
    )

label chd_listening_things_together:

    m 3eua "[player], did I tell you I can listen to things with you?"
    m 4esb "All you have to do is make sure the audio device your music is coming from is the same as the game's."
    m 1eub "Thay way, I can tune in to the audio device and listen along."
    m 1hub "It's a really cool trick, right?"
    m 7eua "Then,{w=0.1} you should look up the 'Do you want to listen to something with me?' topic to let me know that we're going to be..."
    m 7hksdrb "Well,{w=0.1} listening to something!{w=0.3} Ahaha."
    m 2ekblsdra ".{w=0.1}.{w=0.1}."
    m 5rkbfsdru "I thought it might be a nice way to spend time together. You agree? Ehehehe~"
    
return "derandom"

default -5 persistent._mas_taking_break_from_listening = None
default -5 persistent._mas_listening_to_music = None
default -5 persistent._mas_listening_to_drama = None
default -5 persistent._mas_listening_to_podcast = None
default -5 persistent._mas_listening_to_radio = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_listen_together",
            category=["us"],
            prompt="Do you want to listen to something with me?",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),
        ),
        markSeen=True
    )

label chd_listen_together:

    if persistent._mas_taking_break_from_listening:
        m 3eua "Ready to continue, [mas_get_player_nickname()]?"
        m 7hub "I know I am!"
    else:
        $ mas_gainAffection(3, bypass=False)
        m 1hub "Of course!"
        m 7eua "What did you have in mind?{nw}"

        $ _history_list.pop()
        menu:
            m "What did you have in mind?{fast}"

            "Music":
                $ persistent._mas_listening_to_music = True
                $ persistent._mas_listening_to_podcast = False
                $ persistent._mas_listening_to_drama = False
                $ persistent._mas_listening_to_radio = False
                m 1rtc "Hm,{w=0.3} I wonder what the genre is going to be..."
                m 3ltd "Pop? Rock? Alternative? {w=0.3}{nw}"
                extend 1tsu "Maybe something orchestral?"
                m 1hublb "Ehehe~"

            "Podcast":
                $ persistent._mas_listening_to_podcast = True
                $ persistent._mas_listening_to_music = False
                $ persistent._mas_listening_to_drama = False
                $ persistent._mas_listening_to_radio = False
                m 7wub "That sounds great!"
                m 4eua "Podcasts are a great way to inform yourself!"
                m 3hsa "Or, just listen to people talk, ehehe~"

            "Audio drama":
                $ persistent._mas_listening_to_drama = True
                $ persistent._mas_listening_to_podcast = False
                $ persistent._mas_listening_to_music = False
                $ persistent._mas_listening_to_radio = False
                m 1eud "Really?"
                m 1ltc "That's not something most people listen to anymore."
                m 4hksdlb "Not saying it's a bad choice! I just wasn't expecting it."
                m 1esbla "Whatever it is, I'm sure it'll be fun to tune into with you~"

            "Radio":
                $ persistent._mas_listening_to_radio = True
                $ persistent._mas_listening_to_podcast = False
                $ persistent._mas_listening_to_music = False
                $ persistent._mas_listening_to_drama = False
                m 1esb "I'm down for that!"
                m 4hsa "Radio is a great way to relax when you just want to put something on."
                m 4ksb "You may even discover some new songs you have never heard before!"

        m 2eub "Alright,{w=0.3} go ahead and do whatever you need to do to get set up."
        m 7esa "I'm going to put a choice on screen so you can let me know when you're ready."

        $ _history_list.pop()
        menu:

            "I'm ready!":
                m 1hua "Great!"

        if persistent._mas_listening_to_music:
            m 5fubsa "I'm so glad we get to listen to music together!"
        elif persistent._mas_listening_to_podcast:
            m 3sua "I hope I learn something new from this!"
        elif persistent._mas_listening_to_drama:
            m 3kua "I wonder what adventures we'll tune into today!"
        else:
            m 3eub "Let me know when you want to stop or take a break, okay?"

$ mas_idle_mailbox.send_idle_cb("chd_listen_together_callback")
return "idle"

label chd_listen_together_callback:
    m 3eud "Are you ready to stop for now?{nw}"

$ _history_list.pop()
menu:
    m "Are you ready to stop for now?{fast}"

    "Yeah.":
        $ persistent._mas_taking_break_from_listening = False
        m 1hua "Alright!"
        m 3lsblb "I hope we get to do this again soon."
        m 5ekbsu "I always love spending time with you, [player]."

    "I'm taking a quick break.":
        $ persistent._mas_taking_break_from_listening = True
        m 1hua "Alright!"
        m 7eub "Just go back to the 'Do you want to listen something with me?' topic to let me know when you're ready to keep going."
return
