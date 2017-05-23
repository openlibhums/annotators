from utils import models, setting_handler


PLUGIN_NAME = 'Annotators'
DESCRIPTION = 'This is a plugin to handle consortial billing.'
AUTHOR = 'Andy Byers'
VERSION = '1.0'
SHORT_NAME = 'annotators'
DISPLAY_NAME = 'Annotators'
MANAGER_URL = 'annotators_index'


def get_self():
    new_plugin, created = models.Plugin.objects.get_or_create(name=SHORT_NAME,
                                                              display_name=DISPLAY_NAME,
                                                              version=VERSION,
                                                              enabled=True)
    return new_plugin


def install():
    new_plugin, created = models.Plugin.objects.get_or_create(name=SHORT_NAME,
                                                              display_name=DISPLAY_NAME,
                                                              version=VERSION,
                                                              enabled=True)

    if created:
        print('Plugin {0} installed.'.format(PLUGIN_NAME))
    else:
        print('Plugin {0} is already installed.'.format(PLUGIN_NAME))


def hook_registry():
    # On site load, the load function is run for each installed plugin to generate
	# a list of hooks.
    return {
        'article_js_block': {'module': 'plugins.annotators.hooks', 'function': 'embed_hook'},
        'article_buttons': {'module': 'plugins.annotators.hooks', 'function': 'annotran_button'}
        }