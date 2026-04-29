from rest_framework import viewsets, request
from rest_framework.permissions import IsAuthenticated

from ....models.skill import Skill,ProfileSkill
from ..permissions import IsActivatedUser
from ..serializers.skillserializers import SkillSerializer,ProfileSkillReadSerializer,ProfileSkillWriteSerializer
from rest_framework.filters import SearchFilter

class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = [IsActivatedUser, IsAuthenticated]


    def get_queryset(self):
        return ProfileSkill.objects.select_related("skill").filter(
            profile=self.request.user.profile
        )

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return ProfileSkillWriteSerializer
        return ProfileSkillReadSerializer

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)


class SkillListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title"]