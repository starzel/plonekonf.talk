# -*- extra stuff goes here -*-
from zope.i18nmessageid import MessageFactory

talkMessageFactory = MessageFactory('plonekonf.talk')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
