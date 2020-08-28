from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from myApp import forms
from django.views import View
from myApp import models
from myApp.utils import render_to_pdf
from django.http import HttpResponse
# Create your views here.
class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    template_name='myApp/signup.html'
    success_url=reverse_lazy('login')

class CvCreate(LoginRequiredMixin,generic.CreateView):
    model=models.Cv
    login_url='login'
    template_name='myApp/index.html'
    success_url=reverse_lazy('mylist')
    fields=('phone','skills','achievement','projects','highSchool','highSchoolPercetage','collegeName','degree','collegeGpa','experiance')
    def form_valid(self,form):
        form.instance.person=self.request.user
        return super(CvCreate,self).form_valid(form)
class Thanks(generic.TemplateView):
    template_name='myApp/tq.html'

class ViewPdf(View):
    def get(self,request,*args,**kwargs):
        user=models.Cv.objects.get(id__exact=self.kwargs['cat'])
        data={
        'first_name':user.person.first_name,
        'last_name':user.person.last_name,
        'email':user.person.email,
        'phone':user.phone,
        'achievement':user.achievement,
        'skills':user.skills,
        'highSchool':user.highSchool,
        'highSchoolPercetage':user.highSchoolPercetage,
        'collegeName':user.collegeName,
        'collegeGpa':user.collegeGpa,
        'degree':user.degree,
        'experiance':user.experiance,
        'projects':user.projects,

        }

        pdf=render_to_pdf('myApp/cv.html',data)
        return HttpResponse(pdf,content_type='application/pdf')

class DownloadPdf(View):
    def get(self,request,*args,**kwargs):
        user=models.Cv.objects.get(id__exact=self.kwargs['cat'])
        data={
        'first_name':user.person.first_name,
        'last_name':user.person.last_name,
        'email':user.person.email,
        'phone':user.phone,
        'achievement':user.achievement,
        'skills':user.skills,
        'highSchool':user.highSchool,
        'highSchoolPercetage':user.highSchoolPercetage,
        'collegeName':user.collegeName,
        'collegeGpa':user.collegeGpa,
        'degree':user.degree,
        'experiance':user.experiance,
        'projects':user.projects,

        }
        pdf=render_to_pdf('myApp/cv.html',data)
        response=HttpResponse(pdf,content_type='application/pdf')
        filename='MyCv_%s.pdf' %(user.person.first_name)
        content='attachment; filename="%s"' %(filename)
        response['Content-Disposition']=content
        return response
class MyPdf(LoginRequiredMixin,generic.ListView):
    login_url='login'
    context_object_name='list'
    template_name='myApp/list.html'

    def get_queryset(self):
        return models.Cv.objects.filter(person=self.request.user)
class MyCvDetails(LoginRequiredMixin,generic.DetailView):
    login_url='login'
    model=models.Cv
    context_object_name='dt'
    template_name='myApp/cv.html'
class about(generic.TemplateView):
    template_name='myApp/about.html'
