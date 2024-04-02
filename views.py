from django.shortcuts import render, redirect
from django.urls import reverse

from plugins.annotators import plugin_settings
from utils import setting_handler


def index(request):
    plugin = plugin_settings.AnnotatorsPlugin.get_self()

    enable_hypothesis = setting_handler.get_plugin_setting(
        plugin=plugin,
        setting_name='enable_hypothesis',
        journal=request.journal,
    )
    if request.POST:
        hypothesis = request.POST.get('hypothesis')
        setting_handler.save_plugin_setting(
            plugin,
            'enable_hypothesis',
            hypothesis,
            request.journal,
        )
        return redirect(reverse('annotators_index'))

    template = 'annotators/index.html'
    context = {
        'enable_hypothesis': enable_hypothesis,
    }

    return render(request, template, context)