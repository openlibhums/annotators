from utils import models, plugins
from utils.install import update_settings

PLUGIN_NAME = 'Annotators'
DESCRIPTION = 'This is a plugin to handle consortial billing.'
AUTHOR = 'Andy Byers'
VERSION = '1.0'
SHORT_NAME = 'annotators'
DISPLAY_NAME = 'Annotators'
MANAGER_URL = 'annotators_index'
JANEWAY_VERSION = "1.5.0"
IS_WORKFLOW_PLUGIN = False


class AnnotatorsPlugin(plugins.Plugin):
    plugin_name = PLUGIN_NAME
    display_name = DISPLAY_NAME
    description = DESCRIPTION
    author = AUTHOR
    short_name = SHORT_NAME

    manager_url = MANAGER_URL

    version = VERSION
    janeway_version = JANEWAY_VERSION

    is_workflow_plugin = IS_WORKFLOW_PLUGIN


def install():
    AnnotatorsPlugin.install()
    update_settings(
        file_path='plugins/annotators/install/settings.json'
    )


def register_for_events():
    pass


def hook_registry():
    # On site load, the load function is run for each installed plugin to generate
    # a list of hooks.
    return {
        'article_js_block': {'module': 'plugins.annotators.hooks', 'function': 'embed_hook'},
    }
