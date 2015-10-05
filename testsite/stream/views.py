from django.shortcuts import render

from models import Stream

def stream(request):
    return render(request, 'stream.html',
                  {'stream': Stream.objects.all()})
