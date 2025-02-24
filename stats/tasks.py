# from celery import shared_task
# from django.utils import timezone
# from stats.models import UserStats, OrderStats, ProposalStats

# @shared_task
# def update_stats_every_10_seconds():
#     today = timezone.now().date()
#     now = timezone.now().time()  # Получаем только время

#     # Определяем поля для каждой модели
#     field_mappings = {
#         UserStats: 'registered_users',
#         OrderStats: 'created_orders',
#         ProposalStats: 'created_proposals',
#     }

#     for model, field_name in field_mappings.items():
#         stats, created = model.objects.get_or_create(date=today)

#         last_updated = stats.last_updated

#         if last_updated is None:
#             # Инициализируем last_updated, если он не установлен
#             stats.last_updated = now
#             setattr(stats, field_name, getattr(stats, field_name) + 1)
#             print(f"Initialized last_updated and incremented {field_name}.")
#         else:
#             last_updated_time = timezone.datetime.combine(today, last_updated)
#             current_time = timezone.datetime.combine(today, now)
#             time_diff = (current_time - last_updated_time).total_seconds()
#             print(f"Time since last update: {time_diff} seconds")

#             if time_diff >= 10:  # Если прошло больше 10 секунд
#                 stats.last_updated = now
#                 setattr(stats, field_name, getattr(stats, field_name) + 1)
#                 print(f"Updated {field_name} due to time threshold.")
#             else:
#                 setattr(stats, field_name, getattr(stats, field_name) + 1)
#                 print(f"Incremented {field_name} without updating last_updated.")

#         stats.save()
#         print(f"Saved {model.__name__} with {field_name} = {getattr(stats, field_name)}")

#     return "Stats updated successfully every 10 seconds."
