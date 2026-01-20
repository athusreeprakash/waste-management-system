from django.contrib import admin
from .models import (
    UserType,
    UserRegistration,
    CollectorRegistration,
    Category,
    WastePickup,
    CollectionHistory,
    Products,
    Purchase,
    StockHis,
    OrderUpdates,
    Complaints,
    Locations
)

admin.site.register(UserType)
admin.site.register(UserRegistration)
admin.site.register(CollectorRegistration)
admin.site.register(Category)
admin.site.register(WastePickup)
admin.site.register(CollectionHistory)
admin.site.register(Products)
admin.site.register(Purchase)
admin.site.register(StockHis)
admin.site.register(OrderUpdates)
admin.site.register(Complaints)
admin.site.register(Locations)
