# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define Vanya = Character('Ваня', color="#c8ffc8")

define Pavla = Character('Павла', color="#b18e1c")

define Noy = Character('Ной', color="#7bd328")

define Vadim = Character('Вадим', color="#a395c9")

define inkogn = Character('???', color="#7bd328")

define inkogn1 = Character('???', color="#b18e1c")

define inkogn2 = Character('???', color="#a395c9")

default cybersecurity_score = 0
default current_day = 1
default total_days = 5


init:
    $ player_score = 0
    $ task_number = 0
    $ tasks_completed = 0
    $ tasks_count = 3 #количество фаз
    $ current_model = ""
    $ code_parameter = ""
    $ test_result = ""

    $ task_index = 0
    $ tasks = ['color', 'text', 'shrift']

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.R
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # Устанавливает постепенное появление и исчезновение бара и требуется только один раз в скрипте

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # Это  вертикальная черта таймера.

init:
    $ timer_range = 0
    $ timer_jump = 0

default diz_score = 0
default cur_day = 1
default tot_days = 3

define audio.vzriv = "vzriv.ogg"
define audio.run = "run.mp3"
define audio.vzryiv_osk = "vzryiv_osk.ogg"

define audio.menu_music= "menu_music.mp3"
define audio.stress = "stress.mp3"
define audio.robot = "robot.mp3"
define audio.laptop = "laptop.mp3"
define audio.people = "people.mp3"
define audio.timer = "timer.mp3"
define audio.predm = "predm.mp3"

define audio.prizeml = "prizeml.mp3"
define audio.ship = "ship.mp3"
define audio.inship = "inship.mp3"
define audio.svist = "svist.mp3"

define audio.strelba = "strelba.mp3"
define audio.inkomn = "inkomn.mp3"
define audio.fin = "fin.mp3"
define audio.zadachi = "zadachi.mp3"
# Игра начинается здесь:
label start:
    scene square with Dissolve(1)
    #проверка
    $ renpy.music.set_volume(0.3)
    "Ах, дивный Новый мир! На горизонте раскинулся яркий пейзаж, где небеса искрятся оттенками синего и фиолетового, а золотистое солнце освещает мир,
    создавая удивительные игры света и тени." 

    "Гладкие, обтекаемые здания, покрытые зелёными насаждениями и светодиодными панелями, плавно излучают мягкий свет, 
    наполняя воздух ощущением надежды и прогресса. Дым поднимается в воздух, смешиваясь с яркими огнями, освещающими обломки старых звездолётов и металлических конструкций."

    scene city with Dissolve(1)

    "Пешеходные мосты, словно ленты, соединяют небоскребы, а люди, одетые в легкие, яркие одежды, с улыбками на лицах перемещаются между ними, наслаждаясь жизнью в этом идеальном мире. Мире, где человеческий прогресс дошёл до создания чего-то живого, чего-то, что умнее самих людей.
    Они помогают, они учат, они защищают, они вдохновляют, они - уже не просто будущее, они - настоящее."

    "Вокруг парят дроны, доставляющие товары и информацию, а в воздухе слышен мелодичный шум — это гул природы, смешивающийся с технологическими звуками. Парк, раскинувшийся на уровне земли, полон цветущих растений и искусственных водоемов, где плавают светящиеся рыбы.
    Здесь царит гармония, между людьми и природой. И всё благодаря человечеству, что создало их. И тут же пожалело об этом"
    stop music fadeout 2.0
    play music vzriv fadein(1.0)
    $ renpy.music.set_volume(0.3)
    scene blast with Dissolve(2)

    pause(3.0)
    stop music fadeout 3
    scene hallway

    play music run fadein(1.0)
    $ renpy.music.set_volume(0.3)
    "Даже раз уж удалось спрятаться от ударной волны, звук разрушений всё равно болью рубанул по ушам. 
    Это дезориентировало. А дезориентироваться было нельзя. Сражаясь с головокружением, девушка со всех ног бежала по коридору."

    show vanya_def:
        xalign 0.75
        yalign 1.0
    with Dissolve(.5) 

    Vanya "НЕТ НЕТ НЕТ"

    "Заскользив на очередном повороте, она схватилась за выступающую ручку на углу, дабы не упасть."
    
    stop music fadeout 3

    hide vanya_def
    play sound robot fadein(1.0)
    pause(2.0)
    "звуки роботов"

    show vanya_def
    with Dissolve(.5) 
    Vanya "Ой мамочки, покааа!!!"

    hide vanya_def

    "Подтянувшись за этот выступ, девушка ринулась обратно, на ходу копаясь в своей сумке, а найдя нужное, с воодушевлением вставила флешку в своё устройство."
    
    show vanya_funny:
        xalign 0.2
        yalign 1.0
    with Dissolve(.5) 

    Vanya "Да где же это... Это точно правильная карта? Что за бред... Опачки"

    hide vanya_funny
    stop sound fadeout 2

    play music run fadein(1.0)

    "Вновь меняя своё направление, начала набирать скорость."

    scene hallway2 with Dissolve(.5)

    show vanya_def:
        xalign 0.50
        yalign 1.0
    with Dissolve(.5) 

    Vanya "Кто же знал, что я выживу! Да я в себя уверовать готова!"
    stop music fadeout 3
    hide vanya_def
    
    play music vzryiv_osk fadein(6.0)
    "Пробегая мимо одной из разрушенных дверей, Ваня резко остановилась. Между бровей вновь залегла морщинка. Вид из импровизированного окна открывался на.. Местное селение?
    Обычные люди отрешённо наблюдали за разрушающейся лабораторией, где находилась девушка. А ещё были заметны роботы, что подбирались к ним. 
    Ваня забегала глазами. А через мгновение ..."
    

    scene black with Dissolve(.5)
    pause(2.5)
    $ renpy.music.set_volume(0.5)


    scene hallway3 with Dissolve(.5)
    play music run fadein(2.0)
    $ renpy.music.set_volume(0.3)
    
    play sound people fadein(2.0)
    $ renpy.sound.set_volume(0.3)
    "Девушка бежит по разрушающимся коридорам лаборатории. Слышит крики людей - недалеко есть обычные люди, которые в ужасе наблюдают за происходящим"

    scene place_1
    
    stop music fadeout 3

    play music stress fadein(1.0)
    $ renpy.music.set_volume(0.1)
    "Ваня выбегает, останавливаясь рядом с вертикальной поверхностью, более-менее подходящей на роль холста. Взгляд скачет по всему окружению, стараясь найти хоть что-нибудь, 
    с помощью чего она может оставить послание для людей"
 
    show vanya_funny:
        xalign 0.75
        yalign 1.0
    with Dissolve(.5) 

    Vanya "И как здесь вообще использовался проектор…"

    hide vanya_funny

    show vanya_def:
        xalign 0.8
        yalign 1.0
    with Dissolve(.5) 

    play sound laptop fadein(0.1)
    $ renpy.sound.set_volume(1.0)
    "Времени мало, так что быстрыми движениями она включает его, попутно начиная вводить текст с предупреждением."

    stop sound fadeout 2

    show noy_angry:
        xalign 0.25
        yalign 1.0
    with Dissolve(.5) 

    inkogn "Бу! Испугалась?"

    hide noy_angry

    show noy_def:
        xalign 0.35
        yalign 1.0
    with Dissolve(.5) 

    inkogn "Не бойся, я друг, я тебя не обижу. Иди сюда, иди ко мне, посмотри мне в глаза. Ты видишь меня?"

    hide vanya_def

    show vanya_zaxv:
        xalign 0.8
        yalign 1.0
    with Dissolve(.5) 

    "Ваня переключала взгляд со странного парня на проекцию призыва бежать."

    inkogn "Я тоже тебя вижу! Давай смотреть друг на друга до тех пор, пока наши глаза не устанут!"

    hide vanya_zaxv

    show vanya_sad:
        xalign 0.82
        yalign 1.0
    with Dissolve(.5)

    "Её лицо скривилось с отвращением"

    hide noy_def

    show noy_rad:
        xalign 0.4
        yalign 1.0
    with Dissolve(.5) 

    inkogn "Ты не хочешь? Почему? Что-то не так?"

    hide vanya_sad

    show vanya_zaxv:
        xalign 0.8
        yalign 1.0
    with Dissolve(.5) 

    label menu1:
    $ time = 7
    $ timer_range = 7
    $ timer_jump = 'nothing'

    play sound timer fadein(0.1)
    $ renpy.sound.set_volume(0.5)
    show screen countdown
    menu:
        "Атаковать":
            stop sound fadeout 0.1
            hide screen countdown
            jump atack
        "Продолжить писать":
            stop sound fadeout 0.1
            hide screen countdown
            jump write
        "Расспросить":
            stop sound fadeout 0.1
            hide screen countdown
            jump ask
   
    label atack:
        #"Ты выбрал атаку"
        Vanya "(шёпотом)... нужно что-то, нужно какое-то оружие!... "
        play sound predm fadein(0.1)
        $ renpy.sound.set_volume(0.3)
        "Оружие не находится, так что пока близлежащие вещи отправляются в полёт."
        hide noy_rad
        show noy_angry:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        
        inkogn "ЭЙ, Я ЖЕ ГОВОРЮ: Я ДРУГ, НЕ БОЙСЯ! \nЯ, конечно, не трус, к сожалению, но самому щас стрёмно...
        \nУСПОКОЙСЯ, ПОЖАЛУЙСТА, Я МИРНЫЙ... Что же еще сказать то... КТО ДВИНЕТСЯ - ТОТ ГУМ"
        stop sound fadeout 2
        "Ваня резко замирает"
        hide vanya_zaxv
        show vanya_def:
            xalign 0.8
            yalign 1.0
        with Dissolve(.5) 
        Vanya "*про себя* ... Что он несёт, я не ослышалась вообще?"
        hide noy_angry
        show noy_def:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        inkogn "Ахаха, ну физматы, ну дают! Никогда не подводили в этом!"
        hide noy_def
        show noy_bal:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5) 
        "Юноша ловким движением достаёт из сумки баллончик с красной краской"
        inkogn "Это не оружие. А я не враг. Ну, и не гум и не физмат"
        jump after_menu1
    label write:
        #"продолжим писать"
        inkogn "Не понял... \nЧто за игнор, ау!?"
        hide noy_rad
        show noy_angry:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 

        hide vanya_zaxv

        show vanya_def:
            xalign 0.8
            yalign 1.0
        with Dissolve(.5) 
        Vanya "Не отвлекай, видишь я делом занята"
        hide noy_angry
        show noy_def:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        inkogn "Делом она занята... \nМолодец конечно, а толку то???"
        Vanya "Эй! Я вообще-т..."
        inkogn "*перебивая* \nСмогут ли они прочитать? Что насчёт тех, кто не умеет читать на этом языке?"
        inkogn "Ну-ка в сторону"
        hide noy_def
        show noy_bal:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        "На этих словах юноша вытащил красный баллончик с краской"
        jump after_menu1
    label ask:
        "расспросим..."
        Vanya "Ты кто вообще?"
        hide noy_rad
        show noy_angry:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        inkogn "О тебе бы хотелось узнать побольше так-то. Бегает она в одиночку по лаборатории ПРС, преследуемая их роботами. 
        Да ещё и живая. \nЯ - графический дизайнер, а ты-то кто?"
        Vanya "Я - ... я не знаю..."
        inkogn "Нуу, не к спеху \n Подумай пока в сторонке"
        hide noy_angry
        show noy_bal:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5) 
        "У юноши в руках появился красный баллончик с краской."
        jump after_menu1
    label nothing:
        #"ничего, ну и ладно"
        inkogn "..."
        hide noy_rad
        show noy_angry:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        inkogn "Мда, супер. Я рад, конечно, что ты уже начала играть, но все-таки немного не вовремя. 
        С вашего позволения, пока вы задумались о чем-то"
        hide noy_angry
        show noy_bal:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5) 
        "Юноша взял красный баллончик с краской из своей сумки."
        jump after_menu1
    stop music fadeout 3
    label after_menu1:

        "Ваня не сводит глаз с неназвавшегося человека, наблюдая за ним с опаской."
        Vanya "Это...?"
        inkogn "Называется донести информацию, не используя слов. Бывает полезно в таких ситуациях. Но надо уметь это делать"
        Vanya "А ты умеешь? Как то это не внушает..."   
        inkogn "Ооо, не волнуйся, они поймут, как только заметят. А они заметят, не сомневайся."
        Vanya "Изумительно. Они заметят. И нас заметят. И не только невинные люди. Что делать будем?"
        inkogn "А теперь - ..."
        "Парень останавливается на полуслове"
        hide noy_bal
        show noy_def:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        inkogn "Как там тебя?"
        Vanya "Ваня"
        inkogn "Меня - Ной"
        Noy "Так вот, Ваня, если хочешь продолжать, то.. Тебе лучше побежать со мной, иначе тебя поймают"
        
        hide vanya_zaxv
        hide noy_rad

        scene hallway

        "После злорадной улыбки, что становилась всё явнее к концу предложения, он лишь пожал плечами и начал убегать прочь"
        play sound run fadein(0.1)
        $ renpy.sound.set_volume(0.3)
        Vanya "Куда мы бежим?!?"
        Noy "К таким, как мы: к друзьям, домой!"

        stop sound fadeout 3.0
        play sound ship fadein(0.1)
        $ renpy.sound.set_volume(0.3)
        scene view_1 with Dissolve(.5)
        "Ваня не видит, но слышит как искажённая улыбка опять появляется на его лице. А ещё она слышит гудящие звуки, пронизывающие ветер."
        
        scene view_2 with Dissolve(.5)
        "Перед ними взлетает корабль."
        scene view_3 with Dissolve(.5)
        pause(3.0)
        "Не сомневаясь ни мгновения, Ной в него запрыгивает, схватившись рукой за борт. А после протягивает Ване вторую.
        \nКолеблясь мгновение, девушка прыгает за ним, вкладывая после свою ладонь в его в поисках опоры."
        pause(1.0)
        stop music fadeout 2.0

        play music inship fadein(2.0)
        $ renpy.music.set_volume(0.1)
        "Отдаляющийся вой двигатель словно забрал всё остальные звуки с собой. Лишь сирена грохотала в воздухе, впитывая потрескивание огня. 
        Дым от него захватывал пространство вокруг, становясь владельцем этой территории."
        pause(2.0)
        
        scene view_2
        "Но и он будто обходил стороной только что покинутую площадку. Где на всю стену красовалась эмблема. 
        Такая метка привыкла появляться именно в таких местах. Там она привыкла и оставаться. Здесь были мы."
        pause(1.0)
        play sound prizeml fadein(0.1)
        $ renpy.sound.set_volume(0.3)
        scene black

        pause(1.0)
        
        scene ship
        
        show vanya_funny_sm_rev:
            xalign 0.8
            yalign 1.0
        with Dissolve(.5) 

        Noy "*убегая* Я скоро вернусь, жди здесь!"

        "И убежал. Ваня бродила взглядом по помещению, но глазу было не за что зацепиться: корабль как корабль. 
        \nОставалось только неловко зажиматься посреди комнаты. Провода, механизмы, огоньки. "

        hide vanya_funny_sm_rev

        show vanya_zaxv_sm:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5)

        show pavla_def_sm_rev:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5)

        "Внезапно кто-то соединяет её руки за спиной, толкая в одну из панелей"
        
        inkogn1 "Кто ты, и как обошла систему безопасности. У тебя 3 секунды на ответ!"

        show noy_def_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5) 

        pause (1.0)

        show vadim_udivl_sm_rev:
            xalign 0.9
            yalign 1.0
        with Dissolve(.5) 

        Noy "Павла, милая, всё пучком, это я её впустил. У нас прибавление в команде!"

        "Видя, что никто не стал радостным после его столь позитивного заявления, в конце он решил добавить"
        hide noy_def_sm_rev
        show noy_angry_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)

        Noy "Извините, что не сказал заранее \nЯ бы и сказал раньше, если бы не пришлось топать за мистером-панелью-управления, до которого просто так не достучаться"

        hide noy_angry_sm_rev
        show noy_def_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)
        "Ваня только сейчас заметила ещё одного парня, который пришёл за Ноем"

        Vanya "Но если он тут, то... Кто тогда управляет кораблём? Сколько вас тут вообще?"

        inkogn2 "Нас здесь трое. Кораблём управляет мой искусственный интеллект"

        Pavla "Перед тем, как всё это ей говорить, было бы неплохо вначале узнать о ней. Ты кто? "

        Vanya "Ох, я сама не уверена. Я беглянка. Мне легко давалась информатика, так что в своё время я изучала разные штуки, чтобы понять, чем бы хотела заниматься"

        Vanya "Понять мне не удалось, но хоть в программировании и компьютерах начала разбираться. Я знала, что сопротивление есть, но сама ни разу ни на кого так не выходила"

        play sound svist fadein(0.1)
        $ renpy.sound.set_volume(0.3)
        "*Ной присвистнул*"
        hide noy_def_sm_rev
        show noy_rad_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)

        Noy "Вот это речь. Уверена, что не шпионка и это не заготовленная речь?"
        
        hide noy_rad_sm_rev
        show noy_def_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)
        "Он смеет ставить под сомнение её искренность? И это он-то? Агрессия так и сочилась в её интонации"

        Vanya "Это называется ораторское мастерство и умение показать себя. Не обесценивай мои навыки"

        inkogn2 "И что ты делала в лаборатории ПРС? "

        Vanya "Как я и говорила, людей вроде вас я не находила. Поэтому я пыталась справляться сама "

        Pavla "Давай ближе к делу!"
        hide vanya_zaxv_sm
        show vanya_def_sm_rev:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5)
        "Ваня засмущалась, но полезла в сумку, доставая флешку" 

        hide vanya_def_sm_rev
        show vanya_zaxv_sm:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5)
        Vanya "Я скачала данные, на которых схемы зданий и карты лабораторий. "

        hide pavla_def_sm_rev with Dissolve(.5)
        "Павла смерила и Ваню, и флешку тяжёлым взглядом. Забрав её, молча ушла"

        hide vadim_udivl_sm_rev
        show vadim_udivl_sm_rev:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        inkogn2 "Не переживай, она вернётся. Специализацию мою и Ноя ты уже знаешь, а вот у Павлы информационная безопасность. 
        \nТы же Ваня, да? Я Вадим. Не держи зла на неё, это просто её характер. "

        Vadim "К слову, скоро приземляемся"
        play sound prizeml fadein(0.1)
        $ renpy.sound.set_volume(0.3)
        hide vadim_udivl_sm_rev with Dissolve(.5)
        pause(0.5)
        hide noy_def_sm_rev with Dissolve(.5)
        "На этих словах он развернулся, уходя. Ной поскакал за ним"

        hide vanya_zaxv_sm
        show vanya_funny_sm_rev:
            xalign 0.5
            yalign 1.0
        with Dissolve(.5)
        "Ваня с видом принятия тленности бытия пыталась переварить произошедшее. 
        \nБыть может, она с ними окажет больше пользы этому миру? Ну или хотя бы продвинется в понимании себя. "
        stop music fadeout 2.0

        play music inkomn fadein(2.0)
        $ renpy.music.set_volume(0.1)
        scene black with Dissolve(.5)

        "...Ваню охватило лёгкое чувство дежавю. Вот опять она в новом месте, и вот опять её сразу же оставляют одну. Но в этот раз гулять взглядом по интерьеру было интересно..."

        scene bg room11 with Dissolve(.5)

        "Комната была наполнена яркими вспышками света от экранов и мерцанием различных устройств. На стенах висели постеры с лозунгами, призывающими к свободе и сопротивлению, а также графические работы, созданные членами группы. В углу стоял большой стол, уставленный мониторами, клавиатурами и графическими планшетами, где дизайнеры работали над новыми проектами."
        
        "На одном из столов лежали распечатки с чертежами и схемами, а рядом находились контейнеры с красками и маркерами – следы недавней работы над визуальными материалами для их кампании. В воздухе витал запах свежей краски и электроники, создавая атмосферу творчества и активности."

        scene bg room2
        "На другом конце комнаты был небольшой уголок с мягкими креслами и подушками, где члены группы иногда собирались для обсуждений или просто для отдыха. Здесь же стоял кофейный автомат, вокруг которого наверняка всегда крутились люди, обмениваясь идеями и шутками."

        "Вдоль одной из стен стояли полки, заполненные книгами по программированию, безопасности данных и искусственному интеллекту. На одной из полок также стояли старые видеоигры и консоли, которые, казалось, служили не только для отдыха, но и для изучения технологий."

        "В центре комнаты находился большой экран, на котором демонстрировались новости и обновления о движении повстанцев. Иногда на экране появлялись сообщения от других баз, создавая ощущение единства и связи между членами команды."
        
        scene black

        "Ваня чувствовала, как энергия этого места наполняет её, и понимала, что здесь, среди этих людей и технологий, начинается её новое приключение."

        scene bg room2

        show vanya_zaxv_sm:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5)
        $ renpy.music.set_volume(0.1)
        Vanya "О! Нашлись! Что мне делать? Для меня есть задания? "

        show noy_def_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)
        
        show pavla_def_sm_rev:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5)

        show vadim_udivl_sm_rev:
            xalign 0.83
            yalign 1.0
        with Dissolve(.5) 

        Vadim "Хммм, наверное нет..."
        "Произнёс Вадим с еле сдерживающейся ухмылкой"

        hide vanya_zaxv_sm
        
        show vanya_sad_sm_rev:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5)
        "Запал Вани быстро иссяк... "

        Pavla "Все обязаны быть заняты делом. Мы тебя подобрали, отвечать за тебя тоже нам. 
        \nТак что не подведи, тем более в твоей флешке было кое-что очень важное"

        hide vanya_sad_sm_rev
        
        show vanya_def_sm_rev:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5)
        "Отсутствие запала начало меняться накатывающей тревогой"

        hide noy_def_sm_rev
        show noy_rad_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)
        Noy "Ванюша, не переживай так. Ты подсунула нам работёнку!"

        hide noy_rad_sm_rev 

        show noy_def_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)

        Vadim " Да, это очень ценные данные"

        hide noy_def_sm_rev 

        show noy_angry_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)

        Noy "Я так и сказал так-то."

        hide noy_angry_sm_rev

        show noy_def_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)
        Noy "Так вот, ..."

        pause(2.0)

        "Спасибо, Ной. Самое время для драматичной паузы. "

        Noy "... тебе предстоит выполнять нашу работу!"

        hide vanya_def_sm_rev
        
        show vanya_funny_sm_rev:
            xalign 0.2
            yalign 1.0
        with Dissolve(.5)

        Vanya "???"
        Pavla "От тебя никто не ждёт ничего сверхъестественного."

        hide noy_def_sm_rev

        show noy_rad_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)
        
        Noy "Просто выбери чью работу будешь выполнять, не переживай - мы поможем!"

        hide noy_rad_sm_rev

        show noy_def_sm_rev:
            xalign 0.6
            yalign 1.0
        with Dissolve(.5)

        "В комнате царит напряженная атмосфера. Ваня чувствует на себе взгляды членов команды, 
        каждый из которых надеется на её помощь и предлагает свои уникальные навыки. Девушка вздыхает, собирая мысли."

        hide noy_def_sm_rev
        hide vanya_funny_sm_rev
        hide vadim_udivl_sm_rev
        hide pavla_def_sm_rev

        Vanya "*про себя* Кого выбрать? Ной, Павла, Вадим... У каждого из них в работе есть что-то интересное..."
        
        show noy_def:
            xalign 0.4
            yalign 1.0
        with Dissolve(.5) 
        "Ной: Графический дизайнер, ответственный за визуальную часть наших кампаний. Создает яркие и запоминающиеся образы, которые вдохновляют людей."

        hide noy_def

        show pavla_dumaet:
            xalign 0.45
            yalign 1.0
        with Dissolve(.5)
        "Павла: Специалист по информационной безопасности, умный стратег, предоставляющий надежную защиту для всех наших данных. Иногда занимается взломом систем противника"
        hide pavla_dumaet
        
        show vadim_udivl:
            xalign 0.45
            yalign 1.0
        with Dissolve(.5)
        "Разработчик искусственного интеллекта. Работает над созданием программ, которые могут предсказать действия врага, а также помогают в оптимизации наших операций.
        \nВсегда нужен для задач с высокими технологиями."
        hide vadim_udivl

        menu:
            Vanya "Чью работу будем выполнять?"
            "Ной":
                Vanya "Отлично, мне нравится изучать графический дизайн!"
                scene black
                jump after_menu_Noy
            "Павла":
                Vanya "Здорово, меня интересуют навыки специалиста по ИБ!"
                scene black
                jump after_menu_Pavla
            "Вадим":
                Vanya "Супер! Разработка ИИ - увлекательно и познавательно!"
                scene black
                jump after_menu_Vadim
        
        label after_menu_Noy:
            play music zadachi fadein(2.0)
            $ renpy.music.set_volume(0.1)
            scene place_diz
            show noy_def:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)
            show vanya_def:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Vanya "Я выберу твою работу! Мне всегда нравилось рисовать и создавать что-то новое"
            hide noy_def
            show noy_rad:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)
            Noy "Отлично! Мы проработаем кейс по графическому дизайну, чтобы помочь в борьбе против повстанцев!"
            scene black with Dissolve(.5)
            #jump start_diz_game

        label start_diz_game:
            scene place_diz with Dissolve(.5)
            show noy_def:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)

            show vanya_def:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)

            Noy "Нам нужно придумать, как помочь людям узнать о надвигающейся опасности. Есть идеи?"
            Vanya "Мы бы могли предупредить, громко крикнув. У меня довольно пронзительный голос"
            hide noy_def
            show noy_angry:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)

            Noy "Нет, это слишком опасно. Мы сделаем визуальное сообщение"
            hide vanya_def
            show vanya_funny:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Vanya "Типо плаката?"
            hide noy_angry
            show noy_def:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)
            Noy "Именно! Но только помни, что в данной ситуации, чем ярче и заметней плакат, тем больше людей будут предостережены!"
            hide vanya_funny
            show vanya_zaxv:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Vanya "Хорошо, я постараюсь!"
            Noy "Для начала я расскажу тебе о главных требованиях в мире дизайна"
            scene black with Dissolve(.5)
            jump diz_game

        label diz_game:
            scene tablet with Dissolve(.5)
            Noy "И так, начнем"
            Noy "Первое - это, разумеется, цветовая палитра. Она должна быть гармоничной и контрастной, чтобы выделять необходимые моменты. \nОй, забыл сказать, текст мы можем сделать только черным, учти это"
            Noy "Запомни парочку идеальных цветосочетаний: \n 1) Черное на пурпурном \n 2) Красное на белом \n 3) Зеленое на белом \n 4) Черное на красном" 
            Noy "Второе - это чёткая структура. Оформление должно быть таким, чтобы плакат легко воспринимался читателем. Для этого нужно соблюдать логическую структуру, позволяющую быстро уловить основную концепцию"
            Noy "Третье- информативный и краткий текст. Заголовок должен быть броским, состоящим не более чем из 4–5 слов. Текст должен быть читаемым, для этого используются контрастные цвета и шрифты"
            Noy "Четвертое - выразительные изображения. Они должны гармонировать с основной идеей плаката, передавать необходимую информацию или эмоции. Кроме того, изображения должны быть качественными, проработанными"
            Noy "Наконец, пятое - грамотная типографика. Шрифты должны соответствовать основной идее и целевой аудитории плаката, быть читаемыми и хорошо воспринимаемыми"
            Noy "Универсальные шрифты: Arial, Calibri, Verdana"
            Noy "Теперь перейдем к задаче - создать цифровой плакат \nЗа каждое правильное решение ты получаешь баллы. Старайся набрать максимум!"
            jump diz_tasks

        label diz_tasks:
            while cur_day <= tot_days:
                $ current_task = tasks[task_index]
                call hand_task(current_task) from _call_hand_task
                $ task_index = (task_index + 1) % len(tasks)
                $ cur_day += 1
            jump game_fin
        # Обработка заданий
        label hand_task(tasks):
            scene place_diz
            if tasks == 'color':
                call task1 from _call_task1
            elif tasks == 'text':
                call task2 from _call_task2
            elif tasks == 'shrift':
                call task3 from _call_task3
            return
        # Задание по фону
        label task1:
            "Подберем фон для нашего инфоплаката"
            menu:
                "Какой оттенок выберем, исходя из целей данного плаката?"
                
                "Белый":
                    $ diz_score += 5
                    "Хороший, универсальный вариант, продолжим"
                    
                "Зеленый":
                    $ diz_score -= 5
                    "Не совсем подходящий оттенок для привлечения внимания"
                    
                "Красный":
                    $ diz_score += 3
                    "Подойдет, хорошо привлечет внимание и сразу вызовет насторожение"
            return
        # Задание по тексту
        label task2:
            "Теперь очередь выбора текстового сообщения, которое мы напишем"
            menu:
                "Что пишем на плакате?"
                
                "ОПАСНОСТЬ":
                    $ diz_score += 5
                    "В самый раз"
                    
                "БЕГИТЕ СКОРЕЕ, ВТОРЖЕНИЕ РОБОТОВ, ОНИ БЛИЗКО":
                    $ diz_score -= 5
                    "Не совсем подойдет, очень длинно"
                    
                "ВНИМАНИЕ, ВТОРЖЕНИЕ":
                    $ diz_score += 5
                    "Коротко и ясно. Все как и положено"
            return
        # Задание по шрифту
        label task3:
            "Переходим к шрифту текста"
            menu:
                "Какой шрифт наиболее подходит?"
                
                "Шрифт 'Winter Belly' (художественные элементы)":
                    $ diz_score -= 5
                    "Плохо сочетается, издалека можно и не прочитать"
                    
                "Шрифт 'Druk wide' (широкие элементы)":
                    $ diz_score += 3
                    "На крайний случай, можно использовать. Но есть и получше вариант"
                    
                "Шрифт 'Verdana'(насыщенный, средней контрастности)":
                    $ diz_score += 5
                    "Идеально!"
            return
        # Конец игры
        label game_fin:
            scene place_diz
            show noy_def:
                xalign 0.35
                yalign 1.0
            with Dissolve(.5)
            if diz_score >=12 :
                "Поздравляю! Вы отлично справились с работой графического дизайнера!"
                "Ваш итоговый счет: [diz_score] баллов."
                Noy "Не сомневался в тебе, ты все схватываешь на лету!"
                Noy "Вот какой плакат получился, здорово, молодец!"
                
                #добавить сюда картину
                jump diz
            elif diz_score >= 8:
                "Неплохой результат, но есть куда расти."
                "Ваш итоговый счет: [diz_score] баллов."
                "Изучи больше о принципах создания графического интерфейса!"
                #добавить сюда картину
                Noy "Немножко подшаманил, но ты тоже молодец, смотри что получилось"
                jump diz
            else:
                "Тебе нужно больше практики."
                "Ваш итоговый счет: [diz_score] баллов."
                "Попробуй еще раз и изучи основы создания графического интерфейса!"
                $ diz_score = 0
                $ cur_day = 1
                jump diz_game
            return            

        label after_menu_Pavla:
            play music zadachi fadein(2.0)
            $ renpy.music.set_volume(0.1)
            scene place_ib
            show pavla_def:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)

            show vanya_def:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Vanya "Я помогу Павле! Меня интересуют технологии безопасности. "
            Pavla "Хорошо. Я покажу тебе, как всё работает, но прежде..."
            scene black with Dissolve(.5)

            label start_security_game:
            scene place_ib
            show pavla_dumaet:
                xalign 0.5
                yalign 1.0
            with Dissolve(.5)
            Pavla "Добро пожаловать в симулятор специалиста по информационной безопасности!"
            Pavla "Расскажу кратко, кто такой и чем занимается, специалист по ИБ"
            hide pavla_dumaet

            scene tablet with Dissolve(.5)
            Pavla "Работа специалиста по ИБ включает в себя понимание различных угроз, применение мер защиты и постоянное повышение своей квалификации. 
            \nИнформационная безопасность является критически важной для защиты организаций от кибератак и обеспечения непрерывной работы их информационных систем."
            Pavla "Три столпа ИБ: Конфиденциальность, целостность и доступность (CIA Triad)."
            Pavla "Виды угроз делятся на 3 вида: \n 1) Внешние угрозы - хакеры, вредоносное ПО (Malware), фишинг, DDoS-атаки \n 2) Внутренние угрозы - ошибки персонала, недобросовестные сотрудники \n 3) Физические угрозы - кража, повреждение оборудования"
            Pavla "Основные направления работы специалиста по ИБ: \n 1) Анализ угроз и рисков: Оценка потенциальных угроз и уязвимостей 
            \n 2) Разработка политики безопасности: Создание правил и процедур, направленных на защиту информации. \n 3) Внедрение мер безопасности: Настройка и сопровождение технических средств защиты."
            Pavla "4) Мониторинг безопасности: Отслеживание событий безопасности и выявление инцидентов. 
            \n 5) Реагирование на инциденты: Расследование и устранение последствий инцидентов безопасности. \n 6) Аудит безопасности: Проверка эффективности мер защиты."
            Pavla "А теперь приступим к задаче - защищать нашу базу от различных киберугроз \n За каждое правильное решение ты получаешь баллы. Попробуй набрать максимум!"
            jump daily_tasks

        label daily_tasks:
            $ tks = ['phishing', 'malware', 'access', 'audit', 'incident']
            $ cur_task_index = 0
            while current_day <= total_days and cur_task_index < len(tks):
                $ task = tks[cur_task_index]
                call handle_task(task) from _call_handle_task
                $ current_day += 1
                $ cur_task_index += 1
            jump game_end

        # Обработка заданий
        label handle_task(task):
            scene place_ib
            if task == 'phishing':
                call phishing_task from _call_phishing_task
            elif task == 'malware':
                call malware_task from _call_malware_task
            elif task == 'access':
                call access_control_task from _call_access_control_task
            elif task == 'audit':
                call security_audit_task from _call_security_audit_task
            elif task == 'incident':
                call incident_response_task from _call_incident_response_task
            return

        # Задание по фишингу
        label phishing_task:
            Pavla "Повстанец получил подозрительное письмо"          
            menu:
                "Как вы поступите?"   
                "Проверить отправителя, ссылки и вложения":
                    $ cybersecurity_score += 10
                    "Правильно! Вы обнаружили фишинговую атаку и предотвратили утечку данных."
                    
                "Открыть вложение":
                    $ cybersecurity_score -= 5
                    "Неправильно! Открытие подозрительных вложений может привести к заражению системы."
                    
                "Переслать письмо коллегам":
                    $ cybersecurity_score -= 5
                    "Неправильно! Пересылка подозрительных писем может распространить угрозу."
            return

        # Задание по вредоносному ПО
        label malware_task:
            Pavla "Антивирус обнаружил подозрительную активность на компьютере."        
            menu:
                "Ваши действия?"
                "Изолировать компьютер и провести полное сканирование":
                    $ cybersecurity_score += 10
                    "Отлично! Вы предотвратили распространение вредоносного ПО."
                    
                "Игнорировать предупреждение":
                    $ cybersecurity_score -= 5
                    "Неправильно! Игнорирование угроз может привести к серьезным последствиям."
                    
                "Перезагрузить компьютер":
                    $ cybersecurity_score -= 5
                    "Неправильно! Перезагрузка не решит проблему с вредоносным ПО."
            return

        # Задание по контролю доступа
        label access_control_task:
            Pavla "Новенький, как и ты, просит доступ ко всем системам компании"           
            menu:
                "Как поступим?"            
                "Предоставить минимально необходимые права доступа":
                    $ cybersecurity_score += 10
                    "Правильно! Принцип минимальных привилегий - основа безопасности."
                    
                "Дать полный доступ":
                    $ cybersecurity_score -= 5
                    "Неправильно! Излишние права доступа повышают риски безопасности."
                    
                "Отказать в доступе полностью":
                    $ cybersecurity_score -= 5
                    "Неправильно! Сотрудник не сможет выполнять свою работу."
            return

        # Задание по аудиту безопасности
        label security_audit_task:
            Pavla "Пора провести аудит безопасности системы."          
            menu:
                "Что проверим в первую очередь?"
                "Обновления системы и права доступа":
                    $ cybersecurity_score += 10
                    "Правильно! Это ключевые аспекты безопасности системы."
                    
                "Пароли пользователей, работающих в системе":
                    $ cybersecurity_score += 5
                    "Частично верно, но аудит должен быть более комплексным."
                    
                "Антивирус системы":
                    $ cybersecurity_score += 5
                    "Недостаточно. Нужен комплексный подход к аудиту."
            return

        # Задание по реагированию на инциденты
        label incident_response_task:
            Pavla "Обнаружена утечка данных! Что делаем?"  
            menu:
                "Выберите порядок действий:"
                
                "Изолировать проблему, собрать данные, устранить причину":
                    $ cybersecurity_score += 10
                    "Отлично! Правильный порядок действий при инциденте."
                    
                "Отключить все системы":
                    $ cybersecurity_score -= 5
                    "Неправильно! Это может навредить другим процессам."
                    
                "Проигнорировать до завтра":
                    $ cybersecurity_score -= 10
                    "Очень плохо! Промедление увеличит ущерб от инцидента."
            return

        # Конец игры
        label game_end:
            scene place_ib
            show pavla_def:
                xalign 0.35
                yalign 1.0
            with Dissolve(.5)
            if cybersecurity_score >= 40:
                "Поздравляю! Вы отлично справились с работой специалиста по ИБ!"
                "Ваш итоговый счет: [cybersecurity_score] баллов."
                "Вы готовы к работе в сфере информационной безопасности!"
                jump ib
            elif cybersecurity_score >= 20:
                "Неплохой результат, но есть куда расти."
                "Ваш итоговый счет: [cybersecurity_score] баллов."
                "Изучи больше о принципах информационной безопасности!"
                jump ib
            else:
                "Вам нужно больше практики."
                "Ваш итоговый счет: [cybersecurity_score] баллов."
                "Попробуй еще раз и изучите основы информационной безопасности!"
                $ cybersecurity_score = 0
                $ current_day = 1
                jump start_security_game
            return  

        label after_menu_Vadim:
            play music zadachi fadein(2.0)
            $ renpy.music.set_volume(0.1)
            scene place_ii
            show vadim_def:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)

            show vanya_def:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Vanya "Я выберу Вадима! Разработка ИИ - это невероятно увлекательно! "
            Vadim "Прекрасный выбор! Я тебе кратко расскажу про свою деятельность и попробуем изменить ИИ роботов"
            scene black with Dissolve(.5)
            jump mini_game_start

        label mini_game_start:
            scene place_ii
            show vadim_udivl:
                xalign 0.5
                yalign 1.0
            with Dissolve(.5)
            # Теория о работе разработчика ИИ
            Vadim "**Теория: Разработчик ИИ**"
            "Разработчик искусственного интеллекта (ИИ) в IT-сфере занимается созданием интеллектуальных систем, способных обучаться, решать проблемы и взаимодействовать с окружающей средой."
            "**Основные задачи:** \n - Разработка и обучение моделей машинного обучения (ML) и глубокого обучения (DL) 
            \n - Обработка естественного языка (NLP) для понимания и генерации текста \n - Разработка систем компьютерного зрения для анализа изображений и видео \n - Интеграция ИИ-моделей в существующие системы и приложения."
            "**Ключевые навыки:** \n - Знание математики, статистики и алгоритмов машинного обучения \n - Опыт программирования на языках Python, R и др
            \n - Знание библиотек, таких как TensorFlow, PyTorch, scikit-learn, Keras \n - Навыки работы с данными: сбор, очистка, анализ и интерпретация"
            "**Процесс разработки:** \n 1. Сбор данных: Подготовка наборов данных для обучения моделей \n 2. Предварительная обработка данных: Очистка и подготовка данных 
            \n 3. Выбор модели: Определение наиболее подходящего алгоритма или архитектуры нейронной сети" 
            "4. Обучение модели: Процесс обучения модели на подготовленных данных \n 5. Оценка модели: Оценка точности и производительности обученной модели \n 6. Развертывание модели: Интеграция модели в нужную среду"
            Vadim "Думаю, ты все запомнила. Пришло время проверить на практике полученные знания"
            hide vadim_udivl
            pause (1.0)
            "Ваня попала в лабораторию, где разрабатывают роботов. Но, похоже, их ИИ настроен враждебно. Задача Вани - изменить ситуацию."
            scene tablet with Dissolve(.5)
            jump analysis_phase

        label analysis_phase:
            "Фаза сбор данных и выбор модели: Изучите поведение роботов."
            menu:
                "Какая модель у исследуемых роботов?"
                "Агрессивная модель":
                    $ current_model = "aggressive"
                    jump check_analysis
                "Защитная модель":
                    $ current_model = "defensive"
                    jump check_analysis
                "Патрульная модель":
                    $ current_model = "patrol"
                    jump check_analysis

        label check_analysis:
            if current_model == "aggressive":
                "Вы верно определили модель поведения роботов. Теперь нужно изменить их код."
                $ player_score += 10
                $ tasks_completed += 1
                jump code_phase
            else:
                "Вы ошиблись. Но это не страшно, можно попробовать снова."
                jump analysis_phase
            
        label code_phase:
            "Фаза переобучение модели: Смотрите на код управления роботами"
            menu:
                "В коде есть параметр 'aggression_level'. Текущее значение '100'. Что нужно сделать?"

                "Изменить на '50'":
                    $ code_parameter = "50"
                    jump check_cod
                "Изменить на '0'":
                    $ code_parameter = "0"
                    jump check_cod
                "Изменить на '200'":
                    $ code_parameter = "200"
                    jump check_cod

        label check_cod:
            if code_parameter == "0":
                "Ваня успешно снизила уровень агрессии. Теперь нужно провести тестирование."
                $ player_score += 15
                $ tasks_completed += 1
                jump test_phas
            else:
                "Что-то пошло не так, роботы остались агрессивными или начали вести себя непредсказуемо. Необходимо изменить код снова."
                jump code_phase
            
        label test_phas:
            "Фаза оценки и развертывание модели: наблюдайте за поведением роботов."
            
            if code_parameter == "0":
                "Роботы патрулируют лабораторию, не проявляя агрессии. Тест пройден!"
                $ player_score += 20
                $ test_result = "passed"
                $ tasks_completed += 1
                jump mini_game_end
            else:
                "Роботы атакуют все что движется, тест провален, надо попробовать снова."
                $ test_result = "failed"
                jump code_phase
                
        label mini_game_end:
            scene place_ii
            show vadim_def:
                xalign 0.3
                yalign 1.0
            with Dissolve(.5)

            show vanya_zaxv:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            if test_result == "passed":
                "Итоговый счет: [player_score] \nВы успешно изменили алгоритм поведения роботов!"
                Vadim "Молодец, у тебя отлично получается!"
                jump ii
            else:
                "Вы немножко не справились, но получен опыт, который пригодится в дальнейшем"
                jump ii    
            return

        label diz:
            play music stress fadein(2.0)
            $ renpy.music.set_volume(0.1)
            scene place_diz
            show noy_def_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            show pavla_def_sm_rev:
                xalign 0.75
                yalign 1.0
            with Dissolve(.5)
            show vanya_funny_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            show vadim_udivl_sm_rev:
                xalign 0.35
                yalign 1.0
            with Dissolve(.5)
            "В укрытии повстанцев мерцают экраны, а стены украшают яркие плакаты с лозунгами сопротивления. Ваня, Ной, Павла и Вадим работают над доработкой нового инфоплаката."
            hide noy_def_sm_rev
            show noy_angry_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Noy "Если мы сделаем этот плакат ярким и заметным, мы сможем привлечь внимание всего города!"
            hide noy_angry_sm_rev
            show noy_def_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Pavla "Это рискованно. Если враг заметит нас, это может обернуться худшими последствиями."

            Vadim "Но если мы не сделаем это, люди не узнают о нашей борьбе. Нам нужно вдохнуть надежду в их сердца"
            hide vanya_funny_sm_rev
            show vanya_def_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            Vanya "Мы можем использовать наши навыки, чтобы создать что-то, что они не забудут. Давайте зажжем искру надежды!"

            play music trevoga fadein(2.0)
            $ renpy.music.set_volume(0.1)

            "*В этот момент раздается тревожный сигнал*"
            Pavla "Они уже близко. Мы должны быстро закончить и спрятаться!"
            "Однако Ной, полный решимости, подбегает к двери, пытаясь увидеть, что происходит снаружи"
            hide noy_def_sm_rev with Dissolve(.5)

            Noy "Давайте сделаем это сейчас! Мы не можем допустить, чтобы они нас остановили!"
            "Он бросается наружу, чтобы продемонстрировать плакат, который только что закончил. Вадим пытается его остановить"
            stop music fadeout 3.0
            Vadim "Ной, вернись! Это слишком опасно!"
            play music stress fadein(2.0)
            $ renpy.music.set_volume(0.1)
            "Ной все еще выходит на улицу, поднимая плакат, когда вражеские солдаты разбивают двери укрытия и врываются внутрь. Команда понимает, что время истекло."
            Vanya "Бежим! Нам нужно уйти отсюда!"
            hide vanya_def_sm_rev with Dissolve(.5)
            hide vadim_udivl_sm_rev with Dissolve(.5)
            hide pavla_def_sm_rev with Dissolve(.5)

            Pavla "Ной! Уходи!"
            Noy "Вы не сможете заглушить наш голос! Мы будем бороться!"
            play sound strelba fadein(1.0)
            $ renpy.music.set_volume(0.1)
            "Они открывают огонь. Ной встает между врагами и Ваней, спасая её ценой своей жизни, и получает тяжелое ранение. Команда в ужасе смотрит на происходящее."
            stop sound fadeout 1.0
            play music stress fadein(2.0)
            $ renpy.music.set_volume(0.1)
            Vadim "Нет! Ной!"

            #сюда новый фон и Ноя валяющегося
            "Ной падает, поймав на себе огонь"
            Noy "Этот мир... он не может закончиться... Ваня… продолжай..."
            Vanya "Ты не должен был этого делать! Мы могли бы сбежать!"

            Pavla "Ты не можешь оставить нас! Мы не можем без тебя!"
            "Но Ной уходит, оставляя Ваню, Павлу и Вадима потрясенными. \n На улице начинается хаос, вражеские солдаты продолжают наступление."
            $ renpy.music.set_volume(0.2)
            "Ваня, полная решимости, встает, ее сердце полно ярости и решимости."

            Vanya "Мы сделаем это. Мы продолжим борьбу ради него! Никто не должен быть забытым! Я буду заниматься твоим делом!"
            "Они покидают укрытие, полные решимости отомстить за Ноя и продолжить его дело" 
            stop music fadeout 2.0
            #Музыка затихает, экраны мерцают, камеру медленно отдаляют, показывая их силу в момент горя и надежды."        
            jump final

        label ib:
            play music stress fadein(2.0)
            $ renpy.music.set_volume(0.1)
            scene place_ib
            show pavla_dumaet:
                xalign 0.4
                yalign 1.0
            with Dissolve(.5)
            scene place_diz
            show noy_def_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            show pavla_def_sm_rev:
                xalign 0.75
                yalign 1.0
            with Dissolve(.5)
            show vanya_funny_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            show vadim_udivl_sm_rev:
                xalign 0.35
                yalign 1.0
            with Dissolve(.5)
            "В укрытии повстанцев, освещенном тусклым светом, Ваня, Павла, Ной и Вадим работают над настройкой новых защитных систем для своих данных.
            \nНа экране появляются графики и коды, а в воздухе витает напряжение."
            Pavla "Мы должны запустить шифрование данных. Если враг получит доступ к нашей информации, это может стоить нам жизни."
            hide vanya_funny_sm_rev
            show vanya_def_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            Vanya "Я помогу с кодированием. Мы должны сделать это как можно быстрее."
            hide noy_def_sm_rev
            show noy_angry_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Noy "Но что, если нас поймают? Мы должны быть в безопасном месте, пока все это не завершится!"
            hide noy_angry_sm_rev
            show noy_def_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Vadim "Павла права. Нам нужно защитить нашу информацию и обеспечить безопасность нашей команды."
            "Вдруг на экране появляется тревожное сообщение. Камера запрашивает доступ к серверу, и появляются предупреждения о попытках взлома. Все резко останавливаются."
            hide pavla_def_sm_rev
            show pavla_dum_sm_rev:
                xalign 0.75
                yalign 1.0
            with Dissolve(.5)
            Pavla "Нет! Это атака! Враги пытаются прорваться в нашу систему!"
            "Павла быстро начинает нажимать кнопки, активируя защитные меры и шифрование, но враг все равно продолжает атаковать."

            hide pavla_dum_sm_rev
            show pavla_def_sm_rev:
                xalign 0.75
                yalign 1.0
            with Dissolve(.5)

            hide vanya_def_sm_rev
            show vanya_funny_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            Vanya "Что нам делать? Мы не сможем удержать их в одиночку!"

            Noy "Я отвлеку их! У них нет шансов, если я выйду наружу!"
            hide noy_def_sm_rev
            show noy_angry_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            "Павла смотрит на Ноя с ужасом"
            Pavla "Нет, Ной! Ты не можешь это сделать! Мы не можем потерять тебя!"
            Noy "Вы не понимаете. Если я смогу отвлечь их, вы получите время на установку защиты!"
            hide noy_angry_sm_rev
            show noy_def_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            pause(1.0)
            hide noy_def_sm_rev with Dissolve(.5)
            "Он выскальзывает в подворотню, привлекая внимание врагов своим криком и яркими движениями. Война на улице разгорается."
            "Пока Ной отвлекает врагов, Павла продолжает работу. Но враг начинает пробиваться внутри, и один из солдат проникает в укрытие."

            Pavla "Я не позволю вам добраться до наших данных!"
            hide pavla_def_sm_rev with Dissolve(.5)

            "В этот момент Павла бросается на врага, пытаясь защитить важные устройства, но в результате получает ранение."
            Vanya "Павла! Нет!"
            hide vanya_funny_sm_rev with Dissolve(.5)
            hide vadim_udivl_sm_rev with Dissolve(.5)
            "Ной, услышав крики, поворачивается, но уже слишком поздно"
            "Команда в панике пытается помочь Павле, но осознает, что ее ранения слишком тяжелы"
            Noy "Почему ты это сделала? Мы могли бы сбежать!"
            Pavla "Ваня… ты  должна продолжить бороться... защищай то, за что мы сражались..."
            "Последние слова Павлы звучат, и она закрывает глаза, оставляя команду охваченную горем."

            Vanya "Мы сделаем это, Павла. Мы не забудем твой подвиг. Я буду продолжать твое дело"
            stop music fadeout 2.0
            #Камера отдаляется, показывая, как они покидают укрытие, полные решимости отомстить за Павлу и продолжить борьбу с врагом. 
            #На фоне слышны звуки выстрелов и крики, отражающие их потерю и гнев."
            jump final

        label ii:
            play music stress fadein(2.0)
            $ renpy.music.set_volume(0.1)
            scene place_ii
            show noy_def_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            show pavla_def_sm_rev:
                xalign 0.75
                yalign 1.0
            with Dissolve(.5)
            show vanya_funny_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            show vadim_udivl_sm_rev:
                xalign 0.35
                yalign 1.0
            with Dissolve(.5)
            "В укрытии повстанцев мерцают экраны, а Ваня, Вадим, Ной и Павла работают над настройкой ИИ, который поможет проанализировать данные о перемещениях врага."
            hide vanya_funny_sm_rev
            show vanya_def_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            Vanya "Если мы сможем доработать алгоритмы для дронов, мы сможем заранее предсказать действия врага. Это должно помочь нам в атаке!"
            hide vanya_def_sm_rev
            show vanya_zaxv_sm:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)

            Vadim "Я почти закончил с обновлением. Давайте проверим все системы на случай, если нас попытаются атаковать."
            hide noy_def_sm_rev
            show noy_rad_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Noy "И пусть дроны делают красивую визуализацию при разведке! Это может поднять мораль!"
            hide noy_rad_sm_rev
            show noy_def_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Pavla "Но мы должны быть осторожны. Если враг узнает о нашем плане, мы окажемся в опасной ситуации."
            play music trevoga fadein(2.0)
            $ renpy.music.set_volume(0.1)
            #звук тревоги
            "Внезапно на экранах появляются сообщения о приближающейся вражеской группировке. Звучит тревога, и комната наполняется напряжением."
            hide pavla_def_sm_rev
            show pavla_dum_sm_rev:
                xalign 0.75
                yalign 1.0
            with Dissolve(.5)
            Pavla "Это атака! Они уже близко! Нам нужно активировать защитные системы и подготовиться!"
            "Вадим пытается запустить программу безопасности, но система начинает давать сбой."
            Vadim "Нет, не может быть! Они пытались взломать нашу сеть! Дроны! Где наши дроны?"
            play music stress fadein(2.0)
            $ renpy.music.set_volume(0.1)
            hide pavla_dum_sm_rev
            show pavla_def_sm_rev:
                xalign 0.75
                yalign 1.0
            with Dissolve(.5)
            hide vanya_zaxv_sm
            show vanya_funny_sm_rev:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            Vanya "Мы можем использовать дронов для отвлечения врага. Но нам нужно действовать быстро!"

            hide noy_def_sm_rev
            show noy_angry_sm_rev:
                xalign 0.6
                yalign 1.0
            with Dissolve(.5)
            Noy "Я отвлеку их! Если я смогу привлечь их внимание, вы получите время для работы!"
            hide noy_angry_sm_rev with Dissolve(.5)
            "Ной выскакивает из укрытия, начинает кричать и привлекает внимание вражеского патруля. В это время Ваня и Павла остаются внутри, настраивая защиту."
            Pavla "Ной, не стой на пути! Ты не сможешь с ними справиться!"
            "В это время в укрытие проникают вражеские солдаты, и Вадим понимает, что им нужно спешить."
            Vadim "Скорее! Я закрою задний выход, чтобы они не прорвались к вам!"
            hide vadim_udivl_sm_rev with Dissolve(.5)
            hide vanya_funny_sm_rev
            show vanya_zaxv_sm:
                xalign 0.15
                yalign 1.0
            with Dissolve(.5)
            Vanya "Вадим, нет! Это слишком опасно!"
            "Но он уже стремится к двери, быстро вводя команды"
            Noy "Вадим, уходи! Это ловушка!"
            stop music fadeout 1.0
            play sound strelba fadein(2.0)
            $ renpy.music.set_volume(0.3)
            "Но в этот момент Вадим получает ранение от вражеского огня"
            stop sound fadeout 1.0
            hide vanya_zaxv_sm with Dissolve(.5)
            hide pavla_def_sm_rev with Dissolve(.5)
            play music stress fadein(2.0)
            $ renpy.music.set_volume(0.1)
            Vanya "Нет! Вадим, пожалуйста, удержись! Мы не можем потерять тебя!"
            Pavla "Ты должен бороться! Мы справимся!"
            "Вадим, с трудом говорит Ване"
            Vadim "Ты должна... продолжать... бороться... я всегда буду помогать... Ваня.."
            "С этими словами Вадим уходит, оставляя Ваню и Павлу в полном шоке и горе."
            Noy "Нет! Мы это не можем допустить!"
            #звуки стрельбы
            play sound strelba fadein(2.0)
            $ renpy.music.set_volume(0.1)
            "Из укрытия доносятся звуки борьбы, и команда встает, полная решимости."
            Vanya "Мы отомстим за тебя, Вадим! Никто не забудет твой героизм! Я продолжу твое дело!"
            stop sound fadeout 1.0
            stop music fadeout 2.0
            jump final

        label final:
            play music fin fadein(2.0)
            $ renpy.music.set_volume(0.1)
            scene ship with Dissolve(.5)
            show vanya_def:
                xalign 0.5
                yalign 1.0
            with Dissolve(.5)
            Vanya "*мысленно* Я пришла сюда, чтобы сделать этот мир лучше"
            show vanya_zaxv:
                xalign 0.5
                yalign 1.0
            with Dissolve(.5)
            Vanya "Это только начало... я готова!"
            pause (2.0)
            scene black with Dissolve(.5)
            pause(1.0)
            "Конец... или, возможно, новый старт?..."
            stop music fadeout 5.0


            