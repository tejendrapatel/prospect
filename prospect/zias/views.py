from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from zias.models import *
from django.template.loader import get_template
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from prospect.settings import EMAIL_HOST_USER

def LOGIN(request):
    error = False
    if request.method == "POST":
        d = request.POST
        u = d['user']
        p = d['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('admin_index')
        else:
            error = True
    d = {'error': error}
    return render(request, "login.html", d)

def LOGOUT(request):
    logout(request)
    return redirect('home')

def All_category():
    allcat = COURSES.objects.all()
    return allcat

def HOME(request):
    vid = Videos.objects.all()
    if request.method == "POST":
        if 'enquirey' in request.POST:
            c = request.POST
            ename = c['name']
            eemail = c['email']
            emobile = c['mobile']
            ecourse = c['course']
            emessage = c['message']
            HOME_ENQUIRY.objects.create(name=ename,Course=ecourse,Email=eemail,mobile=emobile,message=emessage)
            email = 'prospectias@gmail.com'
            subject = "Enquiry form Requests"
            content = "Prospectias"
            msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
            d = {'ename': ename, 'eemail': eemail,"emobile":emobile,"ecourse":ecourse,"emessage":emessage}
            html = get_template('email.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('home')
        elif 'meet' in request.POST:
            c = request.POST
            mname = c['name']
            memail = c['email']
            mobile = c['mobile']
            mstate = c['state']
            mMessage = c['Message']
            HOME_ENQUIRY.objects.create(name=mname, state=mstate, Email=memail, mobile=mobile, message=mMessage)
            email = 'prospectias@gmail.com'
            subject = "Meet Our Faculty Requests "
            content = "Prospectias"
            msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
            d = {'mname': mname, 'memail': memail, "mobile": mobile, "mstate": mstate, "mMessage": mMessage}
            html = get_template('email2.html').render(d)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('home')


    d = {"allcat": All_category(),"vid": vid}
    return render(request,'index.html',d)

def CONTACT(request):
    if request.method == "POST":
        c = request.POST
        cname = c['first-name']
        clname = c['last-name']
        cemail = c['email']
        cmobile = c['phone']
        cmessage = c['message']
        email = 'prospectias@gmail.com'
        subject = "Contact US Requests "
        content = "Prospectias"
        msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
        d = {'cname': cname, 'clname': clname, "cemail": cemail, "cmobile": cmobile,"cmessage":cmessage}
        html = get_template('email3.html').render(d)
        msg.attach_alternative(html, 'text/html')
        msg.send()
        return redirect('contact')
    d = {"allcat": All_category()}
    return render(request,'contact.html',d)

def ABOUT_INSTITUTION(request):
    d = {"allcat": All_category()}
    return render(request,'about_institution.html',d)

def PROSPECT_BOOK(request):
    d = {"allcat": All_category()}
    return render(request,'Prospact_Books.html',d)

def NEWS_CLIPPINGS(request):
    d = {"allcat": All_category()}
    return render(request,'news_clippings.html',d)

def PROSPECT_ARTICLES(request):
    d = {"allcat": All_category()}
    return render(request,'Prospact_articles.html',d)

def PROSPECT_MAGAZINE(request):
    d = {"allcat": All_category()}
    return render(request,'Prospact_magazine.html',d)

def NCRT_BOOKS(request):
    cat = NCERT_CATEGORY.objects.all()
    booknamss = NCERT_BOOKS.objects.all()
    booknam = booknamss[:10]
    d = {"allcat": All_category(),"cat":cat,"booknam":booknam}
    return render(request,'ncrt_books.html',d)

def NCRT_BOOKS_SEARCH(request):
    query = request.GET['key']
    cat = NCERT_CATEGORY.objects.all()
    booknamss = NCERT_BOOKS.objects.all()
    boosear = NCERT_BOOKS.objects.filter(Book_name__icontains=query)
    booknam = booknamss[:10]
    d = {"allcat": All_category(),"cat":cat,"booknam":booknam,"boosear":boosear}
    return render(request,'ncrt_books_search.html',d)

def YOJANA(request):
    cat = YOJANA_CATEGORY.objects.all()
    buk = YOJANA_PDF.objects.all()
    booknam = buk[:10]
    d = {"allcat": All_category(), "cat": cat, "booknam": booknam}
    return render(request,'yojana.html',d)

def ADMISSION_PROCEDURE(request):
    adm = ADMISSION_PRO.objects.all()
    allcat = COURSES.objects.all()
    d = {"adm":adm,"allcat": allcat}
    return render(request,'admission_procedure.html',d)

def FEE_STRUCTURE(request):
    pre = FEE_STRUCTURES.objects.filter(courses="PRELIMINARY_CUM_MAIN")
    premil = FEE_STRUCTURES.objects.filter(courses="OPTIONAL_PAPERS")
    main = FEE_STRUCTURES.objects.filter(courses="GENERAL_STUDIES")
    d = {"pre":pre,"premil":premil,"main":main,"allcat": All_category()}
    return render(request,'fee_structure.html',d)
def ABOUT_CSEE(request):
    cat = ABOUT_CSE.objects.get(id = 1)
    d = {"allcat": All_category(),"cat":cat}
    return render(request,'about_cse.html',d)

def SYLLABUS(request):
    cate = SYLLABUSS.objects.all()
    d = {"allcat": All_category(),"cate":cate}
    return render(request,'syllabus.html',d)
def MCQS(request):
    d = {"allcat": All_category()}
    return render(request,'mcqs.html',d)
def AIR_NEWS(request):
    d = {"allcat": All_category()}
    return render(request,'air_news.html',d)
def PIB(request):
    d = {"allcat": All_category()}
    return render(request,'pib.html',d)

def DAILY_EDITORIAL(request):
    adm = DAILY_EDITORI.objects.all()
    d = {"allcat": All_category(),"adm":adm}
    return render(request,'daily_editorial.html',d)

def PGSTSS(request):
    adm = PGSTS.objects.all()
    d = {"allcat": All_category(),"adm":adm}
    return render(request,'pgsts.html',d)


def MGSTSS(request):
    adm = MGSTS.objects.all()
    d = {"allcat": All_category(),"adm":adm}
    return render(request,'mgsts.html',d)

def INFO_GRAPHICS(request):
    adm = INFOGRAPHICS.objects.all()
    d = {"allcat": All_category(),"adm":adm}
    return render(request,'info_graphics.html',d)

def RSTV_DEBATES(request):
    d = {"allcat": All_category()}
    return render(request,'rstv_debates.html',d)
def PROSPECT_PLANNER(request):
    d = {"allcat": All_category()}
    return render(request,'prospect_planner.html',d)

def SUGGESTED_READINGS(request):
    d = {"allcat": All_category()}
    return render(request,'suggested_readings.html',d)

def KURUKSHETRA(request):
    adm = KURUKSHERTAA.objects.all()
    d = {"allcat": All_category(),"adm":adm}
    return render(request,'kurukshetra.html',d)

def PREVIOUS_PAPERS(request):
    pre = PREVIOUS_PAPER.objects.filter(Paper_Category="UPSC Prelims Previous Year Question Papers")
    essay = PREVIOUS_PAPER.objects.filter(Paper_Category="Essay Previous Year Question Papers")
    gen = PREVIOUS_PAPER.objects.filter(Paper_Category="UPSC Mains General Studies Previous Year Question Papers")
    sub = PREVIOUS_PAPER.objects.filter(Paper_Category="UPSC Mains Optional Subjects Previous Year Question Papers")
    d = {"allcat": All_category(),"pre":pre,"gen":gen , "sub":sub,"essay":essay}
    return render(request,'previous_papers.html',d)


# #######  dynamic urls ################
def Course_detail(request,cat_id):
    catdata = COURSES.objects.get(id=cat_id)
    d = {"cat":catdata,"allcat": All_category()}
    return render(request,'course_detail_dynamic.html',d)

def NCERT_BOOK_DETAIL(request,nce_id):
    catdata = NCERT_CATEGORY.objects.get(id=nce_id)
    ncbook = NCERT_BOOKS.objects.filter(book_category=catdata)
    cat = NCERT_CATEGORY.objects.all()
    booknamss = NCERT_BOOKS.objects.all()
    booknam = booknamss[:10]
    d = {"cat":catdata,"allcat": All_category(),"ncbook":ncbook,"cat":cat,"booknam":booknam}
    return render(request,'dynamic_ncrt_bookdetail.html',d)

def YOJANA_DETAIL(request,yoj_id):
    catdata = YOJANA_CATEGORY.objects.get(id=yoj_id)
    ncbook = YOJANA_PDF.objects.filter(book_category=catdata)
    cate = YOJANA_CATEGORY.objects.all()
    buk = YOJANA_PDF.objects.all()
    booknam = buk[:10]
    d = {"cat":catdata,"allcat": All_category(),"ncbook":ncbook,"cate":cate,"booknam":booknam}
    return render(request,'dynamic_yojana_detail.html',d)

def YOJANA_SEARCH(request):
    cat = YOJANA_CATEGORY.objects.all()
    buk = YOJANA_PDF.objects.all()
    booknam = buk[:10]
    query = request.GET['key']
    boosear = YOJANA_PDF.objects.filter(Book_name__icontains=query)
    d = {"allcat": All_category(), "cat": cat, "booknam": booknam,"boosear":boosear}
    return render(request,'yojana_search.html',d)

######         admin  page             ########

def ADINDEX(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            email = request.POST['emai']
            subject = request.POST['subj']
            content = request.POST['msg']
            msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
            g = {'subject': subject, 'content': content}
            html = get_template('email4.html').render(g)
            msg.attach_alternative(html, 'text/html')
            msg.send()
            return redirect('admin_index')
        con = CONTACT_US.objects.all().order_by('-id')
        cont = con[:5]
        enq = HOME_ENQUIRY.objects.all().order_by('-id')
        enqq = enq[:5]
        emet = HOME_MEET_FACULTY.objects.all().order_by('-id')
        emettt = emet[:5]
        cour = COURSES.objects.all().order_by('-id')
        book = NCERT_BOOKS.objects.all().order_by('-id')
        buk = book[:7]
        prev = PREVIOUS_PAPER.objects.all().order_by('-id')
        pev = prev[:7]
        d = {"allcat": All_category(),"cont":cont,"enqq":enqq,"emettt":emettt,"cour":cour,"pev":pev,"buk":buk}
        return render(request, 'admin_index.html',d)

def CONTACT_USS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        co = CONTACT_US.objects.all()
        d ={"co":co,"allcat": All_category()}
        return render(request, 'admin_contact_us.html',d)

def AD_PGSTS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            PGSTS.objects.update(content=cname)
            return redirect('ad_pgsts')
        pg = PGSTS.objects.get(id=1)
        d = {"pg":pg,"allcat": All_category()}
        return render(request, 'admin_pgsts.html',d)

def ADMIN_ADD_COURSE(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            names = request.POST['nam']
            filname = request.POST['fulnam']
            COURSES.objects.create(content=cname,name=names,full_name=filname)
            return redirect('admin_index')
        d = {"allcat": All_category()}
        return render(request, 'admin_add_course.html',d)

def AD_MGSTS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            MGSTS.objects.update(content=cname)
            return redirect('ad_mgsts')
        pg = MGSTS.objects.get(id=1)
        d = {"pg":pg,"allcat": All_category()}
        return render(request, 'admin_mgsts.html',d)

def AD_PAGE_NOT_FOUND(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        d = {"allcat": All_category()}
        return render(request, 'admin_page_not_found.html',d)

def AD_ADMISSION_PRO(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            ADMISSION_PRO.objects.update(content=cname)
            return redirect('ad_mgsts')
        pg = ADMISSION_PRO.objects.get(id=1)
        d = {"pg":pg,"allcat": All_category()}
        return render(request, 'admin_admission_procedure.html',d)

def AD_FEE_PRECUMMAIN(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            FEE_STRUCTURES.objects.update(content=cname)
            return redirect('admin_fee_precummain')
        pre = FEE_STRUCTURES.objects.get(id= 1)
        d = {"pre":pre,"allcat": All_category()}
        return render(request, 'admin_fee_precummain.html',d)

def AD_FEE_OPTIONAL(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            FEE_STRUCTURES.objects.update(content=cname)
            return redirect('admin_fee_optionalpap')
        premil = FEE_STRUCTURES.objects.get(id= 3)
        d = {"premil":premil,"allcat": All_category()}
        return render(request, 'admin_fee_optionalpap.html',d)

def AD_FEE_GENSTUDIES(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            FEE_STRUCTURES.objects.update(content=cname)
            return redirect('admin_fee_genstudies')
        main = FEE_STRUCTURES.objects.get(id= 2)
        d = {"main":main,"allcat": All_category()}
        return render(request, 'admin_fee_genstudies.html',d)


def ADMIN_ABOUT_CSEE(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            ABOUT_CSE.objects.update(content=cname)
            return redirect('admin_about_cse')
        pg = ABOUT_CSE.objects.get(id = 1)
        d = {"allcat": All_category(),"pg":pg}
        return render(request,'admin_about_cse.html',d)


def ADMIN_SYLLABUS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            cname = request.POST['txt']
            SYLLABUSS.objects.update(content=cname)
            return redirect('admin_syllabus')
        pg = SYLLABUSS.objects.get(id = 1)
        d = {"allcat": All_category(),"pg":pg}
        return render(request,'admin_syllabus.html',d)

def ADMIN_PREVIOUS_PAPERS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            if 'enquirey' in request.POST:
                s = request.POST
                cat = s['cat']
                yea = s['year']
                tit = s['title']
                pap1n = s['pap1nam']
                pap1p = request.FILES['pap1pdf']
                pap2n = s['pap2name']
                pap2p = request.FILES['pap2pdf']
                PREVIOUS_PAPER.objects.create(Paper_Category=cat,year=yea,name=tit,paper1_name=pap1n,paper2_name=pap2n,paper1_pdf=pap1p,paper2_pdf=pap2p)
                return redirect('admin_previous_papers')
        pre = PREVIOUS_PAPER.objects.filter(Paper_Category="UPSC Prelims Previous Year Question Papers")
        essay = PREVIOUS_PAPER.objects.filter(Paper_Category="Essay Previous Year Question Papers")
        gen = PREVIOUS_PAPER.objects.filter(Paper_Category="UPSC Mains General Studies Previous Year Question Papers")
        sub = PREVIOUS_PAPER.objects.filter(Paper_Category="UPSC Mains Optional Subjects Previous Year Question Papers")
        d = {"allcat": All_category(), "pre": pre, "gen": gen, "sub": sub, "essay": essay}
        return render(request,'admin_previous_papers.html',d)

def ADMIN_DEMO_IMG(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            if 'enquirey' in request.POST:
                ename = request.FILES['imgsd']
                DEMO_IMG.objects.create(image=ename)
                return redirect('admin_demo_img')
        pg = DEMO_IMG.objects.all().order_by('-id')
        d = {"allcat": All_category(),"pg":pg}
        return render(request,'admin_demo_img.html',d)



def ADMIN_HOME(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            d = request.POST
            tit = d['title']
            Videos.objects.create(video=tit)
        enq = HOME_ENQUIRY.objects.all()
        vid = Videos.objects.all()
        meet = HOME_MEET_FACULTY.objects.all()
        d = {"allcat": All_category(), "enq": enq,"meet":meet,"vid":vid}
        return render(request,'admin_home.html',d)

def ADMIN_NCRT_BOOKS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            if 'bact' in request.POST and request.FILES:
                catnam = request.POST['nam']
                catimg = request.FILES['pap2pdf']
                NCERT_CATEGORY.objects.create(name=catnam,category_image=catimg)
                return redirect('admin_ncert_book')
            elif 'book' in request.POST:
                bcat = request.POST['cat']
                bookcat = NCERT_CATEGORY.objects.get(name=bcat)
                bnam = request.POST['bname']
                bimage = request.FILES['bimg']
                bpdfs = request.FILES['bpdf']
                NCERT_BOOKS.objects.create( book_category=bookcat,Book_name=bnam,Book_image=bimage,Book_pdf=bpdfs)
                return redirect('admin_ncert_book')
        cat = NCERT_CATEGORY.objects.all()
        d = {"allcat": All_category(),"cat":cat}
        return render(request,'admin_ncert_book.html',d)

def ADMIN_YOJANA_BOOKS(request):
    if not request.user.is_authenticated:
        return redirect('Login')
    else:
        if request.method == "POST":
            if 'bact' in request.POST and request.FILES:
                catnam = request.POST['nam']
                catimg = request.FILES['pap2pdf']
                YOJANA_CATEGORY.objects.create(name=catnam,category_image=catimg)
                return redirect('admin_yojana_book')
            elif 'book' in request.POST:
                bcat = request.POST['cat']
                bookcat = YOJANA_CATEGORY.objects.get(name=bcat)
                bnam = request.POST['bname']
                bimage = request.FILES['bimg']
                bpdfs = request.FILES['bpdf']
                YOJANA_PDF.objects.create( book_category=bookcat,Book_name=bnam,Book_image=bimage,Book_pdf=bpdfs)
                return redirect('admin_yojana_book')
        cat = YOJANA_CATEGORY.objects.all()
        d = {"allcat": All_category(),"cat":cat}
        return render(request,'admin_yojana_book.html',d)
###    admin dynamic  ####


def ADMIN_BOOK_DYNAMIC(request,bcd_id):
    catdata = NCERT_CATEGORY.objects.get(id=bcd_id)
    ncbook = NCERT_BOOKS.objects.filter(book_category=catdata)
    d = {"ncbook":ncbook,"allcat": All_category()}
    return render(request,'admin_ncert_book_dynamic.html',d)

def ADMIN_YOJANA_DYNAMIC(request,yoj_id):
    catdata = YOJANA_CATEGORY.objects.get(id=yoj_id)
    ncbook = YOJANA_PDF.objects.filter(book_category=catdata)
    d = {"ncbook":ncbook,"allcat": All_category()}
    return render(request,'admin_yojana_book_dynamic.html',d)

def ADMIN_Course_detail(request,adc_id):
    catdata = COURSES.objects.get(id=adc_id)
    if request.method == "POST":
        cname = request.POST['txt']
        catdata.content = cname
        catdata.save()
        return redirect('admin_home')
    d = {"cat":catdata,"allcat": All_category()}
    return render(request,'admin_course_detail.html',d)

def ADMIN_YOUTUBE_GALLERY(request):
    d = {"allcat": All_category()}
    return render(request,'admin_youtube_gallery.html',d)

def ADMIN_GOOGLE_REVIEW(request):
    d = {"allcat": All_category()}
    return render(request,'admin_google_review.html',d)

#####   admin delete ####

def PREVIOUS_PAPAERS_DELETE(request,prev_id):
    PREVIOUS_PAPER.objects.get(id=prev_id).delete()
    return redirect("admin_previous_papers")

def BOOK_CAT_DELETE(request,book_id):
    NCERT_CATEGORY.objects.get(id=book_id).delete()
    return redirect("admin_ncert_book")

def BOOKS_DELETE(request,bookdel_id):
    NCERT_BOOKS.objects.get(id=bookdel_id).delete()
    return redirect("admin_ncert_book")

def YOJANA_CAT_DELETE(request,yoj_id):
    YOJANA_CATEGORY.objects.get(id=yoj_id).delete()
    return redirect("admin_yojana_book")

def YOJANA_DELETE(request,yojdel_id):
    YOJANA_PDF.objects.get(id=yojdel_id).delete()
    return redirect("admin_yojana_book")

def YOUTUBE_DELETE(request,youdel_id):
    Videos.objects.get(id=youdel_id).delete()
    return redirect("admin_home")

def ADMIN_COURSE_DELETE(request,adc_id):
    COURSES.objects.get(id=adc_id).delete()
    return redirect("admin_index")