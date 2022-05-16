from django.db import models
from djrichtextfield.models import RichTextField
from embed_video.fields import EmbedVideoField


class ADMISSION_PRO(models.Model):
    content = RichTextField(null=True)

class DEMO_IMG(models.Model):
    image = models.FileField(upload_to='media/',null=True)

class PGSTS(models.Model):
    content = RichTextField(null=True)


class INFOGRAPHICS(models.Model):
    content = RichTextField(null=True)

class KURUKSHERTAA(models.Model):
    content = RichTextField(null=True)


class ABOUT_CSE(models.Model):
    content = RichTextField(null=True)

class MGSTS(models.Model):
    content = RichTextField(null=True)

class DAILY_EDITORI(models.Model):
    Date = models.CharField(max_length= 200)
    Title = models.CharField(null=True,max_length= 200)
    pdf = models.FileField(null=True)


class FEE_STRUCTURES(models.Model):
    CHOICES = [("PRELIMINARY_CUM_MAIN", "prelimitary_cum_main"),("OPTIONAL_PAPERS", "optional_papers"),("GENERAL_STUDIES", "general_studies")]
    courses = models.CharField(max_length=30, choices=CHOICES, default='prelimitary_cum_main')
    content = RichTextField(null=True)

class COURSES(models.Model):
    name = models.CharField(max_length=50)
    full_name = models.CharField(null=True,max_length=90)
    content = RichTextField(null=True)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class NCERT_CATEGORY(models.Model):
    name =  models.TextField(max_length=60)
    category_image = models.FileField(null=True)
    def book_count(self):
        books = NCERT_BOOKS.objects.filter(book_category=self)
        return books.count()
    def __str__(self):
        return self.name

class NCERT_BOOKS(models.Model):
    book_category = models.ForeignKey(NCERT_CATEGORY, on_delete=models.CASCADE, null=True)
    Book_name = models.CharField(max_length= 200)
    Book_image = models.FileField(null=True)
    Book_pdf = models.FileField(null=True)
    date = models.DateTimeField(auto_now=True)

class YOJANA_CATEGORY(models.Model):
    name =  models.TextField(max_length=60)
    category_image = models.FileField(null=True)
    def book_count(self):
        books = YOJANA_PDF.objects.filter(book_category=self)
        return books.count()
    def __str__(self):
        return self.name
class YOJANA_PDF(models.Model):
    book_category = models.ForeignKey(YOJANA_CATEGORY, on_delete=models.CASCADE, null=True)
    Book_name = models.CharField(max_length= 200)
    Book_image = models.FileField(null=True)
    Book_pdf = models.FileField(null=True)

class SYLLABUSS(models.Model):
    content = RichTextField(null=True)

class PREVIOUS_PAPER(models.Model):
    CHOICES = [("UPSC Prelims Previous Year Question Papers", "UPSC Prelims Previous Year Question Papers"), ("Essay Previous Year Question Papers", "Essay Previous Year Question Papers"),
               ("UPSC Mains General Studies Previous Year Question Papers", "UPSC Mains General Studies Previous Year Question Papers"),("UPSC Mains Optional Subjects Previous Year Question Papers","UPSC Mains Optional Subjects Previous Year Question Papers")]
    Paper_Category = models.CharField(max_length=100, choices=CHOICES,null=True)
    year = models.IntegerField(null=True)
    name = models.TextField(max_length=60,null=True,blank=True)
    paper1_name = models.TextField(max_length=60,null=True,blank=True)
    paper2_name = models.TextField(max_length=60,null=True,blank=True)
    paper1_pdf = models.FileField(max_length=60,null=True)
    paper2_pdf = models.FileField(max_length=60,null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CONTACT_US(models.Model):
    first_name = models.CharField(max_length=60,null=True)
    last_name = models.CharField(max_length=60, null=True)
    Email = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    message = models.TextField(null=True)
    def __str__(self):
        return self.first_name

class HOME_ENQUIRY(models.Model):
    name = models.CharField(max_length=60,null=True)
    Course = models.CharField(max_length=60, null=True)
    Email = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True)
    def __str__(self):
        return self.name

class HOME_MEET_FACULTY(models.Model):
    name = models.CharField(max_length=60,null=True)
    state = models.CharField(max_length=60, null=True)
    Email = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    message = models.TextField(null=True)
    def __str__(self):
        return self.name

class Videos(models.Model):
    video = EmbedVideoField()