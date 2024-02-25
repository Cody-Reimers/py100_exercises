import textwrap
def char_type(char):
    if ord(char) == 95:
        return "_"
    elif ord(char) >= 65 and ord(char) <= 90:
        return "A"
    elif ord(char) >= 97 and ord(char) <= 122:
        return "a"
    elif ord(char) >= 48 and ord(char) <= 57:
        return "1"
    else:
        return "?"

name = input(textwrap.dedent("""
    Give me a name for an identifier and
    I'll tell you if the name is valid!
    """)
)

identifier_type = input(textwrap.dedent("""
    I also need to know what kind
    of Identifier I'm working with:
    a "C"ONSTANT, a C"l"ass, or "o"ther.
    Please enter "C", "l", or "o" now.
    """)
)

valid = True
idiomatic = True
initial = char_type(name[0])
types = []
for i in range(len(name)):
    types.append(char_type(name[i]))

if initial == "1" or initial == "?":
    valid = False
elif identifier_type == "o":
    for i in range(len(types)):
        char = types[i]
        if char == "?":
            valid = False
        elif char == "A":
            idiomatic = False
elif identifier_type == "C":
    for i in range(len(types)):
        char = types[i]
        if char == "?":
            valid = False
        elif char == "a":
            idiomatic = False
elif identifier_type == "l":
    for i in range(len(types)):
        char = types[i]
        if char == "?":
            valid = False
        elif char == "_":
            idiomatic = False

print(textwrap.dedent("""
    One thing to clarify: I can't spellcheck
    your Identifier name, so you'll have to
    double check yourself that you spelled
    your words and spaced your underscores
    correctly, and also make sure your name
    isn't one of Python's protected words
    like "if", "while", or "def".
    """)
)

if identifier_type == "o" and valid:
    if not idiomatic:
        print(textwrap.dedent("""
            Your name is valid, however it is not
            idiomatic. For most Identifier names,
            you're advised to not use capital letters.
            """)
        )
    else:
        print("Good job! Your Identifier name is valid!")
        if initial == "_":
            print(textwrap.dedent("""
                Just make sure you know what you're
                doing with those underscores at the start!
                """)
            )
elif identifier_type == "C" and valid:
    if not idiomatic:
        print(textwrap.dedent("""
            Your name is valid, however it is not
            idiomatic. For CONSTANT names, you're
            advised to only use capital letters.
            """)
        )
    else:
        print("Good job! Your CONSTANT name is valid!")
        if initial == "_":
            print(textwrap.dedent("""
                Just make sure you know what you're
                doing with those underscores at the start!
                """)
            )
elif identifier_type == "l" and valid:
    if not idiomatic:
        print(textwrap.dedent("""
            Your name is valid, however it is not
            idiomatic. For Class names, you're
            advised to not use underscores.
            """)
        )
    else:
        print(textwrap.dedent("""
        Good job! Your Class name is valid!
        It's also probably idiomatic, but
        you'll have to check that the first
        letter of each word is capitalized.
        """)
    )

if not valid:
    if identifier_type == "o":
        print("Your Identifier name is invalid! You")
    elif identifier_type == "C":
        print("Your CONSTANT name is invalid! You")
    elif identifier_type == "l":
        print("Your Class name is invalid! You")
    print(textwrap.dedent("""
        may have used a control character or
        punctuation from the ASCII set, or you
        may have started the name with a number.
        """)
    )