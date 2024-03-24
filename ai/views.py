from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

import g4f
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
    content = "Задай семь смешных вопросов ребенку про него."
    # content = "Задай семь пошлых вопросов взрослому про него и перечисли их через точку с запятой."
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                provider='ChatgptNext',
                messages=[{"role": "user", "content": content}],
            )
            break
        except:
            pass
    questions = response.choices[0].message.content
    questions = questions.split('\n')
    questions = map(lambda q: q.strip(), questions)
    return render(request, context={'questions': questions}, template_name='ai/questions.html')


def story(request):
    if request.method == 'POST':
        answers = []
        for key, value in request.POST.items():
            if key == 'names':
                names = value
            if key != 'csrfmiddlewaretoken':
                answers.append(value.lower())
        content = f"Придумай смешной рассказ про {names} с фразами: {', '.join(answers)}"
        # content = f"Придумай пошлый ржачный рассказ про {names} с фразами: {', '.join(answers)}"
        client = Client()
        while True:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    provider='ChatgptNext',
                    messages=[{"role": "user", "content": content}],
                )
                break
            except:
                pass
        story = response.choices[0].message.content
        return render(request, context={'story': story}, template_name='ai/story.html')
    else:
        return render(request, context={'story': 'Test'}, template_name='ai/story.html')