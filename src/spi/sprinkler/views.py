from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Scheduler, Sprinkler
from django.core.urlresolvers import reverse
import sys, json
from core import sprinkler as sprinkler

my_sprinkler = sprinkler.Sprinkler()


def __del__():
    my_sprinkler.__del__()


def index(request):
    try:
        # LOAD DATA FROM DATABASE
        scheduler = Scheduler.objects.get(pk=1)
        sprinkler_list = Sprinkler.objects.order_by('order')
        context = {
            "scheduler": scheduler,
            "sprinkler_list": sprinkler_list,
        }

        return render(request=request,
                      template_name="sprinkler/index.html",
                      context=context)
    except:
        print(sys.exc_info()[0])
        raise render(request=request,
                     template_name='sprinkler/error.html',
                     context={"message": "This is the page you are looking for"},
                     content_type="application/json")


def submit(request):
    try:
        print('RAW: %r' % request.body)
        data = json.loads(request.body.decode('utf-8'))

        # STORE DATA INTO DATABASE
        scheduler = Scheduler.objects.get(pk=1)
        scheduler.name = data['name']
        scheduler.start_time = data['start_time']
        scheduler.skip_days = data['skip']
        scheduler.days = data['days']
        scheduler.save()
        for sprinkler_object in data['sprinkler']:
            sprinkler_instance = Sprinkler.objects.get(pk=sprinkler_object['id'])
            sprinkler_instance.name = sprinkler_object['name']
            sprinkler_instance.duration = sprinkler_object['duration']
            sprinkler_instance.notes = sprinkler_object['notes']
            sprinkler_instance.save()


        # cron-tab code
        # restart script code

        return HttpResponseRedirect(reverse('sprinkler:index'))
    except Exception as e:
        message = "Something went wrong: " + e
        return render(request=request,
                      template_name='sprinkler/error.html',
                      context={"message": message})


def act(request, sprinkler_id):
    try:
        if request.method == 'POST' and request.is_ajax():
            print('RAW: %s' % request.body)
            data = json.loads(request.body.decode('utf-8'))

            sprinkler_id = int(data['sprinkler']['id'])
            sprinkler_table = Sprinkler.objects.get(pk=sprinkler_id)
            sprinkler_port = sprinkler_table.GPIO_pin
            print(sprinkler_port)
            my_sprinkler.init_GPIO(int(sprinkler_port), my_sprinkler.GPIO_TYPE["output"])
            print(0)
            if bool(data['sprinkler']['status']):
                print('activate sprinkler')
                my_sprinkler.activate(int(sprinkler_port))
            else:
                print('deactivate sprinkler')
                my_sprinkler.deactivate(int(sprinkler_port))
        else:
            return render(request=request,
                          template_name='sprinkler/error.html',
                          context={"message": "act request should be a POST request"})

        return HttpResponse(json.dumps(data),
                            content_type="application/json")
    except Exception as e:
        message = "Something went wrong: " + e
        return render(request=request,
                      template_name='sprinkler/error.html',
                      context={"message": message})


def error(request):
    return render(request=request,
                  template_name='sprinkler/error.html',
                  context={"message": "something went wrong"})
