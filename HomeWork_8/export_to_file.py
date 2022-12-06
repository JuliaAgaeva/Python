import json


def export_txt():
 with open("db.json", 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
           # if name == data[i]['Name'] or name == data[i]['Surname']:
                with open('myphonbook.txt', 'a') as export:
                    export.write('\n' + "".join(data[i]) + ' ' + "".join(
                        data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

        print('\nКонтакты успешно экспортированы в файл!\n')
        