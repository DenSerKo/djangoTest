from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

from g4f.client import Client


class IndexView(TemplateView):
    template_name = 'ai/index.html'


def detail(request, question_id):
    return HttpResponse(f'You are looking at question {question_id}.')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def chatgpt(request):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        provider='ChatgptNext',
        messages=[{"role": "user", "content": "Что вреднее кальян или сигареты?"}],
    )
    return JsonResponse({'message': response.choices[0].message.content})