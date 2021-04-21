## Структура проекта

@startuml

hide circle
' skinparam linetype ortho
top to bottom direction

rectangle "CoreshAPP" {
}
package "Утилиты" {

    ' Справочник - группы категорий проектов
    entity "1-1" {
    id : int
    }

    ' Справочник - группы категорий проектов
    entity "1-2" {
    id : int

}
' Справочник - группы категорий проектов
entity "1-3" {
id : int
--
name : string
sort : int
}

}

package "Вьюхи" {

    ' Справочник - группы категорий проектов
    entity "2-1" {
    id : int
    --
    name : string
    sort : int
    }

    entity "2-2" {
    id : int
    --
    name : string
    sort : int
    }
    entity "2-3" {
    id : int
    --
    name : string
    sort : int
    }

}

package "БД" {

' ## Пользователь ##
    entity "users" {
  
  ' id пользователя
    id : int
    --
  ' id в телеграме
    tg_unid : int
  ' логин в Телеграме
    tg_username : string
  ' общий рейтинг 
    overall_rating : int
  ' Позиция сприрта - группа.
    position_group : int
  ' Позиция спринта - шаг.
    position_step : int
  ' Позиция сприрта - повторение.
    position_repeat : int
  ' количество пройденных спринтов
    number_sprints : int
  ' количество сбросов аккаунта
    number_drops : int
  ' забанен
    ban : bool
  }


' ## Cобеседник ##
    entity "inters" {
  ' id собеседника пользователя
    id : int  
  ' id пользователя
    user_id : int
    --
  ' рейтинг соседства
    rating : int
  ' количество показов карточки за спринт. если меньше 1 - это вероятность
    number_cards : float
  ' является другом
    friend : bool
  ' забанен
    ban : bool
  }


' ## Карточки ##
    entity "cards" {
  ' id карточки
    id : int
  ' id языка карточк
    lang_id : int
    --
  ' контент в карточке
    content : json  
  ' тип карточки
    type : string
  
    }

' ## Спринты ##
    entity "sprints" {
  ' id спринта
    id : int
  ' id пользователя
    user_id : int
    --
  ' Содержимое спринта
    content : json  
  ' Пройден/ не пройден
    type : bool
  
    }

' ## Группа тегов
  entity "tags_groups" {
  ' id группы тегов
    id : int
    --
  ' название группы тегов       
    name : json
  ' выкл/вкл 
    available : bool
    }
  
  ' ## Теги ##
    entity "tags" {
  ' id тега
    id : int
  ' группа тегов
    tag_group : int
    --
  ' название тега         
    name : json
  
  ' например: слушаю, смотрю, поддерживаю (перевод)
    visible_name : int
  ' выкл/вкл 
    available : bool
    }

' ## Подписки пользователей по тегам ##
    entity "tags_subs" {
  ' id пользователя
    user_id : int
  ' id тега
    tag_id : int
    --
  ' рейтинг по тегу
    rating : int
  ' отображение тега у пользователя
    visible : bool 
  ' компетентность
    competence : bool 
    }

' ## Теги карточек ##
    entity "tags_cards" {
  ' id карточки
    card_id : int
  ' id тега
    tag_id : int
    --
    }

' ## Язык ##
    entity "langs" {
  ' id языка
    id : int
    --
  ' Переводы интерфейса на языки
    trans_interface : json
  ' Короткий код языка (en, us, ru, ...)
    code : string
    }

}

"CoreshAPP" -[hidden]-> "Утилиты"
"CoreshAPP" -[hidden]-> "Вьюхи"
"CoreshAPP" -[hidden]-> "БД"

"1-1" -d[hidden]-> "1-2"
"1-2" -d[hidden]-> "1-3"

"2-1" -d[hidden]-> "2-2"
"2-2" -d[hidden]-> "2-3"

users -d[hidden]-> inters
inters -d[hidden]-> cards
cards -d[hidden]-> sprints
sprints -d[hidden]-> tags_groups
tags_groups -d[hidden]-> tags
tags -d[hidden]-> tags_subs
tags_subs -d[hidden]-> tags_cards
tags_cards -d[hidden]-> langs


inters::user_id -[#blue]-> users::id
tags::tag_group -[#blue]-> tags_groups::id
tags_cards::card_id -[#blue]-> cards::id
tags_cards::tag_id -[#blue]-> tags::id
tags_subs::tag_id -[#blue]-> tags::id
cards::lang_id -[#blue]-> langs::id
tags_subs::user_id -[#blue]-> users::id
sprints::user_id -[#blue]-> users::id

@enduml
users -d[hidden]-> inters
inters -d[hidden]-> cards
cards -d[hidden]-> tags_groups
tags_groups -d[hidden]-> tags
tags -d[hidden]-> tags_subs
tags_subs -d[hidden]-> tags_cards

tags_cards -d[hidden]-> langs

## Сущности БД
tags::tag_group -[#blue]-> tags_groups::id
_Значения указываются в файлах переводах_

**Пользователь**

- Айди в системе : число
- Айди в Телеграме : число
- Логин в Телеграме : кор.текст
- Общий рейтинг : число
- последний пройденный спринт : дата/время
- Количество пройденных спринтов : число
- Количество сбросов аккаунта : число
- Забанен : булев

**Собеседник**

- Айди пользователя : Число
- Айди собеседника : Число
- Рейтинг собеседника : Число
- Является другом : булев
- Забанен : булев
  в

**Теги**

- Айди : число
- Группа тегов : число -> Группа тегов / Айди (текст берётся сразу из переводов)
- Айди ответа "практикую", "поддерживаю" итд - число (текст берётся сразу из переводов)
- вкл/выкл : булев

**Подписки пользователей по тегам**

- Айди пользователя : число
- Айди тега : число
- Рейтинг : число
- Интерес: булев
- Позитивный (активный) интерес : булев
- Компетентность : булев
- вкл/выкл : булев



**Карточки**

- Айди карточки
- Тип карточки
- Язык карточки

**Карточки**

- Айди карточки
- Тип карточки
- Язык карточки

**Язык**

- Айди : Число
- Короткий код языка : кор.текст, 2 символа

- **main.py** - точка входа
- **config.py** - страница с объявлением необходимых переменных
- **pages/** - вьюхи страниц бота
  --- **sprint.py** - основной интерфейс карусельки спринта
  --- **sprint_my_question_1.py** - тип карточки "мой вопрос", первый экран - выбор тега
  --- **sprint_my_question_2.py** - тип карточки "мой вопрос", второй экран - написать вопрос
  --- **sprint_my_answer.py** - тип карточки "мой ответ"
  --- **sprint_like.py** - тип карточки "оценить ответы пользователей"
  --- **sprint_info.py** - тип карточки "информация для пользователя"
  --- **settings.py** - страница настроек пользователя
  --- **friends.py** - страница со списком друзей пользователя
- **helpers/** - папка с дополнительными классами, с которыми работают основные файлы
  --- **lang_card.py** - возвращает язык карточки вопроса или ответа
  --- **lang_ui.py** - возвращает передов интерфейса на язык пользователя
- **langs/** - файлы с переводами
  --- **en.json** - английский язык
  --- ............. - другие языки
  --- **ru.json** - русский язык
