from five import grok
from plone.directives import dexterity
from zope.interface import Interface
from Products.CMFCore import permissions

class DemoView2(dexterity.DisplayForm):
    grok.require("zope2.View")
    grok.context(Interface)
    pass

class DemoView3(grok.View):
    grok.require("zope2.View")
    grok.context(Interface)
    pass
