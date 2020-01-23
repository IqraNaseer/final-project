from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Test,result_db
import json
from django.http import JsonResponse
from django.core import serializers
import requests



   


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': 1
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'



def test_page(request, myid):
    q = Test.objects.all()
    question = Test.objects.filter(id=myid)
    length = len(q)
    return render(request,'General_knowledge.html', { 'Test':question,'length': length})  


 


# def nextpage(request, myid):
#     quet = Test.objects.filter(id=myid)
#     return render(request,'page1.html', {"Test": questions, 'quet': quet})





def result(request):
    res = result_db()
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Test.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
                print(score)
    #     # print(qid)
    #     # print(qans)
    #     # print(ans)
    #     # print(score, request.user.id)
    #    # eff = (score / total) * 100
    #     print(eff, score)
    #     res = result_db()
    #     res.res_user = request.user
    #     res.score = score
    #     res.eff = eff
    #     res.save()
    return render(request, 'result.html', {'score': score, 'total': total})


@login_required
def profile(request):
    return render(request, 'profile.html')