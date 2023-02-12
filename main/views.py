from django.shortcuts import render


def index(request):
    # if request.user.is_authenticated:
    #     pass
    #
    # events = Article.objects.filter(div_code=0)
    #
    # context = {
    #     'events': events,
    #     'news': {},
    # }

    return render(request, 'index.html', {})


def contacts(request):
    # if request.user.is_authenticated:
    #     pass
    #
    # events = Article.objects.filter(div_code=0)
    #
    # context = {
    #     'events': events,
    #     'news': {},
    # }

    return render(request, 'contacts.html', {})
