from zope.interface import noLongerProvides
from Products.CMFCore.utils import getToolByName

def removeInterfaces(ob, event):
    catalog = getToolByName(self, 'portal_catalog')
    brains = catalog(object_provides='younglives.content.interfaces.content.IBannerAware')
    
    print len(brains)

#noLongerProvides(content, IUserRatable)
