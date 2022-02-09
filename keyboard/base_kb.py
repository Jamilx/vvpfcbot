from calendar import TUESDAY
from ctypes import resize
from hashlib import sha3_224
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton #ReplyKeyboardRemove


'''
add
insert
row
resize_keyboard = True - размер кнопок подстраивается под текст
one_time_keyboard = True -одноразовая клавиатура
'''
#СТ-ПР
see = KeyboardButton('Переглянути розклад')
addds = KeyboardButton('Редагувати розклад')
cancels = KeyboardButton('Назад')


see_add = ReplyKeyboardMarkup(resize_keyboard = True)

see_add.add(see).add(addds).add(cancels)


#Потверждение
okay =KeyboardButton('Готово')
notokay = KeyboardButton('Назад')
kb_okay = ReplyKeyboardMarkup(resize_keyboard = True)
kb_okay.add(okay).add(notokay)
#Главная клавиатура
kb2 = KeyboardButton('/Розклад')
#kb_updates = KeyboardButton('/Зміни')
kb_1 = ReplyKeyboardMarkup(resize_keyboard = True)

kb_1.add(kb2)#.add(kb_updates)



#Клавиатура создания
monday1 = KeyboardButton('Понеділок')
tuesday1 = KeyboardButton('Вівторок')
wednesday1 = KeyboardButton('Середа')
thursday1 = KeyboardButton('Четверг')
friday1 =  KeyboardButton('П\'ятниця')
cancel = KeyboardButton('Назад')

kb_week = ReplyKeyboardMarkup(resize_keyboard = True)

kb_week.row(monday1, tuesday1).row(wednesday1,thursday1).add(friday1).add(cancel)



#Клавиатура просмотра

monday = KeyboardButton('/понеділок')
tuesday = KeyboardButton('/Вівторок')
wednesday = KeyboardButton('/Середа')
thursday = KeyboardButton('/Четверг')
friday =  KeyboardButton('/П\'ятниця')
cancel = KeyboardButton('/Назад')

kb_week_see = ReplyKeyboardMarkup(resize_keyboard = True)

kb_week_see.row(monday, tuesday).row(wednesday,thursday).add(friday).add(cancel)


#Пари
cancels = KeyboardButton('Назад')
nothing =KeyboardButton('немає')
####################---- А
s1= KeyboardButton('Анотомія')
s2= KeyboardButton('Анотомія, фізіологія і гігієна')
s3= KeyboardButton('Англійська мова')
s4= KeyboardButton('Архівознавство')
####################---- Б
s5= KeyboardButton('Бальні танці')
s6= KeyboardButton('Безпека життєдіяльності')
s7= KeyboardButton('Біологія')
####################---- В
s8= KeyboardButton('Валеологія')
####################---- Г
s9= KeyboardButton('Гурткова робота з ОМ')
s10= KeyboardButton('Гурткова робота')
####################---- Д
s11= KeyboardButton('Дизайн')
s12= KeyboardButton('Дитячий музичний інструмент')
s13= KeyboardButton('Діловодство')
s14= KeyboardButton('Документознавство')
s15= KeyboardButton('ДПМ з методикою')
####################---- Е
s16= KeyboardButton('Економічна теорія')
s17= KeyboardButton('Економіка виробництва')
s18= KeyboardButton('Економіка підприємства')
####################---- Ж
s19= KeyboardButton('Живопс')
####################---- З
s20= KeyboardButton('Заг електротехн') #
s21= KeyboardButton('Зарубіжна література')
s22= KeyboardButton('Захист України')
####################---- І
s23= KeyboardButton('інформ. забезпечення управ.') #
s24= KeyboardButton('інформ. технол. та тех. засоби ')
s25= KeyboardButton('інформ. технол. і комп. графіка')
s26= KeyboardButton('інформатика')
s27= KeyboardButton('ІСМ')
s28= KeyboardButton('історія образотворчого мистецтва')
s29= KeyboardButton('історія україни')
s30= KeyboardButton('історія: Ураїна і світ')
####################---- К
s31= KeyboardButton('класичний танець ')
s32= KeyboardButton('культура мовлення ')
s33= KeyboardButton('композиція')
s34= KeyboardButton('комп\'ютерна графіка')
s35= KeyboardButton('культурологія')
####################---- Л
s36= KeyboardButton('література для дітей')
s37= KeyboardButton('логопедія')
####################---- M
s38= KeyboardButton('математика')
s39= KeyboardButton('методика  громадської освіти')
s40= KeyboardButton('методика навчання інформатики')
s41= KeyboardButton('методика навчання математики')
s42= KeyboardButton('методика навчання Укр. мови')
s43= KeyboardButton('методика іноземної мови')
s44= KeyboardButton('методика музичного виховання ')
s45= KeyboardButton('методика трудового навчання')
s46= KeyboardButton('методика формув здоров’я')
s47= KeyboardButton('музичний інструмент ')
s48= KeyboardButton('музичне вихов. з методикою')
####################---- H
s49= KeyboardButton('нарисна геометрія')
s50= KeyboardButton('народний танець')
s51= KeyboardButton('німецька мова')
####################---- O
s52= KeyboardButton('оброботка констр матер')
s53= KeyboardButton('обчис. тех. і програмування')
s54= KeyboardButton('організаційна техніка')
s55= KeyboardButton('основи інклюз освіти')
s56= KeyboardButton('основи корекц педагог')
s57= KeyboardButton('основи пед майстерн')
s58= KeyboardButton('основи природи з метод')
s59= KeyboardButton('основи сценічного мистецтва')
s60= KeyboardButton('основи кольорознавства')
s61= KeyboardButton('основи менеджменту')
s62= KeyboardButton('основи правознавства')
s63= KeyboardButton('основи реставрації')
s64= KeyboardButton('основи сцен мист')
s65= KeyboardButton('основни філософії ')
s66= KeyboardButton('охорона праці')
####################---- П
s67= KeyboardButton('педагогічна психологія ')
s68= KeyboardButton('педагогіка')
s69= KeyboardButton('пласт анотомія')
s70= KeyboardButton('польська мова')
s71= KeyboardButton('постановка танцю')
s72= KeyboardButton('практ. зв\'яз. з громадкістю ')
s73= KeyboardButton('практ. курс англ м.')
s74= KeyboardButton('практикум англ.м (Iiпідг)')
s75= KeyboardButton('професійна англ. м. ')
s76= KeyboardButton('психологія')
#####################---- Р
s77= KeyboardButton('рисунок')
s78= KeyboardButton('рисунок і живопис')
s79= KeyboardButton('ритміка / метод труд')
#####################---- С
s80= KeyboardButton('скульптура')
s81= KeyboardButton('соціологія')
s82= KeyboardButton('спец системи док')
s83= KeyboardButton('співи і музика')
s84= KeyboardButton('стандартизація')
s85= KeyboardButton('стенографія')
s86= KeyboardButton('стилістика')
s87= KeyboardButton('сучасна українська мова')
#####################---- Т
s88= KeyboardButton('техніка креслення')
s89= KeyboardButton('техніка мовлення')
s90= KeyboardButton('технол практ')
s91= KeyboardButton('техноло (заг пит метод)')
s92= KeyboardButton('технологія реставраційних робіт')
#####################---- У
s93= KeyboardButton('українська література')
s94= KeyboardButton('українська мова')
#####################---- Ф
s95= KeyboardButton('фізичне виховання')
s96= KeyboardButton('фізика')
s97= KeyboardButton('фізкультура')
#####################---- Х
s98= KeyboardButton('хімія')
s99= KeyboardButton('художнє конструювання')
s100= KeyboardButton('художня праця')
#####################---- Ш
s101= KeyboardButton('шрифти')
#####################---- Абривіатури
s102= KeyboardButton('БЖД')
s103= KeyboardButton('ДПМ')
s104= KeyboardButton('ЕОМ')
s105= KeyboardButton('ІМІКС')
s106= KeyboardButton('МФЕМУ')
s107= KeyboardButton('ОМЗ')
s108= KeyboardButton('ООП')
s109= KeyboardButton('ОХТ')
s110= KeyboardButton('ТВКМ')
s111= KeyboardButton('ТМРДМО')
s112= KeyboardButton('ХОМ')
plus= '+'



s_add = ReplyKeyboardMarkup(resize_keyboard = True)

s_add.add(cancels).add(nothing).add(plus).add(s1).insert(s2).add(s3).insert(s4).add(s5) \
.insert(s6).add(s7).insert(s8).add(s9).add(s10) \
.insert(s11).add(s12).add(s13).insert(s14).add(s15) \
.insert(s16).add(s17).add(s18).add(s19).insert(s20) \
.add(s21).insert(s22).add(s23).add(s24).add(s25) \
.add(s26).add(s28).add(s29).insert(s30) \
.add(s31).insert(s32).add(s33).insert(s34).add(s35) \
.insert(s36).add(s37).insert(s38).add(s39).add(s40) \
.add(s41).add(s42).add(s43).add(s44).add(s45) \
.add(s46).add(s47).add(s48).add(s49).insert(s50) \
.add(s51).add(s52).add(s53).add(s54).add(s55) \
.add(s56).add(s57).add(s58).add(s59).add(s60) \
.add(s61).add(s62).add(s63).add(s64).add(s65) \
.add(s66).add(s67).add(s68).insert(s69).add(s70) \
.insert(s71).add(s72).add(s73).add(s74).add(s75) \
.insert(s76).add(s77).insert(s78).add(s79).insert(s80) \
.add(s81).insert(s82).add(s83).insert(s84).add(s85) \
.insert(s86).add(s87).add(s88).insert(s89).add(s90) \
.insert(s91).add(s92).add(s93).insert(s94).add(s95) \
.insert(s96).add(s97).insert(s98).add(s99).add(s100) \
.insert(s101).add(s102).insert(s103).insert(s104).insert(s105) \
.insert(s106).insert(s107).insert(s108).insert(s109).insert(s27).insert(s110) \
.insert(s111).insert(s112).add(cancels)
