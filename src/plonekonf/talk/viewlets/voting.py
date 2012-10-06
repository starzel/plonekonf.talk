# encoding=utf-8
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.permissions import ViewManagementScreens
from five import grok
from plone.app.layout.viewlets import interfaces as viewletIFs
from plonekonf.talk.interfaces import IVoting
from zope.component import Interface


class Vote(grok.Viewlet):
    grok.context(IVoting)
    grok.viewletmanager(viewletIFs.IBelowContentTitle)

    def _vote(self):
        return IVoting(self.context)

    @property
    def voted(self):
        return self._vote.already_voted(self.request)

    @property
    def average(self):
        return self._vote.average_vote()

    @property
    def is_manager(self):
        membership_tool = getToolByName(self.context, 'portal_membership')
        return membership_tool.checkPermission(ViewManagementScreens,
                                               self.context)
    @property
    def has_votes(self):
        return self._vote.has_votes()
