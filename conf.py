# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If your modules are outside the root, add paths here
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Lowe’s SYF Credit Card Activation'
copyright = '2025, Lowe’s'
author = 'Lowe’s SYF Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add more if needed)
extensions = []

# Allow raw HTML blocks inside .rst
raw_enabled = True

# Paths and exclude rules
templates_path = ['_templates']  # use only if you create custom templates
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (default: 'alabaster'; you can change to 'sphinx_rtd_theme')
# html_theme = 'sphinx_rtd_theme'

# SEO-friendly page info
html_title = "How to Activate Your Lowe’s SYF Credit Card Online"
html_short_title = "Lowe’s SYF Card Activation"
html_favicon = 'favicon.ico'  # place favicon.ico in _static or root

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst (for buttons, embeds, etc.)
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (CSS/JS/images) if needed
# html_static_path = ['_static']
