from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


# Question一覧画面へ
def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    text = { "latest_question_list": latest_question_list }
    return render(request, "./polls/index.html", text)


# Questionの投票画面へ
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        text = {"question": question}
    except Question.DoesNotExist:
        raise Http404("Questionが存在しません。")
    return render(request, "./polls/detail.html", text)


# 投票処理→resultsにリダイレクト
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "選択してください。",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


# 投票結果の画面へ
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
