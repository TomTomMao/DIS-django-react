from django.contrib import admin
from api.models import Vehicle, People, Ownership, Offense, Incident, Fine
# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    pass


class PeopleAdmin(admin.ModelAdmin):
    pass


class OwnershipAdmin(admin.ModelAdmin):
    pass


class OffenseAdmin(admin.ModelAdmin):
    pass


class IncidentAdmin(admin.ModelAdmin):
    pass


class FineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Ownership, OwnershipAdmin)
admin.site.register(Offense, OffenseAdmin)
admin.site.register(Incident, IncidentAdmin)
admin.site.register(Fine, FineAdmin)
