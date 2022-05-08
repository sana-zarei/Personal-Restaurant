from django.db.models import Count
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article, Category
from Restaurant.models import Profile,Contact
from .forms import CommentForm


def home(request):
    articles_list = Article.objects.filter(status="p").order_by('-publish')
    
    paginator = Paginator(articles_list, 6)
    page = request.GET.get('page',1)
    profile = Profile.objects.all()
    contact = Contact.objects.latest('updated')

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        "articles":result,
        "profile":profile,
        "contact":contact,
    }

    return render(request, 'Blog/blog.html',context)



def detail(request, slug):

    article = get_object_or_404(Article, slug = slug, status="p")
    comments = article.comments.filter(active=True)

    context = {
        # "article":Article.objects.filter(slug = slug),
        "article" : article,
        "comments" : comments,
        "form" : CommentForm,
        "categories" : Category.objects.filter(articles__status='p').annotate(posts_count=Count('articles')),
        "category" : Category.objects.filter(status=True),
        "profile" : Profile.objects.all(),
        "contact" : Contact.objects.latest('updated')
    }

    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            newcomment = commentform.save(commit=False)
            newcomment.article = article
            newcomment.save()
    else:
        commentform = CommentForm()

    return render(request, 'Blog/blog-detail.html',context)



def category(request, slug):
    category = get_object_or_404(Category, slug = slug, status=True)
    articles_list = category.articles.publishd()
    paginator = Paginator(articles_list, 9)
    articles = request.GET.get('page',1)

    try:
        result = paginator.page(articles)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    context = {
        "category" : category,
        "articles" : result,
    }

    return render(request, 'Blog/category.html',context)