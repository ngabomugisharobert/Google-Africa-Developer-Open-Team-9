from rest_framework import serializers
from complaint.models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'title', 'crime', 'complainant', 'description', 'status', 'location')