# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~

    Configuration settings.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE for more details.
"""
config = {}

# Configurations for the 'tipfy' module.
config['tipfy'] = {
    # Enable debugger. It will be loaded only in development.
    'middleware': [
        'tipfy.ext.debugger.DebuggerMiddleware',
    ],
    # Enable the Hello, World! app example.
    'apps_installed': [
    ],
}

config['tipfy.ext.session'] = {
    'secret_key': 'XXXXXXXXXXXXXXX',
}

config['tipfy.ext.auth.facebook'] = {
    'api_key':    'XXXXXXXXXXXXXXX',
    'app_secret': 'XXXXXXXXXXXXXXX',
}

config['tipfy.ext.auth.friendfeed'] = {
    'consumer_key':    'XXXXXXXXXXXXXXX',
    'consumer_secret': 'XXXXXXXXXXXXXXX',
}

config['tipfy.ext.auth.twitter'] = {
    'consumer_key':    'XXXXXXXXXXXXXXX',
    'consumer_secret': 'XXXXXXXXXXXXXXX',
}
