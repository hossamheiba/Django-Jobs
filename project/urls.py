
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/',include("django.contrib.auth.urls")),
    path('accounts/',include("accounts.urls",namespace="accounts")),
    path('admin/', admin.site.urls),
    path('jobs/',include("job.urls",namespace="jobs")),
    # path('home/',include("home.urls")),
    # path('contact-us/',include("contact.urls",namespace='contact-us')),
    # path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
    # path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)