print("Welcome to my Computer quiz!!")

playing = input("Do you want to play? ")
if playing.lower()!= "yes" : 
    quit ()

print("Okay! Lets play!!!")
score = 0

answer = input ("What does EC2 stand for? ")
if answer == "Elastic compute cloud" :
    print("Correct✅")
    score += 1
else: 
    print("Incorrect❌")

answer = input ("What is the function of S3 in AWS? ")
if answer == "Scalable Storage service" :
    print("Correct✅")
    score += 1
else: 
    print("Incorrect❌")

answer = input ("What does VPC stand for? ")
if answer == "Virtual Private Cloud" :
    print("Correct✅")
    score += 1
else: 
    print("Incorrect❌")

answer = input ("What does IAM stand for? ")
if answer == "Identity and Access Management" :
    print("Correct✅")
    score += 1
else: 
    print("Incorrect❌")

answer = input ("What does RDS stand for? ")
if answer == "Relational Database Service" :
    print("Correct✅")
    score += 1
else: 
    print("Incorrect❌")
    
answer = input ("What does EBS stand for? " )
if answer == "Elastic Block Storage" :
    print("Correct✅")
    score += 1
else: 
    print("Incorrect❌")
    
answer = input ("What does ELB stand for? ")
if answer == "Elastic Load Balancer" :
    print("Correct✅")
    score += 1
else: 
    print("Incorrect❌")

print("You got " + str(score)  + " Question Correct")
print("You scored " + str(score/7*100) + "%")
    
    
    
    






