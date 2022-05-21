from rest_framework import serializers
from todos.models import Todo
from hadith.models import Hadith


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description'
        )
        model = Todo

class HadithSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'parent',
            'title',
            'subtitle',
            'description_bn',
            'description_arb',
            'description_eng'

        )
        model = Hadith

class HadithTitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'parent',
            'title',

        )
        model = Hadith
