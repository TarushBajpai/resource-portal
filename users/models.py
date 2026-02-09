from django.db import models

class Resource(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ECE', 'Electronics'),
        ('ME', 'Mechanical'),
        ('CE', 'Civil'),
        ('EE', 'Electrical'),
    ]

    SEMESTER_CHOICES = [(str(i), f"Semester {i}") for i in range(1, 8)]

    CATEGORY_CHOICES = [
        ('notes', 'Notes'),
        ('sessional', 'Sessional Papers'),
        ('pyq', 'AKTU PYQs'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='resources/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
