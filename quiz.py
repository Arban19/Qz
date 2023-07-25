print("Hello, Welcome to my Pop Quiz!\n")
response1 = input("Would you like to play? Please type Y to confirm yes or N to quit game. \n")
if response1.title() != "Y":
    quit()

print("OK, let's play!!!\n")
print("Kindly note you can Press Control + D anytime to exit the game\n")
print("This is a lazy guy's quiz, so you could type the entire answer, sure.\nAlternatively you could also type the first two or more letters of your answer and it'll suffice.\n")
score = 0

answer1 = input("Which state's Koloriang is contending for wettest place on Earth? Arunachal Mizoram \n").title()
if answer1.startswith("A"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer2 = input("Who is the said to be the father of economics? Adam Smith Milton Keynes \n").title()
if answer2.startswith("A"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer3 = input("Which is the latest company to enter the USD 1 trillion market valuation camp? Netflix Nvidia \n").title()
if answer3.startswith("Nv"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer4 = input("Which was the constituency of the last Khasi Chief Minister Meghalaya had? Shella Nongpoh  \n").title()
if answer4.startswith("N"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer5 = input("Where was Jesus crucified? Golgotha Jerusalem \n").title()
if answer5.startswith("G"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer6 = input("Which Indian state is called 'God's own country'? Goa Kerala \n").title()
if answer6.startswith("K"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer7 = input("What is ISRO's third lunar mission called? Chandrayaan Aditya L1  \n").title()
if answer7.startswith("C"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer8 = input("Kendrick Lamar won which grammy in 2023? Best Rap Song Record of the Year  \n").title()
if answer8.startswith("B"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer9 = input("Who is the Finance Minister of India? Nirmala Piyush  \n").title()
if answer9.startswith("N"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

answer10 = input("With which country is India currently negotiating border dispute settlement? Pakistan China \n").title()
if answer10.startswith("C"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!!")

print("Thank you for finishing the quiz!!!")
print("Your score is " + str(score) + " out of 10" )
print("You got " + str(score/10*100) +"%")
if score == 10:
	print("You're a genius. Sit for Civils!")
elif score > 7:
    print("Wow, well done on this quiz!")
elif 4<= score <= 7:
    print("Good performace!")
else:
    print("Read the newspaper, you blithering idiot!")

exit()
