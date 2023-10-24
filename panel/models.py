from uuid import uuid4
from django.db import models

from accounts.models import User

# Create your models here.


class Vacation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    STATUS = ((1, 'Pending'), (2, 'Approved'), (3, 'Decline'))
    status = models.IntegerField(choices=STATUS, default=1)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    VACATION_TYPE= ((1, 'illness'), (2, 'entitlement'))
    vacation_status = models.IntegerField(choices=VACATION_TYPE, default=1)

    class Meta:
        permissions = [
            ("can_create_vacation", "Can create vacation"),
            ("can_view_vacation", "Can view vacation"),
            ("can_edit_vacation", "Can edit vacation"),
            ("can_delete_vacation", "Can delete vacation"),
            ("can_get_all_vacation", "Can Get All vacation"),
        ]
        ordering = ('-created_at',)

    def __str__(self):
        user = User.objects.get(id=self.user_id)
        return user.first_name + " " + user.last_name
