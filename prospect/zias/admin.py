from django.contrib import admin
from zias.models import*

from embed_video.admin import AdminVideoMixin
from .models import Videos

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)
admin.site.register(ADMISSION_PRO)
admin.site.register(FEE_STRUCTURES)
admin.site.register(COURSES)
admin.site.register(NCERT_CATEGORY)
admin.site.register(NCERT_BOOKS)
admin.site.register(SYLLABUSS)
admin.site.register(PGSTS)
admin.site.register(MGSTS)
admin.site.register(YOJANA_CATEGORY)
admin.site.register(YOJANA_PDF)
admin.site.register(PREVIOUS_PAPER)
admin.site.register(CONTACT_US)
admin.site.register(ABOUT_CSE)
admin.site.register(DEMO_IMG)
admin.site.register(HOME_ENQUIRY)
admin.site.register(HOME_MEET_FACULTY)
admin.site.register(INFOGRAPHICS)
admin.site.register(DAILY_EDITORI)
admin.site.register(KURUKSHERTAA)