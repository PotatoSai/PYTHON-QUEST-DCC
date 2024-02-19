file = open('user_info.txt','w')


userInfo = input("Enter your name: ")


file.write(userInfo)

file.close()
