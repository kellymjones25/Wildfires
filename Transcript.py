class Transcript:
    def __init__(self, classes, major, minor, student_name):
        self.classes = classes
        self.major = major
        self.minor = minor
        self.student_name = student_name

    def display(self):
        print(f"Transcript for {self.student_name}:")
        print(f"Major: {self.major}, Minor: {self.minor}")
        print("Transcript Text:")
        for course in self.classes:
            print(f"classes")

    def calculate_gpa(self):
        grade_points = {
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1.0,
            'F': 0.0
        }
        total_points = 0
        total_classes = len(self.classes)

        for course in self.classes:
            grade = course.get('grade')
            if grade in grade_points:
                total_points += grade_points[grade]

        gpa = total_points / total_classes if total_classes > 0 else 0
        return round(gpa, 2)
    
    def display_classes_taken(self):
        print("Classes Taken:")
        for course in self.classes:
            print(f"{course.get('name')} - Grade: {course.get('grade')}")