from django.db import models

# Create your models here.
class UserInfo(models.Model):
    major = models.CharField(max_length=100, db_collation='utf8_general_ci')
    school = models.CharField(max_length=200, db_collation='utf8_general_ci')
    area = models.CharField(max_length=255, db_collation='utf8_general_ci')
    grade = models.CharField(max_length=20, db_collation='utf8_general_ci')
    student_num = models.IntegerField()


class UserTable(models.Model):
    user_id = models.CharField(primary_key=True, max_length=15, db_collation='utf8_bin')
    class_id = models.CharField(max_length=15, db_collation='utf8_general_ci')
    email = models.CharField(max_length=40, db_collation='utf8_general_ci')
    pin = models.CharField(max_length=4, db_collation='utf8_general_ci')
    password = models.CharField(max_length=20, db_collation='utf8_general_ci')
    level = models.IntegerField()
    last_login_time = models.DateTimeField()
    user_name = models.CharField(max_length=100, db_collation='utf8_general_ci')
