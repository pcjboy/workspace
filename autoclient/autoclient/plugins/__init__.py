from lib.conf.config import settings
import importlib


class PluginManager(object):
    def __init__(self, hostname=None):
        self.hostname = hostname
        self.plugin_dict = settings.PLUGINS_DICT

        self.mode = settings.MODE
        if self.mode == "SSH":
            self.ssh_user = settings.SSH_USER
            self.ssh_port = settings.SSH_PORT
            self.ssh_pwd = settings.SSH_PWD

    def exec_plugin(self):
        """
        获取所有的插件，并执行获取插件返回信息
        :return:
        """
        response = {}
        for k, v in self.plugin_dict.items():
            ret = {'status': True, 'data': None}
            try:
                # 'basic': "src.plugins.basic.Basic",
                module_path, class_name = v.rsplist(',', 1)
                m = importlib.import_module(module_path)
                cls = getattr(m, class_name)
                if hasattr(cls, "initial"):
                    obj = cls.initial()
                else:
                    obj = cls()
                result = obj.procss(self.command, self.debug)  # "根据v获取类，并执行其方法采集资产"
                ret['data'] = result
            except Exception as e:
                ret['status'] = False
                ret['data'] = "[%s][%s] 采集数据出现错误： %s" % (self.hostname if self.hostname else "AGENT", class_name, e)
                response[k] = ret

    def command(self, cmd):
        if self.mode == "AGENT":
            return self.__agent(cmd)
        elif self.mode == "SSH":
            return self.__ssh(cmd)
        elif self.mode == "SALT":
            return self.__salt(cmd)
        else:
            raise Exception('模式只能是 AGENT、SSH、SALT')

    def __agent(self, cmd):
        import subprocess
        output = subprocess.getoutput(cmd)
        return output

    def __salt(self, cmd):
        # python 2.7
        # import salt.client
        # local = salt.client.LocalClient()
        # result = local.cmd(self.hostname, 'cmd.run', [cmd])
        # return result[self.hsotname]

        # python 3
        salt_cmd = "salt '%s' cmd.run '%s'" % (self.hostname, cmd,)
        import subprocess
        output = subprocess.getoutput(salt_cmd)
        return output

    def __ssh(self, cmd):
        pass
