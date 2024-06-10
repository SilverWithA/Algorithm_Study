
while True:
    s = input()
    if s == "0":
        break
    palindrome = True
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            palindrome = False
            break


    if palindrome == True:
        print("yes")
    else:
        print("no")