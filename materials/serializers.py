from rest_framework import serializers
from materials.models import Handout

class HandoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handout
        fields = ('id', 'created', 'updated', 'text', 'words', 'definitions', 'user', 'score', 'title', 'directions', 'display_words', 'display_definitions', 'column_order', 'image_url')
