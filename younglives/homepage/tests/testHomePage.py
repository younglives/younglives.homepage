import unittest2 as unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from base import INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Test intranet folder content type"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('HomePage', 'hp1')
        hp1 = getattr(self.portal, 'hp1')
        assert 'hp1' in self.portal.objectIds()
