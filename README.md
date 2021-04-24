# Coresh #

_Данный текст является черновиком. С радостью выслушаем ваши замечания. Контакты кураторов внизу._

**Сервис для поиска друзей на базе телеграм-бота. Помогает найти единомышленников задавая вопросы сообществу, а так же отвечая на вопросы и оценивая ответы других пользователей.**

Пользователь получает с паузой в сутки набор карточек для взаимодействия с сообществом, который называется спринтом. С помощью карточек задаются вопросы сообществу, даются ответы на вопросы других юзеров и оцениваются их мысли, что формирует связи для алгоритмов рекомендаций. После прохождения спринта пользователь может посмотреть историю активности лучшего по мнению алгоритма потенциального друга, а так же пользователей для которых он сам стал лучшей парой, если такие есть. При взаимной симпатии - система позволяет обменяться контактами.
<!-- asas -->
Платформа выбирает интересных для пользователя людей с помощью рейтинга соседства. В алгоритме рекомендаций учитывается совместимость по типажу, который определяется на основе опросника пройденного пользоватем после регистрации, лайков мыслей других юзеров, общим подпискам на теги и прочим весам (см. описание алгоритмов ниже). Сервис не учитывает пол, возраст и другие анкетные данные не связанные с качествами личности. Платформа имеет открытый исходный код, средства на содержание и разработку собираются с помощью пожертвований, данные пользователей никак не используются в коммерческих целях.

Цель алгоритмов сервиса - быстро поместить пользователя в среду с потенциально самыми близкими по духу людьми, дать шанс быстро стать популярными в своей среде, быстро убирать из общего вывода пользователей, которые не нравятся основной массе сообщества, формируя отдельный мир аутсайдеров внутри платформы.

---
## Ссылки ##
---

- [Рабочий чат](https://t.me/joinchat/EyxWDelw7VKZPTuO)
- [Figma-макеты](https://www.figma.com/file/NlikNEJQHliYlxI3MHhiSW/Share?node-id=9566%3A8798)
- [Схемы проекта](README-files/map.drawio)
- [Семантическая структура](README-files/semantic-list.md)
- [Идеи для проекта](README-files/ideas.md)

**Кураторы проекта**
- [t.me/grandcore](https://t.me/grandcore)
- [t.me/Mechislav](https://t.me/Mechislav)

---
## Вводная информация ##
---
### Основные термины ###

**Пользователь:** человек зарегистрированный в системе. Может так же называться участником и юзером.

**Сообщество:** все прользователи платформы

**Собеседник:** высшая категория для друга и соседа.

**Соседи:** потенциальные собеседники, которые автоматически добавляются в список соседей в случае совпадения типажа или лайка их карточки. Соседи имеют рейтинг соседства. Пользователи с самым высоким рейтингом соседства после каждого спринта взаимно предлагаются друг-другу стать друзьями. Пользователь может заблокировать.

**Друзья:** собеседники, которые были предложены системой как потенциальные друзья и были взаимно одобрены обеими сторонами. Друзья могут смотреть ленты активности друг-друга, так же им доступны ссылки на их личные аккаунты в Телеграме. 

**Языки:** доступные в сообществе языки. Пользователи могут выбирать языки которыми они владеют. Система автоматически определяет язык карточек и показывает их тем юзерам, которые владеют этими языками. 

**Карточка:** интерфейс позволяющий написать вопрос и дать ответ на вопросы сообщества, оценить ответы других пользователей, а так же, например, пройти опросник на определение знания языков, типажа и интересов пользователя и т.д. Является частью спринта. В таблице юзера текущая карточка хранится в трёх ячейках, которые формируют число типа "1.2.5", где первый блок цифр - группа карточек, второй - номер самой карточки в группе, третий - счётчик показа одной и той же карточки, там где это нужно. Каждая карточка основана на базовом классе, например, "вопрос" и дополнена параметрами для формирования карточки для конкретного шага.   

**Спринт:** генерируемый алгоритмами рекомендаций персональный набор карточек для пользователя. В конце каждого спринта пользователю предлагаются новые друзья - собеседник имеющий самый высокий рейтинг соседства и юзеры, если они имеются, для которых пользователь сам является соседом с самым высоким рейтингом соседства. Далее, перед началом нового спринта пользователь должен подождать 24 часа. Позиция спринта представляется в формате "этап.шаг.повтор_шага", например "2.3.4".

**Этап (Спринта):** спринт группируется на этапы, данная сущность создана для удобства и не несёт в себе дополнительного смысла. 

**Шаг (Этапа Спринта):** сформированная карточка на основе базового класса (вопрос, ответ итд) с определёнными переданными параметрами.

**Типаж:** Типажи созданы как один из коэффициентов для алгоритмов рекомендаций. Они не связаны с какими-то интересами или убеждениями пользователей, но помогают находить более комфортных по общему бэкграунду людей, что особенно полезно для новых пользователей. В базе представляются в виде кодов. "0" - код для "не важно". Для остальных - "1", "2" итд. Т.е., чтобы попасть в соседи по типажу нужно совпонедение "1/1" или "1(2,3...)/0", но никак не "1/2". Текущий список вопросов для определения типажей см. [здесь](README-files/semantic-list.md).

**Теги:** интересы, жизненные взгляды, темы для обсуждения и прочее. Пользователь должен указать своё отношение к каждому тегу в процессе прохождения спринта. Ответы на теги являются важным критерием в формировании спринта. Отношение к тегу имеют три градации: "не интересно" - вопросы по тегу не отображаются, "интересуюсь" - низкий приоритет показа карточек, "занимаюсь/поддерживаю/итд" - высокий приоритет показа карточек и повышенный рейтинг соседства для собеседников, которые указали этот же тег. Текущий набор тегов вы можете увидеть [здесь](README-files/semantic-list.md).


---
### Веса для алгоритмов ###

_Переменные от значений которых зависит работа алгоритмов_

- **Рейтинг Пользователя** : у каждого юзера есть личный рейтинг. Он существует параллельно с рейтингом вопросов и ответов. Например, пользователь лайкнул чей-то ответ и рейтинг добавится не только карточке, но и собеседнику. Если рейтинг станет отрицательным, пользователь сможет общаться только с другими юзерами, которые так же имеют отрицательный рейтинг. Пользователям с положительным рейтингом так же не доступны карточки собеседников с отрицательным рейтингом.
- **Глобальный рейтинг Тега** : рейтинг тега равен количеству вопросов по нему. 
- **Глобальный рейтинг Вопроса** : увеличивается при ответе на него, а уменьшается, если пользователь указал, вопрос ему не нравится. 
- **Глобальный рейтинг Ответа** : увеличивается - если пользователь лайкнул ответ, уменьшается - если нажал кнопку "далее", или заблокировал автора вопроса.  
- **Личный рейтинг Соседства** : собеседники, которые были добавлены после прохождения теста на определения типажа, а так же юзеры карточки которых пользователь хоть раз лайкнул - добавляются в список соседей и в дальшейшем, лайкая или дислайкая их карточки, изменяется рейтинг соседства.

---
## Базовые экраны и классы ##

---
### Точка входа ###

После запуска бота - система проверяет существует ли пользователь. Если нет - в базу записываются его данные и время регистрации, после проверки он перекидывается на главный экран. Если пользователь забанен - выводится сообщение "Вам здесь не рады". Модифицируется время последнего запуска бота пользователем.

---
### Главный экран ###

Проверяется статус спринта. Проверяется шаг спринта, если шаг 0.0, проверяется время и если прошли 1 сутки, шаг меняется на 1.1 или передаётся оставшееся время до возможности начать новый сринт. 

На экране расположены 3 кнопки.
- Кнопка "Запустить спринт" - вызывает базовый класс спринт-роутера. Если шаг 0.0 - отображается оставшееся время до возможности начать спринт.
- Кнопка "Настройки" - переход в "раздел настроек".
- Кнопка "Мои Друзья" - переход в "раздел Друзей".

---

### Раздел Друзей ###

Проверяется список друзей пользователя. Если друзей нет - выводится сообщение "Вы пока что не нашли друзей".

Если друзья есть - выводится список друзей в формате - Имя / кликабельный юзернейм / кнопка "Лента" / кнопка "Удалить". 

При нажатии на кнопку "Лента" - выводятся последний ответ или ворос пользователя. Ниже - кнопки ">>" и "<<" 

Нажав на кнопку "Удалить" - пользователю предлагается подтвердить своё желание. Пользователи взаимно больше не будут пересекаться на платформе и иметь доступ к профилям друг-друга. 

---
### Раздел Настроек ###

На странице присутствует 2 кнопки. "Удалить Аккаунт", "Обнулить аккаунт".

"Обнулить аккаунт" - появляется экран с предложением "Подтвердить обнуление". После подтверждения - сбрсываются теги и ответы на опрос по типажу, а так же языки пользователя. Это позволит заново ответить на все вопросы в ходе спринтов.  

"Удалить Аккаунт" - появляется экран с предложением "Подтвердить удаление". После подтверждения - в таблице юзера добавляетсявлаг true в поле delete. 

---
## Экраны и алгоритмы карусели ##
---

Ниже описываются классы и их экземпляры связанные непосредственно со сринтом

### Спринт-Роутер ###

При запуске спринт обращается к этому классу. Проверяется текущий шаг пользователя и в зависимости от шага запускается класс нужной карточки с необходимыми параметрами. После завершения шага - в таблице юзера обновляется значение поля с текушим шагом и класс роутера запускает следующий шаг, либо, при необходимости повторяет текущий.

### Базовые классы Карточек ###

**Ожидание:** проверяется, прошли ли сутки с последнего завершенного спринта. Если нет - выводится сообщение "Вы сможете начать новый сринт через n часов n минут". 

**Вилка спринта:** сопоставляется общее количество ответов пользователя по профилю (языки, типаж, теги) и текущее общее количество вопросов для заполнения профиля в системе. В зависимости от результата выбирается следующий шаг для спринта.

**Выбор языков:** возвращается язык, который пользователь ещё не указал. Возвращается карточка с двумя вариантами ответа - "знаю/не знаю". 

**Опрос на типаж:** возвращается вопрос на типаж, который пользователь ещё не указал. Возвращаются варианты ответа для конкретной карточки.

**Подписка на теги:** возвращается тег, который пользователь ещё не выбрал. Возвращается карточка с тремя вариантами ответа - "интересно/не интересно/хорошо разбираюсь".

**Вопрос от Пользователя для Участников Сообщества:** возвращаются группы тегов, после выбора группы тегов возвращаются теги группы. После выбора тега возвращается приглашение к вводу вопроса и кнопка выбора тега, которая возвращает пользователя к выбору групы тега.

TODO сделать группу тегов в базе

**Вопрос от Сообщества для Пользователя:** возвращается самый ролевантный для пользователя вопрос. Веса для алгоритма указываются в экземпляре класса в роутере.

**Оценка Пользователем ответа Участника Сообщества:** возвращается самый ролевантный для пользователя ответ участника сообщества. Веса для алгоритма указываются в экземпляре класса в роутере.

**Инфрмационная Карточка:** возвращается случайная из списка информационная карточка на языке интерфейса пользователя.

**Лучший для пользователя сосед:** возвращается юзер с самым высоким для пользователя рейтингом соседства. Возвращается карточка с его последним  вопросом или ответом. Ниже карточки пагинация вида "<<" ">>". Ниже две кнопки - "предложить дружбу" и "заблокировать". Если выбрать "заблокировать" - выводится подтверждение.   

**Юзеры для которых пользователь лучший сосед:** проверяется, есть ли юзер для которого пользователь является лучшим соседом. Если нет - меняется шаг и возвращается в роутер. Если есть - возвращается карточка с его последним  вопросом или ответом. Ниже карточки пагинация вида "<<" ">>". Ниже две кнопки - "предложить дружбу" и "заблокировать". Если выбрать "заблокировать" - выводится подтверждение. 

---
### Этап 0 (основные вопросы Пользователю) ###

---
**Шаг 0.0** 


- После первого запуска бота или после сбрВопрос от Пользователя для Сообществаоса аккаунта каждый пользователь должен пройти первичный опрос, который определит его первичные рекомендации. С точки зрения дазы данных это точно такой же спринт который хранится в таблице "sprints" в формате json. Создаются карточки, где пользователь должен ответить на вопросы относительно языка интерфейса и языков карточки на которых он хочет видеть. Также проходится опрос, по которому будет определён его типаж, после чего показываются 15 самых популярных тегов, на которые предлагается подписаться пользователю.  
- Для новых и сброшенный аккаунтов всегда вначале показываются карточки с выбором языков, которыми владеет пользователь и карточки теста на определение типажа что бы с самого начала более-менее рассадить людей "по жанрам". В случае если появятся новые языки или вопросы по определению типажа они добавляются в следующие спринты для всех пользователей.
- предложение подписаться на интересные теги. Так как тегов много - ставится лимит на 5 тегов за спринт. Для каждого тега пользователь может указать - интересно/не интересно. Если не интересно - карточки по этому тегу не будут показываться. И если интересно - так же пользователь может указать что он компетентен в этой области. Пользователи компетентные в одной области будут иметь больший приоритет в выводе карточек друг-другу.
- Языки
- Типажи
- Теги
---

### Этап 1 (Вопрос от Пользователя для Участников Сообщества) ###

**Шаг 1.1**




- предложение задать 1 вопрос сообществу. Пользователь выбирает тег и пишет по нему сообщение. Система автоматически выбирает язык, что бы показывать его только пользователям кто им владеет.

---
**Шаг 1.2**
TODO


---

### Этап 2 (Вопросы от Сообщества для Пользователя) ###

**Шаг 2.1**
TODO
- 5 самых релевантных по мнению алгоритмов вопросов, от других пользователей по тегам на которые он подписан, которые будут оценивать другие юзеры. 
- 5 вопросов на которые должен ответить пользователь. Сначала выводится вопрос и просьба его оценить. Если пользователь выбирает "плохой вопрос", ему показывается следующий вопрос для текущих правил, а карточка получает -1 в свой рейтинг.
- 1 вопрос : самый новый вопрос по тегам пользователя, у которого рейтинг 0 или больше. 
- 1 вопрос : самый популярный по тегам на которые подписан пользователь.
- 3-5 вопрос : по одному самому популярному ещё не отвеченому вопросу от трёх собеседников с самым высоким рейтингом соседства. 
- самый новый вопрос 3-ёх соседей с самым 
-         
- если не набирается 5 вопросов
- Пользователь может нажать "плохой вопрос", тогда е
Шестой вопрос задаётся с вероятностью 10 процентов. В отличии от остальных вопросов - 
- выбирается собеседник с самым высоким рейтингом показов (см. ниже) и рейтингом соседства как второй фильтр, выбирается  
- показывает 5 самых релевантных по мнению алгоритмов вопросов пользователю, которые будут оценивать другие юзеры. Они так же автоматически переводятся. 

---
### Этап 3 (оценка Пользователем ответов Участников Сообщества) ###

TODO
- 25 ответов на вопросы других юзеров, которые система считает самыми релевантными для оценки пользователем. Их можно лайкнуть, дизлайкнуть, а так же заблокировать и пожаловаться.
- 25 ответов на вопросы других юзеров, которые система считает самыми релевантными для оценки пользователем. Их можно лайкнуть, дизлайкнуть, а так же заблокировать и пожаловаться.
- сделать 2 сущность для количества карточек одно пользователя в спринте независимо от рейтинга соседства. Задача - что бы пользователь не отправил в бан человека, с которым он категорически не согласен по одном/двум вопросам. 

---
### Этап 4 (инфрмационная Карточка) ###

TODO

- информационная карточка добавленная админом, например, с просьбой пожертвовать денег на основном для пользователя языке. Если админ добавил несколько карточек - выбирается случайная.
- - информационная карточка добавленная админом, например, с просьбой пожертвовать денег. Если админ добавил несколько карточек - выбирается случайная.


---
### Этап 5 (предлагаемые Друзья) ###

TODO
- выводится история вопросов и ответов соседа с самым высоким рейтингом соседства и юзеров для которых пользователь сам стал соседом с самым высоким рейтингом, если они есть. Просмотрев вопросы и ответы каждого потенциального друга, пользователь может предложить дружбу, если это будет взаимно - они добавятся друг-другу в друзья и получат доступ к контактам друг-друга. В дальнейшем карточки вопросов и ответов друзей больше не появляются в спринтах, но пользователь всегда может посмотреть их, зайдя в раздел друзей и выбрав необходимый профиль.
- 
---  

**Шаг 5.2-n**

TODO  
- (другие соседи)


---
## Классы-хелперы ##
---
### Формирование списка Соседей ###

Каждый пользователь после прохождения теста на типаж получает в соседи группу юзеров. Если у пользователей будет хотя бы один противоположный ответ - соседство по типажу не состоится. Для каждого соседа по типажу формируется рейтинг соседства. Те вопросы, у которых ответ одинаковый, например, оба юзера предпочитают общаться только на "Вы" - добавляют рейтингу соседства 1 балл, если хотя бы у одного из юзеров на вопрос ответ нейтральный, например, один предпочитает общаться только на "Вы", а другой указал что может подстроиться под собеседника - балл соседству не добавляется. Соседу по типажу новый пользователь так же добавляется в соседи вместе с рейтингом соседства.

---
### Определение языка ###
[TODO](
- Система автоматически определит язык карточек с помощью специального хелпера. 

