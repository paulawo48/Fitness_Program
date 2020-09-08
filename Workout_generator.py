# Import libaries
import random
import sys
import datetime

# Enter one rep max for compund workouts
print("Please enter your one rep max for the following compound movements")
bpress = int(input("Bench Press: "))
spress = int(input("Shoulder Press: "))
bcp = int(input("Barbell Curl: "))
tcp = int(input("Push downs: "))
crows = int(input("Cable row: "))
sqt = int(input("Squats: "))

def personal_record():
      # Print Start date
      now = datetime.datetime.now()
      print("Start Date:", now.day, "-", now.month, "-",
            now.year, "\nPersonal Records")
      # Print current PRs
      print("Bench Press 1RPM: ", bpress)
      print("Shoulder Press 1RPM: ", spress)
      print("Barbell Curl 1RPM: ", bcp)
      print("Push down 1RPM: ", tcp)
      print("Cable rows 1RPM: ", crows)
      print("Squats 1RPM: ", sqt, "\n")

def create_workout():
      # Create list of workout for each body part

      # Deltoids workout selection
      deltoids = ["Barbell press", "Dumbbell press",
                  "Shoulder press", "Cable Rows", "Front raises", "Miltary Press"]
      random.shuffle(deltoids)
      awo = deltoids[1]
      bwo = deltoids[2]
      cwo = deltoids[3]
      # Trapz workout selection
      trapz = ["Shrugs", "Bent Over Rows"]
      random.shuffle(trapz)
      dwo = trapz[0]
      ewo = trapz[1]
      # Bicep workout selection
      biceps = ["Inner Bicep Curl", "EZ-Bar Curl",
            "Hammer Curl", "Concentration Curl"]
      random.shuffle(biceps)
      fwo = biceps[1]
      gwo = biceps[2]
      # Tricep workout selection
      triceps = ["Dips", "EZ-Bar Skull Crusher",
            "French Curls", "Tricep Push Downs",
            "Overhead Cable Extensions", "KickBacks"]
      random.shuffle(triceps)
      iwo = triceps[1]
      jwo = triceps[2]
      kwo = triceps[3]
      # UpperChest workout selection
      upchest = ["Incline Barbell Bench Press",
            "Incline Dumbell Press", "Cable fly", ]
      random.shuffle(upchest)
      lwo = upchest[0]
      mwo = upchest[1]
      # Chest workout selection
      chest = ["Cable fly",
            "Flat Bench Dumbbell press", "Barbell Bench Press"]
      random.shuffle(chest)
      owo = chest[1]
      pwo = chest[2]
      # Leg workout selection
      legs = ["Barbell Sqaut", "Dumbell Lunges", "Leg Press",
            "Leg Extension", "Standing Calf Rises", "Barbell deadlift"]
      random.shuffle(legs)
      qwo = legs[1]
      rwo = legs[2]
      swo = legs[3]
      # Back workout selection
      back = ["Cable Rows", "Bent-Over Rows", "Wide Grip Pull Downs", "Barbell Deadlifts"
            "Close Grip Pull Downs", "Single Arm Dumble Row"]
      random.shuffle(back)
      two = back[1]
      uwo = back[2]
      wwo = back[3]
      # Bodyweight workout selection
      bwpush = ["Dips", "Push Up", "Bulgarian split squat",
            "Inverted Row", "Air Squat"]
      random.shuffle(bwpush)
      xwo = bwpush[1]
      ywo = bwpush[2]
      zwo = bwpush[3]

      # Pick Workout plan
      if intensity == "h":
            # Set weight range co-efficents
            lwv = 0.60
            upv = 0.80
            print("\nYou choose Hypertrophy training, here's your weekly workout for the month\nMonday Workout: Push ")
            print("Chest Weight Recommended range: ",
                  lwv*bpress, '-', upv*bpress)
            print("", lwo, "\n", owo, "\n", pwo)
            print("Shoulders Weight Recommended range:",
                  lwv*spress, '-', upv*spress)
            print("", awo, "\n", bwo, "\n", dwo)
            print("\nTuesday Workout: Pull")
            print("Bicep Weight Recommended range:", lwv*bcp, '-', upv*bcp)
            print("", fwo, "\n", gwo)
            print("Back Weight Recommended range:", lwv*crows, '-', upv*crows)
            print("", two, "\n", uwo, "\n", wwo)
            print("\nWednesday Recommended Workout: Legs/Tricep")
            print("Leg Weight range:", lwv*sqt, '-', upv*sqt)
            print("", qwo, "\n", rwo, "\n", swo)
            print("Tricep Recommended Weight range:", lwv*tcp, '-', upv*tcp)
            print("", iwo, "\n", jwo, "\n", kwo)
            print("\nThursday Workout\nRest Day!\n")
            print("Friday Workout: Body Weight")
            print("", xwo, "\n", ywo, "\n", zwo,
                  "\nFinish off with 2 Ab Workouts of Choice")
      elif intensity == "s":
            lwv = 0.7
            upv = 0.9
            rlwv = 0.65
            rupv = 0.8
            print("\nYou choose Strength Training, here's your weekly workout for the month\nMonday Workout: Push ")
            print("Chest Weight Recommended range: ",
                  lwv*bpress, '-', upv*bpress)
            print("", lwo, "\n", owo, "\n", pwo)
            print("Shoulders Weight Recommended range:",
                  lwv*spress, '-', upv*spress)
            print("", awo, "\n", bwo, "\n", dwo)
            print("\nTuesday Workout: Pull")
            print("Bicep Weight Recommended range:", lwv*bcp, '-', upv*bcp)
            print("", fwo, "\n", gwo)
            print("Back Weight Recommended range:", lwv*crows, '-', upv*crows)
            print("", two, "\n", uwo, "\n", wwo)
            print("\nWednesday Recommended Workout: Legs/Tricep")
            print("Leg Weight range:", lwv*sqt, '-', upv*sqt)
            print("", qwo, "\n", rwo, "\n", swo)
            print("Tricep Recommended Weight range:", lwv*tcp, '-', upv*tcp)
            print("", iwo, "\n", jwo, "\n", kwo)
            print("\nThursday Workout\nRest Day!")
            print("\nFriday Workout: Push")
            print("Chest Weight Recommended range: ",
                  rlwv*bpress, '-', rupv*bpress)
            print("", mwo, "\n", owo)
            print("Shoulders Weight Recommended range:",
                  rlwv*spress, '-', rupv*spress)
            print("", cwo, "\n", bwo, "\n", ewo)
            print("Tricep Recommended Weight range:", rlwv*tcp, '-', rupv*tcp)
            print("", kwo, "\n", iwo)
            print("\nSaturday Workout: Pull")
            print("Bicep Weight Recommended range:", rlwv*bcp, '-', rupv*bcp)
            print("", fwo, "\n", gwo)
            print("Back Weight Recommended range:", rlwv*crows, '-', rupv*crows)
            print("", two, "\n", uwo, "\n", wwo)
            print("\nSunday Workout: Legs")
            print("Leg Weight range:", rlwv*sqt, '-', rupv*sqt)
            print("", qwo, "\n", rwo, "\n", swo)
            print("Finish off with 2 Ab Workouts of Choice \n\n\n ")
      else:
            print("Pick again, Between Strength or Hypertrophy!")
            f.close()

if __name__ == "__main__":
      # Read workout to file
      setting = input('Press w to write new file, Press a to append file ').lower()
      intensity = str(input('Press H for hypertrophy or S for strength workouts: ').lower())
      f = open("plan.txt", setting)
      sys.stdout = f
      personal_record()
      create_workout()