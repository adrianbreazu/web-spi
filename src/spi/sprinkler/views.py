from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Scheduler, Sprinkler
from django.core.urlresolvers import reverse
import sys


def index(request):
    print("aaa")
    try:
        # LOAD DATA FROM DATABASE
        scheduler = Scheduler.objects.get(pk=1)
        sprinkler_list = Sprinkler.objects.order_by('order')
        context = {
            "scheduler": scheduler,
            "sprinkler_list": sprinkler_list,
        }
    except:
        print(sys.exc_info()[0])
        raise render(request=request, template_name='error.html',context={"message": "This is the page you are looking for"})
    return render(request=request, template_name="sprinkler/index.html", context=context)


def submit(request):
    print("message was submitted")
    try:
        # STORE DATA INTO DATABASE
        pass
    except:
        print(sys.exc_info()[0])
        return render(request=request, template_name='error.html',context={"message": "something when wrong"})
    return HttpResponseRedirect(reverse('sprinkler:index'))


def act(request, sprinkler_id):
    print("ACT !!!")
    print(sprinkler_id)
    try:
        pass
    except:
        print(sys.exc_info()[0])
        return render(request=request, template_name='error.html',context={"message": "something with the sprinkler"})
    return HttpResponseRedirect(reverse('sprinkler:index'))