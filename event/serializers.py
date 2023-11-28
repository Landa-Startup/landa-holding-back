from rest_framework.serializers import ModelSerializer,PrimaryKeyRelatedField
from .models import Event,Images,EventForm
from accounts.serializers import UserSerializer

class ImageSerilizers(ModelSerializer):
    event = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Images
        fields = ('image','event')
        read_only_fields = ['id']
        

class EventListSerializers(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['id','craeted_at']
    speakers = UserSerializer(many=True,read_only=True)

class EventDetailsSerializers(ModelSerializer):
    speakers = UserSerializer(many=True,read_only=True)
    images = ImageSerilizers(many=True,read_only=True,source='event_images')
    class Meta:
        model = Event
        fields = ('id','start_date','end_date','description','banner','video','slug','speakers','images')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }
    speakers = UserSerializer(many=True,read_only=True)
    images = ImageSerilizers(many=True,read_only=True,source='event_images')

class EventFormSerializers(ModelSerializer):
    class Meta:
        model = EventForm
        fields = "__all__"
        read_only_fields = ['id','craeted_at']
