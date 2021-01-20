from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Team, PortfolioCategory, Portfolio, PortfolioImage, Blog

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(PortfolioCategory)
admin.site.register(Portfolio)
admin.site.register(PortfolioImage)
admin.site.register(Blog)
