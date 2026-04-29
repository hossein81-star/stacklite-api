from rest_framework import serializers

from ....models.skill import Skill,ProfileSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["title","id"]

# class ProfileSkillSerializer(serializers.ModelSerializer):
#     title=serializers.CharField(source="skill.title")
#     class Meta:
#         model = ProfileSkill
#         fields=["title","level"]

class ProfileSkillReadSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="skill.title", read_only=True)

    class Meta:
        model = ProfileSkill
        fields = ["id", "title", "level"]


class ProfileSkillWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSkill
        fields = ["skill", "level"]

