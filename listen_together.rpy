#Do you want to listen to something together?, us submod by confiscatedharddrive for Monika After Story.

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
        m "Ready to continue, [mas_get_player_nickname()]?"
        m "I know I am!"
    else:
        $ mas_gainAffection(3, bypass=False)
        m "Of course!"
        m "What did you have in mind?{nw}"

        $ _history_list.pop()
        menu:
            m "What did you have in mind?{fast}"

            "Music":
                $ persistent._mas_listening_to_music = True
                $ persistent._mas_listening_to_podcast = False
                $ persistent._mas_listening_to_drama = False
                m "Hm,{w=0.3} I wonder what the genre is going to be..."
                m "Pop? Rock? Alternative? {w=0.3}{nw}"
                extend "Maybe something orchestral?"
                m "Ehehe~"

            "Podcast":
                $ persistent._mas_listening_to_podcast = True
                $ persistent._mas_listening_to_music = False
                $ persistent._mas_listening_to_drama = False
                m 2eub "That sounds great!"
                m 4eua "Podcasts are a great way to inform yourself!"
                m 3hublb "Or, just listen to people talk, ehehe~"

            "Audio drama":
                $ persistent._mas_listening_to_drama = True
                $ persistent._mas_listening_to_music = False
                $ persistent._mas_listening_to_podcast = False
                m "Really?"
                m "That's not someone most people listen to anymore."
                m "Not to say it's a bad choice! I just wasn't expecting it."
                m "Whatever it is, I'm sure it'll be fun to tune into with you~"

            "Radio":
                $ persistent._mas_listening_to_music = False
                $ persistent._mas_listening_to_drama = False
                $ persistent._mas_listening_to_podcast = False
                m "I'm down for that!"
                m "Radio is a great way to relax when you just want to put something on."
                m "You may even discover some new songs you would have never thought to listen to before!"

        m 2eub "Alright,{w=0.3} go ahead and do whatever you need to do to get set up."
        m 7esa "I'm going to put a choice on screen so you can let me know when you're ready."

        $ _history_list.pop()
        menu:

            "I'm ready!":
                m 1hua "Great!"

        if persistent._mas_listening_to_music:
            m "I'm so glad we get to listen to music together!"
        elif persistent._mas_listening_to_podcast:
            m "I hope I learn something new from this!"
        elif persistent._mas_listening_to_drama:
            m "I wonder what adventures we'll tune into today!"
        else:
            m "Let me know when you want to stop or take a break, okay?"

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
        m 7eub "Just go back to the 'Do you want to watch something with me?' topic to let me know when you're ready to keep going."
return