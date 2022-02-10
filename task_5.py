import csv


class MyData:
    """"
    Создаем класс для работы с csv
    """

    def open_data(self):
        """
        Создание файла
        """
        values = [['hostname', 'vendor', 'model', 'location'],
                  ['sw1', 'Cisco', '3750', 'London, Best str'],
                  ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
                  ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
                  ['sw4', 'Cisco', '3650', 'London, Best str']]

        with open('sw_data_new.csv', 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerows(values)

        with open('sw_data_new.csv') as f:
            print(f.read())

    def new_data(self):
        """
        Метод добавление строки
        """
        with open('sw_data_new.csv', 'a') as f:
            value = ['rer', 'Samsung', '3355', 'Bishkek, Isanov str']
            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(value)

        with open('sw_data_new.csv') as f:
            print(f.read())

# Остальные методы написать нехватило знаний...


m = MyData()

m.open_data()
m.new_data()



