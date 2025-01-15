from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("menu", CustomMenuPageView.as_view(), name="menu"),
    path("course/create", CreateCourseView.as_view(), name="create_course"),
    path("syllabus/create",SyllabusView.as_view(),name="create_syllabus"),
    path("co/create", CreateCOView.as_view(), name="create_co"),
    path("ArticulationMatrix",ArticulationMatrixView.as_view(),name="create_am"),
    path("AssesmentRubrics", AssesmentRubricsView.as_view(), name="create_ar"),
]
