# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import *




class AddReporter(TemplateView):
    template_name = "add_reporter.html"

    def get(self, request):
        return render(request, self.template_name, locals())

    def post(self, request):
        Username = request.POST.get('Username')
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        email = request.POST.get('Email')
        passwor = request.POST.get('password')
        print(Username,'=====Username')
        print(first,'=====first')
        print(last,'=====last')
        print(email,'=====email')
        print(passwor,'=====password')
        try:
            filter_user = User.objects.get(username = Username)
            # filters = User.objects.get(password = passwor)
            print(filter_user,'========filter_user')
            # print(filters,'========filters')            
            messages.info(request, 'username already exists.')

        except User.DoesNotExist:
            student = User.objects.create(
                username = Username,
                first_name = first,
                last_name = last,
                email = email
                )
            student.set_password(passwor)
            student.save()

            messages.success(request, 'Reporter Successfully added.')
        return HttpResponseRedirect(reverse('add_reporter'))


# class AddArticle(TemplateView):
#     template_name = "article.html"

#     def get(self, request):
#         # reporters = Reporter.objects.all()
#         return render(request, self.template_name, locals())




class ReporterList(TemplateView):
    template_name = "reporter_list.html"

    def get(self, request):
        # Username = request.GET.get('Username')
        # print(Username,'======Username')
        # first = request.GET.get('first_name')
        # print(first,'=======first')
        # last = request.GET.get('last_name')
        # print(last,'=======last')
        # add = request.GET.get('address')
        # print(add,'======add')
        # emails = request.GET.get('mail')
        # print(emails,'=====email')

        reporter = User.objects.filter(is_superuser = False)
        print(reporter,'======reporter')
        # if first:
        #     reporter = User.objects.filter(firstname__contains = first)
        # elif last:
        #     reporter = User.objects.filter(lastname__contains = last)
        # elif add:
        #     reporter = User.objects.filter(address__contains = add)
        # elif emails:
        #     reporter = User.objects.filter(email__contains = emails)
        # else:
        #     reporter = User.objects.all()


        return render(request, self.template_name, locals())



class Editreporter(TemplateView):
    template_name = "edit_reporter.html"
    
    def get(self, request, id):
        Grades = User.objects.get(id=id)
        return render(request, self.template_name, locals())

    
    def post(self, request, id):
        Users = request.POST.get('Username')
        print(Users,'=======Users')
        first = request.POST.get('first_name')
        print(first,'===========first_name')
        last = request.POST.get('last_name')
        print(last,'++++++++++last_name')
        email = request.POST.get('Email')
        print(email,"======email")
       

        Grades = User.objects.get(id=id)
        Grades.username = Users
        Grades.first_name = first
        Grades.last_name = last
        Grades.email = email
        Grades.save()
        return HttpResponseRedirect(reverse('reporter_list'))




class Deletereporter(TemplateView):
    template_name = "reporter_list.html"
    
    def get(self, request, id):
        Grades = User.objects.get(id=id)
        Grades.delete()
        return HttpResponseRedirect(reverse('reporter_list'))




class AddArticle(TemplateView):
    template_name = "add_article.html"

    def get(self, request):
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



class ArticleList(TemplateView):
    template_name = "article_list.html"

    def get(self, request):
        if request.user.is_superuser:
            articles = Article.objects.all()
        else:
            # request.user = login for normal user #
            articles = Article.objects.filter(user = request.user)  

        return render(request, self.template_name, locals())



class EditArticle(TemplateView):
    template_name = "edit_article.html"
    
    def get(self, request, id):
        Gradess = Article.objects.get(id=id)
        return render(request, self.template_name, locals())

    
    def post(self, request, id):
        head = request.POST.get('headline')
        print(head,'=======headline')
        des = request.POST.get('description')
        print(des,'===========des')
        pub = request.POST.get('pub_date')
        print(pub,'++++++++++pub_date')
       
       

        Gradess = Article.objects.get(id=id)
        Gradess.headline = head
        Gradess.discription = des
        Gradess.pub_date = pub
        Gradess.save()
        return HttpResponseRedirect(reverse('article_list'))



class DeleteArticle(TemplateView):
    template_name = "article_list.html"

    
    def get(self, request, id):
        Gradess = Article.objects.get(id=id)
        Gradess.delete()
        return HttpResponseRedirect(reverse('article_list'))



class ArticleStatus(TemplateView):
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
        





