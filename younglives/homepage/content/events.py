from Products.CMFCore.utils import getToolByName


def removeInterfaces(ob, event):
    catalog = getToolByName(ob, 'portal_catalog')
    brains = catalog(
        object_provides='younglives.content.interfaces.content.IBannerAware')

    print len(brains)
