from django.shortcuts import render, get_object_or_404
import logging, sys

from .models import Pull

def index(request):
    context = {
        'pull_list': Pull.objects.all()
    }
    return render(request, 'pulls/index.html', context)
    
def detail(request, pull_id):
    pull = get_object_or_404(Pull, pk=pull_id)
    classes_list = []
    
    for klass in pull.classes.all():
        # classes_list[klass.name] = klass.entry_set.filter(pull=pull)
        classes_list.append({ 'class': klass, 'entries': klass.entry_set.filter(pull=pull)})
        
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    logging.debug(len(classes_list))
        
    return render(request, 'pulls/detail.html', {'pull': pull, 'classes_list': classes_list})