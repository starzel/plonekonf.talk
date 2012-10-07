# encoding=utf-8
from five import grok
from plone.app.layout.viewlets import interfaces as viewletIFs
from zope.component import Interface
from plonekonf.talk.behavior.social import ISocial


class Social(grok.Viewlet):
    grok.context(ISocial)
    grok.viewletmanager(viewletIFs.IBelowContentTitle)

    def lanyrd_link(self):
        adapted = ISocial(self.context)
        return adapted.lanyrd
