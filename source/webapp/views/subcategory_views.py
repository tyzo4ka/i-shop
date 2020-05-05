from django.contrib.auth.mixins import UserPassesTestMixin
from webapp.models import SubCategory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.shortcuts import render


# class SubCategoryListView(UserPassesTestMixin, ListView):
#     template_name = 'categories.html'
#     model = SubCategory
#     context_object_name = 'subcategories'
#     page_kwarg = 'page'
#
#     def test_func(self):
#         user = self.request.user
#         return user.is_staff
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data()
#         return context


class SubCategoryCreateView(UserPassesTestMixin, CreateView):
    model = SubCategory
    template_name = 'add.html'
    fields = ['category', 'sub_name']

    def test_func(self):
        user = self.request.user
        return user.is_staff

    def form_valid(self, form):
        subname = form.cleaned_data['sub_name']
        category = form.cleaned_data['category']
        if SubCategory.objects.filter(sub_name=subname.capitalize()):
            messages.error(self.request, 'Подраздел с таким названием уже существует!')
            return render(self.request, 'add.html', {})
        else:
            subcategory = SubCategory(sub_name=subname.capitalize(), category=category)
            subcategory.save()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('webapp:categories_list')


class SubCategoryUpdateView(UserPassesTestMixin, UpdateView):
    model = SubCategory
    template_name = 'edit.html'
    fields = ['category', 'sub_name']

    def test_func(self):
        user = self.request.user
        return user.is_staff

    def form_valid(self, form):
        text = form.cleaned_data['category_name']
        if SubCategory.objects.filter(sub_name=text.capitalize()):
            messages.error(self.request, 'Подраздел с таким названием уже существует!')
            return render(self.request, 'edit.html', {})
        else:
            pk = self.kwargs.get('pk')
            subcategory = get_object_or_404(SubCategory, id=pk)
            subcategory.sub_name = text.capitalize()
            subcategory.save()
        return self.get_success_url()

    def get_success_url(self):
        return redirect('webapp:categories_list')


class SubCategoryDeleteView(UserPassesTestMixin, DeleteView):
    model = SubCategory
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:categories_list')
    permission_required = "webapp.delete_subcategory"
    permission_denied_message = "Доступ запрещен"

    def test_func(self):
        user = self.request.user
        return user.is_staff
