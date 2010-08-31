from django.utils import simplejson

from tipfy import (RequestHandler, RequestRedirect, Response, abort,
    cached_property, redirect, url_for)
from tipfy.ext.auth import MultiAuthMixin, login_required, user_required
from tipfy.ext.auth.facebook import FacebookMixin
from tipfy.ext.auth.friendfeed import FriendFeedMixin
from tipfy.ext.auth.google import GoogleMixin
from tipfy.ext.auth.twitter import TwitterMixin
from tipfy.ext.jinja2 import Jinja2Mixin
from tipfy.ext.session import AllSessionMixins, SessionMiddleware
from tipfy.ext.wtforms import Form, fields, validators
from apps.trader.auth import BaseHandler

allPlanets = ["Planet0", "Planet1", "Planet2", "Planet3", "Planet4", "Planet5", "Planet6"]
allProducts = ["Product0", "Product1", "Product2", "Product3", "Product4", "Product5", "Product6"]

prices= [
          [10, 6, 2, 7, 4, 5, 3],
          [20,18,19,19,17,15,23],
          [25,34,14,27,22,11,12],
          [34,45,34,42,41,50,23],
          [53,51,47,45,50,48,59],
          [57,60,59,63,60,69,52],
          [70,68,65,70,78,72,66]
          ]


class HomeHandler(BaseHandler):
    def get(self, **kwargs):
        return self.render_response('home.html', section='home')


class ContentHandler(BaseHandler):
    @user_required
    def get(self, **kwargs):
        return self.render_response('content.html', section='content')

class BuyOrSellHandler(BaseHandler):
    @user_required
    def get(self):
        """Do a trade"""
        player = self.auth_current_user #self.getPlayer()
        product = int(self.request.args.get('product'))
        action = self.request.args.get('action')
        price = prices[product][player.location]
        if (action=='buy'):
            player.money = player.money-price
            player.products[product] = player.products[product] + 1
            player.numProducts = player.numProducts + 1
        else:
            player.money = player.money+price
            player.products[product] = player.products[product] -1            
            player.numProducts = player.numProducts - 1
        player.put()
        return self.redirect_to('trader')
        
class TravelHandler(BaseHandler):
    @user_required
    def get(self):
        """Render the main trader game page."""
        player = self.auth_current_user #self.getPlayer()
        newLocation = int(self.request.args.get('planet'))
        player.location=newLocation
        player.put()
        return self.redirect_to('trader')

class TraderHandler(BaseHandler):
    @user_required
    def get(self):
        """Render the main trader game page."""
        player = self.auth_current_user #self.getPlayer()
        params = {'player' : player,
                  'allPlanets': allPlanets,
                  'allProducts': allProducts,
                  'prices': prices,
                  }
        return self.render_response('trader.html', **params)
