from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

app_name = "accounting"
urlpatterns = [
    path('', include('accounting.apps.connect.urls',
        namespace="connect")),
    path('books/', include('accounting.apps.books.urls',
        namespace="books")),
    path('people/', include('accounting.apps.people.urls',
        namespace="people")),
    path('reports/', include('accounting.apps.reports.urls',
        namespace="reports")),

    # third party
    path('select2/', include('django_select2.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
