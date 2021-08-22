data = []

while True:
    print("Say Something: ")
    line = input()
    if "/end" in line:
        break
    else:
        data.append(line)
finalText = " ".join(data)
print(finalText)

        