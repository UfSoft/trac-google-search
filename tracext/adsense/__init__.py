# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et

__version__     = '0.1.0'
__author__      = 'Pedro Algarvio'
__email__       = 'ufs@ufsoft.org'
__package__     = 'Adsense4Trac'
__license__     = 'BSD'
__url__         = 'http://trac-hacks.org/wiki/TracSqlAlchemyBridgeIntegration'
__summary__     = 'Google Adsesnse Ads/Search support for trac'

# ==============================================================================
# Trac Upgrade Code
# ==============================================================================
from trac.core import Component, implements
from trac.env import IEnvironmentSetupParticipant
from trac.web.chrome import ITemplateProvider

class AdsenseSetup(Component):
    env = config = log = None # make pylink happy
    implements(IEnvironmentSetupParticipant)

    def environment_created(self):
        "Nothing to do when an environment is created"""

    def environment_needs_upgrade(self, db):
        cursor = db.cursor()
        cursor.execute('SELECT value FROM system WHERE name=%s',
                       ('adspanel.code',))
        if cursor.fetchone():
            self.log.debug('Found old AdsPanel code in database')
            return True
        self.log.debug('Did not find old AdsPanel code in database')
        return False

    def upgrade_environment(self, db):
        cursor = db.cursor()
        cursor.execute('SELECT value FROM system WHERE name=%s',
                       ('adspanel.code',))
        code = cursor.fetchone()
        self.log.debug('Upgrading Ads HTML Code from AdsPanel to Adsense4Trac')
        cursor.execute('INSERT INTO system (name,value) VALUES (%s,%s)',
                       ('adsense.ads_html', code[0]))
        cursor.execute('DELETE from system where name=%s', ('adspanel.code',))
        db.commit()
        self.log.debug("Upgrading configuration from AdsPanel to Adsense4Trac "
                       "if needed")
        for option, value in self.config.options('adspanel'):
            if self.config.has_option('adsense', option):
                self.config.set('adsense', option, value)
            self.config.remove('adspanel', option)
        self.config.save()

# ==============================================================================
# Adsense4Trac Resources
# ==============================================================================
import pkg_resources
from trac.web.chrome import ITemplateProvider

class AdsenseResources(Component):
    implements(ITemplateProvider)
    # ITemplateProvider methods
    def get_htdocs_dirs(self):
        """Return the absolute path of a directory containing additional
        static resources (such as images, style sheets, etc).
        """
        yield 'adsense4trac', pkg_resources.resource_filename(__name__,
                                                              'htdocs')

    def get_templates_dirs(self):
        """Return the absolute path of the directory containing the provided
        Genshi templates.
        """
        yield pkg_resources.resource_filename(__name__, 'templates')
