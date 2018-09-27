from . models import Company, Office
from rest_framework import serializers

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ('street', 'postal_code', 'city', 'is_headquarter', 'monthly_rent')


    def to_representation(self, obj):
        fields = super(OfficeSerializer, self).to_representation(obj)
        if not self.context.get('pk', None):
            fields.pop('is_headquarter')
            fields.pop('monthly_rent')
        return fields 

class CompanySerializer(serializers.ModelSerializer):
    
    headquarter = serializers.SerializerMethodField('get_headquarter_office')
    rent = serializers.DecimalField(source='get_total_office_rent', decimal_places=2, max_digits=20)

    class Meta:
        model = Company
        fields = ('name', 'headquarter', 'rent')

    def get_headquarter_office(self, container):
        pk = self.context.get('pk')
        offices = Office.objects.filter(company=container) if pk else Office.objects.filter(company=container, is_headquarter=True)
        serializer = OfficeSerializer(instance=offices, many=True, context={'pk': pk})
        return serializer.data


    def update(self, instance, validated_data):
        office_id = self.context.get('office_id')
        try:
            new_headquarter_office = Office.objects.get(id=office_id, company=instance)
            offices = Office.objects.filter(company=instance, is_headquarter=True)            
            if offices:
                old_headquarter_office = offices.first()
                old_headquarter_office.is_headquarter = False
                old_headquarter_office.save()

            new_headquarter_office.is_headquarter = True
            new_headquarter_office.save()
        except Exception as e:
            raise serializers.ValidationError('Invalid office id for this company.')        
        return instance