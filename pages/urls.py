from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("menu/", CustomMenuPageView.as_view(), name="menu"),
    path("course/add/", CreateCourseView.as_view(), name="create_course"),
    path("co/add/", CreateCOView.as_view(), name="create_co"),
    path("AssesmentRubrics/", assesmentrubrics.as_view(), name="create_ar"),
]
