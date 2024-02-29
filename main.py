# modules
from datetime import date

bmi_path = "bmi_history/bmi.txt"

p_hight = float(input("Your weight in m: ")) 
p_weight = float(input("Your height in Kg: "))

# if p_

p_bmi = p_weight / (p_hight * p_hight)
print(f"your BMI is :{p_bmi}")

if (p_bmi > 0):
    if (p_bmi <= 16.5):
        print("your underweight")
    elif (p_bmi <= 18.5):
        print("You are underweight")
    elif(p_bmi <=25):
        print("Congrats! You are Healthy")
    elif(p_bmi <=30):
        print("You are overweight")
    else: 
        print("You are very overweight")
else:
    print("enter valid details")
try:
    with open(bmi_path, 'a') as file:
        file.writelines(f"V-- {date.today()}\n")
        file.writelines(f"weight: {p_weight:.2f}kg ; height: {p_hight:.2f}m\n")
        file.writelines(f"bmi :{p_bmi:.2f}\n")
except:
    print("-- couldn't write to history check if the fille exist in ./bmi_history/bmi.txt")


