from django.contrib import admin
from .models import Item, UserProfile

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status')
    actions = ['mark_as_available']

    def mark_as_available(self, request, queryset):
        for item in queryset:
            if not item.status:
                item.status = True
                item.save()
                # Add 10 points when approved
                profile = UserProfile.objects.get(user=item.user)
                profile.points += 10
                profile.save()
        self.message_user(request, "Selected items marked as available and points added.")

    mark_as_available.short_description = "Mark selected items as available and assign points"

admin.site.register(UserProfile)
