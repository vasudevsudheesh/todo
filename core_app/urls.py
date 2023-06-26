from . import views
from django.urls import path
# from .views import login_view
# from django.contrib.auth import views as auth_views
# from .views import add_todo, todo_list

app_name = "core_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("base/", views.base, name="base"),
    path('delete<int:task_id>/', views.delete, name='delete'),
    path('update<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TaskListview.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskDetailview.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),
    # path('movie/<int:movie_id>',views.movie_detail,name='movie_detail'),
]

