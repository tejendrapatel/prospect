
from django.contrib import admin
from django.urls import path
from zias.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.http import HttpResponse
urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('', HOME,name='home'),
    path('contact/', CONTACT,name='contact'),
    path('about_institution/', ABOUT_INSTITUTION,name='about_institution'),
    path('prospect_book/', PROSPECT_BOOK,name='prospect_book'),
    path('prospect_planner/', PROSPECT_PLANNER,name='prospect_planner'),
    path('suggested_readings/', SUGGESTED_READINGS,name='suggested_readings'),
    path('kurukshetra/',KURUKSHETRA,name='kurukshetra'),
    path('news_clippings/', NEWS_CLIPPINGS,name='news_clippings'),
    path('prospect_articles/', PROSPECT_ARTICLES,name='prospect_articles'),
    path('prospect_magazine/', PROSPECT_MAGAZINE,name='prospect_magazine'),
    path('info_graphics/', INFO_GRAPHICS,name='info_graphics'),
    path('rstv_debates/', RSTV_DEBATES,name='rstv_debates'),
    path('ncrt_books/', NCRT_BOOKS,name='ncrt_books'),
    path('yojana/', YOJANA,name='yojana'),
    path('admission_procedure/', ADMISSION_PROCEDURE,name='admission_procedure'),
    path('fee_structure/', FEE_STRUCTURE,name='fee_structure'),
    path('about_cse/', ABOUT_CSEE,name='about_cse'),
    path('smcqs/yllabus/', SYLLABUS,name='syllabus'),
    path('mcqs/', MCQS,name='mcqs'),
    path('air_news/', AIR_NEWS,name='air_news'),
    path('pib/', PIB,name='pib'),
    path('daily_editorial/', DAILY_EDITORIAL,name='daily_editorial'),
    path('pgsts/', PGSTSS,name='pgsts'),
    path('mgsts/', MGSTSS,name='mgsts'),
    path('previous_papers/',PREVIOUS_PAPERS,name='previous_papers'),
    path('Logout/',LOGOUT,name='Logout'),
    path('Login/',LOGIN,name='Login'),
#     dynamic urls   #
    path('course_detail/<int:cat_id>/',Course_detail,name= 'course_detail'),
    path('ncert_book_detail/<int:nce_id>/',NCERT_BOOK_DETAIL,name= 'ncert_book_detail'),
    path('yojana_detail/<int:yoj_id>/',YOJANA_DETAIL,name= 'yojana_detail'),
#     search urls #
    path('ncrt_books_search/', NCRT_BOOKS_SEARCH,name='ncrt_books_search'),
    path('yojana_search/',YOJANA_SEARCH,name='yojana_search'),

#    admin url   #
    path('admin_index', ADINDEX, name='admin_index'),
    path('ad_pgsts', AD_PGSTS, name='ad_pgsts'),
    path('ad_mgsts', AD_MGSTS, name='ad_mgsts'),
    path('ad_page_not_found', AD_PAGE_NOT_FOUND, name='ad_page_not_found'),
    path('admin_contact_us', CONTACT_USS, name='admin_contact_us'),
    path('admin_admission_pro',AD_ADMISSION_PRO, name='admin_admission_pro'),
    path('admin_fee_precummain',AD_FEE_PRECUMMAIN, name='admin_fee_precummain'),
    path('admin_fee_optional',AD_FEE_OPTIONAL, name='admin_fee_optional'),
    path('admin_fee_genstudies',AD_FEE_GENSTUDIES, name='admin_fee_genstudies'),
    path('admin_about_cse',ADMIN_ABOUT_CSEE, name='admin_about_cse'),
    path('admin_demo_img',ADMIN_DEMO_IMG, name='admin_demo_img'),
    path('admin_syllabus',ADMIN_SYLLABUS, name='admin_syllabus'),
    path('admin_previous_papers',ADMIN_PREVIOUS_PAPERS, name='admin_previous_papers'),
    path('admin_ncert_book',ADMIN_NCRT_BOOKS, name='admin_ncert_book'),
    path('admin_yojana_book',ADMIN_YOJANA_BOOKS, name='admin_yojana_book'),
    path('admin_home',ADMIN_HOME, name='admin_home'),
    path('admin_add_courses',ADMIN_ADD_COURSE, name='admin_add_courses'),
    path('admin_youtube_gallery',ADMIN_YOUTUBE_GALLERY, name='admin_youtube_gallery'),
    path('admin_google_review',ADMIN_GOOGLE_REVIEW, name='admin_google_review'),

####  delete #######
    path('previous_paper_delete/<int:prev_id>/', PREVIOUS_PAPAERS_DELETE, name='previous_paper_delete'),
    path('book_cat_delete/<int:book_id>/', BOOK_CAT_DELETE, name='book_cat_delete'),
    path('book_delete/<int:bookdel_id>/', BOOKS_DELETE, name='book_delete'),
    path('yojana_cat_delete/<int:yoj_id>/', YOJANA_CAT_DELETE, name='yojana_cat_delete'),
    path('yojana_delete/<int:yojdel_id>/', YOJANA_DELETE, name='yojana_delete'),
    path('youtube_delete/<int:youdel_id>/', YOUTUBE_DELETE, name='youtube_delete'),
    path('course_delete/<int:adc_id>/', ADMIN_COURSE_DELETE, name='course_delete'),

##   dynamic admin ###
    path('ad_course_detail/<int:adc_id>/',ADMIN_Course_detail,name= 'ad_course_detail'),
    path('book_cat_detail/<int:bcd_id>/',ADMIN_BOOK_DYNAMIC,name= 'book_cat_detail'),
    path('yojana_cat_detail/<int:yoj_id>/',ADMIN_YOJANA_DYNAMIC,name= 'yojana_cat_detail'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
