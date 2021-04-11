@startuml

hide circle
' skinparam linetype ortho

package "Проект" {

    ' Справочник - группы категорий проектов
    entity "projects_directories_categories_groups" {
    id : int
    --
    name : string
    sort : int
    }

    ' Справочник - категории проектов
    entity "projects_directories_categories" {
    id : int
    --
    name : string
    sort : int
    group_id : int
    }

    ' Справочник - типов внешних ссылки проектов
    entity "projects_directories_types_links" {
    id : int
    --
    avatar_url : string
    name : string
    }

    ' Основная информация о проекте
    entity "projects" {
    id : int
    --
    name : string
    category_id : int
    avatar_url : int
    description : text
    creator_id: int
    chat_id : int
    sort : int
    }

    ' Кураторы страниц
    entity "projects_curators" {
    curator_id : int
    project_id : int
    description : text
    sort : int
    }

    ' Внешние ссылки проектов
    entity "projects_links" {
    id : int
    --
    description : string
    url : string
    project_id: int
    type_id: int
    sort: int
    }

    ' Лог дискрипшена проекта
    entity "projects_logs_descriptions" {
    id : int
    --
    point : text
    date: timestamp
    editor_id: int
    }

}

package "Участники" {

    ' Справочник - компетенции для задач и пользователей
    entity "users_directories_skills" {
    id : int
    --
    name : string
    sort: int
    }

    ' Справочник - ранги пользователей
    entity "users_directories_ranges" {
    id : int
    --
    name : string
    sort: int
    }

    ' Основные данные пользователей
    entity "users" {
    id : int
    --
    login : string
    password_hash : string
    full_name : string
    date_registration : timestamp
    avatar : string
    invite_id : int
    email : string
    telegram : string
    about: text
    settings: json
    sort : int
    activity : boolean
    delite : boolean
    }

    ' Сиписок компетенций пользователей
    entity "users_skills" {
    user_id : int
    skill_id : int
    }

    ' Список званий пользователей
    entity "users_ranges" {
    user_id : int
    rang_id : int
    }

}

package "Инвайты" {

    ' Инвайт
    entity "invites" {
    id : int
    --
    uuid : uuid
    total : int
    balance : int
    comment : string
    create_time : timestamp
    creator_id : int
    activity : boolean
    }

    ' Лог регистраций по инвайту
    entity "invites_logs_regs" {
    id : int
    --
    create_time : timestamp
    editor_id : int
    invite_id : int
    }

    ' Лог редактирования значений в инвайтах
    entity "invites_logs_changes" {
    id : int
    --
    change_time : timestamp
    editor_id : int
    invite_id : int
    point_uuid : uuid
    point_total : int
    point_balance : int
    point_comment : string
    }

    }

package "Оборот средств" {

    ' Справочник - цели сборов
    entity "donations_directories_targets" {
    id : int
    --
    name : string
    }

    ' Пожертвования
    entity "donations" {
    id : int
    --
    create_time : timestamp
    target_id: int
    user_id : int
    comment : string
    sum : int
    }

}

package "Другое" {

    ' Переменные (например, текст страницы abaut)
    entity "vars" {
    id : int
    --
    name : string
    text : string
    }

    ' История изменения переменных
    entity "vars_logs" {
    id : int
    --
    vars_id : int
    create_time : timestamp
    editor_id : int
    point : string
    }

}

projects::category_id --> projects_directories_categories::id
projects::creator_id --> users::id
projects_directories_categories::project_category_group_id --> projects_directories_categories_groups::id
projects_links::project_id --> projects::id
projects_links::project_directory_type_id --> projects_directories_types_links::id
projects_curators::curator_id --> users::id
projects_curators::project_id --> projects::id
projects_logs_descriptions::editor_id --> users::id

users::invite_id --> invites::id
users_skills::user_id --> users::id
users_skills::skill_id--> users_directories_skills::id
users_ranges::user_id --> users::id
users_ranges::rang_id --> users_directories_ranges::id

invites::creator_id --> users::id
invites_logs_regs::user_id --> users::id
invites_logs_regs::invite_id --> invites::id
invites_logs_changes::editor_id --> users::id
invites_logs_changes::invite_id --> invites::id

donations::target_id --> donations_directories_targets::id
donations::user_id --> users::id

vars_logs::var_id --> vars::id
vars_logs::editor_id --> users::id
@enduml
