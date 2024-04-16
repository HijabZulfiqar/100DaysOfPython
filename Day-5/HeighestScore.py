scores=input("Enter your score: ").split()
for i in range(0,len(scores)):
    scores[i]=int(scores[i])
print(scores)
max=0
for score in scores:
    if(score>max):
        max=score
print(f"The highest score is {max}")