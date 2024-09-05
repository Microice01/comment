from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Note
import json

def get_notes(request):
    notes = Note.objects.all()
    if request.method == 'POST':
        content = request.POST['content']
        new_note = Note(content=content)
        new_note.save()
        return redirect('home')
    return render(request, 'index.html', {'notes': notes})


