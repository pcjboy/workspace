import os
from . import global_settings
import importlib


class Settings(object):
    def __init__(self):
        settings_module = os.environ['USER_SETTINGS']
        # ##################  找到默认配置    ###################
        for name in dir(global_settings):
            if name.isupper():
                value = getattr(global_settings, name)
                setattr(self, name, value)
        # ##################  找到自定义配置  ###################
        # 根据字符串导入模块
        # settings_module = os.environ['USER_SETTINGS']
        if not settings_module:
            return
        m = importlib.import_module(settings_module)
        for name in dir(m):
            if name.isupper():
                value = getattr(m, name)
                setattr(self, name, value)


settings = Settings()
