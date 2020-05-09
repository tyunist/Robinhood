from __future__ import absolute_import
import six

if six.PY3:
    from .Robinhood import Robinhood
else:
    from Robinhood import Robinhood
    import exceptions as RH_exception
