from django.contrib import admin
from django.urls import path,include
from  .views import week,week_uz,week_en,week_ru
urlpatterns = [
    # izoh: url weekday yozuvisiz jadvalni ko'ra olasiz bo'lmasa not found berar edi uz variantini
    #  ko'rmoqchi bo'lsangiz weekday/uz, weekday/ru , weekday/en
    path('weekday',week,name='week'),
    path('',week,name='week'),
    path('weekday/uz',week_uz,name='week_uz'),
    path('weekday/en',week_en,name='week_en'),
    path('weekday/ru',week_ru,name='week_ru')


]
