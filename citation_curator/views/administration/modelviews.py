# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

import flask
import flask.ext.security as security
from flask.ext.admin import expose
from flask.ext.diamond import db
from flask.ext.diamond.facets.administration import AuthModelView, AdminIndexView


adminbaseview = flask.Blueprint('adminbaseview', __name__,
    template_folder='templates', static_folder='static')


class RedirectView(AdminIndexView):
    def is_visible(self):
        return False

    def is_accessible(self):
        return security.current_user.is_authenticated()

    @expose('/')
    def index(self):
        return flask.redirect(flask.url_for('user.list_view'))
