from django.db import models
from django.utils import timezone # For default create_time

class Person(models.Model):
    id = models.BigAutoField(primary_key=True) # Changed to BigAutoField for Django-managed auto-incrementing PK
    name = models.CharField(max_length=255, null=True, blank=True) # blank=True allows empty string in forms
    birthday = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "Person"
        verbose_name_plural = "People" # Optional: for Django admin display

    def __str__(self):
        return self.name or f"Person {self.id}"

class Follows(models.Model):
    id = models.BigAutoField(primary_key=True)

    follower = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='following_relations', # Who this person is following
        db_column='follower_person_id' # Explicit column name
    )

    # The person being followed
    followed_person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='follower_relations', # Who is following this person
        db_column='followed_person_id' # Explicit column name
    )

    create_time = models.DateTimeField(default=timezone.now, null=True, blank=True) # Default to now, can be nullable

    class Meta:
        db_table = "Follows"
        unique_together = (('follower', 'followed_person'),)
        verbose_name_plural = "Follows" # Optional: for Django admin display

    def __str__(self):
        return f"{self.follower} follows {self.followed_person}"