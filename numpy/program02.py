# Assignment Problem on Numpy
# A School’s Student Performance
# Data
# You are tasked with analyzing the performance of students in different
# subjects. The school has conducted exams for three subjects: Math,
# Science, and English. 
# Each student has scored a mark between 0 and 100
# in each subject.

# You are given a dataset in the form of a 2D NumPy array, where each
# row represents a student, and each column represents a subject. Your
# task is to:


# Create a NumPy array representing the students' scores for Math, Science, and English.
# Calculate the total score for each student by adding their scores across all subjects.
# Find the average score of all students for each subject (i.e., the mean score for Math, Science, and English).
# Identify the student with the highest score in Math, Science, and English individually.
# Find the number of students who scored above 75 in all three subjects.
import numpy as np

scores = np.array([
    [85, 78, 90],   # student 1
    [72, 88, 80],   # student 2
    [90, 92, 85],   # student 3
    [65, 70, 75],   # student 4
    [88, 84, 91]    # student 5
])

total_scores = np.sum(scores, axis=1)
print("Total score of each student:", total_scores)

average_scores = np.mean(scores, axis=0)
print("Average score for each subject:", average_scores)

highestMarks_math = np.argmax(scores[:, 0])
highestMarks_science = np.argmax(scores[:, 1])
highestMarks_english = np.argmax(scores[:, 2])

print(f"Student with highest Math score: Student {highestMarks_math + 1}")
print(f"Student with highest Science score: Student {highestMarks_science + 1}")
print(f"Student with highest English score: Student {highestMarks_english + 1}")

students_above_75 = np.all(scores > 75, axis=1)
count_students_above_75 = np.sum(students_above_75)

print("Number of students who scored above 75 in all subjects:", count_students_above_75)
