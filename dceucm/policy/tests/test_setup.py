# -*- coding: utf-8 -*-
import unittest
from dceucm.policy.tests.base import TestCase

class TestSetup(TestCase):
    def test_portal_title(self):
        self.assertEquals("Delegación Central de Estudiantes UCM", self.portal.getProperty('title'))
    def test_portal_description(self):
        self.assertEquals("Sitio web de la Delegación Central de Estudiantes de la Universidad Complutense de Madrid", self.portal.getProperty('description'))
    def test_portal_language(self):
        self.assertEquals("es", 
            self.portal.portal_properties.site_properties.getProperty('default_language'))

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite