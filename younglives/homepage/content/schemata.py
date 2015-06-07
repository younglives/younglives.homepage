from Products.Archetypes.atapi import ImageField
from Products.Archetypes.atapi import ImageWidget
from Products.Archetypes.atapi import ReferenceField
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import StringWidget
from Products.Archetypes.atapi import TextAreaWidget
from Products.Archetypes.atapi import TextField
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.ATContentTypes.interfaces.topic import IATTopic

from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget
from Products.OrderableReferenceField import OrderableReferenceField

from younglives.homepage import _

HomePageSchema = ATContentTypeSchema.copy() + Schema((

    TextField(
        'text',
        required=False,
        searchable=True,
        primary=True,
        validators=('isTidyHtmlWithCleanup',),
        default_output_type='text/x-html-safe',
        widget=RichWidget(
            description='',
            label=_(u'label_body_text', default=u'Body Text'),
            rows=25,),
        ),

    # ========================================================================
    # Box 1
    # ========================================================================
    TextField(
        'box1Title',
        required=0,
        schemata='Box1',
        searchable=1,
        languageIndependent=1,
        widget=StringWidget(
            label=_(u"homepage_box1-title_label",
                    default=u"Box 1 title"),
            description=_(u"homepage_box1-title_desc",
                          default=u"Enter title for first homepage box."),)),

    TextField(
        'box1Description',
        required=0,
        schemata='Box1',
        languageIndependent=0,
        widget=TextAreaWidget(
            label=_(u"homepage_box1-desc_label",
                    default=u"Box 1 description"),
            description=_(u"homepage_box1-desc_desc",
                          default=u"Enter description for this box."),)),

    ImageField(
        'box1Image',
        required=0,
        schemata='Box1',
        languageIndependent=1,
        pil_quality=100,
        original_size=(222, 87),
        validsizes=(222, 87),
        widget=ImageWidget(
            label=_(u"homepage_box1-image_label",
                    default=u"Box 1 image"),
            description=_(u"homepage_box1-image_desc",
                          default=u"Upload image for first homepage box. \
Required size is 222x87px."),)),

    OrderableReferenceField(
        'box1Links',
        required=0,
        schemata='Box1',
        multiValued=1,
        languageIndependent=0,
        relationship="homepageRelatedBox1Links",
        widget=ReferenceBrowserWidget(
            allow_sorting=1,
            hide_inaccessible=1,
            force_close_on_insert=0,
            label=_(u"homepage_box1-links_label",
                    default=u"Box 1 links"),
            description=_(u"homepage_box1-links_desc",
                          default=u"Select featured links for this box."),)),


    # ========================================================================
    # Box 2
    # ========================================================================
    TextField(
        'box2Title',
        required=0,
        schemata='Box2',
        searchable=1,
        languageIndependent=1,
        widget=StringWidget(
            label=_(u"homepage_box2-title_label",
                    default=u"Box 2 title"),
            description=_(u"homepage_box2-title_desc",
                          default=u"Enter title for first homepage box."),)),

    TextField(
        'box2Description',
        required=0,
        schemata='Box2',
        languageIndependent=0,
        widget=TextAreaWidget(
            label=_(u"homepage_box2-desc_label",
                    default=u"Box 2 description"),
            description=_(u"homepage_box2-desc_desc",
                          default=u"Enter description for this box."),)),

    ImageField(
        'box2Image',
        required=0,
        schemata='Box2',
        languageIndependent=2,
        pil_quality=100,
        original_size=(222, 87),
        validsizes=(222, 87),
        widget=ImageWidget(
            label=_(u"homepage_box2-image_label",
                    default=u"Box 2 image"),
            description=_(u"homepage_box2-image_desc",
                          default=u"Upload image for first homepage box. \
Required size is 222x87px."),)),

    OrderableReferenceField(
        'box2Links',
        required=0,
        schemata='Box2',
        multiValued=1,
        languageIndependent=0,
        relationship="homepageRelatedBox2Links",
        widget=ReferenceBrowserWidget(
            allow_sorting=1,
            hide_inaccessible=1,
            force_close_on_insert=0,
            label=_(u"homepage_box2-links_label",
                    default=u"Box 2 links"),
            description=_(u"homepage_box2-links_desc",
                          default=u"Select featured links for this box."),)),

    # ========================================================================
    # Box 3
    # ========================================================================
    TextField(
        'box3Title',
        required=0,
        schemata='Box3',
        searchable=1,
        languageIndependent=1,
        widget=StringWidget(
            label=_(u"homepage_box3-title_label",
                    default=u"Box 3 title"),
            description=_(u"homepage_box3-title_desc",
                          default=u"Enter title for first homepage box."),)),

    TextField(
        'box3Description',
        required=0,
        schemata='Box3',
        languageIndependent=0,
        widget=TextAreaWidget(
            label=_(u"homepage_box3-desc_label",
                    default=u"Box 3 description"),
            description=_(u"homepage_box3-desc_desc",
                          default=u"Enter description for this box."),)),

    ImageField(
        'box3Image',
        required=0,
        schemata='Box3',
        languageIndependent=1,
        pil_quality=100,
        original_size=(222, 87),
        validsizes=(222, 87),
        widget=ImageWidget(
            label=_(u"homepage_box3-image_label",
                    default=u"Box 3 image"),
            description=_(u"homepage_box3-image_desc",
                          default=u"Upload image for first homepage box. \
Required size is 222x87px."),)),

    OrderableReferenceField(
        'box3Links',
        required=0,
        schemata='Box3',
        multiValued=1,
        languageIndependent=0,
        relationship="homepageRelatedBox3Links",
        widget=ReferenceBrowserWidget(
            allow_sorting=1,
            hide_inaccessible=1,
            force_close_on_insert=0,
            label=_(u"homepage_box3-links_label",
                    default=u"Box 3 links"),
            description=_(u"homepage_box3-links_desc",
                          default=u"Select featured links for this box."),)),


    ReferenceField(
        'homeNews',
        required=0,
        multiValued=0,
        relationship='relatedHomepageNews',
        allowed_types=('Topic',),
        widget=ReferenceBrowserWidget(
            hide_inaccessible=1,
            force_close_on_insert=0,
            allow_search=0,
            allow_browse=0,
            allow_sorting=1,
            show_review_state=1,
            image_portal_types=('Collection',),
            image_method='++atfield++homepageBoxImage-thumb',
            base_query={'object_provides': IATTopic.__identifier__},
            show_results_without_query=1,
            label=_(u"homepage_news_label",
                    default=u"News"),
            description=_(u"homepage_news_desc",
                          default=u"Select collection to show its contents \
on homepage news section."),)),

    ImageField(
        'homeFooterImage',
        required=0,
        languageIndependent=1,
        pil_quality=100,
        original_size=(468, 128),
        validsizes=(468, 128),
        widget=ImageWidget(
            label=_(u"homepage-footer-image_label",
                    default=u"Image"),
            description=_(u"homepage-footer-image_desc",
                          default=u"Upload image for homepage footer. \
Required size is 468x128px."),)),

))

HomePageSchema["title"].widget.visible = {"edit": "invisible",
                                          "view": "invisible"}
HomePageSchema["description"].widget.visible = {"edit": "invisible",
                                                "view": "invisible"}

finalizeATCTSchema(HomePageSchema, moveDiscussion=False)
