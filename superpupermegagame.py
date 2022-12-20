import time
import random
dwarffire=4
enemyfiring=0
bossfiring=0
enemybleed=0
bossbleed=0
enemypois=0
bosspois=0
dwarfen=0
alchemisten=0 
alchemist=0
alchemistpois=4
poisat=4
bleed=6
fireat=4
firecan=0
poisb=0
foresttip=1
cavetip=1
mansiontip=1
boss1=0
forestroz=0
dwarf=0
boss2=0
hp=100
patana=0
death=0
dofire=0
dobleed=0
dopois=0
firecanshopstart=0
poisbshopstart=0
apple=random.randint(2,5)
med=random.randint(2,3)
money=random.randint(4,12)
inv=['іржавий меч', 'яблуко', 'медовуха']
equippedweap=[]
##############################             ІНВЕНТАР
def inventory():
    global hp
    global apple
    global med
    global firecan
    global poisb
    invloop=1
    while invloop==1:
        print('\n\n\n\n\n***ІНВЕНТАР***\n', inv, '\nМонети:', money, '\nЗдоров\'я:', hp)
        vubinv=str(input('\nЩо ви будете робити?\nвикористати предмет - 1\nменю обладнання - 2\nдізнатись більше про предмет - 3\nназад - 4\n', ))
        if vubinv=='1':
            itemonloop=1
            while itemonloop==1:
                itemon=str(input('\nЯкий предмет хочете використати?\nназад - 1\n', ))
                ################           ЗБРОЯ
                if itemon=='розплавлений меч':
                    if 'розплавлений меч' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('розплавлений меч')
                            equippedweap.append('розплавлений меч')
                            print('\n\n\n\n\nВи взяли розплавлений меч')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='катана роніна':
                    if 'катана роніна' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('катана роніна')
                            equippedweap.append('катана роніна')
                            print('\n\n\n\n\nВи взяли катану роніна')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='іржавий меч':
                    if 'іржавий меч' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('іржавий меч')
                            equippedweap.append('іржавий меч')
                            print('\n\n\n\n\nВи взяли іржавий меч')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='ніж відлюдника':
                    if 'ніж відлюдника' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('ніж відлюдника')
                            equippedweap.append('ніж відлюдника')
                            print('\n\n\n\n\nВи взяли ніж відлюдника')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='сталевий меч':
                    if 'сталевий меч' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('сталевий меч')
                            equippedweap.append('сталевий меч')
                            print('\n\n\n\n\nВи взяли сталевий меч')
                if itemon=='лісний кинджал':
                    if 'лісний кинджал' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('лісний кинджал')
                            equippedweap.append('лісний кинджал')
                            print('\n\n\n\n\nВи взяли лісний кинджал')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='вогняний меч':
                    if 'вогняний меч' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('вогняний меч')
                            equippedweap.append('вогняний меч')
                            print('\n\n\n\n\nВи взяли вогняний меч')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='отруєний кинджал':
                    if 'отруєний кинджал' in inv:
                        if len(equippedweap):
                            print('\n\n\n\n\nСпершу зніміть зброю, що використовується')
                        else:
                            inv.remove('отруєний кинджал')
                            equippedweap.append('отруєний кинджал')
                            print('\n\n\n\n\nВи взяли отруєний кинджал')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                ################           РЕГЕН
                if itemon=='яблуко':
                    if 'яблуко' in inv:
                        if hp<100:
                            apple=apple-1
                            hp=hp+25
                            if hp>100:
                                hp=100
                            if apple==0:
                                inv.remove('яблуко')
                            print('\n\n\n\n\nВи з\'їли яблуко, hp:', hp)
                        else:
                            print('\n\n\n\n\nНемає сенсу це робити')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='медовуха':
                    if 'медовуха' in inv:
                        if hp<100:
                            med=med-1
                            hp=hp+50
                            if hp>100:
                                hp=100
                            if med==0:
                                inv.remove('медовуха')
                            print('\n\n\n\n\nВи випили медовуху, hp:', hp)
                        else:
                            print('\n\n\n\n\nНемає сенсу це робити')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                #########################                  РОЗХІДНИКИ
                if itemon=='балончик запалювальної суміші':
                    if 'балончик запалювальної суміші' in inv:
                        print('\n\n\n\n\nВи не можете це використати')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='бутилочка з ядом':
                    if 'бутилочка з ядом' in inv:
                        print('\n\n\n\n\nВи не можете це використати')
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                if itemon=='1':
                    itemonloop=0
                if itemon=='1':
                    itemonloop=0
        if vubinv=='2':
            equloop=1
            while equloop==1:
                print('\n\n\n***ОБЛАДНАННЯ***\n', equippedweap)
                vubequ=str(input('\nЩо ви будете робити?\nЗняти предмет - 1\nназад - 2\n', ))
                if vubequ=='1':
                    equoff=str(input('\nЩо ви хочете зняти?\n', ))
                    if equoff=='розплавлений меч':
                        if 'розплавлений меч' in equippedweap:
                            equippedweap.remove('розплавлений меч')
                            inv.append('розплавлений меч')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                    if equoff=='катана роніна':
                        if 'катана роніна' in equippedweap:
                            equippedweap.remove('катана роніна')
                            inv.append('катана роніна')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                    if equoff=='іржавий меч':
                        if 'іржавий меч' in equippedweap:
                            equippedweap.remove('іржавий меч')
                            inv.append('іржавий меч')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                    if equoff=='ніж відлюдника':
                        if 'ніж відлюдника' in equippedweap:
                            equippedweap.remove('ніж відлюдника')
                            inv.append('ніж відлюдника')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                    if equoff=='сталевий меч':
                        if 'сталевий меч' in equippedweap:
                            equippedweap.remove('сталевий меч')
                            inv.append('сталевий меч')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                    if equoff=='лісний кинджал':
                        if 'лісний кинджал' in equippedweap:
                            equippedweap.remove('лісний кинджал')
                            inv.append('лісний кинджал')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                    if equoff=='вогняний меч':
                        if 'вогняний меч' in equippedweap:
                            equippedweap.remove('вогняний меч')
                            inv.append('вогняний меч')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                    if equoff=='отруєний кинджал':
                        if 'отруєний кинджал' in equippedweap:
                            equippedweap.remove('отруєний кинджал')
                            inv.append('отруєний кинджал')
                            print('\n\n\n\n\nВи зняли', equoff)
                        else:
                            print('\n\n\n\n\nУ вас такого немає')
                if vubequ=='2':
                    equloop=0
        if vubinv=='3':
            infoloop=1
            while infoloop==1:
                inf=str(input('\nПро що ви хочете дізнатись більше?\nназад - 1\n', ))
                ##############################                 ЗБРОЯ
                if inf=='розплавлений меч':
                    print('\n\n\n***РОЗПЛАВЛЕНИЙ МЕЧ***\nНанесення шкоди - 1-5')
                if inf=='іржавий меч':
                    print('\n\n\n***ІРЖАВИЙ МЕЧ***\nНанесення шкоди - 1-5')
                if inf=='ніж відлюдника':
                    print('\n\n\n***НІЖ ВІДЛЮДНИКА***\nНанесення шкоди - 3-7')
                if inf=='сталевий меч':
                    print('\n\n\n***СТАЛЕВИЙ МЕЧ***\nНанесення шкоди - 3-7')
                if inf=='лісний кинджал':
                    print('\n\n\n***ЛІСНИЙ КИНДЖАЛ***\nНанесення шкоди - 6-10')
                if inf=='катана роніна':
                    if 'катана роніна' in inv or 'катана роніна' in equippedweap:
                        print('\n\n\n***КАТАНА РОНІНА***\nНанесення шкоди - 10-15\nПеріодична шкода - 10 протягом 5 ходів')
                if inf=='вогняний меч':
                    print('\n\n\n***ВОГНЯНИЙ МЕЧ***\nНанесення шкоди - 8-12\nПеріодична шкода - 1 протягом 3 ходів')
                if inf=='отруєний кинджал':
                    print('\n\n\n***ОТРУЄНИЙ КИНДЖАЛ***\nНанесення шкоди - 6-10\nПеріодична шкода - 3 протягом 3 ходів')
                ##############################                 РЕГЕН
                if inf=='яблуко':
                    print('\n***ЯБЛУКО***\nВідновлення - 25hp\nКількість -', apple)
                if inf=='медовуха':
                    print('\n***МЕДОВУХА***\nВідновлення - 50hp\nКількість -', med)
                ##############################                 РОЗХІДНИКИ
                if inf=='балончик запалювальної суміші':
                    print('\n***БАЛОНЧИК ЗАПАЛЮВАЛЬНОЇ СУМІШІ***\nАвтоматично використовується вогняним мечем\nКількість -', firecan)
                if inf=='бутилочка з ядом':
                    print('\n***БУТИЛОЧКА З ЯДОМ***\nАвтоматично використовується отруєним кинджалом\nКількість -', poisonb)
                if inf=='1':
                    infoloop=0
        if vubinv=='4':
            invloop=0
##########################################               ФОРПОСТ 
def base():
    global hp
    baseloop=1
    while baseloop==1:
        print('\n\n\n\n\nВи знаходитесь в центрі форпоста найманців.')
        way=str(input('Куди підете?\n1 - ваша палатка(інвентар та сон)\n2 - крамниця(купівля та продаж)\n3 - вийти з форпосту\n', ))
        if way=='1':
            time.sleep(1)
            print('Ви йдете до палатки.')
            time.sleep(2)
            print('Ви йдете до палатки..')
            time.sleep(2)
            print('Ви йдете до палатки...')
            time.sleep(1)
            homeloop=1
            while homeloop==1:
                home=str(input('\n\n\n\n\nВи стоїте перед своєю палаткою\nЩо будете робити?\n1 - поспати(+10hp)\n2 - повернутись\n3 - інвентар\n'))
                if home=='1':
                    input('Ви лягаєте спати\nНатисніть Enter для продовження')
                    if hp<100:
                        time.sleep(1)
                        print('Вам сняться різні сни.')
                        time.sleep(2)
                        print('Вам сняться різні сни..')
                        time.sleep(2)
                        print('Вам сняться різні сни...')
                        time.sleep(1)
                        hp=hp+10
                        if hp>100:
                            hp=100
                    else:
                        print('\n\n\n\n\n\n\n\n\n\nВи не можете заснути')
                if home=='2':
                    time.sleep(1)
                    print('Ви йдете до центру форпосту.')
                    time.sleep(2)
                    print('Ви йдете до центру форпосту..')
                    time.sleep(2)
                    print('Ви йдете до центру форпосту...')
                    time.sleep(1)
                    homeloop=0
                if home=='3':
                    inventory()
        if way=='2':
            time.sleep(1)
            print('Ви йдете до крамниці.')
            time.sleep(2)
            print('Ви йдете до крамниці..')
            time.sleep(2)
            print('Ви йдете до крамниці...')
            time.sleep(1)
            shop()
        if way=='3':
            print('\n\n\n\n\nВи вирішуєте відправитись далі')
            time.sleep(2)
            print('Ви йдете до виходу з форпосту.')
            time.sleep(3)
            print('Ви йдете до виходу з форпосту..')
            time.sleep(3)
            print('Ви йдете до виходу з форпосту...')
            time.sleep(2)
            ways() 
##########################################             ШЛЯХИ
def ways():
    global forestroz
    global moneyf
    global medf
    global applef
    global money
    global med
    global apple
    waysloop=1
    while waysloop==1:
        waysloop1=1
        while waysloop1==1:
            way=str(input('\n\n\n\n\nПеред вами декілька шляхів\nКуди підете?\n1 - далі у ліс\n2 - до печер\n3 - третій шлях\n4 - повернутись у форпост\n'))
            if way=='1':
                input('\n\n\n\n\nВи вирішуєте йти далі в ліс\nНатисніть Enter для продовження')
                forest()
            if way=='2':
                if boss1==1:
                    input('\n\n\n\n\nВи вирішуєте йти в печери\nНатисніть Enter для продовження')
                    caves()
                else:
                    input('\n\n\n\n\nНайманці сказали, що вам туди поки зарано\nНатисніть Enter для продовження')
                    waysloop=0
            if way=='3':
                if boss2==1:
                    input('\n\n\n\n\nВи вирішуєте йти\nНатисніть Enter для продовження')
                else:
                    input('\n\n\n\n\nНайманці сказали, що вам туди поки зарано\nНатисніть Enter для продовження')
                    waysloop=0
            if way=='4':
                time.sleep(2)
                print('Ви повертаєтесь у форпост.')
                time.sleep(3)
                print('Ви повертаєтесь у форпост..')
                time.sleep(3)
                print('Ви повертаєтесь у форпост...')
                time.sleep(2)
                waysloop1=0
                base()
##########################################              ЛІС
def forest():
    global forestroz
    global moneyf
    global medf
    global applef
    global money
    global med
    global apple
    global foresttip
    global boss1
    forestloop=1
    while forestloop==1:
        if foresttip==1:    
            input('\n\n\n\n\nНайманці сказали вам, що в цій стороні лісу розбили табір приблизно 5 розбійників\nМожливо ви дізнаєтесь якусь корисну для вас інформацію в них\nНатисніть Enter для продовження\n')
            foresttip=0
        time.sleep(2)
        print('Ви йдете вглиб лісу.')
        if forestroz==5:
            pass
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав лісний розбійник\nНатисніть Enter для продовження')
                fighting()
                forestroz=forestroz+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати розбійника?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(1)
                        moneyf=random.randint(0,6)
                        applef=random.randint(1,3)
                        medf=random.randint(0,1)
                        apple=apple+applef
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        time.sleep(3)
        print('Ви йдете вглиб лісу..')
        if forestroz==5:
            pass
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав лісний розбійник\nНатисніть Enter для продовження')
                fighting()
                forestroz=forestroz+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати розбійника?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(1)
                        moneyf=random.randint(0,6)
                        applef=random.randint(1,3)
                        medf=random.randint(0,1)
                        apple=apple+applef
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        time.sleep(3)
        print('Ви йдете вглиб лісу...')
        time.sleep(2)
        if forestroz==5:
            print('\n\n\nЗдається лісних розбійників більше не залишилось\nВи продовжували йти по доріжці з притоптаних рослин\nАж поки не натрапили на їхній табір\nВ центрі табору була найбільша палатка, можливо там їх командир\n\nМоже перед тим, як туди заходити, варто повернутись у форпост та підготуватись?')
            bossvubloop=1
            while bossvubloop==1:
                bossvub=str(input('1 - ввійти у палатку\n2 - повернутись у форпост\n'))
                if bossvub=='1':
                    if boss1==1:
                        print('\n\n\n\n\nТам нічого немає\n')
                    else:
                        input('\n\n\n\n\nВи ввійшли в палатку. На щастя, там нікого не було\nПоки ви обшукували її в пошуках будь чого, що могло би дати вам хоч якусь інформацію\nВи почули, як розлітаються птахи. Спочатку ви не звернули на це увагу\nАле у палатку зайшов дуже високий чоловік зі списом в руках. Це їхній командир!\nНатисніть Enter для продовження\n')
                        bossfighting()
                if bossvub=='2':
                    bossvubloop=0
                    time.sleep(2)
                    print('Ви повертаєтесь у форпост.')
                    time.sleep(3)
                    print('Ви повертаєтесь у форпост..')
                    time.sleep(3)
                    print('Ви повертаєтесь у форпост...')
                    time.sleep(2)
                    base()
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав лісний розбійник\nНатисніть Enter для продовження')
                fighting()
                forestroz=forestroz+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати розбійника?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        forestknife=random.randint(1,25)
                        if forestknife==1:
                            input('Ви знайшли лісний кинджал!\nНатисніть Enter для продовження')
                            inv.append('лісний кинджал')
                        time.sleep(1)
                        moneyf=random.randint(0,6)
                        applef=random.randint(1,3)
                        medf=random.randint(0,1)
                        apple=apple+applef
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        forestvub=1
        while forestvub==1:
            dia=input('\n\n\nЩо ви будете робити далі?\n1 - продовжити свій шлях\n2 - повернутись у форпост\n', )
            if dia=='1':
                forestvub=0
            if dia=='2':
                time.sleep(2)
                print('Ви повертаєтесь у форпост.')
                time.sleep(3)
                print('Ви повертаєтесь у форпост..')
                time.sleep(3)
                print('Ви повертаєтесь у форпост...')
                time.sleep(2)
                base()
##########################################               ПЕЧЕРИ
def caves():
    global dwarf
    global moneyf
    global medf
    global applef
    global money
    global med
    global apple
    global cavetip
    global boss1
    global firecan
    global firecanf
    global dwarfen
    caveloop=1
    while caveloop==1:
        if cavetip==1:    
            input('\n\n\n\n\nНайманці сказали вам, що в цих печерах недавно поселилось десь 10 дворфів\nМожливо ви дізнаєтесь якусь корисну для вас інформацію в них\nНатисніть Enter для продовження\n')
            cavetip=0
        time.sleep(2)
        print('Ви спускаєтесь в печери.')
        if dwarf==10:
            pass
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав дворф. У нього палаючий меч!\nНатисніть Enter для продовження')
                dwarfen=1
                fighting()
                dwarf=dwarf+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати дворфа?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(1)
                        firecanf=random.randint(0,7)
                        moneyf=random.randint(2,8)
                        applef=random.randint(1,5)
                        medf=random.randint(0,4)
                        apple=apple+applef
                        firecan=firecan+firecanf
                        if firecanf>0:
                            if 'балончик запалювальної суміші' not in inv:
                                inv.append('балончик запалювальної суміші')
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if firecanf>0:
                            print('Балончик запалювальної суміші', firecanf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        time.sleep(3)
        print('Ви спускаєтесь в печери..')
        if dwarf==10:
            pass
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав дворф. У нього палаючий меч!\nНатисніть Enter для продовження')
                dwarfen=1
                fighting()
                dwarf=dwarf+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати дворфа?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(1)
                        firecanf=random.randint(0,7)
                        moneyf=random.randint(2,8)
                        applef=random.randint(1,5)
                        medf=random.randint(0,4)
                        apple=apple+applef
                        firecan=firecan+firecanf
                        if firecanf>0:
                            if 'балончик запалювальної суміші' not in inv:
                                inv.append('балончик запалювальної суміші')
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if firecanf>0:
                            print('Балончик запалювальної суміші', firecanf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        time.sleep(3)
        print('Ви спускаєтесь в печери...')
        time.sleep(2)
        if dwarf==10:
            print('\n\n\nЗдається дворфів тут більше не залишилось\nВи продовжували йти по печерам\nАж поки не натрапили стіну з дерев\'яними дверима\n\n\nМоже перед тим, як туди заходити, варто повернутись у форпост та підготуватись?')
            bossvubloop=1
            while bossvubloop==1:
                bossvub=str(input('1 - ввійти за двері\n2 - повернутись у форпост\n'))
                if bossvub=='1':
                    if boss2==1:
                        print('\n\n\n\n\nТам нічого немає')
                    else:
                        input('\n\n\n\n\nВи відкрили двері та зайшли. За ними була кімната повністю закладена інструментами та шестернями\nПоки ви обшукували її в пошуках будь чого, що могло би дати вам хоч якусь інформацію\nВи почули, як з гуркітом захлопнулись двері. Цей звук ехом пролунав по всій печерній системі\nВи швидко повернулись до дверей. Там стояв досить великий дворф з палаючим молотом\nНатисніть Enter для продовження\n')
                        bossfighting()
                if bossvub=='2':
                    bossvubloop=0
                    time.sleep(2)
                    print('Ви повертаєтесь у форпост.')
                    time.sleep(3)
                    print('Ви повертаєтесь у форпост..')
                    time.sleep(3)
                    print('Ви повертаєтесь у форпост...')
                    time.sleep(2)
                    base()
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав дворф. У нього палаючий меч!\nНатисніть Enter для продовження')
                dwarfen=1
                fighting()
                dwarf=dwarf+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати дворфа?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        firesword=random.randint(1,25)
                        if firesword==1:
                            input('Ви знайшли вогняний меч!\nНатисніть Enter для продовження')
                            inv.append('вогняний меч')
                        time.sleep(1)
                        firecanf=random.randint(0,7)
                        moneyf=random.randint(2,8)
                        applef=random.randint(1,5)
                        medf=random.randint(0,4)
                        apple=apple+applef
                        firecan=firecan+firecanf
                        if firecanf>0:
                            if 'балончик запалювальної суміші' not in inv:
                                inv.append('балончик запалювальної суміші')
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if firecanf>0:
                            print('Балончик запалювальної суміші', firecanf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        cavevub=1
        while cavevub==1:
            dia=input('\n\n\nЩо ви будете робити далі?\n1 - продовжити свій шлях\n2 - повернутись у форпост\n', )
            if dia=='1':
                cavevub=0
            if dia=='2':
                time.sleep(2)
                print('Ви повертаєтесь у форпост.')
                time.sleep(3)
                print('Ви повертаєтесь у форпост..')
                time.sleep(3)
                print('Ви повертаєтесь у форпост...')
                time.sleep(2)
                base()
##########################################              ОСОБНЯК
def mansion():
    global alchemist
    global moneyf
    global medf
    global applef
    global money
    global med
    global apple
    global mansiontip
    global boss2
    global poisb
    global poisbf
    global alchemisten
    mansionloop=1
    while mansionloop==1:
        if mansiontip==1:    
            input('\n\n\n\n\nНайманці сказали вам, що в цьому особняку живе 5 алхіміків\nМожливо ви дізнаєтесь якусь корисну для вас інформацію в них\nНатисніть Enter для продовження\n')
            mansiontip=0
        time.sleep(2)
        print('Ви ходите кімнатами особняка.')
        if alchemist==5:
            pass
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав алхімік. У нього отруєний кинджал!\nНатисніть Enter для продовження')
                alchemisten=1
                fighting()
                alchemist=alchemist+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати алхіміка?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(1)
                        poiswordget=0
                        poisbf=random.randint(0,11)
                        moneyf=random.randint(2,12)
                        applef=random.randint(2,9)
                        medf=random.randint(0,6)
                        apple=apple+applef
                        poisb=poisb+poisbf
                        if poisbf>0:
                            if 'бутилочка з ядом' not in inv:
                                inv.append('бутилочка з ядом')
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if poisbf>0:
                            print('Бутилочка з ядом', poisbf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        time.sleep(3)
        print('Ви ходите кімнатами особняка..')
        if alchemist==5:
            pass
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав алхімік. У нього отруєний кинджал!\nНатисніть Enter для продовження')
                alchemisten=1
                fighting()
                alchemist=alchemist+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати алхіміка?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(1)
                        poiswordget=0
                        poisbf=random.randint(0,11)
                        moneyf=random.randint(2,12)
                        applef=random.randint(2,9)
                        medf=random.randint(0,6)
                        apple=apple+applef
                        poisb=poisb+poisbf
                        if poisbf>0:
                            if 'бутилочка з ядом' not in inv:
                                inv.append('бутилочка з ядом')
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if poisbf>0:
                            print('Бутилочка з ядом', poisbf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        time.sleep(3)
        print('Ви ходите кімнатами особняка...')
        time.sleep(2)
        if alchemist==5:
            print('\n\n\nЗдається алхіміків тут більше не залишилось\nВи продовжували обшукувати кімнати особняка\nАж поки не натрапили на величезні двері\n\n\nМоже перед тим, як туди заходити, варто повернутись у форпост та підготуватись?')
            bossvubloop=1
            while bossvubloop==1:
                bossvub=str(input('1 - ввійти в кімнату\n2 - повернутись у форпост\n'))
                if bossvub=='1':
                    input('\n\n\n\n\nВи відкрили двері та зайшли. У кімнаті було багато колб\nДеякі з них були заповнені кров\'ю, деякі пусті, а інші - були з тим самим сяючим зіллям\nВи почули, як з гуркітом захлопнулись двері\nВи швидко повернулись до дверей. Там стояв чоловік з отруєним кинджалом\nНатисніть Enter для продовження\n')
                    bossfighting()
                if bossvub=='2':
                    bossvubloop=0
                    time.sleep(2)
                    print('Ви повертаєтесь у форпост.')
                    time.sleep(3)
                    print('Ви повертаєтесь у форпост..')
                    time.sleep(3)
                    print('Ви повертаєтесь у форпост...')
                    time.sleep(2)
                    base()
        else:
            napad=random.randint(1,6)
            if napad==1:
                input('\n\n\n\n\nПоки ви йшли, на вас напав алхімік. У нього отруєний кинджал!\nНатисніть Enter для продовження')
                alchemisten=1
                fighting()
                alchemist=alchemist+1
                vubloop=1
                while vubloop==1:
                    vub=str(input('\n\n\n\n\nОбшукати алхіміка?\n(так, ні)\n', ))
                    if vub=='так':
                        time.sleep(1)
                        print('Ви обшукуєте тіло.')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(2)
                        print('Ви обшукуєте тіло..')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(2)
                        print('Ви обшукуєте тіло...')
                        if poiswordget==0:
                            poisword=random.randint(1,15)
                            if poisword==1:
                                input('Ви знайшли отруєний кинджал!\nНатисніть Enter для продовження')
                                inv.append('отруєний кинджал')
                                poiswordget=1
                        time.sleep(1)
                        poiswordget=0
                        poisbf=random.randint(0,11)
                        moneyf=random.randint(2,12)
                        applef=random.randint(2,9)
                        medf=random.randint(0,6)
                        apple=apple+applef
                        poisb=poisb+poisbf
                        if poisbf>0:
                            if 'бутилочка з ядом' not in inv:
                                inv.append('бутилочка з ядом')
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                        med=med+medf
                        if med>0:    
                            if 'медовуха' not in inv:
                                inv.append('медовуха')
                        money=money+moneyf
                        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
                        if moneyf>0:
                            print('Монети:', moneyf)
                        if poisbf>0:
                            print('Бутилочка з ядом', poisbf)
                        if medf>0:
                            print('Медовуха:', medf)
                        print('Яблука:', applef)
                        loop=1
                        while loop==1:
                            vub=str(input('\nВідкрити інвентар?\n(так, ні)\n', ))
                            if vub=='так':
                                inventory()
                                vubloop=0
                                loop=0
                            if vub=='ні':
                                loop=0
                                vubloop=0
                            else:
                                pass
                    if vub=='ні':
                        vubloop=0
        mansionvub=1
        while mansionvub==1:
            dia=input('\n\n\nЩо ви будете робити далі?\n1 - продовжити свій шлях\n2 - повернутись у форпост\n', )
            if dia=='1':
                mansionvub=0
            if dia=='2':
                time.sleep(2)
                print('Ви повертаєтесь у форпост.')
                time.sleep(3)
                print('Ви повертаєтесь у форпост..')
                time.sleep(3)
                print('Ви повертаєтесь у форпост...')
                time.sleep(2)
                base()
##########################################              МАГАЗИН
def shop():
    global apple
    global med
    global money
    global firecan
    global boss1
    global firecanshopstart
    global patana
    global poisb
    global poisbshopstart
    appleshop=apple
    medshop=med
    firecanshop=firecan
    poisbshop=poisb
    moneycanuse=money
    input('\n\n\n\n\nКоли ви підійшли до крамниці, продавець з вами привітався\nНатисніть Enter для продовження')
    if 'балончик запалювальної суміші' in inv:
        if firecanshopstart==0:
            input('\n\n\n\n\nСлухай, а що це в тебе висить на поясі? Дай подивлюсь\nЦе якась запалювальна суміш? Якщо тобі така потрібна, я знаю, через кого її дістати\nЯкщо захочеш купити - звертайся\nНатисніть Enter для продовження\n')
            firecanshopstart=1
    if 'бутилочка з ядом' in inv:
        if poisbshopstart==0:
            input('\n\n\n\n\nСлухай, а що це в тебе висить на поясі? Дай подивлюсь\nЦе якийсь яд? Якщо тобі таке потрібно, я знаю, через кого це дістати\nЯкщо захочеш купити - звертайся\nНатисніть Enter для продовження\n')
            poisbshopstart=1
    shoploop=1
    while shoploop==1:
        print('\n\n\n\n\nВаш баланс:', moneycanuse)
        buy=str(input('\nХочете щось купити - 1\nЧи маєте якийсь товар на продажу? - 2\nПовернутись - 3\n', ))
        if buy=='1':
            buyloop=1
            while buyloop==1:
                print('\n\nЩо бажаєте купити?\nяблуко - 5 монет\nмедовуха - 10 монет\nсталевий меч - 20 монет')
                if firecanshopstart==1:
                    print('\nбалончик запалювальної суміші - 3 монети')
                if poisbshopstart==1:
                    print('\nбутилочка з ядом - 3 монети')
                print('\nназад - 1\n')
                buyreg=str(input())
                if buyreg=='яблуко':
                    appleloop=1
                    while appleloop==1:
                        print('\n\n\nВаш баланс:', moneycanuse)
                        try:
                            howm=int(input('\nСкільки хочете купити?(цифрою)\nОдне яблуко - 5 монет\n(щоб повернутись назад, напишіть - 999)\n', ))
                            if howm==999:
                                appleloop=0
                            if moneycanuse<howm*5:
                                print('\n\n\n\n\nУ вас не вистачить грошей.')
                                buyloop=1
                                break
                            if 'яблуко' in inv:
                                howmprice=howm*5
                                appleshop=appleshop+howm
                                moneycanuse=moneycanuse-howmprice
                                buyloop=0
                                break
                            else:
                                howmprice=howm*5
                                inv.append('яблуко')
                                appleshop=appleshop+howm
                                moneycanuse=moneycanuse-howmprice
                                buyloop=0
                                break
                        except ValueError:
                            print('\n\n\n\nВведіть кількість цифрою')
                if buyreg=='медовуха':
                    medloop=1
                    while medloop==1:
                        print('\nВаш баланс:', moneycanuse)
                        try:
                            howm=int(input('\nСкільки хочете купити?(цифрою)\nОдна пляшка медовухи - 10 монет\n(щоб повернутись назад, напишіть - 999)\n', ))
                            if howm==999:
                                medloop=0
                            if moneycanuse<howm*10:
                                print('\n\n\n\n\nУ вас не вистачить грошей.')
                                buyloop=1
                                break
                            if 'медовуха' in inv:
                                howmprice=howm*10
                                medshop=medshop+howm
                                moneycanuse=moneycanuse-howmprice
                                buyloop=0
                                break
                            else:
                                howmprice=howm*10
                                inv.append('медовуха')
                                medshop=medshop+howm
                                moneycanuse=moneycanuse-howmprice
                                buyloop=0
                                break
                        except ValueError:
                            print('\n\n\n\nВведіть кількість цифрою')
                if buyreg=='сталевий меч':
                    print('\nВаш баланс:', moneycanuse)
                    howm=str(input('\nСталевий меч = 20 монет. Ви впевнені, що хочете його купити?\n(так, ні)\n', ))
                    if howm=='так':
                        if moneycanuse<20:
                            print('\n\n\n\n\nУ вас не вистачить грошей.')
                        else:
                            moneycanuse=moneycanuse-20
                            inv.append('сталевий меч')
                            buyloop=0
                if buyreg=='балончик запалювальної суміші':
                    if firecanshopstart==1:
                        firecanloop=1
                        while firecanloop==1:
                            print('\n\n\nВаш баланс:', moneycanuse)
                            try:
                                howm=int(input('\nСкільки хочете купити?(цифрою)\nОдин балончик - 3 монети\n(щоб повернутись назад, напишіть - 999)\n', ))
                                if howm==999:
                                    firecanloop=0
                                if moneycanuse<howm*3:
                                    print('\n\n\n\n\nУ вас не вистачить грошей.')
                                    buyloop=1
                                    break
                                if 'балончик запалювальної суміші' in inv:
                                    howmprice=howm*3
                                    firecanshop=firecanshop+howm
                                    moneycanuse=moneycanuse-howmprice
                                    buyloop=0
                                    break
                                else:
                                    howmprice=howm*3
                                    inv.append('балончик запалювальної суміші')
                                    firecanshop=firecanshop+howm
                                    moneycanuse=moneycanuse-howmprice
                                    buyloop=0
                                    break
                            except ValueError:
                                print('\n\n\n\nВведіть кількість цифрою')
                if buyreg=='бутилочка з ядом':
                    if poisbshopstart==1:
                        poisbloop=1
                        while poisbloop==1:
                            print('\n\n\nВаш баланс:', moneycanuse)
                            try:
                                howm=int(input('\nСкільки хочете купити?(цифрою)\nОдна бутилочка - 3 монети\n(щоб повернутись назад, напишіть - 999)\n', ))
                                if howm==999:
                                    poisbloop=0
                                if moneycanuse<howm*3:
                                    print('\n\n\n\n\nУ вас не вистачить грошей.')
                                    buyloop=1
                                    break
                                if 'бутилочка з ядом' in inv:
                                    howmprice=howm*3
                                    poisbshop=poisbshop+howm
                                    moneycanuse=moneycanuse-howmprice
                                    buyloop=0
                                    break
                                else:
                                    howmprice=howm*3
                                    inv.append('бутилочка з ядом')
                                    poisbshop=poisbshop+howm
                                    moneycanuse=moneycanuse-howmprice
                                    buyloop=0
                                    break
                            except ValueError:
                                print('\n\n\n\nВведіть кількість цифрою')
                if buyreg=='1':
                    buyloop=0   
        if buy=='2':
            sellitemloop=1
            while sellitemloop==1:
                print('\n\n\n\n\n***РЕЧІ НА ПРОДАЖ***\nУ вас є:')
                ################           ЗБРОЯ ПРОДАЖ
                if 'розплавлений меч' in inv:
                    print('\nрозплавлений меч')
                if 'іржавий меч' in inv:
                    print('\nіржавий меч')
                if 'ніж відлюдника' in inv:
                    print('\nніж відлюдника')
                if 'сталевий меч' in inv:
                    print('\nсталевий меч')
                if 'лісний кинджал' in inv:
                    print('\nлісний кинджал')
                if 'отруєний кинджал' in inv:
                    print('\nотруєний кинджал')
                ################           РЕГЕН ПРОДАЖ
                if 'яблуко' in inv:
                    print('\nяблуко:', appleshop, 'шт')
                if 'медовуха' in inv:
                    print('\nмедовуха', medshop, 'шт')
                sell=str(input('\nЩо ви хочете продати?\nназад - 1\n', ))
                ################           РОЗХІДНИКИ ПРОДАЖ
                if 'балончик запалювальної суміші' in inv:
                    print('\nбалончик запалювальної суміші:', firecanshop, 'шт')
                if 'бутилочка з ядом' in inv:
                    print('\nбутилочка з ядом:', poisbshop, 'шт')
                ################           ЗБРОЯ ПРОДАЖ
                if sell=='розплавлений меч':
                    if 'розплавлений меч' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nрозплавлений меч = 15 монет. Ви впевнені, що хочете його продати?\n(так, ні)\n', ))
                            if sold=='так':
                                inv.remove('розплавлений меч')
                                moneycanuse=moneycanuse+15
                                print('\n\n\n\n\nВи продали', sell)
                                sellloop=0
                            if sold=='ні':
                                sellloop=0
                if sell=='іржавий меч':
                    if 'іржавий меч' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nіржавий меч = 15 монет. Ви впевнені, що хочете його продати?\n(так, ні)\n', ))
                            if sold=='так':
                                inv.remove('іржавий меч')
                                moneycanuse=moneycanuse+15
                                print('\n\n\n\n\nВи продали', sell)
                                sellloop=0
                            if sold=='ні':
                                sellloop=0
                if sell=='ніж відлюдника':
                    if 'ніж відлюдника' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nніж відлюдника = 20 монет. Ви впевнені, що хочете його продати?\n(так, ні)\n', ))
                            if sold=='так':
                                inv.remove('ніж відлюдника')
                                moneycanuse=moneycanuse+20
                                sellloop=0
                                print('\n\n\n\n\nВи продали', sell)
                            if sold=='ні':
                                sellloop=0
                if sell=='сталевий меч':
                    if 'сталевий меч' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nсталевий меч = 20 монет. Ви впевнені, що хочете його продати?\n(так, ні)\n', ))
                            if sold=='так':
                                inv.remove('сталевий меч')
                                moneycanuse=moneycanuse+20
                                sellloop=0
                                print('\n\n\n\n\nВи продали', sell)
                            if sold=='ні':
                                sellloop=0
                if sell=='лісний кинджал':
                    if 'лісний кинджал' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nлісний кинджал = 30 монет. Ви впевнені, що хочете його продати?\n(так, ні)\n', ))
                            if sold=='так':
                                inv.remove('лісний кинджал')
                                moneycanuse=moneycanuse+30
                                print('\n\n\n\n\nВи продали', sell)
                                sellloop=0
                            if sold=='ні':
                                sellloop=0
                if sell=='вогняний меч':
                    if 'вогняний меч' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nвогняний меч = 50 монет. Ви впевнені, що хочете його продати?\n(так, ні)\n', ))
                            if sold=='так':
                                inv.remove('вогняний меч')
                                moneycanuse=moneycanuse+50
                                print('\n\n\n\n\nВи продали', sell)
                                sellloop=0
                            if sold=='ні':
                                sellloop=0
                if sell=='отруєний кинджал':
                    if 'отруєний кинджал' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nотруєний кинджал = 65 монет. Ви впевнені, що хочете його продати?\n(так, ні)\n', ))
                            if sold=='так':
                                inv.remove('отруєний кинджал')
                                moneycanuse=moneycanuse+65
                                print('\n\n\n\n\nВи продали', sell)
                                sellloop=0
                            if sold=='ні':
                                sellloop=0
                if sell=='1':
                    sellitemloop=0
                #################       РЕГЕН ПРОДАЖ
                if sell=='яблуко':
                    if 'яблуко' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nодне яблуко = 3 монети, ви впевнені, що хочете їх продавати?\n(так, ні)\n', ))
                            if sold=='так':
                                try:
                                    howm=int(input('\nСкільки яблук ви хочете продати?(цифрою)\n', ))
                                    if howm>appleshop:
                                        print('\n\n\n\n\nУ вас стільки немає')
                                        break
                                    appleshop=appleshop-howm
                                    howmprice=howm*3
                                    if apple==0:
                                        inv.remove('яблуко')
                                    moneycanuse=moneycanuse+howmprice
                                    print('\n\n\n\n\nВи продали', sell,'-', howm, 'шт')
                                    sellitemloop=0
                                    sellloop=0
                                except ValueError:
                                    print('\n\n\n\n\nВведіть кількість цифрою')
                            if sold=='ні':
                                sellloop=0
                                sellitemloop=0
                    else:
                        sellloop=1
                if sell=='медовуха':
                    if 'медовуха' in inv:
                        sellloop=1
                        while sellloop==1:
                            sold=str(input('\nодна пляшка медовухи = 8 монет, ви впевнені, що хочете їх продавати?\n(так, ні)\n', ))
                            if sold=='так':
                                try:
                                    howm=int(input('\nСкільки пляшок ви хочете продати?(цифрою)\n', ))
                                    if howm>medshop:
                                        print('\n\n\n\n\nУ вас стільки немає')
                                        break
                                    medshop=medshop-howm
                                    howmprice=howm*8
                                    if medshop==0:
                                        inv.remove('медовуха')
                                    moneycanuse=moneycanuse+howmprice
                                    print('\n\n\n\n\nВи продали', sell,'-', howm, 'шт')
                                    sellitemloop=0
                                    sellloop=0
                                except ValueError:
                                    print('\n\n\n\nВведіть кількість цифрою')
                            if sold=='ні':
                                sellloop=0
                                sellitemloop=0
                    else:
                        print('\n\n\n\n\nУ вас такого немає')
                        sellloop=0
                        sellitemloop=0
                #################       РОЗХІДНИКИ ПРОДАЖ
                if sell=='балончик запалювальної суміші':
                    if firecanshopstart==1:
                        if 'балончик запалювальної суміші' in inv:
                            sellloop=1
                            while sellloop==1:
                                sold=str(input('\nодин балончик = 3 монети, ви впевнені, що хочете їх продавати?\n(так, ні)\n', ))
                                if sold=='так':
                                    try:
                                        howm=int(input('\nСкільки балончиків ви хочете продати?(цифрою)\n', ))
                                        if howm>firecanshop:
                                            print('\n\n\n\n\nУ вас стільки немає')
                                            break
                                        firecanshop=firecanshop-howm
                                        howmprice=howm*3
                                        if firecanshop==0:
                                            if 'балончик запалювальної суміші' in inv:
                                                inv.remove('балончик запалювальної суміші')
                                        moneycanuse=moneycanuse+howmprice
                                        print('\n\n\n\n\nВи продали', sell,'-', howm, 'шт')
                                        sellitemloop=0
                                        sellloop=0
                                    except ValueError:
                                        print('\n\n\n\nВведіть кількість цифрою')
                                if sold=='ні':
                                    sellloop=0
                                    sellitemloop=0
                if sell=='бутилочка з ядом':
                    if poisbshopstart==1:
                        if 'бутилочка з ядом' in inv:
                            sellloop=1
                            while sellloop==1:
                                sold=str(input('\nодна бутилочка = 3 монети, ви впевнені, що хочете їх продавати?\n(так, ні)\n', ))
                                if sold=='так':
                                    try:
                                        howm=int(input('\nСкільки бутилочок ви хочете продати?(цифрою)\n', ))
                                        if howm>poisbshop:
                                            print('\n\n\n\n\nУ вас стільки немає')
                                            break
                                        poisbshop=poisbshop-howm
                                        howmprice=howm*3
                                        if poisbshop==0:
                                            if 'бутилочка з ядом' in inv:
                                                inv.remove('бутилочка з ядом')
                                        moneycanuse=moneycanuse+howmprice
                                        print('\n\n\n\n\nВи продали', sell,'-', howm, 'шт')
                                        sellitemloop=0
                                        sellloop=0
                                    except ValueError:
                                        print('\n\n\n\nВведіть кількість цифрою')
                                if sold=='ні':
                                    sellloop=0
                                    sellitemloop=0
        if buy=='ронін':
            if patana==0:
                input('\n\n\n\n\nЩо це слово взагалі означає?\nО, точно, я тут недавно на полі битви знайшов такий от цікавий меч\nТобі його не треба? Віддам безкоштовно\nНатисніть Enter для продовження')
                inv.append('катана роніна')
                patana=1
        if buy=='3':
            money=moneycanuse
            apple=appleshop
            med=medshop
            firecan=firecanshop
            time.sleep(1)
            print('Ви йдете до центру форпосту.')
            time.sleep(2)
            print('Ви йдете до центру форпосту..')
            time.sleep(2)
            print('Ви йдете до центру форпосту...')
            time.sleep(1)
            shoploop=0
            base()
##########################################               ФАЙТИНГ
def fighting():
    global hp
    global death
    global enemyhp
    global enemydmg
    global dmg
    global apple
    global med
    global lasthp
    global firecan
    global firecanfight
    global applefight
    global medfight
    global memoryhp
    global memoryfirecan
    global dofire
    global bleed
    global dobleed
    global fireat
    global enemyfiring
    global enemybleed
    global dwarfen
    global alchemisten
    global alchemistpois
    global dwarffire
    global dopois
    global enemypois
    global poisb
    global poisat
    enemyfiring=1
    enemybleed=1
    enemypois=1
    block=0
    attack=0
    lasthp=hp
    memoryhp=hp
    applefight=apple
    medfight=med
    firecanfight=firecan
    poisbfight=poisb
    memoryfirecan=firecan
    memorypoisb=poisb
    print('\n\n\nПрийдеться битись!\n')
    if boss2==1:
        enemyhp=100
    if boss1==1:
        enemyhp=75
    else:
        enemyhp=60
    fightloop=1
    while fightloop==1:
        fightloop1=1
        while fightloop1==1:
            attack=0
            block=0
            print('Ваше здоров\'я:', lasthp, '\nЗдоров\'я противника:', enemyhp)
            if enemyhp<=0:
                print('\n\n\n\n\nВи перемогли')
                firecan=firecanfight
                poisb=poisbfight
                hp=lasthp
                fightloop=0
                fireat=4
                poisat=4
                enemyfiring=0
                enemybleed=0
                enemypois=0
                bleed=6
                dwarffire=4
                alchemistpois=4
                break
            if lasthp<=0:
                print('\n\n\nВи втратили все hp в результаті чого померли...')
                if boss2==1:
                    enemyhp=100
                if boss1==1:
                    enemyhp=75
                else:
                    enemyhp=60
                death=1
                firecanfight=firecan
                poisbfight=poisb
                dwarffire=4
                alchemistpois=4
                if firecanfight>0:
                    if 'балончик запалювальної суміші' not in inv:
                        inv.append('балончик запалювальної суміші')
                if poisbfight>0:
                    if 'бутилочка з ядом' not in inv:
                        inv.append('бутилочка з ядом')
                lasthp=hp
                apple=applefight
                med=medfight
                fireat=4
                bleed=6
                poisat=4
                if apple>0:
                    if 'яблуко' not in inv:
                        inv.append('яблуко')
                if med>0:
                    if 'медовуха' not in inv:
                        inv.append('медовуха')
            if death==1:
                reviveloop=1
                while reviveloop==1:
                    revive=str(input('Повернутись до послідньої битви?\n(так)\n'))
                    if revive=='так':
                        time.sleep(1)
                        print('Зачекайте.')
                        time.sleep(2)
                        print('Зачекайте..')
                        time.sleep(2)
                        print('Зачекайте...')
                        time.sleep(1)
                        print('\nПрийдеться битись!\n\n\n')
                        if boss2==1:
                            enemyhp=100
                        if boss1==1:
                            enemyhp=75
                        else:
                            enemyhp=60
                        reviveloop=0
                death=0
            udarplloop=1
            while udarplloop==1:
                udarpl=str(input('\nВаш хід\nЩо будете робити?\n1 - вдарити\n2 - захищатись\n3 - інвентар\n', ))
                if udarpl=='1':
                    print('\n\n\n\n\nВи атакуєте')
                    attack=1
                    break
                if udarpl=='2':
                    print('\n\n\n\n\nВи поставили блок\n')
                    block=1
                    break
                if udarpl=='3':
                    firecan=firecanfight
                    poisb=poisbfight
                    hp=lasthp
                    inventory()
                    lasthp=hp
                    firecan=memoryfirecan
                    poisb=memorypoisb
                    hp=memoryhp
                    print('\n\nВаше здоров\'я:', lasthp, '\nЗдоров\'я противника:', enemyhp)
            print('\nХід противника\nЗачекайте')
            time.sleep(1)
            udaren=random.randint(1,5)
            if udaren==5:
                print('\n\n\n\n\nПротивник поставив блок\n')
                if attack==1:
                    print('\nПротивник заблокував атаку\n')
                    if dwarfen==1:
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                    if alchemisten==1:
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                    firing()
                    bleedeff()
                    poisoning()
                    attack=0
                    break
                else:
                    if dwarfen==1:
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                    if alchemisten==1:
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                    firing()
                    bleedeff()
                    poisoning()
            else:
                print('\n\n\n\n\nПротивник атакує')
                if block==1:
                    print('\nВи заблокували атаку\n')
                    if dwarfen==1:
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                    if alchemisten==1:
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                    firing()
                    bleedeff()
                    poisoning()
                    block=0
                    break
                whudar=random.randint(1,2)
                if attack==1:
                    if whudar==1:
                        print('\nВи ухилились і контратакували\n')
                        if len(equippedweap):
                            if 'розплавлений меч' in equippedweap:
                                dmg=random.randint(1,5)
                            if 'катана роніна' in equippedweap:
                                dmg=random.randint(10,15)
                            if 'іржавий меч' in equippedweap:
                                dmg=random.randint(1,5)
                            if 'ніж відлюдника' in equippedweap:
                                dmg=random.randint(3,7)
                            if 'сталевий меч' in equippedweap:
                                dmg=random.randint(3,7)
                            if 'лісний кинджал' in equippedweap:
                                dmg=random.randint(6,10)
                            if 'вогняний меч' in equippedweap:
                                dmg=random.randint(8,12)
                            if 'отруєний кинджал' in equippedweap:
                                dmg=random.randint(6,10)
                            if 'отруєний кинджал' in equippedweap:
                                dmg=random.randint(6,10)
                        else:
                            dmg=random.randint(1,2)
                        if dwarfen==1:
                            if dwarffire<4:
                                print('Ви палаєте\n')
                                dwarffire=dwarffire-1
                                lasthp=lasthp-1
                            if dwarffire==0:
                                print('Ви перестали палати\n')
                                dwarffire=4
                        if alchemisten==1:
                            if alchemistpois<4:
                                print('Ви отруєні\n')
                                alchemistpois=alchemistpois-1
                                lasthp=lasthp-3
                            if alchemistpois==0:
                                print('Ви більше не відчуваєте себе отруєним\n')
                                alchemistpois=4
                        firing()
                        bleedeff()
                        poisoning()
                        if 'вогняний меч' in equippedweap:
                            if fireat==4:
                                if firecanfight>0:
                                    firecanfight=firecanfight-1
                                    dofire=1
                                    print('Ви підпалили противника\n')
                                    firing()
                            if firecanfight==0:
                                if 'балончик запалювальної суміші' in inv:
                                    inv.remove('балончик запалювальної суміші')
                        if 'отруєний кинджал' in equippedweap:
                            if poisat==4:
                                if poisbfight>0:
                                    poisbfight=poisbfight-1
                                    dopois=1
                                    print('Ви отруїли противника\n')
                                    poisoning()
                            if poisbfight==0:
                                if 'бутилочка з ядом' in inv:
                                    inv.remove('бутилочка з ядом')
                        if 'катана роніна' in equippedweap:
                            if bleed==6:
                                dobleed=1
                                print('Ви нанесли кровоточиву рану противнику\n')
                                bleedeff()
                        attack=0
                        block=0
                        enemyhp=enemyhp-dmg
                    if whudar==2:
                        print('\nПротивник ухилився і контратакував\n')
                        firing()
                        bleedeff()
                        poisoning()
                        if boss2==1:
                            enemydmg=random.randint(10,15)
                        if boss1==1:
                            enemydmg=random.randint(7,10)
                        else:
                            enemydmg=random.randint(5,7)
                        if dwarfen==1:
                            if dwarffire==4:
                                print('Противник вас підпалив\n')
                                dwarffire=dwarffire-1
                            if dwarffire<4:
                                print('Ви палаєте\n')
                                dwarffire=dwarffire-1
                                lasthp=lasthp-1
                            if dwarffire==0:
                                print('Ви перестали палати\n')
                                dwarffire=4
                        if alchemisten==1:
                            if alchemistpois==4:
                                print('Противник вас отруїв\n')
                                alchemistpois=alchemistpois-1
                            if alchemistpois<4:
                                print('Ви отруєні\n')
                                alchemistpois=alchemistpois-1
                                lasthp=lasthp-3
                            if alchemistpois==0:
                                print('Ви більше не відчуваєте себе отруєним\n')
                                alchemistpois=4
                        lasthp=lasthp-enemydmg
                attack=0
                block=0
######################################                           БОС ФАЙТИНГ
def bossfighting():
    global hp
    global death
    global bosshp
    global bossdmg
    global dmg
    global apple
    global med
    global lasthp
    global memoryhp
    global firecan
    global poisb
    global firecanfight
    global poisbfight
    global applefight
    global medfight
    global memoryfirecan
    global memorypoisb
    global dofire
    global dopois
    global bleed
    global dobleed
    global fireat
    global bossfiring
    global bossbleed
    global bosspois
    global dwarffire
    global alchemistpois
    global poisat
    bosspois=1
    bossfiring=1
    bossbleed=1
    superatcd=0
    superat=0
    if boss2==1:
        block=0
        attack=0
        memoryhp=hp
        lasthp=hp
        applefight=apple
        medfight=med
        firecanfight=firecan
        memoryfirecan=firecan
        poisbfight=poisb
        memorypoisb=poisb
        print('\n\n\nПрийдеться битись!\n')
        bosshp=300
        fightloop=1
        while fightloop==1:
            fightloop1=1
            while fightloop1==1:
                attack=0
                block=0
                print('Ваше здоров\'я:', lasthp, '\nЗдоров\'я боса:', bosshp)
                if bosshp<=0:
                    print('\n\n\n\n\nВи перемогли')
                    firecan=firecanfight
                    poisb=poisbfight
                    fightloop=0
                    hp=lasthp
                    fireat=4
                    poisat=4
                    bossfiring=0
                    bossbleed=0
                    bosspois=0
                    bleed=6
                    dwarffire=4
                    alchemistpois=4
                    bosswinthird()
                if lasthp<=0:
                    print('\n\n\nВи втратили все hp в результаті чого померли...')
                    bosshp=300
                    death=1
                    dwarffire=4
                    alchemistpois=4
                    firecanfight=firecan
                    poisbfight=poisb
                    if firecanfight>0:
                        if 'балончик запалювальної суміші' not in inv:
                            inv.append('балончик запалювальної суміші')
                    if poisbfight>0:
                        if 'бутилочка з ядом' not in inv:
                            inv.append('бутилочка з ядом')
                    fireat=4
                    poisat=4
                    bleed=6
                    lasthp=hp
                    apple=applefight
                    med=medfight
                    if apple>0:
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                    if med>0:
                        if 'медовуха' not in inv:
                            inv.append('медовуха')
                if death==1:
                    reviveloop=1
                    while reviveloop==1:
                        revive=str(input('Повернутись до послідньої битви?\n(так)\n'))
                        if revive=='так':
                            time.sleep(1)
                            print('Зачекайте.')
                            time.sleep(2)
                            print('Зачекайте..')
                            time.sleep(2)
                            print('Зачекайте...')
                            time.sleep(1)
                            print('\nПрийдеться битись!\n\n\n')
                            bosshp=300
                            attack=0
                            block=0
                            reviveloop=0
                            superat=0
                            superatcd=0
                    death=0
                udarplloop=1
                while udarplloop==1:
                    udarpl=str(input('\nВаш хід\nЩо будете робити?\n1 - вдарити\n2 - захищатись\n3 - інвентар\n', ))
                    if udarpl=='1':
                        print('\n\n\n\n\nВи атакуєте')
                        attack=1
                        break
                    if udarpl=='2':
                        print('\n\n\n\n\nВи поставили блок\n')
                        block=1
                        break
                    if udarpl=='3':
                        firecan=firecanfight
                        poisb=poisbfight
                        hp=lasthp
                        inventory()
                        lasthp=hp
                        firecan=memoryfirecan
                        poisb=memorypoisb
                        hp=memoryhp
                        print('\n\nВаше здоров\'я:', lasthp, '\nЗдоров\'я боса:', bosshp)
                print('\nХід боса\nЗачекайте')
                time.sleep(1)
                udaren=random.randint(1,4)
                if udaren==4:
                    print('\n\n\n\n\nБос поставив блок\n')
                    if attack==1:
                        print('\nБос заблокував атаку\n')
                        firing()
                        bleedeff()
                        poisoning()
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін добив вас одним ударом...\n\n')
                            input('Натисніть Enter для продовження')
                            superatcd=0
                            lasthp=0
                        break
                    else:
                        firing()
                        bleedeff()
                        poisoning()
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін спробував вцілити в вас списом, проте ви ухилились\n')
                            superatcd=0
                        block=0
                        break
                else:
                    print('\n\n\n\n\nБос атакує')
                    if block==1:
                        print('\nВи заблокували атаку\n')
                        firing()
                        bleedeff()
                        poisoning()
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін спробував вцілити в вас списом, проте ви ухилились\n')
                            superatcd=0
                        block=0
                        break
                    whudar=random.randint(1,3)
                    if attack==1:
                        if whudar==3:
                            print('\nБос ухилився і контратакував\n')
                            firing()
                            bleedeff()
                            poisoning()
                            if alchemistpois==4:
                                print('Бос вас отруїв\n')
                                alchemistpois=alchemistpois-1
                            if alchemistpois<4:
                                print('Ви отруєні\n')
                                alchemistpois=alchemistpois-1
                                lasthp=lasthp-3
                            if alchemistpois==0:
                                print('Ви більше не відчуваєте себе отруєним\n')
                                alchemistpois=4
                            if superatcd==0:
                                superat=random.randint(1,5)
                            if superat==5:
                                print('Схоже, він готується до чогось...\n')
                                superatcd=1
                            if superatcd==1:
                                superat=superat+1
                            if superat>=9:
                                superat=0
                                print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін добив вас одним ударом...\n\n')
                                input('Натисніть Enter для продовження')
                                superatcd=0
                                lasthp=0
                            bossdmg=random.randint(10,25)
                            lasthp=lasthp-bossdmg
                        else:
                            print('\nВи ухилились і контратакували\n')
                            if len(equippedweap):
                                if 'розплавлений меч' in equippedweap:
                                    dmg=random.randint(1,5)
                                if 'катана роніна' in equippedweap:
                                    dmg=random.randint(10,15)
                                if 'іржавий меч' in equippedweap:
                                    dmg=random.randint(1,5)
                                if 'ніж відлюдника' in equippedweap:
                                    dmg=random.randint(3,7)
                                if 'сталевий меч' in equippedweap:
                                    dmg=random.randint(3,7)
                                if 'лісний кинджал' in equippedweap:
                                    dmg=random.randint(6,10)
                                if 'вогняний меч' in equippedweap:
                                    dmg=random.randint(8,12)
                                if 'отруєний кинджал' in equippedweap:
                                    dmg=random.randint(6,10)
                            else:
                                dmg=random.randint(1,2)
                            if alchemistpois<4:
                                print('Ви отруєні\n')
                                alchemistpois=alchemistpois-1
                                lasthp=lasthp-3
                            if alchemistpois==0:
                                print('Ви більше не відчуваєте себе отруєним\n')
                                alchemistpois=4
                            firing()
                            bleedeff()
                            poisoning()
                            if 'вогняний меч' in equippedweap:
                                if fireat==4:
                                    if firecanfight>0:
                                        firecanfight=firecanfight-1
                                        dofire=1
                                        print('Ви підпалили противника\n')
                                        firing()
                                if firecanfight==0:
                                    if 'балончик запалювальної суміші' in inv:
                                        inv.remove('балончик запалювальної суміші')
                            if 'катана роніна' in equippedweap:
                                if bleed==6:
                                    dobleed=1
                                    print('Ви нанесли кровоточиву рану противнику\n')
                                    bleedeff()
                            if 'отруєний кинджал' in equippedweap:
                                if poisat==4:
                                    if poisbfight>0:
                                        poisbfight=poisbfight-1
                                        dopois=1
                                        print('Ви отруїли противника\n')
                                        poisoning()
                                if poisbfight==0:
                                    if 'бутилочка з ядом' in inv:
                                        inv.remove('бутилочка з ядом')
                            attack=0
                            block=0
                            bosshp=bosshp-dmg
                            if superatcd==1:
                                superat=superat+1
                            if superat>=9:
                                superat=0
                                print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін добив вас одним ударом...\n\n')
                                input('Натисніть Enter для продовження')
                                superatcd=0
                                lasthp=0
                    attack=0
                    block=0
    if boss1==1:
        block=0
        attack=0
        memoryhp=hp
        lasthp=hp
        applefight=apple
        medfight=med
        firecanfight=firecan
        memoryfirecan=firecan
        print('\n\n\nПрийдеться битись!\n')
        bosshp=250
        fightloop=1
        while fightloop==1:
            fightloop1=1
            while fightloop1==1:
                attack=0
                block=0
                print('Ваше здоров\'я:', lasthp, '\nЗдоров\'я боса:', bosshp)
                if bosshp<=0:
                    print('\n\n\n\n\nВи перемогли')
                    firecan=firecanfight
                    fightloop=0
                    hp=lasthp
                    fireat=4
                    bossfiring=0
                    bossbleed=0
                    bleed=6
                    dwarffire=4
                    bosswinsecond()
                if lasthp<=0:
                    print('\n\n\nВи втратили все hp в результаті чого померли...')
                    bosshp=250
                    death=1
                    dwarffire=4
                    firecanfight=firecan
                    if firecanfight>0:
                        if 'балончик запалювальної суміші' not in inv:
                            inv.append('балончик запалювальної суміші')
                    fireat=4
                    bleed=6
                    lasthp=hp
                    apple=applefight
                    med=medfight
                    if apple>0:
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                    if med>0:
                        if 'медовуха' not in inv:
                            inv.append('медовуха')
                if death==1:
                    reviveloop=1
                    while reviveloop==1:
                        revive=str(input('Повернутись до послідньої битви?\n(так)\n'))
                        if revive=='так':
                            time.sleep(1)
                            print('Зачекайте.')
                            time.sleep(2)
                            print('Зачекайте..')
                            time.sleep(2)
                            print('Зачекайте...')
                            time.sleep(1)
                            print('\nПрийдеться битись!\n\n\n')
                            bosshp=250
                            attack=0
                            block=0
                            reviveloop=0
                            superat=0
                            superatcd=0
                    death=0
                udarplloop=1
                while udarplloop==1:
                    udarpl=str(input('\nВаш хід\nЩо будете робити?\n1 - вдарити\n2 - захищатись\n3 - інвентар\n', ))
                    if udarpl=='1':
                        print('\n\n\n\n\nВи атакуєте')
                        attack=1
                        break
                    if udarpl=='2':
                        print('\n\n\n\n\nВи поставили блок\n')
                        block=1
                        break
                    if udarpl=='3':
                        firecan=firecanfight
                        hp=lasthp
                        inventory()
                        lasthp=hp
                        firecan=memoryfirecan
                        hp=memoryhp
                        print('\n\nВаше здоров\'я:', lasthp, '\nЗдоров\'я боса:', bosshp)
                print('\nХід боса\nЗачекайте')
                time.sleep(1)
                udaren=random.randint(1,4)
                if udaren==4:
                    print('\n\n\n\n\nБос поставив блок\n')
                    if attack==1:
                        print('\nБос заблокував атаку\n')
                        firing()
                        bleedeff()
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін добив вас одним ударом...\n\n')
                            input('Натисніть Enter для продовження')
                            superatcd=0
                            lasthp=0
                        break
                    else:
                        firing()
                        bleedeff()
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін спробував вцілити в вас списом, проте ви ухилились\n')
                            superatcd=0
                        block=0
                        break
                else:
                    print('\n\n\n\n\nБос атакує')
                    if block==1:
                        print('\nВи заблокували атаку\n')
                        firing()
                        bleedeff()
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін спробував вцілити в вас списом, проте ви ухилились\n')
                            superatcd=0
                        block=0
                        break
                    whudar=random.randint(1,3)
                    if attack==1:
                        if whudar==3:
                            print('\nБос ухилився і контратакував\n')
                            firing()
                            bleedeff()
                            if dwarffire==4:
                                print('Бос вас підпалив\n')
                                dwarffire=dwarffire-1
                            if dwarffire<4:
                                print('Ви палаєте\n')
                                dwarffire=dwarffire-1
                                lasthp=lasthp-1
                            if dwarffire==0:
                                print('Ви перестали палати\n')
                                dwarffire=4
                            if superatcd==0:
                                superat=random.randint(1,5)
                            if superat==5:
                                print('Схоже, він готується до чогось...\n')
                                superatcd=1
                            if superatcd==1:
                                superat=superat+1
                            if superat>=9:
                                superat=0
                                print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін добив вас одним ударом...\n\n')
                                input('Натисніть Enter для продовження')
                                superatcd=0
                                lasthp=0
                            bossdmg=random.randint(10,25)
                            lasthp=lasthp-bossdmg
                        else:
                            print('\nВи ухилились і контратакували\n')
                            if len(equippedweap):
                                if 'розплавлений меч' in equippedweap:
                                    dmg=random.randint(1,5)
                                if 'катана роніна' in equippedweap:
                                    dmg=random.randint(10,15)
                                if 'іржавий меч' in equippedweap:
                                    dmg=random.randint(1,5)
                                if 'ніж відлюдника' in equippedweap:
                                    dmg=random.randint(3,7)
                                if 'сталевий меч' in equippedweap:
                                    dmg=random.randint(3,7)
                                if 'лісний кинджал' in equippedweap:
                                    dmg=random.randint(6,10)
                                if 'вогняний меч' in equippedweap:
                                    dmg=random.randint(8,12)
                                if 'отруєний кинджал' in equippedweap:
                                    dmg=random.randint(6,10)
                            else:
                                dmg=random.randint(1,2)
                            if dwarffire<4:
                                print('Ви палаєте\n')
                                dwarffire=dwarffire-1
                                lasthp=lasthp-1
                            if dwarffire==0:
                                print('Ви перестали палати\n')
                                dwarffire=4
                            firing()
                            bleedeff()
                            if 'вогняний меч' in equippedweap:
                                if fireat==4:
                                    if firecanfight>0:
                                        firecanfight=firecanfight-1
                                        dofire=1
                                        print('Ви підпалили противника\n')
                                        firing()
                                if firecanfight==0:
                                    if 'балончик запалювальної суміші' in inv:
                                        inv.remove('балончик запалювальної суміші')
                            if 'катана роніна' in equippedweap:
                                if bleed==6:
                                    dobleed=1
                                    print('Ви нанесли кровоточиву рану противнику\n')
                                    bleedeff()
                            attack=0
                            block=0
                            bosshp=bosshp-dmg
                            if superatcd==1:
                                superat=superat+1
                            if superat>=9:
                                superat=0
                                print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала жовтим вогнем\nВін добив вас одним ударом...\n\n')
                                input('Натисніть Enter для продовження')
                                superatcd=0
                                lasthp=0
                    attack=0
                    block=0
    else:
        block=0
        attack=0
        memoryhp=hp
        lasthp=hp
        applefight=apple
        medfight=med
        firecanfight=firecan
        memoryfirecan=firecan
        print('\n\n\nПрийдеться битись!\n')
        bosshp=200
        fightloop=1
        while fightloop==1:
            fightloop1=1
            while fightloop1==1:
                attack=0
                block=0
                print('Ваше здоров\'я:', lasthp, '\nЗдоров\'я боса:', bosshp)
                if bosshp<=0:
                    print('\n\n\n\n\nВи перемогли')
                    firecan=firecanfight
                    fightloop=0
                    hp=lasthp
                    fireat=4
                    bossfiring=0
                    bossbleed=0
                    bleed=6
                    bosswinfirst()
                if lasthp<=0:
                    print('\n\n\nВи втратили все hp в результаті чого померли...')
                    bosshp=200
                    death=1
                    firecanfight=firecan
                    if firecanfight>0:
                        if 'балончик запалювальної суміші' not in inv:
                            inv.append('балончик запалювальної суміші')
                    fireat=4
                    bleed=6
                    lasthp=hp
                    apple=applefight
                    med=medfight
                    if apple>0:
                        if 'яблуко' not in inv:
                            inv.append('яблуко')
                    if med>0:
                        if 'медовуха' not in inv:
                            inv.append('медовуха')
                if death==1:
                    reviveloop=1
                    while reviveloop==1:
                        revive=str(input('Повернутись до послідньої битви?\n(так)\n'))
                        if revive=='так':
                            time.sleep(1)
                            print('Зачекайте.')
                            time.sleep(2)
                            print('Зачекайте..')
                            time.sleep(2)
                            print('Зачекайте...')
                            time.sleep(1)
                            print('\nПрийдеться битись!\n\n\n')
                            bosshp=200
                            attack=0
                            block=0
                            reviveloop=0
                            superat=0
                            superatcd=0
                    death=0
                udarplloop=1
                while udarplloop==1:
                    udarpl=str(input('\nВаш хід\nЩо будете робити?\n1 - вдарити\n2 - захищатись\n3 - інвентар\n', ))
                    if udarpl=='1':
                        print('\n\n\n\n\nВи атакуєте')
                        attack=1
                        break
                    if udarpl=='2':
                        print('\n\n\n\n\nВи поставили блок\n')
                        block=1
                        break
                    if udarpl=='3':
                        firecan=firecanfight
                        hp=lasthp
                        inventory()
                        lasthp=hp
                        firecan=memoryfirecan
                        hp=memoryhp
                        print('\n\nВаше здоров\'я:', lasthp, '\nЗдоров\'я боса:', bosshp)
                print('\nХід боса\nЗачекайте')
                time.sleep(1)
                udaren=random.randint(1,4)
                if udaren==4:
                    print('\n\n\n\n\nБос поставив блок\n')
                    if attack==1:
                        print('\nБос заблокував атаку\n')
                        firing()
                        bleedeff()
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала\nВін добив вас одним ударом...\n\n')
                            input('Натисніть Enter для продовження')
                            superatcd=0
                            lasthp=0
                        break
                    else:
                        firing()
                        bleedeff()
                        if dwarffire<4:
                            print('Ви палаєте\n')
                            dwarffire=dwarffire-1
                            lasthp=lasthp-1
                        if dwarffire==0:
                            print('Ви перестали палати\n')
                            dwarffire=4
                        if alchemistpois<4:
                            print('Ви отруєні\n')
                            alchemistpois=alchemistpois-1
                            lasthp=lasthp-3
                        if alchemistpois==0:
                            print('Ви більше не відчуваєте себе отруєним\n')
                            alchemistpois=4
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала\nВін спробував вцілити в вас списом, проте ви ухилились\n')
                            superatcd=0
                        block=0
                        break
                else:
                    print('\n\n\n\n\nБос атакує')
                    if block==1:
                        print('\nВи заблокували атаку\n')
                        firing()
                        bleedeff()
                        if superatcd==1:
                            superat=superat+1
                        if superat>=9:
                            superat=0
                            print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала\nВін спробував вцілити в вас списом, проте ви ухилились\n')
                            superatcd=0
                        block=0
                        break
                    whudar=random.randint(1,3)
                    if attack==1:
                        if whudar==3:
                            print('\nБос ухилився і контратакував\n')
                            firing()
                            bleedeff()
                            if superatcd==0:
                                superat=random.randint(1,5)
                            if superat==5:
                                print('Схоже, він готується до чогось...\n')
                                superatcd=1
                            if superatcd==1:
                                superat=superat+1
                            if superat>=9:
                                superat=0
                                print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала\nВін добив вас одним ударом...\n\n')
                                input('Натисніть Enter для продовження')
                                superatcd=0
                                lasthp=0
                            bossdmg=random.randint(10,25)
                            lasthp=lasthp-bossdmg
                        else:
                            print('\nВи ухилились і контратакували\n')
                            if len(equippedweap):
                                if 'розплавлений меч' in equippedweap:
                                    dmg=random.randint(1,5)
                                if 'катана роніна' in equippedweap:
                                    dmg=random.randint(10,15)
                                if 'іржавий меч' in equippedweap:
                                    dmg=random.randint(1,5)
                                if 'ніж відлюдника' in equippedweap:
                                    dmg=random.randint(3,7)
                                if 'сталевий меч' in equippedweap:
                                    dmg=random.randint(3,7)
                                if 'лісний кинджал' in equippedweap:
                                    dmg=random.randint(6,10)
                                if 'вогняний меч' in equippedweap:
                                    dmg=random.randint(8,12)
                                if 'отруєний кинджал' in equippedweap:
                                    dmg=random.randint(6,10)
                            else:
                                dmg=random.randint(1,2)
                            if 'катана роніна' in equippedweap:
                                if bleed==6:
                                    dobleed=1
                                    print('Ви нанесли кровоточиву рану противнику\n')
                                    bleedeff()
                            attack=0
                            block=0
                            bosshp=bosshp-dmg
                            if superatcd==1:
                                superat=superat+1
                            if superat>=9:
                                superat=0
                                print('Бос дістав сяюче зілля. Коли він його випив, його зброя запалала\nВін добив вас одним ударом...\n\n')
                                input('Натисніть Enter для продовження')
                                superatcd=0
                                lasthp=0
                    attack=0
                    block=0
####################################                      ПЕРЕМОГА ПЕРШИЙ БОС
def bosswinfirst():
    global apple
    global applef
    global med
    global medf
    global money
    global moneyf
    global boss1
    input('Після перемоги над командиром лісних розбійників ви його обшукуєте\nНатисніть Enter для продовження')
    time.sleep(2)
    print('Ви обшукуєте тіло та палатку.')
    time.sleep(3)
    print('Ви обшукуєте тіло та палатку..')
    time.sleep(3)
    print('Ви обшукуєте тіло та палатку...')
    time.sleep(2)
    moneyf=random.randint(10,30)
    applef=random.randint(3,7)
    medf=random.randint(1,4)
    inv.append('лісний кинджал')
    apple=apple+applef
    if 'яблуко' not in inv:
        inv.append('яблуко')
    med=med+medf
    if med>0:    
        if 'медовуха' not in inv:
            inv.append('медовуха')
    money=money+moneyf
    print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
    print('Лісний кинджал')
    if moneyf>0:
        print('Монети:', moneyf)
    if medf>0:
        print('Медовуха:', medf)
    print('Яблука:', applef)
    boss1=1
    input('Натисніть Enter для продовження')
    input('Також на столі в палатці ви знайшли записку:\n\'Ви поселились надто далеко. У нас немає людей, яких ми можемо послати\nЗаставимо якогось дворфа принести вам партію\nЯкщо зілля не дійдуть, звинувачуйте їх\'\nНатисніть Enter для продовження')
    time.sleep(2)
    print('Ви повертаєтесь у форпост.')
    time.sleep(3)
    print('Ви повертаєтесь у форпост..')
    time.sleep(3)
    print('Ви повертаєтесь у форпост...')
    time.sleep(2)
    base()
####################################                         ПЕРЕМОГА ДРУГИЙ БОС
def bosswinsecond():
    global firecanf
    global firecan
    global apple
    global applef
    global med
    global medf
    global money
    global moneyf
    global dwarfen
    global boss2
    input('Після перемоги над командиром дворфів ви його обшукуєте\nНатисніть Enter для продовження')
    time.sleep(2)
    print('Ви обшукуєте тіло та кімнату в печері.')
    time.sleep(3)
    print('Ви обшукуєте тіло та кімнату в печері..')
    time.sleep(3)
    print('Ви обшукуєте тіло та кімнату в печері...')
    time.sleep(2)
    firecanf=random.randint(5,14)
    if 'балончик запалювальної суміші' not in inv:
        inv.append('балончик запалювальної суміші')
    moneyf=random.randint(20,50)
    applef=random.randint(4,8)
    medf=random.randint(2,6)
    inv.append('вогняний меч')
    apple=apple+applef
    firecan=firecan+firecanf
    if 'яблуко' not in inv:
        inv.append('яблуко')
    med=med+medf
    if med>0:    
        if 'медовуха' not in inv:
            inv.append('медовуха')
    money=money+moneyf
    print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
    print('Вогняний меч')
    if firecanf>0:
        print('Балончик запалювальної суміші', firecanf)
    if moneyf>0:
        print('Монети:', moneyf)
    if medf>0:
        print('Медовуха:', medf)
    print('Яблука:', applef)
    dwarfen=0
    boss2=1
    input('Натисніть Enter для продовження')
    input('\n\n\n\n\nТакож під хламом в кімнаті ви знайшли записку:\n\'Коли ви доробите нові машини для створення зіллів?\nЗмішувати стільки різної крові руками надто довго. Ви ж хочете їх більше?\nТак зробіть машини швидше!\nМи також відправили вам на 1 партію більше. Принесіть це розбійникам\nТим, що живуть в лісі не далеко від вас, якщо залишите собі, вони не зрадіють\'\nНатисніть Enter для продовження')
    time.sleep(2)
    print('Ви повертаєтесь у форпост.')
    time.sleep(3)
    print('Ви повертаєтесь у форпост..')
    time.sleep(3)
    print('Ви повертаєтесь у форпост...')
    time.sleep(2)
    base()
####################################                          ПЕРЕМОГА ТРЕТІЙ БОС
def bosswinthird():
    input('Натисніть Enter для продовження')
    print('Ви перемогли посліднього боса\nПеред смертю він сказав вам:\nТи ж з того селища... Чому тебе не вбили?\nПрийшов за мною щоб помститись? Тобі напевно цікаво, навіщо ми вбили всіх в твому селищі?\nКров... Ми винайшли спосіб створити зілля, що наділяє надлюдською силою... Силою сотень людей разом...\nДля цього потрібна була кров багатьох людей в великих кількостях...\nУвляєш, скільки можна би було заробити, продаючи ці зілля?\nВсе було би ідеально, якби ти не прийш...\nПісля цих слів він помер...')
    input('Ви пройшли гру!')
####################################                         ПЕРІОДИЧНІ ПРІКОЛИ
def firing():
    global firecanfight
    global enemyhp
    global bosshp
    global dofire
    global fireat
    global enemyfiring
    global bossfiring
    if fireat==4:
        if dofire==1:
            fireat=fireat-1
    if fireat<4:
        print('Противник палає\n')
        if bossfiring==1:
            bosshp=bosshp-1
        if enemyfiring==1:
            enemyhp=enemyhp-1
        fireat=fireat-1
        dofire=0
    if fireat==0:
        print('Противник перестав палати\n')
        fireat=4
        dofire=0
def bleedeff():
    global enemyhp
    global bosshp
    global enemybleed
    global bossbleed
    global dobleed
    global bleed
    if bleed==6:
        if dobleed==1:
            bleed=bleed-1
    if bleed<6:
        print('Противник кровоточить\n')
        if bossbleed==1:
            bosshp=bosshp-10
        if enemybleed==1:
            enemyhp=enemyhp-10
        bleed=bleed-1
        dobleed=0
    if bleed==0:
        print('Противник перестав кровоточити\n')
        bleed=6
        dobleed=0
def poisoning():
    global poisbfight
    global enemyhp
    global bosshp
    global dopois
    global poisat
    global enemypois
    global bosspois
    if poisat==4:
        if dopois==1:
            poisat=poisat-1
    if poisat<4:
        print('Противник отруєний\n')
        if bosspois==1:
            bosshp=bosshp-3
        if enemypois==1:
            enemyhp=enemyhp-3
        poisat=poisat-1
        dopois=0
    if poisat==0:
        print('Противник більше не відчуває себе отруєним\n')
        poisat=4
        dopois=0
####################################                         НАВЧАННЯ
print('Коли ви прокинулись, то зрозуміли, що всіх жителів, окрім вас було вбито\nВи вирішуєте дізнатись, хто це зробив, та помститися\nПроте, у вас зовсім нічого для цього немає\nТому ви вирішуєте обшукати ваше селище')
input('Натисніть Enter для продовження')
time.sleep(2)
print('Ви обшукуєте селище.')
time.sleep(3)
print('Ви обшукуєте селище..')
time.sleep(3)
print('Ви обшукуєте селище...')
time.sleep(2)
print('\n\n\n\n\nПісля декількох годин пошуків будь чого, що може знадобитись по пустим дорогам вашого рідного села\nВи знаходите декілька речей, які можуть знадобитися')
loop=1
while loop==1:
    dia=str(input('Щоб подивитися ваш інвентар, напишіть "3"\n', ))
    if dia=='3':
        loop=0
    else:
        loop=1
tru=0
print('\n\n\n\n\nЩоб дізнатись, більше про предмет, в меню інвентаря напишіть "3"')
print('\n***ІНВЕНТАР***\n', inv, '\nМонети:', money, '\nЗдоров\'я:', hp)
loopa=1
while loopa==1:
    dia=str(input('Що ви будете робити?\n', ))
    if dia=='3':
        loop=1
        while loop==1:
            inf=str(input('Про що ви хочете дізнатись більше?\n', ))
            if inf=='іржавий меч':
                print('\n\n***ІРЖАВИЙ МЕЧ***\nНанесення шкоди - 1-5')
                tru=tru+1
                if tru==3:
                    loop=0
                    loopa=0
            if inf=='яблуко':
                print('\n\n***ЯБЛУКО***\nВідновлення - 25hp\nКількість -', apple)
                tru=tru+1
                if tru==3:
                    loop=0
                    loopa=0
            if inf=='медовуха':
                print('\n\n***МЕДОВУХА***\nВідновлення - 50hp\nКількість -', med)
                tru=tru+1
                if tru==3:
                    loop=0
                    loopa=0
else:
    loopa=1
loop=1
while loop==1:
    print('\n\n\nЩоб використати потрібні вам речі, або предмети, напишіть "1"')
    print('\n***ІНВЕНТАР***\n', inv, '\nМонети:', money, '\nЗдоров\'я:', hp)
    dia=str(input('Що будете робити?\n', ))
    if dia=='1':
        equip=str(input('Що ви хочете використати?\n', ))
        if equip=='іржавий меч':
            inv.remove('іржавий меч')
            equippedweap.append('іржавий меч')
            print('\n\n\n\n\nВи використовуєте', equippedweap)
            loop=0
        else:
            print('\n\n\n\n\n\n\n\n\n\nВикористайте меч')
    else:
        loop=1
input('Взявши в руки старий меч, ви йдете по кривавим слідам, що залишили після себе нападники\nНатисніть Enter для продовження', )
loop=1
while loop==1:
    dia=str(input('\nВи пройшли декілька сот метрів, і перед вами з\'явилось 2 дороги - дорога в гори, та дорога до річки\nКуди ви підете?(в гори, до річки)\n', ))
    if dia=='до річки':
        print('\n\n\n\n\nХоч сліди й вели в сторону ріки, ви помітили дим, що піднімався вверх з гір\nКраще перевірити, можливо хтось з вашого селища вцілів, і допоможе вам хоча би інформацією.')
    if dia=='в гори':
        print('\n\n\n\n\nВи вирішили перевірити гірські околиці.\nХодячи по горам ви побачили печеру, з якої виходив дим\nТому ви вирішили перевірити хто розпалив там вогнище')
        print('Коли ви підійшли ближче до печери, то помітили, що там нікого немає\nПроте коли вже хотіли розвернутись, ви побачили старого відлюдника\nВін щось невнятно кричав з піною біля рота, а в його руці був ніж\nКоли він вас помітив, почав кричати ще голосніше і бігти прямо на вас')
        input('Натисніть Enter для продовження', )
        didhp=30
        dia=str(input('\n\n\n\n\nВаші дії?\nнапасти у відповідь - 1\nспробувати поговорити з ним - 2\n'))
        if dia=='1':
            print('\n\n\n\n\nВи вирішили відбиватись')
            fighting()
            break
        if dia=='2':
            print('\n\n\n\n\nВи пробуєте зупинити його словами, проте він не звертає на це ніякої уваги, в результаті чого\nвін встромлює ніж прямо у ваше серце і ви помираєте')
            input('Ви померли...\nНатисніть Enter для продовження', )
print('\n\n\nВи здобули перемогу над божевільним дідом!(Це велике досягнення)\nПісля битви не буде лишнім відкрити інвентар та підкріпитись(якщо є чим)')
loop=1
while loop==1:
    dia=str(input('Щоб відкрити інвентар напишіть "3"\n', ))
    if dia=='3':
        loop=0
        inventory()
print('\n\n\n\n\nПісля перемоги над відлюдником, ви можете обшукати його базу')
loop=1
while loop==1:
    vub=str(input('\nЧи хочете ви цього?\n(так, ні)\n', ))
    if vub=='ні':
        loop=0
    if vub=='так':
        time.sleep(2)
        print('Ви обшукуєте базу відлюдника.')
        sword=random.randint(1,10)
        if sword==1:
            inv.append('ніж відлюдника')
            input('\n\n\n\n\nВи забрали ніж відлюдника!\nНатисніть Enter для продовження',)
        time.sleep(3)
        print('Ви обшукуєте базу відлюдника..')
        sword=random.randint(1,10)
        if sword==1:
            if 'ніж відлюдника' in inv:
                pass
            else:
                inv.append('ніж відлюдника')
                input('\n\n\n\n\nВи забрали ніж відлюдника!\nНатисніть Enter для продовження',)
        time.sleep(3)
        print('Ви обшукуєте базу відлюдника...')
        sword=random.randint(1,10)
        if sword==1:
            if 'ніж відлюдника' in inv:
                pass
            else:
                inv.append('ніж відлюдника')
                input('\n\n\n\n\nВи забрали ніж відлюдника!\nНатисніть Enter для продовження',)
        time.sleep(2)
        applef=random.randint(1,2)
        apple=apple+applef
        if 'яблуко' not in inv:
            inv.append('яблуко')
        moneyf=random.randint(2,5)
        money=money+moneyf
        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
        if 'ніж відлюдника' in inv:
             print('\nНіж відлюдника')
        print('\nЯблука: ', applef, '\nМонети: ', moneyf)
        loop1=1
        while loop1==1:
            vub=input('Відкрити інвентар?\n(так, ні)\n', )
            if vub=='так':
                inventory()
                loop1=0
                loop=0
            else:
                loop1=0
                loop=0
print('\n\n\n\n\nПісля перемоги над божевільним відлюдником ви повертаєтесь до розвилки та продовжуєте йти по слідам\nКоли ви дійшли до річки, почали йти вниз по течії.')
input('Натисніть Enter для продовження')
time.sleep(2)
print('Ви йдете по слідам за течією.')
time.sleep(3)
print('Ви йдете по слідам за течією..')
time.sleep(3)
print('Ви йдете по слідам за течією...')
time.sleep(2)
input('\n\n\n\n\nКоли ви йшли, то помітили вдалині силует низького, проте широкого чоловіка\nВ голові у вас було два питання - це просто карлик, чи дворф?\nНатисніть Enter для продовження')
loop=1
while loop==1:
    vub=str(input('\n\n\n\n\nВи хочете з ним битись?\n(так, ні)\n', ))
    if vub=='так':
        fighting()
        print('\n\n\n\n\nПісля перемоги над противником, ви його обшукуєте')
        input('Натисніть Enter для продовження')
        time.sleep(2)
        print('Ви обшукуєте дворфа та все довколо нього.')
        moltsword=0
        if moltsword!=1:
            moltsword=random.randint(1,7)
        if moltsword==1:
            inv.append('розплавлений меч')
            moltswordgot=1
            input('\n\n\n\n\nВи знайшли розплавлений меч\nНатисніть Enter для продовження',)
        time.sleep(3)
        print('Ви обшукуєте дворфа та все довколо нього..')
        if moltswordgot==0:
            moltsword=random.randint(1,7)
        if moltsword==1:
            inv.append('розплавлений меч')
            moltswordgot=1
            input('\n\n\n\n\nВи знайшли розплавлений меч\nНатисніть Enter для продовження',)
        time.sleep(3)
        print('Ви обшукуєте дворфа та все довколо нього...')
        if moltswordgot==0:
            moltsword=random.randint(1,7)
        if moltsword==1:
            inv.append('розплавлений меч')
            input('\n\n\n\n\nВи знайшли розплавлений меч\nНатисніть Enter для продовження',)
        time.sleep(2)
        moneyf=random.randint(0,6)
        applef=random.randint(1,5)
        medf=random.randint(0,3)
        apple=apple+applef
        if 'яблуко' not in inv:
            inv.append('яблуко')
        med=med+medf
        if med>0:    
            if 'медовуха' not in inv:
                inv.append('медовуха')
        print('\n\n***РЕЗУЛЬТАТИ ОБШУКУ***\n\n')
        if 'розплавлений меч' in inv:
            print('Розплавлений меч')
        if moneyf==1:
            money=money+moneyf
            print('Монети:', moneyf)
        print('\nЯблука:', applef)
        if medf==1:
            med=med+medf
            print('Медовуха:', medf)
        input('Натисніть Enter для продовження')
        input('\n\n\n\n\nНедалеко від дворфа ви знайшли ящик з розбитими колбами\nА все довкола нього випромінювало слабке сяйво\nНатисніть Enter для продовження')
        loop=1
        while loop==1:
            dia=str(input('\nЩоб відкрити інвентар напишіть "3"\n', ))
            if dia=='3':
                inventory()
                loop=0
    if vub=='ні':
        loop=0
time.sleep(2)
print('Ви йдете далі.')
time.sleep(3)
print('Ви йдете далі..') 
time.sleep(3)
print('Ви йдете далі...')
time.sleep(2)
loop=1
while loop==1:
    print('\n\n\n\n\nВи йшли кілька годин, вже почало темніти\nта ви побачили вдалині декілька смуг диму\nСкоріше за все там ціла група людей, може вони щось знають?')
    input('Натисніть Enter для продовження')
    time.sleep(2)
    print('Ви йдете до джерела диму.')
    time.sleep(3)
    print('Ви йдете до джерела диму..')
    time.sleep(3)
    print('Ви йдете до джерела диму...')
    time.sleep(2)
    dialloop=1
    input('\n\n\n\n\nЧерез пів години ви дійшли до дерев\'яних стін, які були щонайменше в два рази вищі за вас\nВи почали обходити їх в пошуках входу, і коли ви його знайшли\nДекілька людей, що стояли на стінах приготували луки\nНатисніть Enter для продовження')
    while dialloop==1:
        dial=str(input('\n\n\n\nЛюди дивились на вас, очікуючи ваших дій\nДовго не думаючи, ви вирішили сказати:\n1 - Хто ви такі?\n2 - Допоможіть мені, будь-ласка\n3 - Відкрийте ворота, або я вас всіх переб\'ю\n', ))
        if dial=='1' or dial=='2':
            print('\n\n\n- Нам би спершу дізнатись хто такий ти, і що тут робиш')
            loop1=1
            dialloop=1
            while loop1==1:
                dial=str(input('\n1 - Я з селища неподалік, всіх жителів, окрім мене вбили, я хочу дізнатись, хто це зробив\n2 - Навіщо це мені вам щось розказувати, відкривайте швидше\n', ))
                if dial=='1':
                    input('\n\n\n- Добре, заходи, але так, щоб я бачив твої руки.\nВідкрити ворота!\nНатисніть Enter для продовження')
                    loop1=0
                    loop=0
                    dialloop=0
                if dial=='2':
                    dial=str(input('\n\n\n- Ти що, насміхаєшся з нас, чи просто померти хочеш?\n\n1 - Тільки спробуйте мене вбити, я вас всіх тут переб\'ю\n2 - Ні, вибачте, не знаю, що на мене найшло\n', ))
                    if dial=='1':
                        print('\n\n\n- Ти так в цьому впевнений? ВОГОНЬ!\nНе встигнувши відреагувати, ваше тіло пронизало десяток стріл, ви померли на місці.\nВи померли...')
                        input('Натисніть Enter, щоб повернутись до послідьої контрольної точки')
                        time.sleep(1)
                        print('Зачекайте.')
                        time.sleep(2)
                        print('Зачекайте..')
                        time.sleep(2)
                        print('Зачекайте...')
                        time.sleep(1)
                        loop1=0
                        dialloop=0
        if dial=='3':
            print('\n\n\n- Ти так в цьому впевнений? ВОГОНЬ!\nНе встигнувши відреагувати, ваше тіло пронизало десяток стріл, ви померли на місці.\nВи померли...')
            input('Натисніть Enter, щоб повернутись до послідьої контрольної точки')
            time.sleep(1)
            print('Зачекайте.')
            time.sleep(2)
            print('Зачекайте..')
            time.sleep(2)
            print('Зачекайте...')
            time.sleep(1)
            loop1=0
        else:
            pass
input('\n\n\n\n\nРозповівши їм свою історію, вони дозволили вам вступити в їхні ряди\nВиявилось, що це старий форпост захоплений цими найманцями\nПоки вам готують нічліг, ви можете пройти до крамниці\nНатисніть Enter для продовження')
shop()
input('\n\n\n\n\nПісля того, як ви вийшли з крамниці, вас зустрів командир найманців, й пояснив, як пройти до вашої палатки\nНатисніть Enter для продовження') 
base()
