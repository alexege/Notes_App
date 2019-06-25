from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Note, Category
import bcrypt

#Landing Page - Localhost:8000
def index(request):
    print("[Localhost:8000/]---Index Page---")

    context = {
        'list_of_notes' : Note.objects.all(),
        'list_of_categories' : Category.objects.all(),
        # 'logged_in_user' : User.objects.
    }

    return render(request, "notes_app/dashboard.html", context)
 
#Add Note
def add_note(request):
    print("[Localhost:8000/add_note/]---Adding a note to Note database---")

    form_title = request.POST['note-title']
    form_category = request.POST['note-category']
    form_form = 1 #Not going to use this, will set it to default value of 1. Should remove completely, but will leave until later.
    form_content = request.POST['form-content']

    # Add note to db
    Note.objects.create(title=form_title, category=form_category, form=form_form, content=form_content)

    return redirect('/dashboard')

#Update Note
def update_note(request):
    print("[Localhost:8000/update_note/]---Updating a note in the Note database---")
    return redirect('/dashboard')

#Delete Note
def delete_note(request, id):
    print("[Localhost:8000/delete_note/]---Deleting a note in the Note database---")
    Category.objects.filter(id=id).delete()
    return redirect('/dashboard')

#New Category
def add_category(request):
    print("[Localhost:8000/add_category/]---Adding a category to Category database---")
    Category.objects.create(name=request.POST['category-name'])
    return redirect('/dashboard')

#Delete Category
def delete_category(request, id):
    print("[Localhost:8000/delete_category/]---Delete a category from Category database---")
    Category.objects.filter(id=id).delete()
    return redirect('/dashboard')

def delete_note(request, id):
    print("[Localhost:8000/delete_note/]---Delete a note from Note database---")
    Note.objects.filter(id=id).delete()
    return redirect('/dashboard')

def logout(request):
    print("[Localhost:8000/logout/]---Destroys session key ['active_user'] from session---")
    request.session.clear()
    return redirect('login_app/')