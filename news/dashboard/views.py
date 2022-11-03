# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.contrib.auth import login, authenticate, logout
import json
from django.contrib.auth.mixins import LoginRequiredMixin


class AddReporter(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "add_reporter.html"

    def get(self, request):
        active_reporter = 'active'
        active_add = 'active'
        return render(request, self.template_name, locals())

    def post(self, request):
        response = {}
        Username = request.POST.get('Username')
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('Email')
        passwor = request.POST.get('password')
        try:
            filter_user = User.objects.get(username = Username)
            response['status'] = False
            response['msg'] = 'username already exists.'

        except User.DoesNotExist:
            student = User.objects.create(
                username = Username,
                first_name = first,
                last_name = last,
                email = email
                )
            student.set_password(passwor)
            student.save()
            response['status'] = True
            response['msg'] = 'Reporter Successfully added.'

        return HttpResponse(json.dumps(response), content_type = 'application/json')


class ReporterList(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "reporter_list.html"

    def get(self, request):
        active_reporter = 'active'
        active_list = 'active'
        reporter = User.objects.filter(is_superuser = False)

        return render(request, self.template_name, locals())



class Editreporter(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "edit_reporter.html"
    
    def get(self, request, id):
        Grades = User.objects.get(id=id)
        return render(request, self.template_name, locals())

    
    def post(self, request, id):
        Users = request.POST.get('Username')
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('Email')
       

        Grades = User.objects.get(id=id)
        Grades.username = Users
        Grades.first_name = first
        Grades.last_name = last
        Grades.email = email
        Grades.save()
        return HttpResponseRedirect(reverse('reporter_list'))




class Deletereporter(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "reporter_list.html"
    
    def get(self, request, id):
        Grades = User.objects.get(id=id)
        Grades.delete()
        return HttpResponseRedirect(reverse('reporter_list'))




class AddArticle(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "add_article.html"

    def get(self, request):
        active_article = 'active'
        active_Add = 'active'
        return render(request, self.template_name, locals())

    def post(self, request):
        headline = request.POST.get('headline')
        pub_date = request.POST.get('pub_date')
        discription = request.POST.get('description')
        img = request.FILES.get('img')

        try:
            article = Article.objects.create(
                headline = headline,
                pub_date = pub_date,
                user = request.user,
                discription = discription 
                )
            if img:
                article.image = img
                article.save()
            messages.success(request, 'Reporter Successfully added.')
        except Exception as e:
            messages.error(request, str(e))
 
        return HttpResponseRedirect(reverse('add_article'))



class ArticleList(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "article_list.html"

    def get(self, request):
        active_article = 'active'
        active_List = 'active'
        if request.user.is_superuser:
            articles = Article.objects.all()
        else:
            # request.user = login for normal user #
            articles = Article.objects.filter(user = request.user)  

        return render(request, self.template_name, locals())



class EditArticle(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "edit_article.html"
    
    def get(self, request, id):
        Gradess = Article.objects.get(id=id)
        return render(request, self.template_name, locals())

    
    def post(self, request, id):
        head = request.POST.get('headline')
        des = request.POST.get('description')
        pub = request.POST.get('pub_date')
       
       

        Gradess = Article.objects.get(id=id)
        Gradess.headline = head
        Gradess.discription = des
        Gradess.pub_date = pub
        Gradess.save()
        return HttpResponseRedirect(reverse('article_list'))



class DeleteArticle(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "article_list.html"

    
    def get(self, request, id):
        Gradess = Article.objects.get(id=id)
        Gradess.delete()
        return HttpResponseRedirect(reverse('article_list'))



class ArticleStatus(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "article_list.html"

    
    def get(self, request, id):
        if  request.user.is_superuser == True:
                article = Article.objects.get(id=id)
                if article.status:
                    article.status = False
                else:
                    article.status = True
                article.save()
            
                return HttpResponseRedirect(reverse('article_list'))
        



class EditProfile(LoginRequiredMixin,TemplateView):
    login_url = '/login'
    template_name = "edit_profile.html"
    
    def get(self, request):
        try:
            Grades = User.objects.get(id = request.user.id)  
        except Exception as e:
            print(e)

        return render(request, self.template_name, locals())

    
    def post(self, request):
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
       

        Grades = User.objects.get(id = request.user.id)
        Grades.first_name = first
        Grades.last_name = last
        Grades.email = email
        Grades.save()
        if password:
            Grades.set_password(password)
            Grades.save()
            login(request, Grades, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Successfully update.')
        return HttpResponseRedirect(reverse('Edit_profile'))


########################  using ForeignKey  ######################## 
                

class AddHome(TemplateView):
    template_name = "home.html"


    def get(self,request):
        return render(request, self.template_name, locals())


    def post(self,request):
        user = request.POST.get('username')
        email = request.POST.get('email')
        first = request.POST.get('first_name')
    

        homes = Home.objects.create(
            username = user,
            email = email,
            first_name = first
            )

        messages.success(request, 'Home Successfully added.')
        return HttpResponseRedirect(reverse('add_home'))



class AddStudent(TemplateView):
    template_name = "students.html"


    def get(self,request):
        stud = Home.objects.all()
        return render(request,self.template_name,locals())


    def post(self,request):
        pho_num = request.POST.get('phone_number')
        last = request.POST.get('last_name')
        user_id = request.POST.get('Home')
       



        stu = Stu.objects.create(
            phone_number = pho_num,
            last_name = last,
            user_id = user_id
            )

        messages.success(request, 'student Successfully added.')
        return HttpResponseRedirect(reverse('add_student'))





# class Addtech(TemplateView):
#     template_name = ".html"


#     def get(self,request):
#         stud = Home.objects.all()
#         return render(request,self.template_name,locals())


#     def post(self,request):
#         pho_num = request.POST.get('phone_number')
#         last = request.POST.get('last_name')
#         user_id = request.POST.get('Home')
       



#         stu = Stu.objects.create(
#             phone_number = pho_num,
#             last_name = last,
#             user_id = user_id
#             )

#         messages.success(request, 'student Successfully added.')
#         return HttpResponseRedirect(reverse('add_student'))