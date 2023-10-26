from rest_framework import serializers

from CCD.models import NewsMonitoring


class MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsMonitoring
        fields = ["date", "description", "area_tag", "topic_tag",
                 "link", "source", "source_tag", "subject", "additional_info",
                 "type_of_threat", "evaluation", "grand_narrative", "narrative", "status",
                 "suggestions_for_response", "country", "ua_region", "index"]

    def create(self, validated_data):
        news = NewsMonitoring(**validated_data)
        news.save()
        return news


'''
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, max_length=15)

    class Meta:
        model = User
        fields = ("name", "email", "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data, confirmed=False)
        user.set_password(password)
        user.save()
        return user

    def validate_password(self, value):
        if not value:
            raise serializers.ValidationError("Password can`t be blank", code="password_cant_be_blank")
        numbers = sum(c.isdigit() for c in value)
        lowercase_letters = sum(c.islower() for c in value)
        uppercase_letters = sum(c.isupper() for c in value)
        spaces = sum(c.isspace() for c in value)
        symbols = len(value) - numbers - lowercase_letters - uppercase_letters
        if spaces > 0:
            raise serializers.ValidationError("Password can`t contain spaces", code="password_cant_contain_spaces")
        if all([numbers, lowercase_letters, uppercase_letters, symbols]):
            return value
        raise serializers.ValidationError(
            "Password must contain lowercase and uppercase letters, a number and one of the characters !@#$%&*",
            code="password_must_contain_upper_lower_number_and_symbol",
        )
'''
