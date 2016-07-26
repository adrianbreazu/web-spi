from django.shortcuts import render
from django.http import Http404
from .models import Scheduler,Sprinkler

# Create your views here.
def index(request):
    try:
        scheduler = Scheduler.objects.get(pk=1)
        sprinkler_list = Sprinkler.objects.order_by('order')
        context = {
            "scheduler": scheduler,
            "sprinkler_list": sprinkler_list,
        }
    except:
        raise Http404("This is the page you are looking for")
    return render(request=request, template_name="sprinkler/index.html", context=context)