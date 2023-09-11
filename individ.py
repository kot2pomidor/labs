#coding: utf-8
class Cars():
    def __init__(self, name, brand, production_date, color, category, price):
        self.name = name
        self.brand = brand
        self.production_date = production_date
        self.color = color
        self.category = category
        self.price = price
    def mash(self):
        price = self.price
        if price % 10 == 1:
            y = ' рубль'
        if price % 10 == 2 or price % 10 == 3 or price % 10 == 4:
            y = ' рубля'
        else:
            y = ' рублей'
        print(self.name + ' ' + self.brand + ' ' + self.color + ' цвета, входящий в категорию ' + self.category + ', стоимостью ' + str(self.price) + y + ', дата производства: ' + str(self.production_date))

class Brand():
    def __init__(self, name, country, factory, address):
        self.name = name
        self.country = country
        self.factory = factory
        self.address = address
    def marka(self):
        name = self.name
        if name == 'Hyundai':
            m = ' производится в '
        if name == 'Lada':
            m = ' производился в '
        else:
            m = ' производится(-лся) в'
        print(self.name + ' производится в ' + self.country + ' на заводе ' + self.factory + ', находящемся по адресу: ' + self.address)
    
class Staff():
    def __init__(self, surname, name, patronymic, experience, salary):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.experience = experience
        self.salary = salary
    def sotrudnik(self):
        experience = self.experience
        if experience > 5:
            f = ', средний стаж работы: '
        if experience > 10:
            f = ', большой стаж работы: '
        else:
            f = ', небольшой стаж работы: '
        print('Ответственный за продажу данного автомобиля: ' + self.surname + ' ' + self.name + ' ' + self.patronymic + f + str(self.experience) + ', заработная плата: ' + str(self.salary))

class Sales():
    def __init__(self, date, employee, car, buyer):
        self.date = date
        self.employee = employee
        self.car = car
        self.buyer = buyer
    def prodazha(self):
        buyer = self.buyer
        if buyer == 'Хромов Андрей Геннадьевич':
            b = ' приобрёл автомобиль '
        else:
            b = ' приобрёл(а) автомобиль '
        print(str(self.date) + ' ' + self.buyer + b + self.car + ' после консультации с сотрудником автосалона ' + self.employee)

class Buyers():
    def __init__(self, surname, name, patronymic, passport_data, address, city, age, gender):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.passport_data = passport_data
        self.address = address
        self.city = city
        self.age = age
        self.gender = gender
    def buy(self):
        age = self.age
        if age % 10 == 1:
            x = 'года'
        else:
            x= 'лет'
        print('О покупателе: ФИО - ' + self.surname + ' ' + self.name + ' ' + self.patronymic + ', Возраст: ' + str(self.age) + x + ',пол: ' + self.gender + ', проживающий в городе ' + self.city + ', по адресу: ' + self.address + ', Паспортные данные: серия и номер - ' + str(self.passport_data))
    
if __name__ == '__main__':
    car_1 = Cars('Solaris', 'Hyundai', 19062007, 'чёрного', 'маленьких автомобилей', 521000)
    car_1.mash()
    brand_1 = Brand('Hyundai', 'Korea', 'HyundaiMotor' , 'Saint-Petersburg, Sestroreck, h.20, s.1')
    brand_1.marka()
    staff_1 = Staff('Ерёмин', 'Алексей', 'Владимирович', 13, 54000)
    staff_1.sotrudnik()
    sales_1 = Sales(23122022, 'Ерёминым Алексеем Владимировичем', 'Hyundai Solaris', 'Хромов Андрей Геннадьевич')
    sales_1.prodazha()
    buyers_1 = Buyers('Хромов', 'Андрей', 'Геннадьевич', 1113174582, 'ул. Думская, д.15, кв.42', 'Санкт-Петербург', 28, 'мужской')
    buyers_1.buy()
    
    
