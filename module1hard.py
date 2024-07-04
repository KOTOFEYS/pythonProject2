grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=list(students)
st1 = students_list[0]
st2 = students_list[1]
st3 = students_list[2]
st4 = students_list[3]
st5 = students_list[4]
gr1 = int(sum(grades[0])/len(grades[0]))
gr2 = int(sum(grades[1])/len(grades[1]))
gr3 = int(sum(grades[2])/len(grades[2]))
gr4 = int(sum(grades[3])/len(grades[3]))
gr5 = int(sum(grades[4])/len(grades[4]))
dict_ = {st1:gr1,
         st2:gr2,
         st3:gr3,
         st4:gr4}
print(dict_)