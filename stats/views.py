from django.shortcuts import render


def main(request):
    return render(request, 'stats/main.html', {})


def dashboard(request, slug):
    return render(request, 'stats/dashboard.html', {})
