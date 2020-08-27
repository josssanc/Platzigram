"""User admin classes"""
#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models 
from users.models import Profile
from posts.models import Post
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk','user','profile','title','photo','created','modified')
    list_display_links = ('pk','user')
    list_editable = ('title','photo')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk','user','phone_number','website','picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website','picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    
    list_filter = (
        'user__is_active',
        'user__is_staff',
        #'created' ,
        'modified'
        
    )
    fieldsets = (
        ('Profile', {
            'fields': (
                ('user','picture'),),
        }),
        ('Extra info',{
            'fields': (
                (('website'),('phone_number')),
                ('biography')
            )
        }),
        ('Metadata',{
            'fields':(('modified'),),
        })
    )
    readonly_fields = ('modified',)

class ProfileInline(admin.StackedInline):
    """Profile in -line admin dor users.""" 
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile to base user admin"""
    inlines = (ProfileInline,)
    
admin.site.unregister(User)
admin.site.register(User,UserAdmin)

