from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("menu/", CustomMenuPageView.as_view(), name="menu"),
    path("course/add/", CreateCourseView.as_view(), name="create_course"),
    path("co/add/", CreateCOView.as_view(), name="create_co"),
    path("am/add",articulationmatrix.as_view(),name="creat_am"),
    path("syl/add",syllabus.as_view(),name="creat_syllabus"),
    path("AssesmentRubrics/", assesmentrubrics.as_view(), name="create_ar"),
]
