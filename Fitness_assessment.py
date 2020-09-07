# User body inputs
print("Please input the following values")
sex = str(input("Are you Male or female?: "))
age = float(input("Age in numbers: "))
height = float(input("Height in m: "))
weight = float(input("Weight in kg: "))
waist = float(input("Waist in cm: "))
bodyfat = float(input("Bodyfat percentage: "))
resthr = float(input("Rest Heartrate: "))

# Calculate health indicators
bmi = weight/((height)*(height)) #BMI 
wth = waist/(100*height) # Weight-to-height ratio
fatmass = weight*bodyfat # Fat mass
ffm = weight - fatmass  # Muscle mass
maxhr = 211 - 0.64*age    # Max heartrate
maxvo2 = 15*resthr/maxhr  # Max oxgen intake(ml/kg/min)

def male():
    # Response to body fat
    bmr = 10*weight + 625*height - 5*age + 5 # Miffin-St Jeor equation(kcal/day)
    # Response to bodyfat
    if bodyfat > 25:
        print("\nBodyfat %: You are obese, focus on weightloss")
    elif bodyfat > 18 and bodyfat > 24:
        print("\nBodyfat %:You are averagely healthy, focus on fitness")
    elif bodyfat < 23 and bodyfat > 6:
        print("\nBodyfat %:You are really fit, keep it up")
    elif bodyfat < 5:
        print("\nBodyfat %:Your body fat is low, weight gain is advised")
    # Response to BMI
    if bmi < 18.5:
        print("BMI: ", round(bmi, 1), ",You are underweight")
        print("Waist-to-height ratio: ", round(wth, 2))
    if bmi > 18.5 and bmi < 24.9:
        print("BMI: ", round(bmi, 1), ",You are healthy")
        print("Waist-to-height ratio: ", round(wth, 2))
    elif bmi > 24.9 and wth >= 0.53:
        print("BMI: ", round(bmi, 1), ",You are overweight")
        print("Waist-to-height ratio: ", round(wth, 2))
    elif bmi > 24.9 and wth <= 0.52:
        print("BMI isn't accurate for your body time")
        print("Waist-to-height ratio: ", round(wth, 2))
   
    print("Your recommened daily calorie intake is:", 0.9*bmr, "kcal")


def female():
    bmr = 10*weight + 625*height - 5*age - 161
    # Response to body fat
    if bodyfat > 32:
        print("\nBodyfat %: You are obese, focus on weightloss")
    elif bodyfat < 31 and bodyfat > 25:
        print("\nBodyfat %:You are averagely healthy, focus on fitness")
    elif bodyfat < 24 and bodyfat > 11:
        print("\nBodyfat %:You are really fit, keep it up")
    elif bodyfat < 10:
        print("\nBodyfat %:Your body fat is low, weight gain is advised")
    # Response to BMI
    if bmi < 18.5:
        print("BMI: ", round(bmi, 1), "You are underweight")
        print("Waist-to-height ratio: ", round(wth, 2))
    elif bmi > 18.5 and bmi <= 25:
        print("BMI: ", round(bmi, 1), "You are healthy")
        print("Waist-to-height ratio: ", round(wth, 2))
    elif bmi > 24.9 and wth >= 0.53:
        print("BMI: ", round(bmi, 1), "You are overweight")
        print("Waist-to-height ratio: ", round(wth, 2))
    elif bmi > 24.9 and wth <= 0.48:
        print("BMI isn't accurate for your body time")
        print("Waist-to-height ratio: ", round(wth, 2))

    print("Your recommened daily calorie intake is:", 0.9*bmr, "kcal")

if __name__ == "__main__":
    if sex == "m":
        male()
    elif sex == "f":
        female()

