from datacenter.models import Schoolkid
from datacenter.models import Subject
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
import random
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned


COMMENDATIONS = [
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
	'Теперь у тебя точно все получится!'
		]

def get_student(schoolkid):
	try:
		child = Schoolkid.objects.get(full_name__contains=schoolkid)
	except Schoolkid.DoesNotExist:
		print("Такого имени не существует")
	except Schoolkid.MultipleObjectsReturned:
		print('Найдено больше 1 совпадений')
	return child


def fix_marks(schoolkid):
	Mark.objects.filter(schoolkid=get_student(schoolkid),points__lt=4).update(points=5)



def remove_chastisements(schoolkid):
		chastisements =  Chastisement.objects.filter(schoolkid=get_student(schoolkid))
		chastisements.delete()


def create_commendation(schoolkid, subject):
	try:
		child = get_student(schoolkid)
		lesson = Lesson.objects.filter(group_letter=child.group_letter,year_of_study=child.year_of_study,subject__title=subject).order_by(?).first()
		positive_comment = Commendation.objects.create(text=random.choice(COMMENDATIONS),created=lesson.date,schoolkid=child,subject=lesson.subject,teacher=lesson.teacher)
	except Lesson.DoesNotExist:
		print("Такого предмета не существует")
	return positive_comment


