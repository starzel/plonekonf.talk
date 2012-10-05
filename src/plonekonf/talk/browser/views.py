# encoding=utf-8
from five import grok
from plone.directives import dexterity
from zope.interface import Interface
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName
# from plonekonf.talk.interfaces import IVoting

class TalkView(dexterity.DisplayForm):
    grok.require("zope2.View")
    grok.context(Interface)


class TalkListView(grok.View):
    grok.require("zope2.View")
    grok.context(Interface)

    def talks(self):
        results = []
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        current_path = "/".join(self.context.getPhysicalPath())
        talks = portal_catalog(portal_type="talk",
                               path=current_path)
        for brain in talks:
            # hold on to your hats, we're waking up the brains!
            talk = brain.getObject()
            # now we're adapting our behavior to the talk so we can get
            # the values of the fields added by the behavior
            # voting = IVoting(talk)

            results.append({
                'title': brain.Title,
                'description': brain.Description,
                # same result as talk.absolute_url()
                'url': brain.getURL(),
                # 'average_rating': voting.average_vote(),
                'speaker': talk.speaker,
                'audience': talk.audience,
                'uuid': brain.UID,
                })
        return results
