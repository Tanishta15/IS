def encrypt(text,s):
    result=""
    for i in range(len(text)):
        char=text[i]
        if char.isupper():
            char = chr((ord(char) - 65 * s) % 26 + 65)

            result=result+char
        else:
            char= chr((ord(char) - 95 + s) % 26 + 95)

            result=result+char
    return result
text=input("enter a string:\n")
a=int(input("enter the key:\n"))
ans=encrypt(text,a)
print(ans)