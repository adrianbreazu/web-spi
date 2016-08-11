from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Scheduler, Sprinkler
from django.core.urlresolvers import reverse
import sys, json

def index(request):
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
        raise render(request=request,
                     template_name='error.html',
                     context={"message": "This is the page you are looking for"})

    return render(request=request,
                  template_name="sprinkler/index.html",
                  context=context)


def submit(request):
    try:
        # STORE DATA INTO DATABASE
        print("message was submitted")
        pass
    except:
        return render(request=request,
                      template_name='error.html',
                      context={"message": "something when wrong"})

    return HttpResponseRedirect(reverse('sprinkler:index'))


def act(request, sprinkler_id):
    try:
        if request.method == 'POST' and request.is_ajax():
            print('RAW: %s' % request.body)
            data = json.loads(request.body.decode('utf-8'))
            #print('Data: %s' % data)

            #print('id: %s' % data['sprinkler']['id'])
            #print('status: %s' % data['sprinkler']['status'])
        else:
            return render(request=request,
                          template_name='error.html',
                          context={"message": "something with the sprinkler"})
    except:
        print(sys.exc_info()[0])
        return render(request=request,
                      template_name='sprinkler/error.html',
                      context={"message": "something with the sprinkler"})

    return HttpResponse(json.dumps(data),
                        content_type="application/json")