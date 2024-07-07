grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=list(students)
students_list.sort()
st1 = students_list[0]
st2 = students_list[1]
st3 = students_list[2]
st4 = students_list[3]
st5 = students_list[4]
gr1 = (sum(grades[0])/len(grades[0]))
gr2 = (sum(grades[1])/len(grades[1]))
gr3 = (sum(grades[2])/len(grades[2]))
gr4 = (sum(grades[3])/len(grades[3]))
gr5 = (sum(grades[4])/len(grades[4]))
dict_ = {st1:gr1,
         st2:gr2,
         st3:gr3,
         st4:gr4,
         st5:gr4}
print(dict_)