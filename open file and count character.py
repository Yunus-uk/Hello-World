def occurences(character, filepath="file.txt"):
    with open("file.txt") as bearnotes:
        content = bearnotes.read()
    return content.count(character)