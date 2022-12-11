list = [['1', 'Васильев Анатолий Евген', '19.11.1999', 'отл', 'муж'], ['2', 'Ананьева Ната Конст', '22.03.2000', 'средн', 'жен'], ['3', 'Тиль Кат Стан', '02.01.2001', 'отл', 'муж']]
def read_file(file):
    f = open(file, 'r') 
    data = f.read().splitlines()
    list = []
    for line in data:
        line = line.split(';')
        list.append(line)
    f.close()
    return list



def write_file(list, mod):
    f = open('result.csv', mod)

    for i in range(len(list)):
        for j in range(len(list[i])):
            f.writelines(list[i][j])
            f.writelines(';')
        f.writelines('\n')
    f.close()
    if mod == 'a':
        print('Данные записаны!')
    if mod == 'w':
        print('Данные перезаписаны!')

mod = 'w'
write_file(list, mod)