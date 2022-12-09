# Generated by Django 4.1.3 on 2022-12-03 06:02

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Learning_Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=5000)),
                ('country', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('phone_no', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('phone_no_optional', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(max_length=500)),
                ('email_optional', models.CharField(blank=True, max_length=500, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('primary_language', models.CharField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30, null=True)),
                ('trainer_type', models.CharField(blank=True, choices=[('Corporate Trainer', 'Corporate Trainer'), ('Academic Trainer', 'Academic Trainer')], max_length=30, null=True)),
                ('trainer_pricing', models.CharField(blank=True, max_length=1000, null=True)),
                ('trainer_course_specialization', models.CharField(max_length=100000)),
                ('trainer_skill_set', models.CharField(blank=True, max_length=100000, null=True)),
                ('trainer_tier', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, null=True)),
                ('trainer_enrolled_with', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portalapp.learning_partner')),
            ],
        ),
        migrations.CreateModel(
            name='Training_LeadHist',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('training_lead_id', models.CharField(max_length=20000)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('handel_by', models.CharField(max_length=2000)),
                ('learning_partner', models.CharField(max_length=2000)),
                ('assign_to_trainer', models.CharField(max_length=2000)),
                ('course_name', models.CharField(max_length=2000)),
                ('lead_type', models.CharField(max_length=2000)),
                ('time_zone', models.CharField(max_length=2000)),
                ('getting_lead_date', models.CharField(max_length=2000)),
                ('start_date', models.CharField(max_length=2000)),
                ('end_date', models.CharField(max_length=2000)),
                ('lead_status', models.CharField(max_length=2000)),
                ('lead_description', models.CharField(max_length=100000)),
                ('updated_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Training_Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=2000)),
                ('lead_type', models.CharField(max_length=2000)),
                ('time_zone', models.CharField(choices=[('IST', 'IST'), ('GMT', 'GMT'), ('BST', 'BST'), ('CET', 'CET'), ('SAST', 'SAST'), ('EST', 'EST'), ('PST', 'PST'), ('MST', 'MST'), ('UTC', 'UTC')], max_length=40)),
                ('getting_lead_date', models.DateTimeField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('lead_status', models.CharField(choices=[('Initial', 'Initial'), ('In Progress', 'In Progress'), ('Follow Up', 'Follow Up'), ('Cancelled', 'Cancelled'), ('Confirmed', 'Confirmed'), ('PO Received', 'PO Received')], max_length=40)),
                ('lead_description', models.CharField(blank=True, max_length=9000, null=True)),
                ('assign_to_trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='portalapp.trainer')),
                ('handel_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('learning_partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portalapp.learning_partner')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='myuploadfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer_attachment', models.FileField(blank=True, null=True, upload_to='')),
                ('trainer_feedback', models.FileField(blank=True, null=True, upload_to='feedback')),
                ('last_modification', models.DateTimeField(auto_now_add=True)),
                ('trainer_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='portalapp.trainer')),
            ],
        ),
    ]
