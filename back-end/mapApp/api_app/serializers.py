from rest_framework import serializers

from .models import ItsmIncidents, Comments


class CommentSCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("user", "new", "text")


class ItsmIncidentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItsmIncidents
        fields = ('id','platform_inc_number','status_inc', 'priority_incident','inc_description','inc_detail_description','name_region','site_id',
                  'event_start_time','event_end_time','network_element',
                  'final_solution','long_site_id','lat_side_id','traffic_affected')
        comments = CommentSCreateSerializer(many=True)


class IncidentDetailViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItsmIncidents
        fields = ('id','platform_inc_number','status_inc', 'priority_incident','inc_description','inc_detail_description','name_region','site_id',
                  'event_start_time','event_end_time','network_element',
                  'final_solution','long_site_id','lat_side_id','traffic_affected')


class CommentViewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Comments
        fields = ("user", "new", "text", "created")