"""todo URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from main.views import main, create, delete, test, edit, tasks, is_done_view

urlpatterns = [
    path("", main,name='main'),
    path("create/", create, name='create'),
    path('test/<int:pk>', test, name = 'test'),
    path('delete/<int:pk>', delete, name='delete'),
    path('edit/<int:pk>', edit, name='edit'),
    path('tasks/', tasks, name="tasks"),
    path('done/<int:pk>', is_done_view, name="done"),
]

