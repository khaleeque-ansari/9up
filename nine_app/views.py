import json
import pprint

from django.http import HttpResponse
from quiz.models import Quiz
from multichoice.models import MCQuestion, Answer


def index(request):
    data = {
        'some_var_1': 'foo',
        'some_var_2': 'bar',
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def first_time(request):
    data = {
        'user_id': '1',
        'categories': [
            {
                'id': '1',
                'name': 'Politics'
            },
            {
                'id': '2',
                'name': 'Politics'
            },
            {
                'id': '3',
                'name': 'Politics'
            },
            {
                'id': '4',
                'name': 'Politics'
            },
            {
                'id': '5',
                'name': 'Politics'
            },
            {
                'id': '6',
                'name': 'Politics'
            },
            {
                'id': '7',
                'name': 'Politics'
            },
            {
                'id': '8',
                'name': 'Politics'
            },
            {
                'id': '9',
                'name': 'Politics'
            },

        ]
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_questions(request, user_id=None):
    print "User ID : ", user_id

    data = {
        'some_var_1': 'foo',
        'some_var_2': 'bar',
    }
    category = request.GET.get('category', '1')
    print "Category : ", category

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
    data = {'data': to_return_arr}

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
