from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.base import ATCTContent
from Products.CMFCore.utils import getToolByName

from younglives.homepage.config import PROJECTNAME
from younglives.homepage.interfaces.homepage import IHomePage

from schemata import HomePageSchema


class HomePage(ATCTContent):
    """ YoungLives homepage archetype. """
    implements(IHomePage)

    meta_type = "HomePage"
    schema = HomePageSchema

    def Title(self):
        """Return the portal title as the home page title"""
        portal_object = getToolByName(self, 'portal_url').getPortalObject()
        return portal_object.title

    def Description(self):
        """Return description based on full description"""
        description = self.text()
        if not description:
            return ''
        transform_tool = getToolByName(self, 'portal_transforms')
        description = transform_tool.convert('html_to_text',
                                             description).getData()
        description = description.strip()
        if len(description) > 150:
            return description[:150] + '...'
        return description

registerType(HomePage, PROJECTNAME)
