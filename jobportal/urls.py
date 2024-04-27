from django.contrib import admin
from django.urls import path
from job import views
from django.conf import settings
from django.conf.urls.static import static

from job.views import gen_resume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('send_email_with_button',views.send_email_with_button,name="send_email_with_button"),
    path('accept_email_with_button',views.accept_email_with_button,name="accept_email_with_button"),
    path('admin_login', views.admin_login, name="admin_login"),
    path('email_template',views.email_template, name="email_template"),
    path('user_login', views.user_login, name="user_login"),
    path('recruiter_login', views.recruiter_login, name="recruiter_login"),
    path('recruiter_home', views.recruiter_home, name="recruiter_home"),
    path('user_signup', views.user_signup, name="user_signup"),
    path('accept', views.accept, name="accept"),
    path('resume/', gen_resume, name = 'resume'),
    path('user_home', views.user_home, name="user_home"),
    path('recruiter_signup', views.recruiter_signup, name="recruiter_signup"),
    path('Logout', views.Logout, name="Logout"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('recruiter1_home', views.recruiter1_home, name="recruiter1_home"),
    path('add_job', views.add_job, name="add_job"),
    path('job_list', views.job_list, name="job_list"),
    path('view_users', views.view_users, name="view_users"),
    path('recruiter_pending', views.recruiter_pending, name="recruiter_pending"),
    path('delete_user/<int:pid>', views.delete_user, name="delete_user"),
    path('change_status/<int:pid>', views.change_status, name="change_status"),
    path('job_detail/<int:pid>', views.job_detail, name="job_detail"),
    path('view_profile/<int:pid>/', views.view_profile, name='view_profile'),

    path('applyforjob/<int:pid>', views.applyforjob, name="applyforjob"),
    path('applied_candidatelist', views.applied_candidatelist, name="applied_candidatelist"),
    path('recruiter_accepted', views.recruiter_accepted, name="recruiter_accepted"),
    path('recruiter_rejected', views.recruiter_rejected, name="recruiter_rejected"),
    path('latest_jobs', views.latest_jobs, name="latest_jobs"),
    path('contact', views.contact, name="contact"),
    path('user_latestjobs', views.user_latestjobs, name="user_latestjobs"),
    path('recruiter_all', views.recruiter_all, name="recruiter_all"),
    path('delete_recruiter/<int:pid>', views.delete_recruiter, name="delete_recruiter"),
    path('delete_job/<int:pid>', views.delete_job, name="delete_job"),
    path('edit_jobdetail/<int:pid>', views.edit_jobdetail, name="edit_jobdetail"),
    path('change_companylogo/<int:pid>', views.change_companylogo, name='change_companylogo'),
    path('change_passwordadmin', views.change_passwordadmin, name="change_passwordadmin"),
    path('change_passwordrecruiter', views.change_passwordrecruiter, name="change_passwordrecruiter"),
    path('change_passworduser', views.change_passworduser, name="change_passworduser")

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)