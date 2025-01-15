from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Batch, Semester, Course, CO, CourseArticulationMatrix, Syllabus, AssementRubrics, AssessmentMarks
from django.contrib import messages

class CreateCourseView(TemplateView):
    template_name = "pages/create_course.html"
    
    def get(self, request):
        batches = Batch.objects.all()
        semester = Semester.objects.all()
        courses = Course.objects.all()
        return render(request, self.template_name, {
            'batches': batches,
            'semesters': semester,
            'courses': courses
        })
    
    def post(self, request):
        try:
            # Handle Batch
            batch_select = request.POST.get('batch_select')
            if batch_select == 'new':
                batch_name = request.POST.get('batch_name')
                if not batch_name:
                    messages.error(request, "Batch name is required for new batch.")
                    return redirect('create_course')
                batch, created = Batch.objects.get_or_create(
                    name=batch_name,
                    defaults={
                        'start_date': '2023-01-01',
                        'end_date': '2023-12-31'
                    }
                )
                if not created:
                    messages.error(request, "Batch already exists.")
                    return redirect('create_course')
            else:
                try:
                    batch = Batch.objects.get(id=batch_select)
                except Batch.DoesNotExist:
                    messages.error(request, "Selected batch does not exist.")
                    return redirect('create_course')

            # Handle Semester
            semester_select = request.POST.get('semester_select')
            semester_name = request.POST.get('semester_name')
            
            if semester_select == 'new':
                if not semester_name:
                    messages.error(request, "Semester name is required for new semester.")
                    return redirect('create_course')
                semester, created = Semester.objects.get_or_create(
                    batch=batch,
                    semester_name=semester_name,
                    defaults={
                        'semester_number': 1,  # You might want to calculate this
                        'start_date': '2023-01-01',
                        'end_date': '2023-12-31'
                    }
                )
                if not created:
                    messages.error(request, "Semester already exists for this batch.")
                    return redirect('create_course')
            else:
                try:
                    semester = Semester.objects.get(id=semester_select)
                except Semester.DoesNotExist:
                    messages.error(request, "Selected semester does not exist.")
                    return redirect('create_course')

            # Handle Course
            course_select = request.POST.get('course_select')
            if course_select == 'new':
                # Get all required course fields
                course_data = {
                    'semester': semester,
                    'course_code': request.POST.get('course_code'),
                    'course_title': request.POST.get('course_title'),
                    'type_of_course': request.POST.get('type_of_course'),
                    'course_Designation': request.POST.get('course_Designation'),
                    'Continuous_Assessment_marks': request.POST.get('Continuous_Assessment_marks'),
                    'final_exam_marks': request.POST.get('final_exam_marks'),
                    'credits': request.POST.get('credits')
                }

                # Validate all fields are present
                if not all(course_data.values()):
                    messages.error(request, "All course fields are required.")
                    return redirect('create_course')

                # Create new course
                
                course = Course.objects.create(**course_data)
                messages.success(request, "Course created successfully.")
                return redirect('create_course')


        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('create_course')
        


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