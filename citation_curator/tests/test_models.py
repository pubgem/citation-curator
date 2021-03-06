# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

from nose.plugins.attrib import attr
from ..models import User
from .mixins import DiamondTestCase


class UserTestCase(DiamondTestCase):
    "Coverage for User Model"

    def test_create(self):
        "ensure an account can be created"
        User.create(name="username", email='an_account@example.com', password='a_password')
        an_account = User.find(name="username")
        assert an_account
        assert an_account.name == "username"
