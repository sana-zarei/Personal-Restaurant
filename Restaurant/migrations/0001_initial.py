# Generated by Django 4.0.3 on 2022-04-23 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greetings_1', models.CharField(help_text='25 Char', max_length=25, verbose_name='Greetings')),
                ('greetings_2', models.CharField(max_length=25, verbose_name='Greetings')),
                ('greetings_3', models.TextField(max_length=100, verbose_name='Greetings')),
                ('image1', models.ImageField(upload_to='About/', verbose_name='Image')),
                ('title1', models.CharField(max_length=25, verbose_name='Title')),
                ('description_1', models.TextField(max_length=350, verbose_name='Description')),
                ('image2', models.ImageField(upload_to='About/', verbose_name='Image')),
                ('title2', models.CharField(max_length=25, verbose_name='Title')),
                ('description_2', models.TextField(max_length=170, verbose_name='Description')),
                ('name', models.CharField(max_length=25)),
                ('description_3', models.TextField(max_length=170, verbose_name='Description')),
                ('image3', models.ImageField(upload_to='About/', verbose_name='Image')),
                ('image4', models.ImageField(upload_to='About/', verbose_name='Image')),
                ('image5', models.ImageField(upload_to='About/', verbose_name='Image')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '01 - About',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to='Audio/')),
            ],
            options={
                'verbose_name_plural': '14 - Audio',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name_plural': '03 - Category',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '13 - Contact',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=35, verbose_name='name')),
                ('subject', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=35)),
                ('message', models.TextField(max_length=250)),
                ('is_read', models.BooleanField(default=False, verbose_name='Read / Unread')),
            ],
            options={
                'verbose_name': 'CONTACT US',
                'verbose_name_plural': '12 - Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Event/')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(max_length=250)),
            ],
            options={
                'verbose_name_plural': '09 - Event',
            },
        ),
        migrations.CreateModel(
            name='Event_Bottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField(max_length=250, verbose_name='Description')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '10 - Event_Bottom',
            },
        ),
        migrations.CreateModel(
            name='Food_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Food_Menu/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': '04 - Food Menu',
            },
        ),
        migrations.CreateModel(
            name='Popular_Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Popular_Dishes/')),
                ('title', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '08 - Popular_Dishes',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=350)),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': '05 - Reservation Item',
            },
        ),
        migrations.CreateModel(
            name='Reservation_Received',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('count', models.CharField(max_length=50)),
                ('table_number', models.CharField(max_length=50)),
                ('is_read', models.BooleanField(default=False, verbose_name='Read / Unread')),
            ],
            options={
                'verbose_name': 'Reservation_Received',
                'verbose_name_plural': '06 - Reservation Received',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Service/')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=150)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': '07 - Service',
            },
        ),
        migrations.CreateModel(
            name='Special_Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Special_Dishes/')),
                ('title', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
            ],
            options={
                'verbose_name_plural': '02 - Special Dishes',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=250)),
                ('image', models.ImageField(upload_to='Testimonial/')),
            ],
            options={
                'verbose_name_plural': '11 - Testimonial',
            },
        ),
        migrations.CreateModel(
            name='Reservation_Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=20)),
                ('reservation_received', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.reservation_item')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation_Table_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=20)),
                ('reservation_received', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.reservation_item')),
            ],
        ),
        migrations.AddConstraint(
            model_name='reservation_received',
            constraint=models.UniqueConstraint(fields=('date', 'time', 'table_number'), name='unique_reserve'),
        ),
        migrations.AddField(
            model_name='reservation_date',
            name='reservation_received',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.reservation_item'),
        ),
        migrations.AddField(
            model_name='reservation_count',
            name='reservation_received',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.reservation_item'),
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_key',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.contact'),
        ),
        migrations.AddField(
            model_name='food_menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.category'),
        ),
    ]
