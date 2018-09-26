from django.conf.urls import url
# from django.conf.urls.static import static
import goods.views
# from django.conf import settings


urlpatterns = [
    url(r'^$', goods.views.AllThingsList.as_view(), name='goods'),
    url(r'^thing/(?P<pk>\d+)$', goods.views.ThingDetail.as_view(), name='thing_detail'),
]
