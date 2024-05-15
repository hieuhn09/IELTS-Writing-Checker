from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.core.paginator import Paginator

from .forms import WrittingForm
from .get_result import get_writting_result
from .models import UserWrittings
from user_auth.models import UserProfile

def home_page(request):
    form = WrittingForm()
    if request.user.is_authenticated and not hasattr(request.user, 'userprofile'):
        UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = WrittingForm(data=request.POST)
        if form.is_valid():
            task = request.POST.get('task')
            writting = request.POST.get('writting')
            # Store task and writting in the session
            request.session['task'] = task
            request.session['writting'] = writting
            request.session['new'] = True

            return redirect('writting-result')
        
    return render(request, 'home_page.html', {'form': form})

def result(request):
    # Get task and writting from the session
    task = request.session.get('task')
    writting = request.session.get('writting')
    result = get_writting_result(task, writting)

    if request.session.get('new'):
        # Save to database
        user_writting = UserWrittings(
            user_name=request.user,
            task=task,
            writting=writting,
            score=result['score'],
            feed_back=result['feed_back'],
            public_status=False 
        )

        user_writting.save()
    context = {'result': result, 'task': task, 'writting': writting}
    return render(request, 'writting_result.html', context)

def public_writting(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        writting = request.POST.get('writting')
        # Store task and writting in the session
        request.session['task'] = task
        request.session['writting'] = writting
        request.session['new'] = False

        return redirect('writting-result')
    else:
        # public_writtings = UserWrittings.objects.filter(public_status=True)
        p = Paginator(UserWrittings.objects.filter(public_status=True), 6)
        page = request.GET.get('page')
        public_writtings = p.get_page(page)

        print(public_writtings)
        return render(request, 'public_writting.html', {'public_writtings': public_writtings})

@login_required(login_url='user-login')
def writting_history(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        writting = request.POST.get('writting')
        # Store task and writting in the session
        request.session['task'] = task
        request.session['writting'] = writting
        request.session['new'] = False

        return redirect('writting-result')
    else:
        current_user = request.user

        user_data = UserWrittings.objects.filter(user_name=current_user)
        return render(request, 'writting_history.html', {'user_data': user_data})

def toggle_public(request):
    if request.method == 'POST':
        writting_id = request.POST.get('id')
        writting = UserWrittings.objects.get(id=writting_id)
        writting.public_status = not writting.public_status
        writting.save()
        return redirect('writting-history')
    else:
        return HttpResponseBadRequest("This URL only supports POST requests")
