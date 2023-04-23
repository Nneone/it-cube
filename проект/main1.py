print("Welcome to the PhotoRec")
print("Загрузите изображение и укажите путь к нему")
Photo = input()
print("Выберите как обработать изображение")
while True:
    print('1.Контрастность: 1        2.Яркость: 2         3.Размытость: 3')
    try:
        print("Введите как изменить изображение: ")
        num = int(input())


        if num == 1:
            print("Выберите контрастность Изображения от 1 до 100: ")
            user = int(input())
            a = user >= 0 or user <= 100
            
        


        if num == 2:
            print("Выберите яркость Изображения от 1 до 100: ")
            user = int(input())
            b = user >= 0 or user <= 100
            
     


        if num == 3:
            print("Выберите размытость Изображения от 1 до 100: ")
            user = int(input())
            c = user >= 0 or user <= 100
            

            

        if user > 100:
            print("Erorr! Не может быть значение больше 100")
             



        if user < 100:
            print("Изображение изменилось)")



            break
    except ValueError:
        print("Oops! Выберите из трех перечисленных вариантов")
