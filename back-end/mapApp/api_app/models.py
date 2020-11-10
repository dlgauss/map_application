from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Coordinates(models.Model):
    site_name =  models.CharField(max_length=60)
    address =models.CharField(max_length=200)
    long_id = models.FloatField(max_length=200)
    lat_id =  models.FloatField(max_length=200)
    region = models.CharField(max_length=60)
    town = models.CharField(max_length=60)

    def __str__(self):
        return self.site_name


class ItsmIncidents(models.Model):
    site_id = models.CharField(max_length=50)
    inc_description = models.CharField(max_length=200)
    inc_detail_description = models.TextField()
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField(null=True, blank=True)
    platform_inc_number = models.CharField(max_length=50)
    long_site_id = models.FloatField()
    lat_side_id =models.FloatField()
    network_element = models.CharField(max_length=100)
    priority_incident = models.CharField(max_length=30)
    final_solution = models.TextField(null=True, blank=True)
    status_inc = models.CharField(max_length=40)
    traffic_affected = models.CharField(max_length=30)
    name_region = models.CharField(max_length=60, null=True)

    def __str__(self):
        return f'{self.platform_inc_number} {self.site_id}'

    class Meta:
        ordering = ("platform_inc_number", "status_inc")


class Comments (models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete = models.CASCADE)
    new = models.ForeignKey(ItsmIncidents, verbose_name='Incident', on_delete=models.CASCADE, )
    text = models.TextField('Comments')
    created = models.DateTimeField('Created date', auto_now_add=True, null=True)
    moderation = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user} {self.new} '
