from rest_framework import viewsets
from . models import Company, Office
from .serializers import CompanySerializer
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response


class CompanyListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_serializer_context(self):
        return {"pk": self.kwargs.get('pk', None)}


class HeadquarterUpdateView(UpdateAPIView):
    queryset = Company.objects.all()
    lookup_field = 'pk'
    serializer_class = CompanySerializer

    def get_serializer_context(self):
        office_id = self.request.data.get('office_id', None)
        return {"office_id": office_id}