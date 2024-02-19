file = open('story.txt','r')


lines = file.readlines()
numberOfLines = len(lines)

print(f"The number of lines in this file is: {numberOfLines}")


file.close()
