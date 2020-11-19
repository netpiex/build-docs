# -*- coding: utf-8 -*-
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Documentation'
copyright = '2020, NETPIE'
author = 'NETPIE'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = '1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Customize Config For NEXPIE Site ----------------------------------------
# --- NEXPIE
portal_domain = 'https://portal.netpie.io'
broker_domain = 'mqtt.netpie.io'
auth_domain = 'https://authx.netpie.io'
rest_domain = 'https://api.netpie.io/v2/device'
rest_domain2 = 'api.netpie.io/v2/device'
feed_domain = 'https://api.netpie.io/v2/feed'
feed_domain2 = 'api.netpie.io/v2/feed'
swagger_part = '(ทดสอบการทำงานของ API ได้ที่ https://trial-api.netpie.io)'
platform_name = 'NETPIE'
coap_domain = 'coap://coap.netpie.io'
#gql_domain = ''

rst_prolog = """
.. |portal_url| replace:: {0}
.. |broker_url| replace:: {1}
.. |auth_url| replace:: {2}
.. |rest_url| replace:: {3}
.. |rest_url2| replace:: {4}
.. |feed_url| replace:: {5}
.. |feed_url2| replace:: {6}
.. |swagger_part| replace:: {7}
.. |platform_name| replace:: {8}
.. |coap_url| replace:: {9}
""".format(
portal_domain, 
broker_domain,
auth_domain,
rest_domain,
rest_domain2,
feed_domain,
feed_domain2,
swagger_part,
platform_name,
coap_domain
)

# -- Customize Config For NEXPIE Site ----------------------------------------

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
#---sphinx-themes-----
html_theme = 'rtcat_sphinx_theme'
import rtcat_sphinx_theme
html_theme_path = [rtcat_sphinx_theme.get_html_theme_path()]

html_logo = 'NETPIE2020-logo.png'
html_favicon = 'netpie_favicon.png'
