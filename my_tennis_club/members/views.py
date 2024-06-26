from django.template import loader
from django.http import HttpResponse
from .models import Member


def members(request):
    mymembers = Member.objects.all()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers
    }
    return HttpResponse(template.render(context=context, request=request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember
    }
    return HttpResponse(template.render(context=context, request=request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
