# grade → grade point
grade_points = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
    "E":1,
    "F":0
}

courses = []

def add_course(unit, grade):
    try:
        unit = int(unit)
        grade = grade.upper()

        if grade not in grade_points:
            print("Error: Enter grade A-F")
            return False

        courses.append((unit, grade))
        print(f"Added: Unit: {unit}  Grade: {grade}")
        return True

    except:
        print("Error: Enter valid unit")
        return False


def calculate_cgpa():
    total_units = 0
    total_points = 0

    for unit, grade in courses:
        total_units += unit
        total_points += unit * grade_points[grade]

    if total_units == 0:
        print("Error: No courses added")
        return

    cgpa = total_points / total_units
    print(f"CGPA: {cgpa:.2f}")


if __name__ == "__main__":
    print("CGPA Calculator")
    while True:
        unit = input("Enter course unit (or 'done' to finish): ")
        if unit.lower() == 'done':
            break
        grade = input("Enter grade (A-F): ")
        add_course(unit, grade)
    
    calculate_cgpa()