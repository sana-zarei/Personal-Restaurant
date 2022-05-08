from ast import Import
from django.db import IntegrityError
from django.shortcuts import render
from django.http import JsonResponse
from .models import About,Special_Dishes,Category,Food_Menu,Reservation_Date,Reservation_Time,Reservation_Count,Reservation_Table_Number,Reservation_Received,Service,Popular_Dishes,Blog_Bottom,Testimonial,ContactUs,Contact,Profile,Audio
from .forms import ContactUsForm,ReservationForm
from Blog.models import Article

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'



def home(request):
    about = About.objects.latest('updated')
    special_Dishes = Special_Dishes.objects.all()
    category = Category.objects.filter()
    food_menu = Food_Menu.objects.all()
    reservation_date = Reservation_Date.objects.all()
    reservation_time = Reservation_Time.objects.all()
    reservation_count = Reservation_Count.objects.all()
    reservation_table_number = Reservation_Table_Number.objects.all()
    service = Service.objects.all()
    popular_dishes = Popular_Dishes.objects.all()
    article = Article.objects.filter(status="p").order_by('-publish')[:3]
    event_bottom = Blog_Bottom.objects.latest('updated')
    testimonial = Testimonial.objects.all()
    contact = Contact.objects.latest('updated')
    profile = Profile.objects.all()
    audio = Audio.objects.latest('id')

    context = {
        'about':about,
        'special_Dishes':special_Dishes,
        'category':category,
        'food_menu':food_menu,
        'reservation_date':reservation_date,
        'reservation_time':reservation_time,
        'reservation_count':reservation_count,
        'reservation_table_number':reservation_table_number,
        'service':service,
        'popular_dishes':popular_dishes,
        'article':article,
        'event_bottom':event_bottom,
        'testimonial':testimonial,
        'contact':contact,
        'form1':ReservationForm,
        'form2':ContactUsForm,
        'profile':profile,
        'audio':audio,
    }

    if request.method == "POST" and request.POST.get('name'):
        reservation = Reservation_Received()
        reservation.name = request.POST.get('name')
        reservation.date = request.POST.get('date')
        reservation.time = request.POST.get('time')
        reservation.count = request.POST.get('count')
        reservation.table_number = request.POST.get('table_number')
        try:
            reservation.save()
            return JsonResponse({'msg':'Success'})
        except IntegrityError:
            return JsonResponse({'msg':'Error'})
            # return HttpResponseRedirect('/duplicate')

    if request.method == "POST" and request.POST.get('name2'):
        contactus = ContactUs()
        contactus.name2 = request.POST.get('name2')
        contactus.subject = request.POST.get('subject')
        contactus.email = request.POST.get('email')
        contactus.message = request.POST.get('message')
        contactus.save()
        return JsonResponse({'msg2':'Success'})

    return render(request, 'Restaurant/home.html',context)



# def home2(request):

#     return render(request, 'home2.html',{})
