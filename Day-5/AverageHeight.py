#Average height Program
students_height=[180,124,165,173,189,169,146]
print(students_height)
sum=0
for student in students_height:
    sum=sum+student
average=round(sum/len(students_height))

print(f"The average is {average}")