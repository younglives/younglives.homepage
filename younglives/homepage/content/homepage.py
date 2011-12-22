from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.base import ATCTContent

from younglives.homepage.config import PROJECTNAME

from schemata import HomePageSchema

class HomePage(ATCTContent):
    """ YoungLives homepage archetype. """
    #implements(IHomePage)

    meta_type = "HomePage"
    schema = HomePageSchema
    

registerType(HomePage, PROJECTNAME)
