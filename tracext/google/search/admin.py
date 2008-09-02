# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et

from trac.core import *
from trac.web.chrome import add_stylesheet
from trac.admin import IAdminPanelProvider
from trac.config import Option, _TRUE_VALUES
from trac.util.text import unicode_unquote


class AdsenseAdminPanel(Component):
    config = env = log = None # make pylint happy
    implements(IAdminPanelProvider)

    def __init__(self):
        self.options = {}

    # IAdminPanelProvider methods
    def get_admin_panels(self, req):
        if req.perm.has_permission('TRAC_ADMIN'):
            yield ('google', 'Google', 'ads', 'Ads Panel')
            yield ('google', 'Google', 'search', 'Search')

    def render_admin_panel(self, req, cat, page, path_info):
        add_stylesheet(req, 'googlesearch/googlesearch.css')
        if page == 'ads':
            return self._render_ads_panel(req, cat, page, path_info)
        elif page == 'search':
            return self._render_search_panel(req, cat, page, path_info)

    def _render_ads_panel(self, req, cat, page, path_info):
        self.log.debug('Saving Ads Panel Options')
        if req.method == 'POST':
            self.config.set('adsense', 'hide_for_authenticated',
                            req.args.get('hide_for_authenticated') in
                            _TRUE_VALUES)
            ads_div_id = req.args.get('ads_div_id') or 'main'
            if ads_div_id:
                self.config.set('adsense', 'ads_div_id', ads_div_id)
            self.config.save()
            code = req.args.get('ads_html')
            db = self.env.get_db_cnx()
            cursor = db.cursor()
            cursor.execute('SELECT value FROM system WHERE name=%s',
                           ('adsense.ads_html',))
            if cursor.fetchone():
                self.log.debug('Updating Ads HTML Code')
                cursor.execute('UPDATE system SET value=%s WHERE name=%s',
                               (code, 'adsense.ads_html'))
            else:
                self.log.debug('Inserting Ads HTML Code')
                cursor.execute('INSERT INTO system (name,value) VALUES (%s,%s)',
                               ('adsense.ads_html', code))
            db.commit()

            req.redirect(req.href.admin(cat, page))
        self._update_config()
        return 'adsense_ads_admin.html', {'ads_options': self.options}

    def _render_search_panel(self, req, cat, page, path_info):
        if req.method == 'POST':
            self.config.set('adsense', 'google_search_active',
                            req.args.get('google_search_active') in
                            _TRUE_VALUES)

            for arg, value in req.args.iteritems():
                if self.config.has_option('adsense', arg):
                    if arg != 'google_search_active':
                        self.config.set('adsense', arg, value)
            self.config.save()
            req.redirect(req.href.admin(cat, page))

        self._update_config()
        return 'adsense_search_admin.html', {'ads_options': self.options}

    # Internal methods
    def _update_config(self):
        for option in [option for option in Option.registry.values()
                       if option.section == 'adsense']:
            if option.name in ('hide_for_authenticated',
                               'google_search_active'):
                option.value = self.config.getbool('adsense', option.name,
                                                   True)
            elif option.name == 'search_iframe_initial_width':
                option.value = self.config.getint('adsense', option.name,
                                                  option.default)
            elif option.name == 'ads_html':
                # Still get the Option to get __doc__ from it
                db = self.env.get_db_cnx()
                cursor = db.cursor()
                cursor.execute('SELECT value FROM system WHERE name=%s',
                               ('adsense.%s' % option.name,))
                code = cursor.fetchone()
                if code:
                    code = unicode_unquote(code[0])
                option.value = code or ''
            else:
                # String options
                option.value = self.config.get('adsense', option.name,
                                               option.default)
            self.options[option.name] = option
