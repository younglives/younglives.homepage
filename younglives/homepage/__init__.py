from Products.Archetypes.atapi import process_types, listTypes
from Products.CMFCore.utils import ContentInit

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('younglives.homepage')

from content.homepage import HomePage
from config import PROJECTNAME

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        ContentInit('%s: %s' % (PROJECTNAME, atype.portal_type),
            content_types      = (atype,),
            permission         = config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors = (constructor,),
            ).initialize(context)
