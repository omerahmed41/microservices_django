from django import dispatch

some_task_done = dispatch.Signal(providing_args=["task_id"])
