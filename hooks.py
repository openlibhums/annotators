from utils import setting_handler
from plugins.annotators import plugin_settings


def embed_hook(context):
    plugin = plugin_settings.get_self()
    enable_hypothesis = setting_handler.get_plugin_setting(plugin, 'enable_hypothesis', context.get('request').journal,
                                                           create=True,
                                                           pretty='Enable Hypothesis').value
    embed_code = ''

    if enable_hypothesis == 'on':
        embed_code = embed_code + '<script src="https://hypothes.is/embed.js" async></script>'

    return embed_code


def annotran_button(context):
    plugin = plugin_settings.get_self()
    enable_annotran = setting_handler.get_plugin_setting(plugin, 'enable_annotran', context.get('request').journal,
                                                         create=True,
                                                         pretty='Enable Annotran').value
    if enable_annotran == 'on':
        return "<li><a href=\"javascript:(function(){window.hypothesisConfig=function(){return{showHighlights:true};};var d=document,s=d.createElement('script');s.setAttribute('src','https://annotran.openlibhums.org/embed.js');d.body.appendChild(s)})();\">Start Annotran</a></li>"

    return ''
