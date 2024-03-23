from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
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


def questions(request):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        provider='ChatgptNext',
        messages=[{"role": "user", "content": "Задай пять вопросов ребенку и перечисли их через точку с запятой."}],
    )
    questions = response.choices[0].message.content.split(';')
    return render(request, context={'questions': questions}, template_name='ai/questions.html')


def story(request):
    if request.method == 'POST':
        answers = []
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                answers.append(value)
        content = f"Придумай смешную историю со словами {', '.join(answers)}, Милослава"
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            provider='ChatgptNext',
            messages=[{"role": "user", "content": content}],
        )
        story = response.choices[0].message.content
        return render(request, context={'story': story}, template_name='ai/story.html')