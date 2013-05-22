# -*- coding: utf-8 -*-

from collective.saversioning.history_meta import VersionedMeta, VersionedListener, ZopeVersionedTransactionExtension

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
