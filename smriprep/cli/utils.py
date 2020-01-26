# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""CLI Utilities."""
from argparse import Action
from niworkflows.utils.spaces import Space, SpatialReferences
from ..conf import TF_TEMPLATES as _TF_TEMPLATES, LEGACY_SPACES


class ParseTemplates(Action):
    """Manipulate a string of templates with modifiers."""

    EXCEPTIONS = tuple()

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest,
                SpatialReferences([Space.from_string(v) for v in values]))
