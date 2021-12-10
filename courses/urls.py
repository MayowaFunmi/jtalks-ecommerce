from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('', views.course_list, name='course_list'),
    #path('<slug:slug>/', views.course_list, name='course_list_by_category'),
    path('<int:id>/<slug:slug>/', views.course_detail, name='course_detail'),
    path('save_review/', views.SaveReview.as_view(), name='save_review'),
    path('load_more_review/', views.load_more_review, name='load_more_review'),
    path('create_user_library/', views.UserCourse.as_view(), name='user_library'),
    path('user_library/', views.user_library, name='user_library')
]