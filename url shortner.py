print("CODE BY VISHIST TULSYAN")
def url():
    import  pyshorteners
    s = input("ENTER YOUR URL")
    f = pyshorteners.Shortener()
    print("HERE IS YOUR LINK:")
    print(f.tinyurl.short(s))
url()
while True:
    ques = input(print("do you want to restart y/n?"))
    if ques == "y":
        url()
    else:
        print("thanks for using my code")
        quit()

