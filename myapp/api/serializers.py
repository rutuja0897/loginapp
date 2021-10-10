from myapp.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['uname','uemail','upassword','uconfirmpassword','uaddress']