from django.shortcuts import render
from .forms import PredictionForm
from .utils import predict_values, get_default_values, get_input_features
import matplotlib.pyplot as plt
import io
import base64
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required



@login_required
def predict_view(request):
    result = profit = actual = None

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            auto1 = cleaned.pop('autofill', False)
            auto2 = cleaned.pop('autofill2', False)
            example1, example2 = get_default_values()
            features = get_input_features()

            # Select based on autofill flags
            if auto1:
                user_input = dict(zip(features, example1))
            elif auto2:
                user_input = dict(zip(features, example2))
            else:
                user_input = {f: cleaned[f] for f in features}

            result, profit, actual = predict_values(user_input)

            # Convert to native Python types for JSON safety
            result = [float(x) for x in result]
            profit = float(profit)
            if actual:
                actual = [float(x) for x in actual]
                form = PredictionForm(initial=user_input)
                form.fields['autofill'].initial = auto1
                form.fields['autofill2'].initial = auto2
    else:
        form = PredictionForm()

    return render(request, 'dashboard/predict.html', {
        'form': form,
        'result': result,
        'profit': profit,
        'actual': actual,
        'labels': ['CK Density', 'CGO Density', 'CFO Density', 'CGO RCR']
    })


from django.shortcuts import render

def home_view(request):
    return render(request, 'dashboard/home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('predict')
    else:
        form = RegisterForm()
    return render(request, 'dashboard/register.html', {'form': form})
