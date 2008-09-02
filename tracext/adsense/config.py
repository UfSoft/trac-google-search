# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et

from trac.core import Component
from trac.config import Option, BoolOption, IntOption

class AdsenseConfig(Component):
    hide_for_authenticated = BoolOption(
        'adsense', 'hide_for_authenticated', True,
        """Should the ads be hidden for authenticated users."""
    )
    ads_html = Option(
        'adsense', 'ads_html', None,
        """The HTML code which displays the ads.

        NOTE: You are responsible for the HTML code you add. The author of this
              plugin won't be held responsible for the breakage of the Google
              Policy."""
    )
    ads_div_id = Option('adsense', 'ads_div_id', 'main',
        """The div ID where ads should be placed.

        If left at default value "main", a table with two columns will be
        created where regular output apears on the left column and the ads on
        the right column."""
    )
    google_search_active = BoolOption(
        'adsense', 'google_search_active', True,
        """Enable Google Adsense search."""
    )
    search_form_id = Option('adsense', 'search_form_id', 'search',
        """The form ID where the adsesnse for search code should be placed.

        The default is "search" which is trac's mini search form. Content will
        be replaced"""
    )
    search_form_text_input_width = IntOption(
        'adsense', 'search_form_text_input_width', 31,
        """
        Initial width(number of characters) of the search string text input.
        """
    )
    search_form_forid = Option('adsense', 'search_form_forid', '',
        """This is the value of the hidden input with the name "cof" that
        Google gives on their code, usualy something like "FORID:n" where n
        is an integer value. This cannot be empty."""
    )
    search_form_client_id = Option('adsense', 'search_form_client_id', '',
        """This is the value of the hidden input with the name "cx" that
        Google gives on their code, usualy something like
        "partner-pub-0000000000000000:0aaa0aaa00a" (this is just an example).
        This cannot be empty."""
    )
    search_iframe_initial_width = IntOption(
        'adsense', 'search_iframe_initial_width', 800,
        """
        Initial width of the IFRAME that Google returns. It will then increase
        the available width of the div by the ID "content".

        This value should not be that bigger because resizing only occurs
        correctly if initial size is smaller than the available width.
        """
    )
