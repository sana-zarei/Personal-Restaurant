from django.db import models
from django.urls import reverse
from django.utils import timezone
# from ckeditor.fields import RichTextField

# Managers
class ArticleManager(models.Manager):
    def publishd(self):
        return self.filter(status="p")


# 1 - Category # 1 - Category # 1 - Category # 1 - Category # 1 - Category
class Category(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '02 - Category'


# 2 - Article # 2 - Article # 2 - Article # 2 - Article # 2 - Article # 2 - Article
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE, editable=False, default=1)
    title = models.CharField(max_length = 150)
    slug = models.SlugField(unique=True, max_length=100)
    category = models.ManyToManyField(Category,related_name="articles")
    description = models.TextField()
    image = models.ImageField(upload_to="Blog_Image")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (('d','Draft'),('p','Published'))
    status = models.CharField(max_length = 1,choices=STATUS_CHOICES)

    def category_publishd(self):
        return self.category.filter(status=True)

    objects = ArticleManager()
    
    def __str__(self):
        return self.title     

    class Meta:
        verbose_name_plural = '01 - Article'


# 3 - Comment # 3 - Comment # 3 - Comment # 3 - Comment # 3 - Comment # 3 - Comment 
class Comment(models.Model): 
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="comments")
    user = models.CharField(max_length = 50)
    content = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=False) 

    class Meta:
        verbose_name_plural = '03 - Comment'
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.user, self.article) 


# 4 - Reply_Comment Reply_Comment Reply_Comment Reply_Comment Reply_Comment 
class Reply_Comment(models.Model): 
    comments = models.ForeignKey(Comment,on_delete=models.CASCADE,related_name="recomments")
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE, editable=False, default=1)
    content = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name_plural = '04 - Reply Comment'
        ordering = ('created',) 

    def __str__(self): 
        return 'Comment Reply by Admin {} --> on the : {}'.format(self.user, self.comments) 