# Исправления электронного дневника

Проект предназначен для работы с базой данных школьного электронного [дневника](https://github.com/devmanorg/e-diary).

### Список скриптов

1. `fix_marks(child_name)` - исправляет все отрицательный оценки ученика на пятерки.
2. `remove_chastisements(child_name)` - удаляет все замечания ученика.
3. `create_commendation(child_name, subject_name)` - добавляет похвалу ученику на последнем уроке выбранного предмета.

### Как использовать

1. Скопировтать файл `scripts.py` в папку проекта (рядом с `manage.py`)
2. Подключиться к базе данных школьного дневника в режиме `shell`:
```
python manage.py shell
```
3. Импортировать скрипты
```
import scripts
```
4. Выполнить требуемый скрипт
```
scripts.script_name(first_argument, second_argument, ...)
```
### Аргументы скриптов

1. `child_name` - ФИО ученика с заглавных букв.
2. `subject_name` - название предмета как в расписании, первая буква - заглавная.

**Например:**
```
scripts.fix_marks('Иванов Петр Кузьмич')
scripts.remove_chastisements('Иванов Петр Кузьмич')
scripts.create_commendation('Иванов Петр Кузьмич', 'Музыка')
```
Возможно использование только фамилии и имени ученика вместо ФИО, однако, если в школе учатся два ученика с одинаковыми ФИ, используйте полное ФИО, иначе скрипт выведет ошибку:
```
scripts.fix_marks('Иванов Петр')
...
datacenter.models.Schoolkid.MultipleObjectsReturned: get() returned more than one Schoolkid -- it returned 2!
```

При введении имени с ошибкой или несуществующего имени скрипт выведет ошибку:
```
scripts.remove_chastisements('Иванов Петя')
...
datacenter.models.Schoolkid.DoesNotExist: Schoolkid matching query does not exist.
```
Аналогично и с названием предмета.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
