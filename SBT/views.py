from django.shortcuts import render
from SBT.models import User, Expenses
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse

def login(request):
    return render(request, "login.html")

@csrf_protect
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('data')
        print(email)
    else:
        return render(request, "signup.html")


def expense(request):
    return render(request, "expense.html")


def index(request):
    data = User.objects.all()
    print(data)
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def project(request):
    return render(request, "project.html")



def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")

def feature(request):
    return render(request, "feature.html")

def team(request):
    return render(request, "team.html")

def testimonial(request):
    return render(request, "testimonial.html")

def policy(request):
    return render(request, "service.html")


def career(request):
    return render(request, "service.html")


def tnc(request):
    return render(request, "service.html")


def base(request):
    return render(request, "base.html")


def chart(request):
    return render(request, "chart.html")