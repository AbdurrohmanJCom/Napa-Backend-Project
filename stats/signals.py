from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from users.models import CustomUser, Order, Proposal
from .models import UserStats, OrderStats, ProposalStats

def update_stats_if_needed(model, field_name):
    today = timezone.now().date()
    stats, created = model.objects.get_or_create(date=today)

    now = timezone.now()
    last_updated = getattr(stats, 'last_updated', None)

    # Отладочные сообщения
    print(f"Now: {now}")
    print(f"Last Updated: {last_updated}")

    if last_updated is None:
        # Инициализируем last_updated, если он не установлен
        stats.last_updated = now
        stats.save()
        print("Initialized last_updated to current time.")
    
    else:
        # Проверяем, прошло ли больше 12 часов с последнего обновления
        time_diff = (now - last_updated).total_seconds()
        print(f"Time since last update: {time_diff} seconds")

        if time_diff >= 12 * 3600:  # 12 * 3600 секунд = 12 часов
            # Если прошло больше 12 часов, обновляем время и добавляем к текущему значению
            stats.last_updated = now
            setattr(stats, field_name, getattr(stats, field_name) + 1)  # Добавляем к текущему значению
            stats.save()
            print(f"Updated {field_name} due to time threshold: {getattr(stats, field_name)}")
        else:
            # Если прошло меньше времени, просто добавляем к текущему значению
            setattr(stats, field_name, getattr(stats, field_name) + 1)
            stats.save()
            print(f"Incremented {field_name} without updating last_updated: {getattr(stats, field_name)}")
            

@receiver(post_save, sender=CustomUser)
def update_user_stats(sender, instance, created, **kwargs):
    if created:
        update_stats_if_needed(UserStats, 'registered_users')

@receiver(post_save, sender=Order)
def update_order_stats(sender, instance, created, **kwargs):
    if created:
        update_stats_if_needed(OrderStats, 'created_orders')

@receiver(post_save, sender=Proposal)
def update_proposal_stats(sender, instance, created, **kwargs):
    if created:
        update_stats_if_needed(ProposalStats, 'created_proposals')
