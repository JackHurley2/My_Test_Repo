Grade = input("what is your Grade?:\n")
Grade = int(Grade)


out = None

if Grade == 40 :
    out =  "Fail"
elif Grade == 40-50:
    out = "Pass"
elif Grade == 50-60:
    out = "Merit"
elif Grade == 60 :
    out = "Distinction"
    
print("Your Grade is : " + str(out))