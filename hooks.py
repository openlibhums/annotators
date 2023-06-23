from utils import setting_handler
from plugins.annotators import plugin_settings


def embed_hook(context):
    plugin = plugin_settings.AnnotatorsPlugin.get_self()
    enable_hypothesis = setting_handler.get_plugin_setting(
        plugin,
        'enable_hypothesis',
        context.get('request').journal,
        create=True,
        pretty='Enable Hypothesis'
    ).value
    embed_code = ''

    if enable_hypothesis == 'on':
        embed_code = embed_code + '<script src="https://hypothes.is/embed.js" async></script>'

    return embed_code
