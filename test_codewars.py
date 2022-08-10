def are_you_playing_banjo(name):
    print("Are you playing banjo?")
    if "r" or "R" in name[0]:
        print(name + " plays banjo")
    else:
        print(name + " does not play banjo")
    return name
are_you_playing_banjo("martin")
