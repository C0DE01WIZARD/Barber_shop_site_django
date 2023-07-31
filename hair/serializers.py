from rest_framework.serializers import ModelSerializer

from hair.models import Hairstyles


class HairsSerializers(ModelSerializer):

    class Meta:
        model = Hairstyles
        fields = ['type', 'price']