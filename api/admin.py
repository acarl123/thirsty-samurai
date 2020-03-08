from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from api.models import Profile, LegacyUser, InterestedUser, Tag, Event, Category

admin.site.register(LegacyUser)
admin.site.register(InterestedUser)
admin.site.register(Tag)
admin.site.register(Category)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class TagsInLine(admin.StackedInline):
    model = Event.tags.through
    verbose_name = u"Tag"
    verbose_name_plural = u"Tags"

class CategoryInLine(admin.StackedInline):
    model = Category
    verbose_name = u"Category"
    verbose_name_plural = u"Categories"

class CustomEventAdmin(admin.ModelAdmin):
    model = Event
    inlines = (TagsInLine,)

admin.site.register(Event, CustomEventAdmin)