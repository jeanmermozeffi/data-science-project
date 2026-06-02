def calculate_class_average(grades):
    """
    Calculate the average grade for a class of students.
    
    Args:
        grades (list): List of student grades
        
    Returns:
        float: Average grade of the class
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)


def calculate_student_average(student_grades):
    """
    Calculate the average grade for a single student.
    
    Args:
        student_grades (list): List of grades for a student
        
    Returns:
        float: Average grade for the student
    """
    if not student_grades:
        return 0
    return sum(student_grades) / len(student_grades)
