def capitalize(string):
    characters = len(string)
    if characters <= 10:
        return string
    character_list = list(string)
    mutating_string = ""
    for i in range(characters):
        char = character_list[i]
        if char >= "a" and char <= "z":
            mutating_string += chr(ord(char) - 32)
        else:
            mutating_string += char
    return str(mutating_string)

print(capitalize(input("Give me a string! ")))