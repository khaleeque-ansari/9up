import json
import pprint

from django.http import HttpResponse
from quiz.models import Quiz
from .models import User
from random import shuffle
from multichoice.models import MCQuestion, Answer


def index(request):
    data = {
        'some_var_1': 'foo',
        'some_var_2': 'bar',
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def first_time(request):
    categories = Quiz.objects.all()
    to_return_categories = []

    for category in categories:
        to_return_item = {'id': category.id, 'name': category.title}
        to_return_categories.append(to_return_item)

    user = User.create('Khaleeque Ansari')
    user.save()

    data = {
        'user_id': user.pk,
        'categories': to_return_categories
    }

    return HttpResponse(json.dumps(data), content_type="application/json")


def get_questions(request, user_id=None):
    print "User ID : ", user_id

    category_id = request.GET.get('category', '1')
    print "Category : ", category_id

    category = Quiz.objects.get(pk=category_id)
    questions = category.get_questions()

    to_return_arr = []
    for question in questions:
        to_return_item = {'question': question.content}
        if question.figure:
            to_return_item['figure'] = {'url': request.META['HTTP_HOST'] + question.figure.url, 'exists': True}
        else:
            to_return_item['figure'] = {'url': None, 'exists': False}
        answers = question.get_answers()
        answers = [{'content': answer.content, 'correct': answer.correct} for answer in answers]
        to_return_item['answers'] = answers
        to_return_arr.append(to_return_item)
    print "Hello"
    print request.META['HTTP_HOST']
    print "Bello"
    print request.build_absolute_uri()
    pp = pprint.PrettyPrinter(indent=4)
    print pp.pprint(to_return_arr)
    shuffle(to_return_arr)
    to_return_arr = to_return_arr[:9]
    data = {'data': to_return_arr}

    return HttpResponse(json.dumps(data), content_type="application/json")


def score_submission(request, user_id=None):
    # This code was written while I was high,
    # please excuse if any mistakes found
    print "User ID : ", user_id

    email = request.GET.get('email', 'default@default.com')
    print "Email : ", email

    mobile = request.GET.get('mobile', '9999999999')
    print "Mobile : ", mobile

    score = request.GET.get('score', 0)
    print "Score : ", score

    user = User.objects.get(pk=user_id)
    user.email = email
    user.mobile = mobile
    user.score = score
    user.save()
    data = {'response': 'sucessfull'}

    return HttpResponse(json.dumps(data), content_type="application/json")


def get_ad_url(request, user_id=None):

    data = {'url': 'https://www.youtube.com/watch?v=GGFMRGhy96U'}
    return HttpResponse(json.dumps(data), content_type="application/json")


def test(request):

    category_id = 1
    category = Quiz.objects.get(pk=category_id)
    questions = category.get_questions()

    to_return_arr = []
    for question in questions:
        to_return_item = {}
        to_return_item['question'] = question.content
        answers = question.get_answers()
        answers = [{'content': answer.content, 'correct': answer.correct} for answer in answers]
        to_return_item['answers'] = answers
        to_return_arr.append(to_return_item)
    pp = pprint.PrettyPrinter(indent=4)
    print pp.pprint(to_return_arr)
    data = {'data':to_return_arr}

    return HttpResponse(json.dumps(data), content_type="application/json")
