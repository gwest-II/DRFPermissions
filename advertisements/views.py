from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from . import filters
from .models import Advertisement
from .permissions import IsOwnerOrReadOnly
from .serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = filters.AdvertisementFilter
    permission_classes = [IsOwnerOrReadOnly]
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

