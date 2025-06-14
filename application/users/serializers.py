from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import CharField, ModelSerializer, ValidationError

User = get_user_model()

class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True, validators=[validate_password])
    password2 = CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'password2', 'role')

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password":"passwords do not match"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop("password2")
        return super().create(validated_data)
    


