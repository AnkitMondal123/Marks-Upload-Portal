# Generated by Django 5.1.2 on 2025-01-14 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssementRubrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co1_full_marks', models.IntegerField(blank=True, null=True)),
                ('co2_full_marks', models.IntegerField(blank=True, null=True)),
                ('co3_full_marks', models.IntegerField(blank=True, null=True)),
                ('co4_full_marks', models.IntegerField(blank=True, null=True)),
                ('co5_full_marks', models.IntegerField(blank=True, null=True)),
                ('co6_full_marks', models.IntegerField(blank=True, null=True)),
                ('co1_attainment_percent', models.IntegerField(blank=True, null=True)),
                ('co2_attainment_percent', models.IntegerField(blank=True, null=True)),
                ('co3_attainment_percent', models.IntegerField(blank=True, null=True)),
                ('co4_attainment_percent', models.IntegerField(blank=True, null=True)),
                ('co5_attainment_percent', models.IntegerField(blank=True, null=True)),
                ('co6_attainment_percent', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('course_title', models.CharField(max_length=100)),
                ('type_of_course', models.CharField(max_length=100)),
                ('course_Designation', models.CharField(max_length=100)),
                ('Continuous_Assessment_marks', models.IntegerField()),
                ('final_exam_marks', models.IntegerField()),
                ('credits', models.IntegerField()),
                ('contact_hours', models.CharField(default='3L/week', max_length=20)),
                ('writer', models.CharField(default='Course Coordinator', max_length=100)),
                ('approved_by', models.CharField(default='HoD', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('co1_marks', models.IntegerField(blank=True, null=True)),
                ('co2_marks', models.IntegerField(blank=True, null=True)),
                ('co3_marks', models.IntegerField(blank=True, null=True)),
                ('co4_marks', models.IntegerField(blank=True, null=True)),
                ('co5_marks', models.IntegerField(blank=True, null=True)),
                ('co6_marks', models.IntegerField(blank=True, null=True)),
                ('co1_attainment', models.BooleanField(blank=True, null=True)),
                ('co2_attainment', models.BooleanField(blank=True, null=True)),
                ('co3_attainment', models.BooleanField(blank=True, null=True)),
                ('co4_attainment', models.BooleanField(blank=True, null=True)),
                ('co5_attainment', models.BooleanField(blank=True, null=True)),
                ('co6_attainment', models.BooleanField(blank=True, null=True)),
                ('assement_rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='pages.assementrubrics')),
            ],
        ),
        migrations.CreateModel(
            name='CO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_outcome', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('action_verb', models.CharField(max_length=40)),
                ('knowledge_level', models.CharField(max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='co', to='pages.course')),
            ],
        ),
        migrations.AddField(
            model_name='assementrubrics',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rubric', to='pages.course'),
        ),
        migrations.CreateModel(
            name='CourseArticulationMatrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conumber', models.CharField(default='-', max_length=5)),
                ('PO1', models.IntegerField(default=0)),
                ('PO2', models.IntegerField(default=0)),
                ('PO3', models.IntegerField(default=0)),
                ('PO4', models.IntegerField(default=0)),
                ('PO5', models.IntegerField(default=0)),
                ('PO6', models.IntegerField(default=0)),
                ('PO7', models.IntegerField(default=0)),
                ('PO8', models.IntegerField(default=0)),
                ('PO9', models.IntegerField(default=0)),
                ('PO10', models.IntegerField(default=0)),
                ('PO11', models.IntegerField(default=0)),
                ('PO12', models.IntegerField(default=0)),
                ('PSO1', models.IntegerField(default=0)),
                ('PSO2', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cam', to='pages.course')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_name', models.CharField(max_length=10)),
                ('semester_number', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='pages.batch')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='pages.semester'),
        ),
    ]
