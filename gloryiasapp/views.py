from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import gallery,contactform,featuredCourse,popularCourse,teacher
from django.contrib import messages


# Create your views here.

def index(request):
    

 sliderimages=gallery.objects.all();   
 return render(request,'index.html',{'sliderimages':sliderimages})



def course(request):

 fcourse=featuredCourse.objects.all()[:3];
 pcourse=popularCourse.objects.all();

 params ={'fcourse':fcourse ,'pcourse':pcourse }
 return render(request,'course.html',params)



def about(request):

 teachers=teacher.objects.all();

 return render(request,'about.html',{'teachers':teachers})


def contact(request):
    if request.method == 'POST' and 'contactforquery' in request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phonenumber')
        whatsappnumber=request.POST.get('whatsappnumber')
        query=request.POST.get('query')
        

        contact = contactform(
            name=name,
            email=email,
            contactNumber=number,
            whatsappNumber=whatsappnumber,
            query=query,
            
        )

        contact.save()
        messages.success(request, 'Form is successfully submitted.You will be contact soon.Thankyou :)')
        return HttpResponseRedirect('/contactus')

    # if request.method == 'POST' and 'feedbackform' in request.POST:
    #      ename=request.POST.get('ename')
    #      classess=request.POST.get('class')
    #      phone=request.POST.get('phone')
    #      feedback=request.POST.get('feedback')
        

    #      Feedback = feedbackform(
    #         name=ename,
    #         classes=classess,
    #         contactNumber=phone,
    #         feedback=feedback,
            
    #      )

    #      Feedback.save()
    #      return HttpResponseRedirect('/contactus')
    return render(request,'contact.html')