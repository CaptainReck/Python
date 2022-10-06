l={"Which of the following cities was capital of Maharaja Ranjit Singh? : ":"LAHORE",
   "Who was the founder of the organisation “Abhinav Bharat” in 1904? : ":"GANESH SAVARKAR",
   "Who among the following formed the group “Brothers of India”? : ":"ANNIE BEASANT",
   "Who among the following brought the first Printing Machine in India? : ":"PORTUGESE",
   "In which year, India Office of the Secretary of State for India and Burma came to an end ? : ":"1947"
   }
L=["Which of the following cities was capital of Maharaja Ranjit Singh? :","Who was the founder of the organisation “Abhinav Bharat” in 1904? :",
   "Who among the following formed the group “Brothers of India”? :","Who among the following brought the first Printing Machine in India? :",
   "In which year, India Office of the Secretary of State for India and Burma came to an end ? :"]
A=["Lahore","Ganesh Sarvarkar","Annie Besant","Portuguese","1947"]
print("Welcome to the Quiz")
c=0
for i in range(5):
    print("Question no.",i+1,L[i])
    x=input("Enter your answer :")
    if x.upper()==A[i].upper():
        c+=1
        print("Right Answer")
    else:
        print("Wrong Answer")
print("You got",c,"out of 5")             

             