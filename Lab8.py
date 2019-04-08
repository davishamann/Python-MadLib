#Davis Hamann               Date: 4/2/2019
#Net ID: dch360
#Description: Reads stories to create mad libs
def generateMadlib(words):
    for i in range(len(words)):
        if( words[i][0]=="["):
            user_input=input("Enter in a(n)"+words[i]+":")
            words[i]=user_input
    
    print(" ".join(words))
def main():
    print("Welcome to MadLibs generator.")
    while True:
        filename=input("Please input a file")
        try:
            file=open(filename)
            break
        except:
            print("Please enter a valid file name! Try again")
    content=file.readline()
    words=content.split()
    generateMadlib(words)

main()
