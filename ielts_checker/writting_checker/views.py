from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import WrittingForm
from .get_result import get_writting_result
from .models import UserWrittings

# Create your views here.
def writting_checker(request):
    form = WrittingForm()

    if request.method == 'POST':
        form = WrittingForm(data=request.POST)
        if form.is_valid():
            task = request.POST.get('task')
            writting = request.POST.get('writting')
            print(task, writting)
            result = get_writting_result(task, writting)

            # Save the user's writting + result to the database
            UserWrittings.objects.create(user_name=request.user, task=task, writting=writting, score = result['score'], feed_back = result['feed_back'])

            context = {'form': form, 'result': result}
            return render(request, 'writting_checker.html', context)
        
    return render(request, 'writting_checker.html', {'form': form})

@login_required(login_url='user-login')
def writting_history(request):
    current_user = request.user
    print(current_user)
    
    user_data = UserWrittings.objects.filter(user_name=current_user)
    
    return render(request, 'writting_history.html', {'user_data': user_data})


