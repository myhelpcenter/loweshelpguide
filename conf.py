# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Project information -----------------------------------------------------

project = 'Lowe’s SYF Credit Card Activation'
copyright = '2025, Lowe’s'
author = 'Lowe’s SYF Support Team'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output -------------------------------------------------------------

# ✅ IMPORTANT FIX
html_theme = 'alabaster'   # stable default theme

# (Optional better UI)
# html_theme = 'sphinx_rtd_theme'

html_title = "How to Activate Your Lowe’s SYF Credit Card Online"
html_short_title = "Lowe’s SYF Card Activation"

html_show_sourcelink = False

html_theme_options = {
    'show_powered_by': False,
}

# Static path (ensure folder exists or comment it)
html_static_path = ['_static']
