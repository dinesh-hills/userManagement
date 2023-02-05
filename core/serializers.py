import datetime
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(method_name="calculate_age")

    def calculate_age(self, user: User):
        today = datetime.date.today()
        birthdate = user.dob
        age = today - birthdate

        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age = age - datetime.timedelta(days=365)

        # 365.25 accoutns for leap years
        return int(age.days / 365.25)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "gender",
            "dob",
            "age",
            "mobile_number",
            "address",
        ]


class ReportSerializer(serializers.Serializer):
    file_type = serializers.CharField()

    def validate_file_type(self, value):
        if not value in ["pdf", "xlsx"]:
            raise serializers.ValidationError("Only pdf or xlsx is allowed.")
        return value