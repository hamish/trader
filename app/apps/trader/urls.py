# -*- coding: utf-8 -*-
"""
    urls
    ~~~~

    URL definitions.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE.txt for more details.
"""
from tipfy import Rule, import_string


def get_rules(app):
    """Returns a list of URL rules for the application. The list can be
    defined entirely here or in separate ``urls.py`` files.

    :param app:
        The WSGI application instance.
    :return:
        A list of class:`tipfy.Rule` instances.
    """
    rules = [
        Rule('/', endpoint='home', handler='apps.trader.handlers.HomeHandler'),
        Rule('/auth/login', endpoint='auth/login', handler='apps.trader.auth.LoginHandler'),
        Rule('/auth/logout', endpoint='auth/logout', handler='apps.trader.auth.LogoutHandler'),
        Rule('/auth/signup', endpoint='auth/signup', handler='apps.trader.auth.SignupHandler'),
        Rule('/auth/register', endpoint='auth/register', handler='apps.trader.auth.RegisterHandler'),

        Rule('/auth/facebook/', endpoint='auth/facebook', handler='apps.trader.auth.FacebookAuthHandler'),
        Rule('/auth/friendfeed/', endpoint='auth/friendfeed', handler='apps.trader.auth.FriendFeedAuthHandler'),
        Rule('/auth/google/', endpoint='auth/google', handler='apps.trader.auth.GoogleAuthHandler'),
        Rule('/auth/twitter/', endpoint='auth/twitter', handler='apps.trader.auth.TwitterAuthHandler'),
        Rule('/auth/yahoo/', endpoint='auth/yahoo', handler='apps.trader.auth.YahooAuthHandler'),

        Rule('/content', endpoint='content/index', handler='apps.trader.handlers.ContentHandler'),

        Rule('/trader', endpoint='trader', handler='apps.trader.handlers.TraderHandler'),
        Rule('/travel', endpoint='travel', handler='apps.trader.handlers.TravelHandler'),
        Rule('/buyorsell', endpoint='buyorsell', handler='apps.trader.handlers.BuyOrSellHandler'),
    ]

    return rules
