from django.contrib import admin
from .models import Article, Category, Comment, Reply_Comment
from django.utils.html import format_html


# - Admin Panel Actions
@admin.action(description='Mark selected Post as Published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')

@admin.action(description='Mark selected Post as Drafted')
def make_drafted(modeladmin, request, queryset):
    queryset.update(status='d')

@admin.action(description='Mark selected Comment as Active')
def make_Active(modeladmin, request, queryset):
    queryset.update(active=True)

@admin.action(description='Mark selected Comment as DeActive')
def make_DeActive(modeladmin, request, queryset):
    queryset.update(active=False)

# -------------------------------------------------------------------------------

# 1 - Category  # 1 - Category # 1 - Category # 1 - Category # 1 - Category 
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug','status']
    list_filter = ['status',]
    list_editable = ['status']
    search_fields = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}


# 2 - Article # 2 - Article # 2 - Article # 2 - Article # 2 - Article # 2 - Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author','title','publish','category_to_str','image_tag','status']
    list_display_links = ['author','title']
    list_filter = ['publish','status','author','category']
    list_editable = ['status',]
    search_fields = ['title','description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status','publish']
    readonly_fields = ['image_tag']
    actions = [make_published,make_drafted]

    def image_tag(self, obj):
        return format_html('<img src="{}" width="110px" height="85x"/>'.format(obj.image.url))
    image_tag.short_description = 'Image Preview'

    def category_to_str(self, obj):
        return [category.title for category in obj.category_publishd()]
    category_to_str.short_description = "Category"

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


# 3 - Comment # 3 - Comment # 3 - Comment # 3 - Comment # 3 - Comment # 3 - Comment 
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','article','created','active']
    list_filter = ['active','created','updated']
    list_editable = ['active']
    actions = [make_Active,make_DeActive]
    # readonly_fields = ['user','content','created']

    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False


# 4 - Reply_Comment # 4 - Reply_Comment # 4 - Reply_Comment # 4 - Reply_Comment # 4 - Reply_Comment 
@admin.register(Reply_Comment)
class Reply_CommentAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
