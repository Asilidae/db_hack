import random
from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid


def fix_marks(child_name):
    """Исправление плохих оценок на 5"""
    child = get_schoolkid_object(child_name)
    Mark.objects.filter(schoolkid=child, points__lt=4).update(points=5)


def remove_chastisements(child_name):
    """Удаление замечаний"""
    child = get_schoolkid_object(child_name)
    Chastisement.objects.filter(schoolkid=child).delete()


def create_commendation(child_name, subject_name):
    """Создание похвального отзыва"""
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!',
    ]
    child = get_schoolkid_object(child_name)
    last_lesson = Lesson.objects.filter(subject__title=subject_name,
                                        subject__year_of_study=child.year_of_study).order_by('-date')[0]
    Commendation.objects.create(
        text=random.choice(commendations),
        created=last_lesson.date,
        schoolkid=child,
        subject=last_lesson.subject,
        teacher=last_lesson.teacher
    )


def get_schoolkid_object(child_name):
    """Взятие объекта отдельного ученика"""
    try:
	child = Schoolkid.objects.get(full_name__contains=child_name)
	return child_info
    
    except Schoolkid.DoesNotExist:
	print('Такого ученика нет. Введите фамилию и имя полностью.')
	
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько учеников по вашему запросу. Уточните запрос')
