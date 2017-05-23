from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from plugins.annotators import plugin_settings
from utils import setting_handler

def index(request):
    plugin = plugin_settings.get_self()

    enable_annotran = setting_handler.get_plugin_setting(plugin, 'enable_annotran', request.journal, create=True,
                                                         pretty='Enable Annotran')

    enable_hypothesis = setting_handler.get_plugin_setting(plugin, 'enable_hypothesis', request.journal, create=True,
                                                           pretty='Enable Hypothesis')
    if request.POST:
        annotran = request.POST.get('annotran')
        hypothesis = request.POST.get('hypothesis')
        setting_handler.save_plugin_setting(plugin, 'enable_annotran', annotran, request.journal)
        setting_handler.save_plugin_setting(plugin, 'enable_hypothesis', hypothesis, request.journal)
        return redirect(reverse('annotators_index'))

    template = 'annotators/index.html'
    context = {
        'enable_annotran': enable_annotran,
        'enable_hypothesis': enable_hypothesis,
    }

    return render(request, template, context)