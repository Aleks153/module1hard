# Variant 1

# Usloviya zadachy
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Reshenie 1
from statistics import mean
grades = [round(mean(grades[0])/1, 1), round(mean(grades[1]), 1)/1, round(mean(grades[2]), 1)/1,  round(mean(grades[3]), 1)/1, round(mean(grades[4]),1)/1]
students = list(students)
students.sort()
dictionary = dict([[students[0], grades[0]], [students[1], grades[1]], [students[2], grades[2]], [students[3], grades[3]], [students[4], grades[4]]])
print('Variant 1: ', '\n', 'Средний балл учеников: ', dictionary)

print('__________')

# Variant 2

# Usloviya zadachy
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Reshenie 2
students = sorted(list(students))
dictionary = dict([[students[0], round(sum(grades[0]) / len(grades[0]), 1)], [students[1], round(sum(grades[1]) / len(grades[1]), 1)], [students[2],
        round(sum(grades[2]) / len(grades[2]), 1)], [students[3], round(sum(grades[3]) / len(grades[3]), 1)], [students[4], round(sum(grades[4]) / len(grades[4]), 1)]])
print('Variant 2;', '\n', 'Средний балл учеников: ', dictionary)

print('__________')

