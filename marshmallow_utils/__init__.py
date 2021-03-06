# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
#
# Marshmallow-Utils is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

r"""Extras and utilities for Marshmallow.

Currently this library contains a couple of extra fields as shown in the
following example:

>>> from marshmallow_utils import fields
>>> from marshmallow import Schema
>>> class MySchema(Schema):
...     trim = fields.TrimmedString()
...     html = fields.SanitizedHTML()
...     text = fields.SanitizedUnicode()
...     isodate = fields.ISODateString()
...
>>> data = MySchema().load({
...    'trim': '    whitespace   ',
...    'html': '<script>evil()</script>',
...    'text': 'PDF copy/paste\u200b\u000b\u001b\u0018 ',
...    'isodate': '1999-10-27',
... })
>>> data['trim']
'whitespace'
>>> data['html']
'evil()'
>>> data['text']
'PDF copy/paste'
>>> data['isodate']
'1999-10-27'
"""

from .version import __version__

__all__ = ('__version__', )
