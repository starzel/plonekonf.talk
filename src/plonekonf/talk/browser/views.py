# encoding=utf-8
from five import grok
from plone.directives import dexterity
from zope.interface import Interface
from Products.CMFCore.utils import getToolByName
# from plonekonf.talk.interfaces import IVoting


class TalkView(dexterity.DisplayForm):
    grok.require("zope2.View")
    grok.context(Interface)
