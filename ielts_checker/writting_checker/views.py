from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import WrittingForm
from .get_result import get_writting_result
from .models import UserWrittings

def home_page(request):
    form = WrittingForm()

    if request.method == 'POST':
        form = WrittingForm(data=request.POST)
        if form.is_valid():
            task = request.POST.get('task')
            writting = request.POST.get('writting')
            # Store task and writting in the session
            request.session['task'] = task
            request.session['writting'] = writting

            return redirect('writting-result')
        
    return render(request, 'home_page.html', {'form': form})

def result(request):

    # Get task and writting from the session
    task = request.session.get('task')
    writting = request.session.get('writting')
    print(task, writting)
    result = get_writting_result(task, writting)

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
    return render(request, 'public_writting.html')

@login_required(login_url='user-login')
def writting_history(request):
    current_user = request.user

    user_data = UserWrittings.objects.filter(user_name=current_user)
    print(user_data)
    return render(request, 'writting_history.html', {'user_data': user_data})

