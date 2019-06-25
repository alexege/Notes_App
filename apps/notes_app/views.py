from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Note
import bcrypt

#Landing Page - Localhost:8000
def index(request):
    print("[Localhost:8000/]---Index Page---")

    context = {
        'list_of_notes' : Note.objects.all(),
    }

    return render(request, "notes_app/dashboard.html", context)
 
def add_note(request):
    print("[Localhost:8000/add_note/]---Adding a note to Note database---")

    form_title = request.POST['note-title']
    form_category = request.POST['note-category']
    form_form = 1 #Not going to use this, will set it to default value of 1. Should remove completely, but will leave until later.
    form_content = request.POST['form-content']

    # Add note to db
    Note.objects.create(title=form_title, category=form_category, form=form_form, content=form_content)

    return redirect('/dashboard')