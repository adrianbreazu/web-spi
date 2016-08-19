from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Scheduler, Sprinkler
from django.core.urlresolvers import reverse
import sys, json, logging, datetime
from core import sprinkler as sprinkler

my_sprinkler = sprinkler.Sprinkler()
logger = logging.getLogger(__name__)

def __del__():
    my_sprinkler.__del__()


def index(request):
    logger.debug('beginning views.index with request: {0}'.format(request))
    try:
        scheduler = Scheduler.objects.get(pk=1)
        sprinkler_list = Sprinkler.objects.order_by('order')
        context = {
            "scheduler": scheduler,
            "sprinkler_list": sprinkler_list,
        }
        logger.info('views.index context: {0}'.format(context))
        return render(request=request,
                      template_name="sprinkler/index.html",
                      context=context)
    except Exception as e:
        logger.error("views.index exception: {0}".format(e))
        return render(request=request,
                     template_name='sprinkler/error.html',
                     context={"message": "This is not the page you are looking for"},
                     content_type="application/json")
    finally:
        logger.debug('end views.index with request: {0}'.format(request))


def submit(request):
    logger.debug('beginning views.submit with request: {0}'.format(request.body.decode('utf-8')))
    try:
        data = json.loads(request.body.decode('utf-8'))

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
        logger.debug('views.submit data saved')

        # cron-tab code
        # restart script code
        # to do

        return HttpResponseRedirect(reverse('sprinkler:index'))
    except Exception as e:
        logger.error("views.index exception: {0}".format(e))
        return render(request=request,
                      template_name='sprinkler/error.html',
                      context={"message": e})
    finally:
        logger.debug('end views.submit')


def act(request, sprinkler_id):
    logger.debug('beginning views.act for sprinkler_id: {0} with request: {1}'.format(sprinkler_id,
                                                                                      request.body.decode('utf-8')))

    try:
        if request.method == 'POST' and request.is_ajax():
            logger.info('RAW POST request : {0}'.format(request.body))
            data = json.loads(request.body.decode('utf-8'))

            sprinkler_id = int(data['sprinkler']['id'])
            sprinkler_table = Sprinkler.objects.get(pk=sprinkler_id)
            sprinkler_port = sprinkler_table.GPIO_pin
            logger.debug('sprinkler port: {0}'.format(sprinkler_port))
            my_sprinkler.init_GPIO(int(sprinkler_port), my_sprinkler.GPIO_TYPE["output"])
            if bool(data['sprinkler']['status']):
                logger.debug('activate sprinkler : {0}'.format(sprinkler_id))
                my_sprinkler.activate(int(sprinkler_port))
            else:
                logger.debug('deactivate sprinkler : {0}'.format(sprinkler_id))
                my_sprinkler.deactivate(int(sprinkler_port))
        else:
            logger.warning('a non POST request was made for sprinkler : {0} with request {1}'.format(sprinkler_id,
                                                                                                     request.body.decode('utf-8')))
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
    finally:
        logger.debug('end views.act for sprinkler_id: {0} with request: {1}'.format(sprinkler_id,
                                                                                    request.body.decode('utf-8')))


def error(request):
    logger.debug('views.error with request: {0}'.format(request))
    return render(request=request,
                  template_name='sprinkler/error.html',
                  context={"message": "something went wrong"})
