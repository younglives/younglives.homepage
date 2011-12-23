from zope.interface import Interface

from plone.theme.interfaces import IDefaultPloneLayer

class IYounglivesHomepage(IDefaultPloneLayer):
    """This interface is registered in profiles/default/browserlayer.xml,
    and is referenced in the 'layer' option of various browser resources.
    When the product is installed, this marker interface will be applied
    to every request, allowing layer-specific customisation.
    """

class IHomePageView(Interface):
    """ Homepage content type view. """
