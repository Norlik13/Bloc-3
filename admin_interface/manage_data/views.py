from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Item
from .forms import UserForm
from django.urls import reverse_lazy


#-----Gestion des éléments------
class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'manage_data/item_list.html'
    context_object_name = 'items'

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'manage_data/item_detail.html'
    context_object_name = 'item'

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'manage_data/item_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('item-list')

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = 'manage_data/item_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('item-list')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = 'manage_data/item_confirm_delete.html'
    success_url = reverse_lazy('item-list')


#------Gestion des utilisateurs------

class UserCreateView(UserPassesTestMixin, CreateView):
    model = User
    template_name = 'manage_data/user_form.html'
    fields = ['username', 'email', 'password', 'is_staff']
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)


    def test_func(self):
        return self.request.user.is_superuser

class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'manage_data/user_list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'manage_data/user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('user-list')

    def test_func(self):
        return self.request.user.is_superuser

class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'manage_data/user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def test_func(self):
        return self.request.user.is_superuser
