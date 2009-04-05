# -*- coding: utf-8 -*-
import unittest
from dceucm.policy.tests.base import TestCase

class TestSetup(TestCase):
    def afterSetUp(self):
        self.site_properties = self.portal.portal_properties.site_properties
    def test_portal_title(self):
        self.assertEquals("Delegación Central de Estudiantes UCM", self.portal.getProperty('title'))
    def test_portal_description(self):
        self.assertEquals("Sitio web de la Delegación Central de Estudiantes de la Universidad Complutense de Madrid", self.portal.getProperty('description'))
    def test_portal_language(self):
        self.assertEquals("es", 
            self.site_properties.getProperty('default_language'))
    def test_icons_authenticated(self):
        """Test that content icons will be shown only to authenticated users
        """
        self.assertEquals("authenticated", 
            self.site_properties.getProperty('icon_visibility'))
    def test_inline_editing_disabled(self):
        """Test that inline editing is disabled
        """
        self.assertEquals(False,
            self.site_properties.getProperty('enable_inline_editing'))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
