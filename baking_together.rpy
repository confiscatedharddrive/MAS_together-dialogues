#Do you want to bake with me?, us submod by confiscatedharddrive for Monika After Story. (use responsibly!! best if you have a laptop. please don't risk ruining monika's home)

#for the sake of adding discord rpc support; cutesy stuff
default -5 persistent._mas_baking_ = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="baking_together",
            category=["us"],
            prompt="Do you want to bake with me?",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None),

        ),
        markSeen=True
    )

label baking_together:

    if persistent._mas_taking_break_from_baking:
        m 3eua "Ready to keep going, [mas_get_player_nickname()]?"
        m 7hub "I know I am!"
    else:
        $ mas_gainAffection(3, bypass=False)
        m "I'd love to!"
        m 7eua "What did you have in mind?{nw}"

        $ _history_list.pop()
        menu:
            m "What did you have in mind?{fast}"

            "Bread":
                m ""

            "Cookies":
                m ""

            "Cake":
                m ""

            "Cupcakes":
                m "Cupcakes, huh?"
                m "That's something more suited towards Sayori..."
                m "I'm kidding!"
                m "I'm sure it's a fun activity regardless."
                m "Though, they're a bit too sweet for my taste."
                m "I'll still have a bite, though! Can't let my [mas_get_player_nickname()]'s work go to waste!"

            "Brownies":
                m ""

            "Cheesecake":
                m ""

            "Cinnamon rolls"
                m "Aww, [player]. There's no need for that..."
                m "I already got my cute cinnamon roll,{w=0.3} you! Ehehe~"
                m "Just teasing, [mas_get_player_nickname()]."

        m 2eub "Alright,{w=0.3} go ahead and gather your ingredients and tools."
        m 7esa "Just let me know when you're ready to start."

        $ _history_list.pop()
        menu:

            "I'm ready!":
                m 1hua "Great!"

        if persistent._mas_baking_:
            m ""
        elif persistent._mas_baking_:
            m ""
        else:
            m 1eub "Let me know when you want to stop or take a break, okay?"

$ mas_idle_mailbox.send_idle_cb("baking_together_callback")
return "idle"

label baking_together_callback:
    m 3eud "Are you ready to stop for now?{nw}"

$ _history_list.pop()
menu:
    m "Are you ready to stop for now?{fast}"

    "Yeah.":
        $ persistent._mas_taking_break_from_baking = False
        m 1hua "Alright!"
        m 3lsblb "I hope we get to do this again soon."
        m 5ekbsu "I always love spending time with you, [player]."

    "I'm taking a quick break.":
        $ persistent._mas_taking_break_from_baking = True
        m 1hua "Alright!"
        m 7eub "Just go back to the 'Do you want to bake with me?' topic to let me know when you're ready to keep going."
return