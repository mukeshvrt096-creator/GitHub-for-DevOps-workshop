age = int(input("Enter the age of person: "))

if age <= 12:
    print("Child")
elif age <= 18:
    print("Teenager")
elif age <= 30:
    print("Adult")
elif age <= 54:
    print("Old")
elif age <= 90:
    print("Grand Old")
else:
    print("Very Senior")