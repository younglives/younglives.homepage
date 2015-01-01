from zope.interface import implements

from Products.CMFCore.utils import getToolByName
from Products.Five import BrowserView
from plone.memoize import view

from interfaces import IHomePageView


class HomePageView(BrowserView):
    implements(IHomePageView)

    @view.memoize
    def html_description(self):
        portal_transforms = getToolByName(self.context, 'portal_transforms')
        return portal_transforms.convert('text_to_html',
                                         self.context.Description())

    @view.memoize
    def homepage_news(self):
        item = None
        home_news_ref = self.context.getHomeNews()
        item = dict(title=home_news_ref.Title(),
                    url=home_news_ref.absolute_url(),
                    links=[])
        brains = home_news_ref.queryCatalog()
        for brain in brains:
            item['links'].append(dict(title=brain.Title,
                                      url=brain.getURL(),
                                      date=brain.Date))

        return item

    @view.memoize
    def boxes(self):
        results = []
        for box in ["1", "2", "3"]:
            links = eval("self.context.getBox%sLinks()" % box) or []
            results.append(dict(
                title=eval("self.context.getBox%sTitle" % box),
                description=eval("self.context.getBox%sDescription()" % box),
                image=eval("self.context.getBox%sImage()" % box),
                links=[{'title': x.Title, 'url': x.absolute_url}
                       for x in links],))
        return results

    def toLocalizedTime(self, time, long_format=None, time_only=None):
        """Convert time to localized time
        """
        util = getToolByName(self.context, 'translation_service')
        return util.ulocalized_time(time,
                                    long_format,
                                    time_only,
                                    self.context,
                                    domain='plonelocales')
