from django.db import models
from django.contrib.auth.models import AbstractUser
from util.model import BaseModel



class Organization(BaseModel):
    title = models.CharField(max_length=30)


class User(AbstractUser):
    
    class Role:
        # full access
        ADMIN = "a"

        # full view, manual editing
        TOP_MANAGER = "t"  

        # manual view & editing
        MANAGER = "m"

        choices = (
            (ADMIN, "Admin"),
            (TOP_MANAGER, "Top manager"),
            (MANAGER, "Manager"),
        )
    
    organization = models.ForeignKey(Organization, related_name="+", null=True, blank=True)
    role = models.CharField(
        max_length=2,
        choices=Role.choices,
        default=Role.ADMIN,
    )
    default_password = models.CharField(max_length=30, null=True, blank=True)
