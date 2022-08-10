def are_you_playing_banjo(name):
    return "{} plays banjo".format(name) if name.startswith("R") or name.startswith("r") else "{} does not play banjo".format(name)
