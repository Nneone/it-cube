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
            print("Изображение изменилось)")
        if num == 2:
            print("Выберите яркость Изображения от 1 до 100: ")
            user2 = int(input())
            b = user2 >= 0 or user2 <= 100
            print("Изображение изменилось)")
        if num == 3:
            print("Выберите размытость Изображения от 1 до 100: ")
            user3 = int(input())
            c = user3 >= 0 or user3 <= 100
            print("Изображение изменилось)")    
        else:     
            print("Eror!") 
        break
    
    except ValueError:
        print("Oops! Выберите из трех перечисленных вариантов")
    