from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView
from .models import CourseDetails,CourseContent,CourseId,Question,Progress,Category
from django.db.models import Count

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .forms import ProgressForm
from django.http import HttpResponseRedirect
from django.urls import reverse

#Courses Blog

@login_required
def blog(request):

    blogs2=CourseDetails.objects.all().values('category').annotate(total=Count('category'))
    cate=Category.objects.all()
    clist= list(cate)
    listb = list(blogs2)
    dat=zip(clist, listb)

    blogs1=CourseDetails.objects.all()
    blogs=CourseDetails.objects.all()


    query=request.GET.get("q")
    if query:
        blogs=blogs.filter(name__icontains=query)

    query=request.GET.get("filter")
    if query:
        blogs=blogs.filter(category__category__icontains=query)



    blogcourse={
    'blogs':blogs,
    'dat':dat,
    'blogs1':blogs1,
    }

    return render(request,'blog-single.html',blogcourse)


#Course Description

def coursedesc(request,id):
    instance=get_object_or_404(CourseDetails,id=id)
    context={
        "name":instance.name,
        "instance":instance
    }
    return render(request,'coursedesc.html',context)
#course Home

def coursehome(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    cohome=CourseDetails.objects.filter(courseid=courseid)

    home={
    'courseid':courseid,
    'cohome':cohome
    }

    return render(request,'coursehome.html',home)



def prog(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    progs=CourseDetails.objects.filter(courseid=courseid)
    return render(request,'blog-single.html',{'progs':progs})






# def coursec(request):
#     coursec=CourseContent.objects.all()
#     return render(request,'coursecontent.html',{'coursec':coursec})

#Course Content
def coursec(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    instance=CourseDetails.objects.filter(courseid=courseid)
    coursecontent_list=CourseContent.objects.filter(courseid=courseid)
    coursetit=CourseContent.objects.filter(courseid=courseid)
    paginator = Paginator(coursecontent_list, 1)
    page = request.GET.get('page')
    coursecontent = paginator.get_page(page)
    content={
    'instance':instance,
    'courseid':courseid,
    'coursecontent':coursecontent,
    'coursetit':coursetit
    }
    return render(request, 'course.html',content)


#Add Question
@login_required
def exam(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    context=Question.objects.filter(courseid=courseid)
    if request.method =='POST':

         # form=ProgressForm(request.POST)
         # if form.is_valid():
         #     form.save()
         user=request.POST.get('user')
         cid=request.POST.get('cid')
         correct=request.POST.get('correct')
         total=request.POST.get('total')
         p=Progress()
         p.user=user
         p.cid=cid
         p.correct=correct
         p.total=total
         p.save()
         return redirect(reverse('progress', kwargs={"courseid": courseid}))

         # progress_obj=Progress(user=user,cid=cid,correct=correct,total=total)
         # progress_obj.save()
        # return redirect('progress')
    # else:
    #     form=ProgressForm()

    equestion={

    'courseid':courseid,
    'context':context,

    }

    return render(request,'quiz.html',equestion)
#Course Requirements

def requirements(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    cohome=CourseDetails.objects.filter(courseid=courseid)

    home={
    'courseid':courseid,
    'cohome':cohome
    }

    return render(request,'requirements.html',home)

#Course schedules

def schedules(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    cohome=CourseDetails.objects.filter(courseid=courseid)

    home={
    'courseid':courseid,
    'cohome':cohome
    }

    return render(request,'schedules.html',home)

#Progress
@login_required
def progress(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    courseref=CourseDetails.objects.filter(courseid=courseid)
    progs=Progress.objects.all()
    context={
    'courseid':courseid,
    'courseref':courseref,
    'progs':progs
    }
    return render(request,'Progress.html',context)

def contact(request):
     return render(request,'contact.html')

def about(request):
     return render(request,'about.html')

def termsofservice(request):
     return render(request,'termsofservice.html')

@login_required
def add_question(request,courseid):
    courseid=get_object_or_404(CourseId,courseid=courseid)
    context=Question.objects.filter(courseid=courseid)
    if request.method == 'POST':

        question=request.POST.get('question')
        option1=request.POST.get('option1')
        option2=request.POST.get('option2')
        option3=request.POST.get('option3')
        option4=request.POST.get('option4')
        answer=request.POST.get('answer')
        q=Question()
        q.courseid=courseid
        q.question=question
        q.option1=option1
        q.option2=option2
        q.option3=option3
        q.option4=option4
        q.answer=answer
        q.save()


    equestion={

    'courseid':courseid,
    'context':context,

    }

    return render(request,'add_question.html',equestion)
