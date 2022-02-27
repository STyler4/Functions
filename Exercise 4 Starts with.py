def starts_with_a(word):
    if word[0] == "A":
        return True
    elif word[0] == "a":
        return True
    else:
        return False


# Main routine
get_word = (input("Enter word: "))
print(starts_with_a(get_word))

