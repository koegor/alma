from django.shortcuts import render, redirect
from main.models import Inst, Specialty, Property


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


def spec(request):
    # if request.user.is_authenticated:
    #     pass
    #
    # events = Article.objects.filter(div_code=0)
    #
    # context = {
    #     'events': events,
    #     'news': {},
    # }

    specs = Specialty.objects.all().values()

    return render(request, 'special.html', {'specs': specs})


def quest(request):
    # if request.user.is_authenticated:
    #     pass
    #
    # events = Article.objects.filter(div_code=0)
    #
    # context = {
    #     'events': events,
    #     'news': {},
    # }

    resp_id = request.POST.get('optradio')
    quest_num = request.POST.get('quest_num')

    if quest_num is None:
        return redirect('/spec')

    quest_num = int(quest_num)
    if quest_num == -1:
        request.session['spec'] = resp_id

    else:
        request.session['quest_%s' % quest_num] = resp_id

    quest = Property.objects.filter(num__gt=quest_num).order_by('num').first()
    if not quest:
        return redirect('/result')
    else:
        return render(request, 'quest.html', {'quest': quest})


def result(request):
    # if request.user.is_authenticated:
    #     pass
    #
    # events = Article.objects.filter(div_code=0)
    #
    # context = {
    #     'events': events,
    #     'news': {},
    # }

    spec = request.session.get('spec')
    insts = Specialty.objects.filter(id=int(spec)).select_related('inst_set').filter(inst__isnull=False).values_list('inst__name', 'inst__short_name', 'inst__url', named=True)

    return render(request, 'result.html', {'insts': insts})


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
