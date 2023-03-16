yequestion = input('Вы загадали персонажа?\n')

yes = 'да' or 'Да'

hero_1 = 'Бэтмен'
hero_2 = 'Человек паук' 
hero_3 = 'Капитан Америка'
hero_4 = 'Тор'
hero_5 = 'Веном'
hero_6 = 'Призрачный гонщик'
hero_7 = 'Шазам'
hero_8 = 'Флеш'
hero_9 = 'Доктор Стренж'
hero_10 = 'Джокер'

if question == yes:
    question_about_person = input('У вашего героя костюм или облик состоит из черного цвета? ')
    if question_about_person == yes:
        q2 = input('Ваш герой осоциируется с летучими мышами? ')
        if q2 == yes:
            print(f'Ваш песонаж: {hero_1}' )
        else:
            print(f'Ваш персонаж: {hero_5}' )
    else:
        question_about_person_2 = input('Ваш персонаж состоит во всленной Марвел? ')
        if question_about_person_2 == yes:
            q3 = input('У вашего персонажа есть паутина? ')
            if q3 == yes:
                print(f'Ваш персонаж: {hero_2}' )
            else:
                print(f'Ваш персонаж: {hero_3}' )
        else:
            question_about_person_3 = input('Ваш персонаж превращается ночью в Скелета с Цепью Или имеет Молот Мьёльнир? ')
        if question_about_person_3 == yes:
            q4 = input('Ваш персонаж является Богом из Скандинавской Мифалогии? ')
            if q4 == yes:
                print(f'Ваш персонаж: {hero_4}' )
            else:
                print(f'Ваш персонаж: {hero_6}')
