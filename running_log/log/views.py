# Create your views here.

from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .forms import ActivityForm, UserForm
from .models import Users, Activity
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render_to_response('log/logout.html')

def register(request):
    context = RequestContext(request)

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'log/registration.html',
            {'user_form': user_form, 'registered': registered},
            context)


def home_page(request):
    activities = Activity.objects.all()
    return render(request, 'log/home_page.html', {'activities': activities})

def activity_list(request):
    users = Users.objects.all()
    return render(request, 'log/activity_list.html', {'users': users})

@login_required(login_url="/login/")
def new_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.name = request.user
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = ActivityForm()
    return render(request, 'log/activity_edit.html', {'form': form})

def index(request):
    output = ', '.join([p.name for p in Users.objects.all()])
    return HttpResponse(output)
