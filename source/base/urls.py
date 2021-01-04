from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _(f'{settings.SITE["NAME"]} administration')
admin.site.site_title = _(f'{settings.SITE["DESCRIPTION"]} administration')
admin.site.index_title = _("Dashboard")

urlpatterns = i18n_patterns(
    path("admin/", admin.site.urls), prefix_default_language=False
)

urlpatterns += [
    path("", include("apps.resume.urls")),
]
# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
