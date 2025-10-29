def feedDog(hunger_level, biscuit_size):
    hunger_level.sort()
    biscuit_size.sort()

    satisfied_dogs = 0
    biscuit_index = 0
    for hunger in hunger_level:
        while biscuit_index < len(biscuit_size) and biscuit_size[biscuit_index] < hunger:
            biscuit_index += 1
        if biscuit_index < len(biscuit_size):
            satisfied_dogs += 1
            biscuit_index += 1

    return satisfied_dogs