#Do you want to listen to something together?, us submod by confiscatedharddrive for Monika After Story.

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="chd_listen_together_notseen",
            category=["you", "us", "misc"],
            prompt="Do you want to listen to something together?",
            pool=True,
            unlocked=True

        ),
    )