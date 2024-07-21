from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'phone', 'fullname', 'church', 'age', 'gender','bio', 'password','profile_image']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            phone=validated_data['phone'],
            fullname=validated_data['fullname'],
            church=validated_data.get('church'),
            age=validated_data['age'],
            bio=validated_data['bio'],
            gender=validated_data['gender'],
            profile_image=validated_data['profile_image'],
            username = validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')

        if not (email or phone):
            raise serializers.ValidationError('An email or phone number is required to log in.')

        user = None
        if email:
            user = User.objects.filter(email=email).first()
        elif phone:
            user = User.objects.filter(phone=phone).first()

        if user is None or not user.check_password(password):
            raise serializers.ValidationError('Invalid credentials.')

        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','phone','fullname','church','age','gender','profile_image','bio','role']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','phone','fullname','church','age','gender','profile_image','bio','role','username']

class UserRoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['roles']

class UserSuperRoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_staff']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','fullname','church','age','profile_image','bio']