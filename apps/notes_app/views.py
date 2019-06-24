from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Note
import bcrypt

#Landing Page - Localhost:8000
def index(request):
    print("Hit the index. Rendering notes/app/dashboard.html")
    return render(request, "notes_app/dashboard.html")
 
def add_note(request):
    print("Hit the add_notes route. Rerouting to /dashboard")
    if request.method == 'POST':
        print("Add notes fired")
        print(request.POST['title'])
        # print(request.POST['note-title'])

        # form_title = request.POST['note-title']
        # form_category = request.POST['note-category']
        # form_form = request.POST['note-form']
        # form_content = request.POST['form-content']

        # Note.objects.create(title=form_title, category=form_category, form=form_form, content=form_content)
    return redirect('/dashboard')