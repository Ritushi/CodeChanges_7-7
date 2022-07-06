# Collects APP objects
import os
import sys
import pkgutil
import logging
import importlib
logger = logging.getLogger("apps")
logger.setLevel(logging.DEBUG)
stdout_handler = logging.StreamHandler(sys.stdout)


class AppCollector:

    _instances_cache = {}
    _instances = None

    def __new__(cls, *args, **kwargs):
        print("[Collector] Initializing collector")
        if "object" not in cls._instances_cache:
            collector = super(AppCollector, cls).__new__(cls, *args, **kwargs)
            collector.logger = logger
            collector.logger.info(
                "[APP COLLECTOR] *****Starting APP Collector**********")
            collector.app_objects = []
            collector.collect_app_objects()
            cls._instances_cache["object"] = collector
            cls._instances = collector
        return cls._instances_cache["object"]
    '''
    def __init__(self):
        self.logger = logger
        self.logger.info(
            "[APP COLLECTOR] *****Starting APP Collector**********")
        self.app_objects = []
        self.collect_app_objects()
    '''

    def collect_app_objects(self):
        """
           This API automatically find out all the source app objects defined under apps folder.
        """
        print("[Collector] Collecting APP OBJECT APIS CALLING")
        for (_, name, _) in pkgutil.iter_modules(
                [os.path.join(os.path.dirname(__file__), 'apps')]):
            print("[Collector] Collecting all APps", name)
            self.logger.info(
                "[APP COLLECTOR] files collected for processing are {}".format(name))
            try:
                stats_path = "src.azure.apps" + '.' + name
                print("[Collector] APP Object is", stats_path)
                app_obj = importlib.import_module(stats_path)
                app_obj = getattr(app_obj, name.capitalize())()
                self.logger.info(
                    "[APP COLLECTOR] app objects are {}".format(app_obj))
                self.app_objects.append(app_obj)
                
            except ImportError as e:
                print("[Collector] Import Error Could not collect app Objects ", e, name)
                self.logger.warn("Not able to import %s. Error is %s", name, e)
            except Exception as e:
                print("[Collector] Could not collect app Objects ", e)
                self.logger.error(
                    "Exception during importing %s.(%s)", name, e)
        return

    def get_app_objects(self):
        print("[Collector] Displaying all the app objects which are supported")
        for app in self.app_objects:
            print("[Collector] Apps are", app)


if __name__ == "__main__":
    obj = AppCollector()
    obj.get_app_objects()