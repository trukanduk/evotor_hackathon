from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True
    
    def _dto(self, public=False):
        return NotImplementedErr

    def public_dto(self):
        return self._dto(public=True)

    def private_dto(self):
        return self._dto(public=False)
