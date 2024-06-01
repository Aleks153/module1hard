# Usloviya zadachy
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Variant 1
from statistics import mean
grades = [mean(grades[0]), mean(grades[1]), mean(grades[2]),  mean(grades[3]), mean(grades[4])]
students = list(students)
students.sort()
dictionary = dict([[students[0], grades[0]], [students[1], grades[1]],
                [students[2], grades[2]], [students[3], grades[3]],
                 [students[4], grades[4]]])
print('Variant 1: ', dictionary)


