from django.shortcuts import render
import random





def home(request):
    choices = (random.randint(1,10))
    # global choices
    print(choices)
    if request.method == 'POST':
        guess = int(request.POST['guess'])

        if guess == choices:
            message = f'Congratulation! You guessed the number.'
            return render(request,'result.html',{'message':message})
        elif guess > choices:
            message = f'This number is too heigh.'
        else:
            message = f'This number is too small.'
        return render(request,'index.html',{'message':message})
    else:
        return render(request,'index.html')

# Create your views here.