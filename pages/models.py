from django.db import models

class Batch(models.Model):
    # Represents an academic batch, e.g., "2023-2024"
    name = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return self.name


class Semester(models.Model):
    # Each batch can have multiple semesters
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='semesters')
    semester_name = models.CharField(max_length=10)  # e.g., "Sem 1", "Sem 2"
    semester_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.batch} - {self.semester_name}"


class Course(models.Model):
    # Represents a course within a given semester
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')
    course_code = models.CharField(max_length=20, unique=True)
    course_title = models.CharField(max_length=100)
    type_of_course = models.CharField(max_length=100)
    course_Designation = models.CharField(max_length=100)
    Continuous_Assessment_marks = models.IntegerField()
    final_exam_marks = models.IntegerField()
    credits = models.IntegerField()
    contact_hours = models.CharField(max_length=20, default='3L/week')
    writer = models.CharField(max_length=100, default='Course Coordinator')
    approved_by = models.CharField(max_length=100, default='HoD')

    def __str__(self):
        return f"{self.semester} {self.course_title} ({self.course_code})"

class CO(models.Model):
    # Represents a course outcome for a given course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='co')
    course_outcome = models.CharField(max_length=255)
    details = models.TextField()
    action_verb = models.CharField(max_length=40)
    knowledge_level = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course.course_title} - {self.course_outcome}"
    
class AssementRubrics(models.Model):
    # Represents a AssementRubrics for a given course
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rubric')
    co1_full_marks = models.IntegerField(null=True, blank=True)
    co2_full_marks = models.IntegerField(null=True, blank=True)
    co3_full_marks = models.IntegerField(null=True, blank=True)
    co4_full_marks = models.IntegerField(null=True, blank=True)
    co5_full_marks = models.IntegerField(null=True, blank=True)
    co6_full_marks = models.IntegerField(null=True, blank=True)
    co1_attainment_percent = models.IntegerField(null=True, blank=True)
    co2_attainment_percent = models.IntegerField(null=True, blank=True)
    co3_attainment_percent = models.IntegerField(null=True, blank=True)
    co4_attainment_percent = models.IntegerField(null=True, blank=True)
    co5_attainment_percent = models.IntegerField(null=True, blank=True)
    co6_attainment_percent = models.IntegerField(null=True, blank=True)

class AssessmentMarks(models.Model):
    # represents a student's marks for a given course
    assement_rubric = models.ForeignKey(AssementRubrics, on_delete=models.CASCADE, related_name='marks')
    roll_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    co1_marks = models.IntegerField(null=True, blank=True)
    co2_marks = models.IntegerField(null=True, blank=True)
    co3_marks = models.IntegerField(null=True, blank=True)
    co4_marks = models.IntegerField(null=True, blank=True)
    co5_marks = models.IntegerField(null=True, blank=True)
    co6_marks = models.IntegerField(null=True, blank=True)
    co1_attainment = models.BooleanField(null=True, blank=True)
    co2_attainment = models.BooleanField(null=True, blank=True)
    co3_attainment = models.BooleanField(null=True, blank=True)
    co4_attainment = models.BooleanField(null=True, blank=True)
    co5_attainment = models.BooleanField(null=True, blank=True)
    co6_attainment = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.course.course_title} - {self.roll_number}"
    
    def save(self, *args, **kwargs):
        rubric = self.assement_rubric

        # CO1 Attainment
        if rubric.co1_full_marks is not None and rubric.co1_attainment_percent is not None and self.co1_marks is not None:
            self.co1_attainment = (self.co1_marks / rubric.co1_full_marks) * 100 >= rubric.co1_attainment_percent

        # CO2 Attainment
        if rubric.co2_full_marks is not None and rubric.co2_attainment_percent is not None and self.co2_marks is not None:
            self.co2_attainment = (self.co2_marks / rubric.co2_full_marks) * 100 >= rubric.co2_attainment_percent
        
        # CO3 Attainment
        if rubric.co3_full_marks is not None and rubric.co3_attainment_percent is not None and self.co3_marks is not None:
            self.co3_attainment = (self.co3_marks / rubric.co3_full_marks) * 100 >= rubric.co3_attainment_percent
        
        # CO4 Attainment
        if rubric.co4_full_marks is not None and rubric.co4_attainment_percent is not None and self.co4_marks is not None:
            self.co4_attainment = (self.co4_marks / rubric.co4_full_marks) * 100 >= rubric.co4_attainment_percent

        # CO5 Attainment
        if rubric.co5_full_marks is not None and rubric.co5_attainment_percent is not None and self.co5_marks is not None:
            self.co5_attainment = (self.co5_marks / rubric.co5_full_marks) * 100 >= rubric.co5_attainment_percent
        
        # CO6 Attainment
        if rubric.co6_full_marks is not None and rubric.co6_attainment_percent is not None and self.co6_marks is not None:
            self.co6_attainment = (self.co6_marks / rubric.co6_full_marks) * 100 >= rubric.co6_attainment_percent
    
        super().save(*args, **kwargs)