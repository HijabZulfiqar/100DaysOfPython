height=input("enter your height?")
weight  =input("enter your weight?")

BMI=float(weight)/float(height)**2
BMI_new=round(BMI)
print(BMI_new)
if BMI_new<18.5:
    print("UnderWeight")
elif BMI_new>18.5 & BMI_new<25:
    print("Normal Weight")
elif BMI_new>25 & BMI_new<30:
    print("OverWeight")
elif  BMI_new>30 & BMI_new<35:
    print("obese")
else:
    print("Clinically Obese")

