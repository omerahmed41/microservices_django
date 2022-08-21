from django.dispatch import receiver

from utils import producer
import logger
from todoList.domain import events
from todoList.domain.services import todo_service


@receiver(events.some_task_done)
def my_task_done(sender, task_id, **kwargs):
    logger.info(f"signal received: {sender}, {task_id}")

    todo_service.schedule_task()
    producer.publish("quote_created", {"message": "user_created"})
