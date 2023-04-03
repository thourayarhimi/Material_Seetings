from import_export import resources
from .models import mara_marc_for_MS



class maraResource(resources.ModelResource):
     class meta:
         model=mara_marc_for_MS
