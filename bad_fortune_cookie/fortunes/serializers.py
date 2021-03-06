from django.contrib.auth.models import User, Group
from bad_fortune_cookie.fortunes.models import Fortune
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

# begin JTK work/switching stuff up
class FortuneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fortune
        fields = ('genre', 'fortune', 'author','id')
