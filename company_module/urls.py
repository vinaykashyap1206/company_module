from django.conf.urls import url, include
from rest_framework import routers
# import pdb;pdb.set_trace()
from organization_test_task import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyListViewSet, base_name='company')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^companies/(?P<pk>\d+)/update$', views.HeadquarterUpdateView.as_view(), name='update-company-headquarter'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
