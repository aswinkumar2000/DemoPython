
from django.urls import path
from . import views
app_name='todoapp'
urlpatterns = [
    path('',views.home,name='ahome'),
    # path('details', views.details,name='ere')
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name= 'home'),
    path('cbvdetail/<int:pk>/',views.Detailview.as_view(),name= 'cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Updateview.as_view(),name='edit'),
    path('cbvdelete/<int:pk>/',views.Deleteview.as_view(),name='cut'),


]