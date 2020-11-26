from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            "password":{
                "write_only":True,
                "style":{"input_type":"password"}
            },
        }

    def create(self, validated_data):
        user = models.UserProfile.objects.create_user(
            name = validated_data.get("name"),
            email = validated_data.get("email"),
            password = validated_data.get("password")
        )

        return user

    def update(self, instance, validated_data):
        print(instance)
        if("password" in validated_data):
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)



class ProfileFeedSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','user_profile','status_text','created_on')
        model = models.UserProfileFeed
        extra_kwargs = {"user_profile":{"read_only":True}}

    