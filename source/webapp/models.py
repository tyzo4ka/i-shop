# from django.contrib.auth.models import User
from django.db import models

# PROJECT_STATUS = [('active', 'Active'), ('closed', 'Closed')]


class Category(models.Model):
    category_name = models.CharField(max_length=20, verbose_name='Категория')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Товар')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT,
                                verbose_name='Категория')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(verbose_name='В наличии', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# class Project(models.Model):
#     name = models.CharField(max_length=50, verbose_name='Project')
#     description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')
#     project_status = models.CharField(max_length=20, default=PROJECT_STATUS[0][0], verbose_name='Project status', choices=PROJECT_STATUS)

#     def __str__(self):
#         return self.name


# class Task(models.Model):
#     summary = models.CharField(max_length=100, verbose_name="Summary")
#     description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description")
#     status = models.ForeignKey(Status, related_name='tasks', on_delete=models.PROTECT, verbose_name='Status')
#     type = models.ForeignKey(Type, related_name='tasks', on_delete=models.PROTECT, verbose_name='Type')
#     project = models.ForeignKey(Project, null=True, related_name='tasks', on_delete=models.PROTECT,verbose_name='Project')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated date')
#     created_by = models.ForeignKey(User, null=True, blank=True, related_name='task_created_by', on_delete=models.CASCADE, verbose_name='Created by')
#     assigned_to = models.ForeignKey(User, null=True, blank=True, related_name='task_assigned_to', on_delete=models.CASCADE, verbose_name='Assigned to')

#     def __str__(self):
#         return self.summary


# class Team(models.Model):
#     user = models.ForeignKey(User, related_name='user_team', on_delete=models.PROTECT, verbose_name='User')
#     project = models.ForeignKey(Project, related_name='project_team', on_delete=models.PROTECT, verbose_name='Project')
#     start = models.DateField(null=True, blank=True, verbose_name='Start')
#     end = models.DateField(null=True, blank=True, verbose_name='End')

#     def __str__(self):
#         return '{}, {}'.format(self.user, self.project)