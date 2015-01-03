from Products.Archetypes.atapi import listTypes
from Products.Archetypes.atapi import process_types
from Products.CMFCore.utils import ContentInit

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('younglives.homepage')

from younglives.homepage.content.homepage import HomePage  # noqa
from younglives.homepage.config import ADD_PERMISSIONS
from younglives.homepage.config import PROJECTNAME


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        ContentInit(
            '%s: %s' % (PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)
