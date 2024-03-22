from django.http import HttpResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'ai/index.html'


def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}.')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)