def grade():
    score = int(input("what is your students score?: "))
    if score >= 90:
        print("Grade: A, Excellent work Marv!")
    elif score >= 80:
        print("Grade: B, Good job Marv!")
    elif score >= 70:
        print("Grade: C, Keep up the good work!")
    elif score >= 60:
        print("Grade: D, You can do better!")
    else:
        print("Grade: F, Failure do well next time!")

grade()