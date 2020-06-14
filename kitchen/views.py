from django.shortcuts import render, get_object_or_404
from .models import Menu, Choice

def choice_list(request, menu_slug=None):
    menu = None
    menus = Menu.objects.all()
    wide_choice = Choice.objects.filter(available=True)
    if menu_slug:
        menu = get_object_or_404(Menu, slug=menu_slug)
        wide_choice = wide_choice.filter(menu=menu)
    return render(request, 'kitchen/choice/list.html', {'menu': menu, 'menus': menus, 'wide_choice': wide_choice})

def choice_detail(request, id, slug):
    choice = get_object_or_404(Choice, id=id, slug=slug, available=True)
    return render(request,
                  'kitchen/choice/detail.html',
                  {'choice': choice})