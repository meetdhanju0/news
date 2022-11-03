from django.urls import path
from .views import *
# Create your tests here.

urlpatterns = [
    path('add-reporter', AddReporter.as_view(), name='add_reporter'),
    path('reporter-list', ReporterList.as_view(), name='reporter_list'),
    path('add-article', AddArticle.as_view(), name='add_article'),
    path('article-list', ArticleList.as_view(), name='article_list'),


    path('Edit/<int:id>', Editreporter.as_view(), name='Edit'), 
    path('Delete/<int:id>', Deletereporter.as_view(), name='Delete'), 



    path('edit/<int:id>', EditArticle.as_view(), name='edit'), 
    path('delete/<int:id>', DeleteArticle.as_view(), name='delete'), 


     path('status/<int:id>', ArticleStatus.as_view(), name='status'),


    path('Edit-profile', EditProfile.as_view(), name='Edit_profile'), 

    path('add-home', AddHome.as_view(), name='add_home'),
    path('add-student', AddStudent.as_view(), name='add_student'),


]