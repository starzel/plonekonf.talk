from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import plonekonf.talk


PLONEKONF_TALK = PloneWithPackageLayer(
    zcml_package=plonekonf.talk,
    zcml_filename='testing.zcml',
    gs_profile_id='plonekonf.talk:testing',
    name="PLONEKONF_TALK")

PLONEKONF_TALK_INTEGRATION = IntegrationTesting(
    bases=(PLONEKONF_TALK, ),
    name="PLONEKONF_TALK_INTEGRATION")

PLONEKONF_TALK_FUNCTIONAL = FunctionalTesting(
    bases=(PLONEKONF_TALK, ),
    name="PLONEKONF_TALK_FUNCTIONAL")
