n = int(input('Введите количество критериев: '))
def fixed(number, digits):#Формат вывода
    return f"{number:.{digits}f}"

def display_matrix():#Отображение матрицы
    print('\nПолучившаяся матрица \n')
    for row in matrix:
        for i in row:
            print(fixed(i, 2) + '  ', end='')
        print('\n')

matrix = []
row = []
diagonal = 0
row_sum=[]
temp_sum=0
matrix_sum=0

#Заполнение матрицы
for i in range(n):
    for j in range(n):
        if i > j:
            row.append(1 / matrix[j][i])
        elif i != j:
            value = float(
                input('Введите коэффициент отношения критерия ' + str(i + 1) + ' к критерию ' + str(j + 1) + ': '))
            row.append(value)
        else:
            row.append(1)
    matrix.append(row)
    row=[]
display_matrix()

#Подсчет сумм строк
for row in matrix:
    for item in row:
        matrix_sum+=item
        temp_sum+=item
    row_sum.append(temp_sum)
    temp_sum=0

iteration=0

#Подсчет и вывод весовых коэффициентов
for row in matrix:
    print('Весовой коэффициент для '+str(iteration+1)+' критерия равен '+str(fixed(row_sum[iteration]/matrix_sum,3)))
    iteration+=1