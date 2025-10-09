from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path, re_path

from arches.app.views.plugin import PluginView

urlpatterns = [
    re_path(
        r"^plugins/application-area", PluginView.as_view(), name="application-area"
    ),
    re_path(
        r"^plugins/consultation-workflow",
        PluginView.as_view(),
        name="consultation-workflow",
    ),
    re_path(r"^plugins/site-visit", PluginView.as_view(), name="site-visit"),
    re_path(
        r"^plugins/correspondence-workflow",
        PluginView.as_view(),
        name="correspondence-workflow",
    ),
    re_path(
        r"^plugins/communication-workflow",
        PluginView.as_view(),
        name="communication-workflow",
    ),
    re_path(r"^plugins/init-workflow", PluginView.as_view(), name="init-workflow"),
]

handler400 = "arches.app.views.main.custom_400"
handler403 = "arches.app.views.main.custom_403"
handler404 = "arches.app.views.main.custom_404"
handler500 = "arches.app.views.main.custom_500"

# Ensure Arches core urls are superseded by project-level urls
urlpatterns.append(path("", include("arches.urls")))

# Adds URL pattern to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Only handle i18n routing in active project. This will still handle the routes provided by Arches core and Arches applications,
# but handling i18n routes in multiple places causes application errors.
if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))
