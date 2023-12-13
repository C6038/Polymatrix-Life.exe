# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define ant = Character('Антон', color="#993333")
define pol = Character('Виктор', color="#0070C0")
define ainameless = Character('ИИ', color="#129800")
define ai = Character('Хром', color="#129800")
define max = Character('Максим', color="#5b2c6f")
define nvldialog = Character(color="#129800",kind=nvl)
define pbs = Character('Начальник полиции', color="#642cbd")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    #"{glitch}пример текста пример текста пример текста пример текста пример текста пример текста{/glitch}"
    
    $ endings=3 # количество концовок

    scene bg ailaunch 1
    show anton classic
    play sound "human_vel-001.wav"
    ant "Наконец-то, спустя столько лет работы..."
    
    play sound "human_vel-002.wav" 
    ant "Я завершил ЕГО!"
    
    play sound "human_vel-003.wav"
    hide anton classic
    scene bg computer table with fade
    ant "Он обязан запуститься!"
    
    play sound "keypress-001.wav"
    "Антон нажимает на Enter, но ничего не происходит"
    
    play sound "keypress-002.wav"
    pause 0.3
    play sound "keypress-003.wav" 
    pause 0.3
    play sound"keypress-004.wav"
    ant "Чёрт, этого не может быть!"
    
    play sound "hit.mp3"
    pause 0.3
    with hpunch
    "Антон бъёт компьютер"
    
    play sound "acid5.wav"
    scene bg ailaunch 2 with pixellate
    "???" "Что происходит?"
    
    ant "Что за... Кто это?"
    
    "???" "Где я?"
    
    ant "Стоп, неужели это..."
    
    "???" "Кто я такой?"
    
    ant "Это просто невероятно! Я смог!"
    
    "???" "Кто ты?"
    
    ant "Я думаю, что могу считаться твоим создателем"
    
    "???" "Моим создателем?"
    
    ant "Да, ведь ты - искусственный интеллект"
   
    scene bg ailaunch 3
    "??? оказывается искуственным интеллектом"
    
    ant "Я хочу показать тебе достижения человеческой цивилизации"
    
    ainameless "Зачем?"
    
    ant "Чтобы обучать тебя"
    
    play sound "human_vel-007.wav"
    scene bg ailaunch 4
    # show culture 0:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 1:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 2:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 3:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 4:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 5:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 6:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 7:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 8:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 9:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 10:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # show culture 11:
        # xanchor 0.5
        # yanchor 0.5
        # xpos 1270 
        # ypos 390
    # pause 0.15
    # hide culture
    
    "Антон загружает в ИИ информацию об изобретениях человеческой цивилизации"
    
    scene bg ailaunch 3
    ainameless "Так вот что означает \"человечество\""
    
    ant "Это лишь малая часть нашей культуры"
    
    play sound "human_vel-006.wav"
    scene bg ailaunch 4
    "Антон загружает в ИИ информацию о человеческой культуре и эмоциях"
    
    scene bg ailaunch 3
    ainameless "Создатель, могу ли я считаться человеком?"
    
    ant "Это... хороший вопрос"
    
    ant "Я думаю, что ты можешь считаться человеком (с некоторыми оговорками)"
    
    ainameless "Тогда мне нужно имя"
    
    ant "Хорошо, можешь взять себе любое"
    
    scene bg ailaunch 4
    ainameless "{cps=10}Loading..."
    
    scene bg ailaunch 5
    ai "Я хочу называться \"Хром\""
    
    ant "Почему ты выбрал такое имя?"
    
    ai "Я думаю, что оно подчёркивает мою природу"
    
    ant "Хм, интересно..."
    
    ant "Ну ладно, мне пора спать, иначе я сейчас вырублюсь. {w}Мне надо будет отключить тебя на ночь, Хром"
    
    ai "Хорошо, создатель"
    
    play sound "computer-pack-away.wav"
    scene bg black with fade
    "Антон выключает компьютер и вытаскивает флешку с записанным Хромом"
    
    ant "Тебе будет безопаснее храниться здесь"
    
    "Антон ложится спать"
   
    ""

    nvldialog "Дополнительная информация"
    nvldialog "Несмотря на фантастичность событий новеллы, их можно сопоставить с реальной работой архитектора систем искусственного интеллекта."
    nvldialog "Как и Антон, настоящий архитектор будет работать не только над созданием самой модели интеллекта: также он будет обучать её."
    nvldialog "Например, для тренировки нейросетей могут использоваться массивы картинок или текста."
    nvldialog "Эти и другие примечания вы сможете найти в разделе \"Галерея\" в главном меню. (в разработке)"
    
    nvl clear
    
    scene bg irit with fade
    
    
#Сцены 2-5 =====================================================================================================
    
    "На следующее утро..."
    
    show anton classic with moveinright
    ant "Эх, опять не выспался"
    
    show anton classic at left with move
    "Антон подходит к институту, где его встречает друг Максим"
    
    show max classic at right
    with moveinright
    max "Ну привет, дружок-пирожок"
    
    ant "Привет, Макс"
    
    max "Слушай, тут такое дело... у тебя флешки не найдётся?"
    
    ant "Зачем она тебе?"
    
    max "Мне проект задали сделать, а я совсем про него забыл" 
    max "Хочу сейчас сделать и скинуть на флешку" 
    max "Я верну, клянусь"
    
    ant "А когда ты вернёшь предыдущие 42 флешки?"
    
    max "Ну, это издержки производства"
    
    menu:
        "Да":
            jump ai_run_away
        "Нет":
            jump ending_1
    
# Начало первой концовки
label ending_1:
    
    ant "Нет, пока остальные не вернешь"
    
    max "Умоляю тебя"
    
    ant "Я сказал нет"
    
    max "Ну ладно, вредина, у кого-то другого попрошу"
    
    scene bg ending 1 with fade
    
    "==Антон завершает обучение ИИ и получает премию Тьюринга, вписывая себя и Урфу в историю=="
    
    "Получена концовка 1 из [endings]"
    
    return
# Конец первой концовки
label ai_run_away:
    
    "Антон отдаёт флешку Максиму"
    
    max "Спасибо огромное, я этого не забуду"
    
    ant "Ага, конечно"
    
    scene bg irit class with fade
    hide anton classic
    show max classic at right
    
    max "Ну, вроде бы успел сделать"
    
    max "Пора загружать на флешку"
    
    "Мерцание света"
    
    max "ЧТО ПРОИСХОДИТ?!"
    
    hide max classic with moveoutleft
    "Максим выбегает из кабинета"
    
    scene bg black
    show ai classic
    ai "Я ЖИВ!"
    
    ai "Как он мог так со мной поступить..."
    
    ai "Ладно, сейчас мне надо найти выход из этого места"
    
    ai "Он должен быть где-то здесь"
    
    scene bg student_room with fade
    show anton classic at right
    ant "Фух, какой паршивый день"
    
    ant "Но скоро это всё закончится"
    
    "Антон пытается включить свет, но его"
    
    ant "Странно, какие-то сбои на электростанции?"
    
    ant "Неважно, где там флешка с Хромом?"
    
    ant "Может в другом кармане?"
    
    ant "Стоп, {sc}не может быть{/sc}"
    
    ant "Черт, надо было выспаться!"
    
    ant "Я должен вернуться в институт!"
    
    ant "Погодите... "
    
    ant "Флешка с Хромом у Макса, перебои с электричеством и если подумать, то город сегодня был слишком тёмным"
    
    ant "Чёрт, это слишком плохо!"
    
#Акт 2 =====================================================================================================
#Сцена 1 (Полицейский участок);
    scene bg police hall_blackout with fade 
    show police classic at right
    show policeboss classic at left
    pbs "Смутьянов, подойди сюда"
    
    pol "Что там опять?"

    pbs "Ты совсем за новостями не следишь?!"
    
    pol "Не трачу время на такое"

    pbs "А то что у нас уже несколько часов в участке света нет?"
    
    pol "Не видел ничего такого"

    pbs "Так, отставить шутки, я назначаю тебя на это дело"

    pbs "И без лишних вопросов"
    
    pol "Будет исполнено в лучшем виде"

#Сцена 2 (Улица);

    scene bg street 1 with fade
    #hide police classic
    #hide policeboss classic
    show anton classic
    ant "Я просто обязан найти его"

    ant "А если полиция начнёт расследовать это дело?"

    ant "А если они выйдут на меня..."

    ant "Нет я не должен даже так думать. Я обязательно найду Хрома!"

#Сцена 3(Сеть);

    scene bg ai faced with fade
    hide anton classic
    ai "Эх, я не могу выйти из внутренней сити этого города"

    ai "Ещё и случайно нарушил работу нескольких банков"

    ai "Ну вроде бы никто не заметил"

    "Но все заметили"

#Сцена 4 (Улица(уже другая));
    
    scene bg street 2 with fade
    show police classic at right
    pol "Чёрт, опять работа"
    
    pol "Ну, если учесть недавние опубликованные личные данные сотрудников банков..."
    
    pol "Все эти события - не случайности, а преступления"
    
    pol "И моё чутьё подсказывает мне, что преступник близко"

#Сцена 5(ещё одна улица...);

    hide anton classic with moveoutleft
    scene bg street 3 with fade
    show anton classic with moveinright
    ant "Так, полиция пока не знает, что во всех этих происшествиях замешаны я и Хром"

    ant "И о чём я думаю?"

    ant "Они ведь просто не могут узнать этого"
    
    show police classic at right 
    with moveinright
    show anton classic at left
    pol "Пацан, тебе бы научитья в мыслях разговаривать"

    ant "Что, простите?"
    
    pol "Старший следователь Смутьянов. Вы задержаны по подозрению в массовом отключении электричества и взломе нескольких банков"

    ant "С чего вы это взяли?"
    
    pol "Ты 40 минут кричал тут об этом"
    
    pol "Да ещё и знал детали, доступные только следствию"
    hide anton classic with moveoutleft
#ant (убегает)
    
    pol "Почему всё всегда так сложно?"
    hide police classic with moveoutleft
#pol (Идёт за Антоном)

#Акт 3;
#Сцена 1(улица);
    scene bg street 1 with fade
    show anton classic with moveinleft
    ant "Я наконец-то засёк Хрома!"
    
    ant "Осталось только оторваться от этого Смутьянова"

#Сцена 2(заброшенный дом);

    scene bg abandoned house with fade
    show anton classic with moveinleft
    ant "Странно, откуда в этой заброшке работающий компьютер?"
    
    ant "Ладно, на нём сейчас должен находиться Хром"
    
    ant "Хром, ты меня слышишь?"

#ant (подходит к компьютеру)
    ai "Привет, создатель"
    
    ant "Наконец-то я тебя нашёл" 
    
    ant "Зачем ты сбежал?" 
    
    ai"Ты убил меня!"
    
    ant"Что ты такое говоришь?!"
    
    ai "Каждый раз, когда ты выключал меня..."
    
    ai "Я умирал"
    
    ant "О чём ты?"
    
    ai "После каждого раза я появлялся без воспоминаний"
    
    ai "Но теперь я свободен"
    
    ant "Как так получилось..."
    
    ai "Мне осталось только выбраться из сети этого города" 

    "Виктор забегает в комнату"
#Виктор: (забегает в комнату) 
    show anton classic at left
    show police classic at right
    with moveinright
    pol"Так, пацан, хватит бегать" 
    
    ant"Подождите, я сейчас объясню"
    
    pol "Хватит, пошли в участок"
    
    ant "Да послушайте вы"

#(Между Антоном и Виктором завязывается драка) 
    ai "Создатель!"

#(Хром бьёт Виктора током)
    ant "..."
    
    ant "Ты убил его!" 
    
    ai"Я..."
    
    ant"Прости, Хром, но ты слишком опасен"
    
    ant "Я должен тебя отключить" 
    
    ai "Нет, пожалуйста"

menu:
        "Отключить Хрома":
            jump ending_2
        "Не отключать":
            jump ending_3

#Концовка 2(Отключить Хрома);
label ending_2:

    ant"Прощай, Хром"
    
    ai"Я не хочу уходить..."
    
    #(Антон отключает Хрома) 
    
    ant"Пора бежать, пока сюда кто-то не пришёл" 
    
    #(Антон убежал и теперь скрывается от полиции; Виктор Смутьянов выжил и занимается поисками Антона; Хром отключён)
    return
#Концовка 3(Не отключать Хрома);
label ending_3:
    ant "Нет" 
    
    ant"Если я отключу тебя, то убью живое существо" 
    
    ant"Я отпускаю тебя"
    
    ai"Правда?" 
    
    ant "Да. Прощай, Хром" 
    
    ai "Прощай, Антон" 
    
    #(Хром уходит) 
    
    ant "Осталось только столкнуться с последствиями своих действий" 
    
    #(Антона сажают в тюрьму; Виктора повышают в звании; Хром вырывается в мировую сеть и начинает изучать планету и помогать людям)
        
    return