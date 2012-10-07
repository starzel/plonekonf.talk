# -*- coding: utf-8 -*-
from plone.directives import form
from zope import schema
from zope.interface import alsoProvides

class ISocial(form.Schema):

    form.fieldset(
            'social',
            label=u'Social',
            fields=('lanyrd',),
        )

    lanyrd = schema.URI(
            title=u"Lanyrd-link",
            description=u"Add URL",
            required=False,
        )

alsoProvides(ISocial, form.IFormFieldProvider)
