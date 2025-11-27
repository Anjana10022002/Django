from rest_framework import serializers
from .models import Note, Product

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Note
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Product
        fields = '__all__'