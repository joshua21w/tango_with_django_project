from django.contrib import admin
from rango.models import Category, Page, HomePage
from rango.models import UserProfile,SignUpForEmail

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

    # Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
        prepopulated_fields = {'slug': ('name',)}

class HomePageAdmin(admin.ModelAdmin):
    list_display = ('Heading', 'subheading', 'text')

class SignUpAdmin(admin.ModelAdmin):
        list_display = ('email','empty','created','day')

    # Update the registeration to include this customised interface



admin.site.register(Category, CategoryAdmin)
admin.site.register(HomePage, HomePageAdmin)

admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

admin.site.register(SignUpForEmail,SignUpAdmin)


