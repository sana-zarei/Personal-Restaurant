from django.db import models
from django.utils.safestring import mark_safe

# 1 - About Page 1 - About Page 1 - About Page 1 - About Page 1 - About Page
class About(models.Model):
    greetings_1 = models.CharField(max_length=25,help_text='25 Char',verbose_name="Greetings")
    greetings_2 = models.CharField(max_length=25,verbose_name="Greetings")
    greetings_3 = models.TextField(max_length=100,verbose_name="Greetings")
    image1 = models.ImageField(upload_to='About/',verbose_name="Image")
    title1 = models.CharField(max_length=25,verbose_name='Title')
    description_1 = models.TextField(max_length=350,verbose_name="Description")
    image2 = models.ImageField(upload_to='About/',verbose_name="Image")
    title2 = models.CharField(max_length=25,verbose_name="Title")
    description_2 = models.TextField(max_length=170,verbose_name="Description")
    name = models.CharField(max_length=25)
    description_3 = models.TextField(max_length=170,verbose_name="Description")
    image3 = models.ImageField(upload_to='About/',verbose_name="Image")
    image4 = models.ImageField(upload_to='About/',verbose_name="Image")
    image5 = models.ImageField(upload_to='About/',verbose_name="Image")
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '01 - About'

    def __str__(self):
        return self.name


# 2 - Special_Dishes Page # 2 - Special_Dishes Page # 2 - Special_Dishes Page # 2 - Special_Dishes Page # 2 - Special_Dishes Page
class Special_Dishes(models.Model):
    image = models.ImageField(upload_to='Special_Dishes/')
    title = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = '02 - Special Dishes'

    def __str__(self):
        return self.title


# 3 - Category Page 3 - Category Page 3 - Category Page 3 - Category Page 3 - Category Page
class Category(models.Model):
    name = models.CharField(max_length=35)

    class Meta:
        verbose_name_plural = '03 - Category'

    def __str__(self):
        return self.name


# 4 - Menu Page 4 - Menu Page 4 - Menu Page 4 - Menu Page 4 - Menu Page
class Food_Menu(models.Model):
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Food_Menu/')
    date = models.DateTimeField(auto_now_add=True)

    def show_photo(self):
        return mark_safe('<img src="{}" width="250" />'.format(self.image.url))

    class Meta:
        verbose_name_plural = '04 - Food Menu'

    def __str__(self):
        return self.title


# 5 - Reservation_Item # 5 - Reservation_Item # 5 - Reservation_Item # 5 - Reservation_Item
class Reservation_Item(models.Model):
    description = models.TextField(max_length=350)

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = '05 - Reservation Item'

    def __str__(self):
        return self.description

class Reservation_Date(models.Model):
    date = models.CharField(max_length=20)
    reservation_received = models.ForeignKey(Reservation_Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

class Reservation_Time(models.Model):
    time = models.CharField(max_length=20)
    reservation_received = models.ForeignKey(Reservation_Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.time

class Reservation_Count(models.Model):
    count = models.CharField(max_length=20)
    reservation_received = models.ForeignKey(Reservation_Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.count    

class Reservation_Table_Number(models.Model):
    table_number = models.CharField(max_length=20)
    reservation_received = models.ForeignKey(Reservation_Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.table_number


# 6 - Reservation_Received # 6 - Reservation_Received # 6 - Reservation_Received # 6 - Reservation_Received
DATE_OPTION = (('Saturday', 'Saturday'),('Sunday', 'Sunday'),('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),('Friday', 'Friday'))
TIME_OPTION = (('5 - 5.30 PM', '5 - 5.30 PM'),('5.30 - 6 PM', '5.30 - 6 PM'),('6 - 6.30 PM', '6 - 6.30 PM'),('6.30 - 7 PM', '6.30 - 7 PM'),('7 - 7.30 PM', '7 - 7.30 PM'),('7.30 - 8 PM', '7.30 - 8 PM'),('8 - 8.30 PM', '8 - 8.30 PM'),('8.30 - 9 PM', '8.30 - 9 PM'),
('9 - 9.30 PM', '9 - 9.30 PM'),('9.30 - 10 PM', '9.30 - 10 PM'),('10 - 10.30 PM', '10 - 10.30 PM'),('10.30 - 11 PM', '10.30 - 11 PM'),('11 - 11.30 PM', '11 - 11.30 PM'),('11.30 - 11.59 PM', '11.30 - 11.59 PM'))
COUNT_OPTION = (('1 Person', '1 Person'),('2 Person', '2 Person'),('3 Person', '3 Person'),('4 Person', '4 Person'),('5 Person', '5 Person'),('6 Person', '6 Person'),('7 Person', '7 Person'))
TABLE_OPTION = (('Table 1', 'Table 1'),('Table 2', 'Table 2'),('Table 3', 'Table 3'),('Table 4', 'Table 4'),('Table 5', 'Table 5'),('Table 6', 'Table 6'),('Table 7', 'Table 7'))
class Reservation_Received(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50, choices = DATE_OPTION)
    time = models.CharField(max_length=50, choices = TIME_OPTION)
    count = models.CharField(max_length=50, choices = COUNT_OPTION)
    table_number = models.CharField(max_length=50, choices = TABLE_OPTION)
    is_read = models.BooleanField(default=False , verbose_name='Read / Unread')

    def __str__(self):
        return "Reservation Received From" + " -----> " + self.name

    class Meta:
        verbose_name = 'Reservation_Received'
        verbose_name_plural = '06 - Reservation Received'
        # unique_together = ('date', 'time', 'table_number',)
        constraints = [models.UniqueConstraint(fields=['date', 'time', 'table_number'], name='unique_reserve')]


# 7 - Service Page 7 - Service Page 7 - Service Page 7 - Service Page 7 - Service Page
class Service(models.Model):
    image = models.ImageField(upload_to='Service/')
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '07 - Service'

    def __str__(self):
        return self.title


# 8 - Popular_Dishes Page # 8 - Popular_Dishes Page # 8 - Popular_Dishes Page # 8 - Popular_Dishes Page # 8 - Popular_Dishes Page
class Popular_Dishes(models.Model):
    image = models.ImageField(upload_to='Popular_Dishes/')
    title = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = '08 - Popular_Dishes'

    def __str__(self):
        return self.title



# 9 - Event_Bottom Page # 9 - Event_Bottom Page # 9 - Event_Bottom Page # 9 - Event_Bottom Page
class Blog_Bottom(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(max_length=250,verbose_name="Description")
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '09 - Blog Bottom'

    def __str__(self):
        return self.title


# 10 - Testimonial Page # 10 - Testimonial Page # 10 - Testimonial Page # 10 - Testimonial Page
class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='Testimonial/')

    class Meta:
        verbose_name_plural = '10 - Testimonial'

    def __str__(self):
        return self.name


# 11 - ContactUs Page 11 - ContactUs Page 11 - ContactUs Page 11 - ContactUs Page 11 - ContactUs Page
class ContactUs(models.Model):
    name2 = models.CharField(verbose_name="name",max_length=35)
    subject = models.CharField(max_length=30)
    email = models.EmailField(max_length=35)
    message = models.TextField(max_length=250)
    is_read = models.BooleanField(default=False , verbose_name='Read / Unread')

    def __str__(self):
        return "Message From" + " -----> " + self.email

    class Meta:
        verbose_name = 'CONTACT US'
        verbose_name_plural = '11 - Contact Us'


# 12 - Contact Page 12 - Contact Page 12 - Contact Page 12 - Contact Page 12 #  - Contact Page
class Contact(models.Model):
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    address = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = '12 - Contact'

    def __str__(self):
        return self.email


# 12 - Inline Profile Page # 12 - Inline Profile Page # 12 - Inline Profile Page # 12 - Inline Profile Page # 12 - Inline Profile Page
class Profile(models.Model):
    contact_key = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 13 - Audio # 13 - Audio # 13 - Audio # 13 - Audio # 13 - Audio
class Audio(models.Model):
    audio = models.FileField(upload_to='Audio/')

    def __str__(self):
        return str(self.audio)

    class Meta:
        verbose_name_plural = '13 - Audio'