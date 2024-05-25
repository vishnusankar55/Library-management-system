from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, History

@receiver(post_save, sender=Book)
def create_history_entry(sender, instance, created, **kwargs):
    if not created and instance.return_date:
        History.objects.create(book=instance, user=instance.borrower, return_date=instance.return_date)
