# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import socket


class IPShow(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.EventHandlerPlugin):
    
    def on_after_startup(self):
        self._logger.info("IP Show on  LCD!")
        
    def get_settings_defaults(self):
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
        except:
            ip = 'Can not connect to internet to get IP'
        return dict(ip=ip)

    def get_template_vars(self):
        return dict(ip=self._settings.get(["ip"]))

	def on_event(self, event, payload):
		# Return if not enabled
		if not self._settings.get(['enabled']):
			self._logger.info("Not enabled, will not send.")
			return
        if event == 'Connected':
            self._logger.info("IP Show on  LCD! connected event")
            
            
            
            
            
            
__plugin_name__ = "IP Show on  LCD"
__plugin_implementation__ = IPShow()