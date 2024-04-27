from email.message import EmailMessage
from django.core.mail import EmailMessage

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404
from datetime import date
# Create your views here.
def index(request):
    context = {
        'walmart_image_url': 'https://media.designrush.com/inspiration_images/345908/conversions/walmart_1-preview.jpg',
        'tata_image_url': 'https://i.pinimg.com/originals/5b/ac/94/5bac942d02e70ce67498bf2ff04efe97.png',
        'slack_image_url': 'https://t3.ftcdn.net/jpg/03/98/76/08/360_F_398760837_vHn5HpwkSdupuTzZll5nKEHtjhEqVVCH.jpg',
        'nvidia_image_url': 'https://www.nvidia.com/content/dam/en-zz/Solutions/about-nvidia/logo-and-brand/01-nvidia-logo-vert-500x200-2c50-p@2x.png',
        'logo_index' : 'https://media.licdn.com/dms/image/C5612AQENZ2eM4ifDig/article-cover_image-shrink_600_2000/0/1520092031253?e=2147483647&v=beta&t=a9AXehnlV2KWREsKjreAuXNJ4IdtRBS12iJHPFzTHjg',
    }
    return render(request,'index.html',context)
def gen_resume(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        about = request.POST.get('about', '')
        age = request.POST.get('age', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skill4 = request.POST.get('skill4', '')
        skill5 = request.POST.get('skill5', '')
        degree1 = request.POST.get('degree1', '')
        college1 = request.POST.get('college1', '')
        year1 = request.POST.get('year1', '')
        degree2 = request.POST.get('degree2', '')
        college2 = request.POST.get('college2', '')
        year2 = request.POST.get('year2', '')
        college3 = request.POST.get('college3', '')
        year3 = request.POST.get('year3', '')
        degree3 = request.POST.get('degree3', '')
        lang1 = request.POST.get('lang1', '')
        lang2 = request.POST.get('lang2', '')
        lang3 = request.POST.get('lang3', '')
        project1 = request.POST.get('project1', '')
        durat1 = request.POST.get('duration1', '')
        desc1 = request.POST.get('desc1', '')
        project2 = request.POST.get('project2', '')
        durat2 = request.POST.get('duration2', '')
        desc2 = request.POST.get('desc2', '')
        company1 = request.POST.get('company1', '')
        post1 = request.POST.get('post1', '')
        duration1 = request.POST.get('duration1', '')
        lin11 = request.POST.get('lin11', '')
        company2 = request.POST.get('company2', '')
        post2 = request.POST.get('post2', '')
        duration2 = request.POST.get('duration2', '')
        lin21 = request.POST.get('lin21', '')
        ach1 = request.POST.get('ach1', '')
        ach2 = request.POST.get('ach2', '')
        ach3 = request.POST.get('ach3', '')
        return render(request, 'resume.html', {'name': name,
                                               'about': about, 'skill5': skill5,
                                               'age': age, 'email': email,
                                               'phone': phone, 'skill1': skill1,
                                               'skill2': skill2, 'skill3': skill3,
                                               'skill4': skill4, 'degree1': degree1,
                                               'college1': college1, 'year1': year1,
                                               'college3': college3, 'year3': year3,
                                               'degree3': degree3, 'lang1': lang1,
                                               'lang2': lang2, 'lang3': lang3,
                                               'degree2': degree2, 'college2': college2,
                                               'year2': year2, 'project1': project1,
                                               'durat1': durat1, 'desc1': desc1,
                                               'project2': project2, 'durat2': durat2,
                                               'desc2': desc2, 'company1': company1,
                                               'post1': post1, 'duration1': duration1,
                                               'company2': company2, 'post2': post2,
                                               'duration2': duration2, 'lin11': lin11,
                                               'lin21': lin21, 'ach1': ach1,
                                               'ach2': ach2, 'ach3': ach3})

    return render(request, 'rindex.html')

def admin_login(request):
    error=""
    if request.method =='POST':
        u= request.POST['uname']
        p = request.POST['pwd']
        user= authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'admin_login.html',d)

def user_login(request):
    error=" "
    if request.method=="POST":
        u =request.POST['uname'];
        p=request.POST['pwd'];
        user = authenticate(username=u,password=p)
        if user:
            try:
                user1=StudentUser.objects.get(user=user)
                if user1.type == "student":
                    login(request,user)
                    error="no"
                else:
                    error="yes"
            except:
                error="yes"
        else:
            error="yes"
    d={'error':error}
    return render(request,'user_login.html',d)

def user_home(request):
    if not request.user.is_authenticated:
          return redirect('user_login')
    return render(request,'user_home.html')

def add_job(request):
    if not request.user.is_authenticated:
          return redirect('recruiter_login')
    error = " "
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['Description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter,start_date=sd,end_date=ed,title=jt,salary=sal,image=l,description=des,experience=exp,location=loc,skills=skills,creationdate=date.today())

            error = "no"
        except:
            error = "yes"
    d = {'error': error}

    return render(request,'add_job.html',d)

def edit_jobdetail(request,pid):
    if not request.user.is_authenticated:
          return redirect('recruiter_login')
    error = " "
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']

        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']

        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skills
        job.description = des

        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        if sd:
            try:
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass
        if ed:
            try:
                job.end_date = ed
                job.save()
            except:
                pass
        else:
            pass
    d = {'error': error,'job': job}

    return render(request,'edit_jobdetail.html',d)

def change_companylogo(request,pid):
    if not request.user.is_authenticated:
          return redirect('recruiter_login')
    error = " "
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        cl = request.FILES['logo']
        job.image = cl
        try:
            job.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'job': job}

    return render(request,'change_companylogo.html',d)


def job_list(request):
    # Check if user is authenticated
    if not request.user.is_authenticated:
        # Redirect to recruiter login page if not authenticated
        return redirect('recruiter_login')

    # Get the authenticated user
    user = request.user

    # Retrieve the recruiter associated with the authenticated user
    recruiter = Recruiter.objects.get(user=user)

    # Retrieve all jobs associated with the recruiter
    job = Job.objects.filter(recruiter=recruiter)

    # Prepare the context to be passed to the template
    context = {'job': job}

    # Render the job_list.html template with the context
    return render(request, 'job_list.html', context)


def recruiter_home(request):
    if not request.user.is_authenticated:
          return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    error = " "
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']

        recruiter.user.first_name = f
        recruiter.user.last_name = l
        recruiter.mobile = con
        recruiter.gender = gen

        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error = "no"
        except:
            pass
    d = {'recruiter':recruiter,'error':error}
    return render(request,'recruiter_home.html',d)

def user_home(request):
    if not request.user.is_authenticated:
          return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = " "
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']

        student.user.first_name = f
        student.user.last_name = l
        student.mobile = con
        student.gender = gen

        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error = "no"
        except:
            pass
    d = {'student':student,'error':error}
    return render(request,'user_home.html',d)


def view_profile(request, pid):
    if not request.user.is_authenticated:
        return redirect('applied_candidatelist')

    student = get_object_or_404(StudentUser, pk=pid)  # Fetch the student based on pid

    if request.method == 'POST':
        try:
            f = request.POST['fname']
            l = request.POST['lname']
            con = request.POST['contact']
            gen = request.POST['gender']

            student.user.first_name = f
            student.user.last_name = l
            student.mobile = con
            student.gender = gen

            student.save()
            student.user.save()
            error = "no"
        except Exception as e:
            error = "yes: " + str(e)

        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error = "no"
        except Exception as e:
            error = "yes: " + str(e)

    else:
        error = ""

    d = {'student': student, 'error': error}
    return render(request, 'view_profile.html', d)


def Logout(request):
    logout(request)
    return redirect('index')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    rcount = Recruiter.objects.all().count()
    scount = StudentUser.objects.all().count()
    d = {'rcount':rcount,'scount':scount}
    return render(request, 'admin_home.html',d)
def recruiter1_home(request):
    if not request.user.is_authenticated:
          return redirect('recruiter_login')
    return render(request,'recruiter1_home.html')


def recruiter_login(request):
    error = " "
    if request.method == "POST":
        u = request.POST['uname'];
        p = request.POST['pwd'];
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter" and user1.status!="pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request,'recruiter_login.html',d)

def user_signup(request):
    error =" "
    if request.method =='POST':
        f=request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        try:
           user= User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
           StudentUser.objects.create(user=user,mobile=con,image=i,gender=gen ,type="student")
           error="no"
        except:
            error="yes"
    d= {'error':error}
    return render(request,'user_signup.html',d)

def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=StudentUser.objects.all()
    d={'data':data}
    return render(request, 'view_users.html',d)

def latest_jobs(request):
    job=Job.objects.all()
    d={'job':job}
    return render(request, 'latest_jobs.html',d)

def user_latestjobs(request):
    job=Job.objects.all().order_by('-start_date')
    user =request.user
    student = StudentUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    li=[]
    for i in data:
        li.append(i.job.id)
    d={'job':job,'li':li}
    return render(request, 'user_latestjobs.html',d)

def job_detail(request,pid):
    job=Job.objects.get(id=pid)
    d={'job':job}
    return render(request, 'job_detail.html',d)

def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student=StudentUser.objects.get(id=pid)
    student.delete()
    return redirect('view_users')
def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter=Recruiter.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiter_all')

def delete_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('job_list')
    job = Job.objects.get(id=pid)
    job.delete()
    return redirect('job_list')

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method== "POST":
        c= request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
              error="not"
        except:
             error="yes"
    d={'error':error}
    return render(request, 'change_passwordadmin.html',d)
def change_passwordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method== "POST":
        c= request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
              error="not"
        except:
             error="yes"
    d={'error':error}
    return render(request, 'change_passwordrecruiter.html',d)
def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""
    if request.method== "POST":
        c= request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
              error="not"
        except:
             error="yes"
    d={'error':error}
    return render(request, 'change_passworduser.html',d)
def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Recruiter.objects.filter(status='pending')
    d={'data':data}
    return render(request, 'recruiter_pending.html',d)

def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    recruiter=Recruiter.objects.get(id=pid)
    if request.method== "POST":
        s= request.POST['status']
        recruiter.status=s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
    d={'recruiter':recruiter,'error':error}
    return render(request, 'change_status.html',d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    if request.method== "POST":
        c= request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u=User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
              error="not"
        except:
             error="yes"
    d={'error':error}
    return render(request, 'change_passwordadmin.html',d)

def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Recruiter.objects.filter(status= 'Accept')
    d={'data':data}
    return render(request, 'recruiter_accepted.html',d)
def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Recruiter.objects.filter(status= 'Reject')
    d={'data':data}
    return render(request, 'recruiter_rejected.html',d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data=Recruiter.objects.all()
    d={'data':data}
    return render(request, 'recruiter_all.html',d)

def recruiter_signup(request):
    error = " "
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        company=request.POST['company']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=con, image=i, gender=gen,company=company, type="recruiter",status="pending")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'recruiter_signup.html',d)
def applyforjob(request,pid):
    if not request.user.is_authenticated:
          return redirect('user_login')
    error = " "
    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1 =date.today()
    if job.end_date < date1:
        error = ("close")
    elif job.start_date > date1:
        error ="notopen"
    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            Apply.objects.create(job=job,student=student,resume=r,applydate=date.today())
            error="done"

    d = {'error': error}

    return render(request,'applyforjob.html',d)

def applied_candidatelist(request):
    if not request.user.is_authenticated:
          return redirect('recruiter_login')

    data =Apply.objects.all()

    d = {'data': data}

    return render(request,'applied_candidatelist.html',d)

def contact(request):

    return render(request, 'contact.html')

def send_email_with_button(request):
    if request.method == 'POST':

        email_ = request.POST.get('email')
        email = EmailMessage(
            'Your selected for the interview',
            ' <a>You have been shortlist for this job attend the interview in zoom call at 7.00pm tomorrow</a>',
            'bjakira04@gmail.com',
            [email_],
        )
        email.content_subtype = "html"
        email.send()
        return render(request,'recruiter_signup.html')

def email_template(request):
    return render(request, 'email_template.html')

def accept(request):
    user = Apply.objects.get(id=request.user.id)  # Assuming you're using user authentication

    # Pass email data to the template
    con = {
        'email': user.student
    }
    return render(request, 'email_template.html',con)

def accept_email_with_button(request):
    if request.method == 'POST':

        email_ = request.POST.get('email')
        email = EmailMessage(
            'Your are selected for the interview',
            ' <a>You have been shortlist for this job attend the interview in zoom call at 7.00pm tomorrow</a>',
            'bjakira04@gmail.com',
            [email_],
        )
        email.content_subtype = "html"
        email.send()
        return render(request,'applied_candidatelist.html')


# def accept(request, pid):
#     if not request.user.is_authenticated:
#         return redirect('view_profile')
#
#     student = get_object_or_404(StudentUser, pk=pid)  # Fetch the student based on pid
#     if request.method == 'POST':
#         try:
#             f = request.POST['fname']
#             l = request.POST['lname']
#             con = request.POST['contact']
#             gen = request.POST['gender']
#
#             student.user.first_name = f
#             student.user.last_name = l
#             student.mobile = con
#             student.gender = gen
#
#             student.save()
#             student.user.save()
#             error = "no"
#         except Exception as e:
#             error = "yes: " + str(e)
#
#
#
#
#     d = {'student': student,'error': error}
#     return render(request, 'accept.html', d)
