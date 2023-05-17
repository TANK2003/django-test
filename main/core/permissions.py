### ALL ABOUT DJANGO
from rest_framework.permissions import BasePermission
### ALL ABOUT THIS PROJECT
from sales.models import Sale

class CanUpdateSale(BasePermission):
    """
        Permission to update SALE
    """

    def has_object_permission(self, request, view, obj:Sale):
 
        return obj.author == request.user
       
        