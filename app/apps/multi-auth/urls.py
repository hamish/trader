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
        Rule('/', endpoint='home', handler='handlers.HomeHandler'),
        Rule('/auth/login', endpoint='auth/login', handler='handlers.LoginHandler'),
        Rule('/auth/logout', endpoint='auth/logout', handler='handlers.LogoutHandler'),
        Rule('/auth/signup', endpoint='auth/signup', handler='handlers.SignupHandler'),
        Rule('/auth/register', endpoint='auth/register', handler='handlers.RegisterHandler'),

        Rule('/auth/facebook/', endpoint='auth/facebook', handler='handlers.FacebookAuthHandler'),
        Rule('/auth/friendfeed/', endpoint='auth/friendfeed', handler='handlers.FriendFeedAuthHandler'),
        Rule('/auth/google/', endpoint='auth/google', handler='handlers.GoogleAuthHandler'),
        Rule('/auth/twitter/', endpoint='auth/twitter', handler='handlers.TwitterAuthHandler'),
        Rule('/auth/yahoo/', endpoint='auth/yahoo', handler='handlers.YahooAuthHandler'),

        Rule('/content', endpoint='content/index', handler='handlers.ContentHandler'),
    ]

    return rules
