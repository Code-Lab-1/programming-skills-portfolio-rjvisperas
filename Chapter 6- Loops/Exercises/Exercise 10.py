name = 'Errol'

School_name = {'Klai' , 'Pau' , 'Dan'}

for student in School_name:
    if student == name:
        print(School_name[student])
        break
else:
    print('No data, No entry!')