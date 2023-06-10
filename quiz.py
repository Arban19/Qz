print("Hello, Welcome to my Pop Quiz!")
response1 = input("Would you like to play? Please type Y to confirm yes or N to quit game. ")
if response1.title() != "Y":  
    quit()

print("OK, let's play!!!")
score = 0

answer1 = input("Which state's Koloriang is contending for wettest place on Earth? Arunachal Mizoram ")
if answer1.title() == "Arunachal":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer2 = input("Who is the said to be the father of economics? Adam Smith Milton Keynes ")
if answer2.title() == "Adam Smith":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer3 = input("Which is the latest company to enter the USD 1 trillion market valuation camp? Netflix Nvidia ")
if answer3.title() == "Nvidia":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer4 = input("Which was the constituency of the last Khasi Chief Minister Meghalaya had? Shella Nongpoh  ")
if answer4.title() == "Nongpoh":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer5 = input("Where was Jesus crucified? Golgotha Jerusalem ")
if answer5.title() == "Golgotha":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer6 = input("Which Indian state is called 'God's own country'? Goa Kerala ")
if answer6.title() == "Kerala":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer7 = input("What is ISRO's third lunar mission called? Chandrayaan Aditya L1  ")
if answer7.lower() == "chandrayaan":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer8 = input("Kendrick Lamar won which grammy in 2023? Best Rap Song Record of the Year  ")
if answer8.title() == "Best Rap Song":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer9 = input("Who is the Finance Minister of India? Nirmala Piyush  ")
if answer9.title() == "Nirmala":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

answer10 = input("With which country is India currently negotiating border dispute settlement? Pakistan China ")
if answer10.title() == "China":
    print("Correct!")
    score += 1
else: print("Incorrect!!")

print("Thank you for finishing the quiz!!!")
print("Your score is " + str(score) + " out of 10" )
print("You got " + str(score/10*100) +"%")
if score > 7:
    print("Wow, well done on this quiz!")
elif 4<= score <= 7:
    print("Good performace!")
else: print("Read the newspaper, you blithering idiot!")

exit()
