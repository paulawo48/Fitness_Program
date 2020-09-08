# Import libraries
import calendar
import sys
import datetime
from datetime import date

# Open file for reading and appending
f = open("plan.txt", 'r')
x = open("plan.txt", 'a')

# Determine the day of the week and seperate workout from progress log
my_date = date.today()
day = calendar.day_name[my_date.weekday()]
today = str(datetime.date.today())
# Define progress section
x.write("\n------------------------------------------")
x.write("\nWorkout progression\n")
x.write(today)

# Write the number of workout reps to file
def wo_write():
    print(cur_wo)
    stats = []
    reps = input('How much any total reps did you do?')
    stats.append(reps)
    x.write("\n")
    x.write(cur_wo)
    x.write(str(stats))


# Determine the type of workout program and pull out workouts planned for the day
program = input("Are you on the Strength(s) or Hypertrophy(h) program?: ").lower()
if program == "s":
    if day == "Monday":
        a = 13
        lines = [13, 14, 15, 17, 18, 19]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Tuesday":
        a = 23
        lines = [23, 24, 26, 27, 28]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Wednesday":
        a = 32
        lines = [32, 33, 34, 36, 37, 38]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Thursday":
        print("Enjoy your day off")
    elif day == "Friday":
        a = 44
        lines = [44, 45, 46]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Saturday":
        a = 59
        lines = [59, 60, 62, 63, 64]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Sunday":
        a = 68
        lines = [68, 69, 70]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
elif program == "h":
    if day == "Monday":
        a = 13
        lines = [13, 14, 15, 17, 18, 19]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Tuesday":
        a = 23
        lines = [23, 24, 26, 27, 28]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Wednesday":
        a = 32
        lines = [32, 33, 34, 36, 37, 38]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    elif day == "Thursday":
        print("Enjoy your day off")
    elif day == "Friday":
        a = 44
        lines = [44, 45, 46]
        workout = f.readlines()
        for a in lines:
            cur_wo = workout[a]
            wo_write()
    else:
        pass

f.close()
x.close()
