from django.contrib import admin

# Register your models here.
from SiteConfig.models import HeaderNotice, AboutSite, FriendUrl, Contact

admin.site.register(HeaderNotice)
admin.site.register(AboutSite)
admin.site.register(FriendUrl)
admin.site.register(Contact)