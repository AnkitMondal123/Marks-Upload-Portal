from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Batch, Semester, Course, CO, CourseArticulationMatrix, Syllabus, AssementRubrics, AssessmentMarks


class CreateCOView(TemplateView):
    template_name = "pages/create_co.html"

    def get(self, request):
        batches = Batch.objects.all()
        semesters = Semester.objects.all()
        courses = Course.objects.all()
        return render(request, self.template_name, {
            'batches': batches,
            'semesters': semesters,
            'courses': courses
        })

    def post(self, request):
        course_id = request.POST.get('course_selector')
        course = Course.objects.get(id=course_id)
        total_rows = int(request.POST.get('total_rows', 0))
        for i in range(total_rows):
            co_text = request.POST.get(f'co_text_{i}', '')
            details = request.POST.get(f'details_{i}', '')
            verb = request.POST.get(f'verb_{i}', '')
            level = request.POST.get(f'level_{i}', '')
            if co_text:
                CO.objects.create(
                    course=course,
                    course_outcome=co_text,
                    details=details,
                    action_verb=verb,
                    knowledge_level=level
                )
        return redirect('menu')

class CreateCourseView(TemplateView):
    def get(self, request):
        return render(request, 'pages/add_course.html')

    def post(self, request):
        batch_name = request.POST.get('batch_name')
        
        sem_name = request.POST.get('semester_name')
        sem_number = request.POST.get('semester_number')
        
        course_code = request.POST.get('course_code')
        title = request.POST.get('course_title')

        batch, _ = Batch.objects.get_or_create(
            name=batch_name,
            defaults={
                'start_date': '2023-01-01',
                'end_date': '2023-12-31'
            }
        )
        semester, _ = Semester.objects.get_or_create(
            batch=batch,
            semester_name=sem_name,
            semester_number=sem_number,
            defaults={
                'start_date': '2023-01-01',
                'end_date': '2023-12-31'
            }
        )
        Course.objects.create(
            semester=semester,
            course_code=course_code,
            course_title=title,
            type_of_course='Theory',
            course_Designation='Compulsory',
            Continuous_Assessment_marks=50,
            final_exam_marks=50,
            credits=3
        )

        return redirect('menu')
    
class HomePageView(TemplateView):
    template_name = "pages/home.html"

class CustomMenuPageView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account_login')  

    def get_template_names(self):
        if not self.request.user.is_approved:
            return ["pages/menu1.html"]
        else:
            return ["pages/menu2.html"]

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)
    
class AssesmentRubricsView(TemplateView):
    template_name = "pages/create_ar.html"
    def get(self, request):
        batches = Batch.objects.all()
        semesters = Semester.objects.all()
        courses = Course.objects.all()
        return render(request, self.template_name, {
            'batches': batches,
            'semesters': semesters,
            'courses': courses
        })
    def post(self, request):
        if 'rubrics_form' in request.POST:  # Handle assessment rubrics save
            course_id = request.POST.get('course_selector')
            if course_id:
                course = Course.objects.get(id=course_id)
                rubric, created = AssementRubrics.objects.update_or_create(
                    course=course,
                    defaults={
                        'co1_full_marks': request.POST.get('CO1_full_marks') or None,
                        'co2_full_marks': request.POST.get('CO2_full_marks') or None,
                        'co3_full_marks': request.POST.get('CO3_full_marks') or None,
                        'co4_full_marks': request.POST.get('CO4_full_marks') or None,
                        'co5_full_marks': request.POST.get('CO5_full_marks') or None,
                        'co6_full_marks': request.POST.get('CO6_full_marks') or None,
                        'co1_attainment_percent': request.POST.get('CO1_attainment_percent') or None,
                        'co2_attainment_percent': request.POST.get('CO2_attainment_percent') or None,
                        'co3_attainment_percent': request.POST.get('CO3_attainment_percent') or None,
                        'co4_attainment_percent': request.POST.get('CO4_attainment_percent') or None,
                        'co5_attainment_percent': request.POST.get('CO5_attainment_percent') or None,
                        'co6_attainment_percent': request.POST.get('CO6_attainment_percent') or None,
                    }
                )
                return JsonResponse({'status': 'success', 'message': 'Assessment Rubrics saved successfully!'})
            return JsonResponse({'status': 'error', 'message': 'Course not selected!'})

        elif 'marks_form' in request.POST:  # Handle assessment marks save
            rubric_id = request.POST.get('rubric_id')
            if rubric_id:
                rubric = AssementRubrics.objects.get(id=rubric_id)
                total_rows = int(request.POST.get('total_rows', 0))
                for i in range(total_rows):
                    roll_number = request.POST.get(f'roll_number_{i}')
                    name = request.POST.get(f'name_{i}')
                    co1_marks = request.POST.get(f'CO1_marks_{i}') or None
                    co2_marks = request.POST.get(f'CO2_marks_{i}') or None
                    co3_marks = request.POST.get(f'CO3_marks_{i}') or None
                    co4_marks = request.POST.get(f'CO4_marks_{i}') or None
                    co5_marks = request.POST.get(f'CO5_marks_{i}') or None
                    co6_marks = request.POST.get(f'CO6_marks_{i}') or None

                    AssessmentMarks.objects.update_or_create(
                        assement_rubric=rubric,
                        roll_number=roll_number,
                        defaults={
                            'name': name,
                            'co1_marks': co1_marks,
                            'co2_marks': co2_marks,
                            'co3_marks': co3_marks,
                            'co4_marks': co4_marks,
                            'co5_marks': co5_marks,
                            'co6_marks': co6_marks,
                        }
                    )
                return JsonResponse({'status': 'success', 'message': 'Assessment Marks saved successfully!'})
            return JsonResponse({'status': 'error', 'message': 'Rubric not selected!'})

        return JsonResponse({'status': 'error', 'message': 'Invalid request!'})
    
class ArticulationMatrixView(TemplateView):
    template_name="pages/create_am.html"

class SyllabusView(TemplateView):
    template_name="pages/create_syllabus.html"