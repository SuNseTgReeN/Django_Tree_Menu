from django.views.generic import ListView, DetailView
from menu.models import Menu


class MenuListView(ListView):
    model = Menu
    template_name = 'menu/menu_list.html'
    context_object_name = 'menu_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_menus'] = Menu.objects.filter(parent=None)
        return context


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/menu_detail.html'
    context_object_name = 'menu'
