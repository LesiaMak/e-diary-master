from datacenter.models import Schoolkid
from datacenter.models import Subject
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Commendation
import random
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned


list_of_commendations = [
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


def fix_marks(schoolkid):	
	try:
		child = Schoolkid.objects.get(full_name__contains=schoolkid)
		Mark.objects.filter(schoolkid=child,points__lt=4).update(points=5)
	except Schoolkid.DoesNotExist:
		print("Такого имени не существует")
	except Schoolkid.MultipleObjectsReturned:
		print('Найдено больше 1 совпадений')
    	


def remove_chastisements(schoolkid):
	try:
		child = Schoolkid.objects.get(full_name__contains=schoolkid)
		chastisements =  Chastisement.objects.filter(schoolkid=child)
		chastisements.delete()
	except Schoolkid.DoesNotExist:
		print("Такого имени не существует")
	except Schoolkid.MultipleObjectsReturned:
		print('Найдено больше 1 совпадений')


	


def create_commendation(schoolkid, subject):
	try:
		child = Schoolkid.objects.get(full_name__contains=schoolkid)
		full_list = Lesson.objects.filter(group_letter=child.group_letter,year_of_study=child.year_of_study,subject__title=subject)
		number = random.randint(0, full_list.count())
		date  = full_list[number].date
		subject_title = full_list[number].subject
		teacher = full_list[number].teacher
		commendation = list_of_commendations[random.randint(0, len(list_of_commendations))]
		positive_comment = Commendation.objects.create(text=commendation,created=date,schoolkid=child,subject=subject_title,teacher=teacher)
	except Schoolkid.DoesNotExist:
		print("Такого имени не существует")
	except Schoolkid.MultipleObjectsReturned:
		print('Найдено больше 1 совпадений в имени ученика')
	except Lesson.DoesNotExist:
		print("Такого предмета не существует")
	return positive_comment


