#Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

#Task 2
average_grade = sum(grades) / 10
print("The average grade in the class was", average_grade)

#Task 3
grades[-1] = 'Failed'
grades[-2] = 'Failed'
grades[-3] = 'Failed'
print(grades)