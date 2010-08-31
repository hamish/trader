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
        'apps.trader',
    ],
}
config['tipfy.ext.session'] = {
    'secret_key': 'vutCriSd4UqehbV62mHXs3',
}
config['tipfy.ext.auth'] = {
    'user_model': 'apps.trader.model.Player',
}
config['tipfy.ext.auth.facebook'] = {
    'api_key':    '4d0b2b7973072a1a86acb3449faf023c',
    'app_secret': 'a7c2e45799acd445b29e6dc347f20165',
}

config['tipfy.ext.auth.friendfeed'] = {
    'consumer_key':    'd1e4e957c681439cadeb56b0f7ab19d1',
    'consumer_secret': '7957106a81fa4c808ba8a31dccebf7b5e36ebba5d42e4d43b7af48454fd48dc2',
}

config['tipfy.ext.auth.twitter'] = {
    'consumer_key':    'jGiBTNAOCF7vInfeWYQOw',
    'consumer_secret': 'b0j9cms3ALLiCV7XE35GKXHSVl8nnR6qUudcVnEs',
}
