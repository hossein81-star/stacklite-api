from rest_framework import serializers

from ....models.skill import Skill,ProfileSkill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["title","id"]

class ProfileSkillSerializer(serializers.ModelSerializer):
    title=serializers.CharField(source="skill.title")
    class Meta:
        model = ProfileSkill
        fields=["title","level"]