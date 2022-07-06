# Initializes the schedule by creating an instance of Collector and invoking post method from controller file
from src.azure.collector import AppCollector


class Scheduler:
    def __init__(self):
        print("[Scheduler] Initializing Schedule")
        self.resource = AppCollector()
        self.resource.get_app_objects()

    def create(self):
        print("[Scheduler] create")
        print(self.resource, self.resource.app_objects)
        for app in self.resource.app_objects:
            app.post()

    def remove(self):
        for app in self.resource.app_objects:
            app.delete()

    def update(self):
        for app in self.resource.app_objects:
            app.post()


if __name__ == "__main__":
    obj = Scheduler()
    obj.create()
