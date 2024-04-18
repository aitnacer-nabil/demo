from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CostumeLoginView, CostumeRegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CostumeLoginView.as_view(), name='login'),
    path('register/', CostumeRegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]