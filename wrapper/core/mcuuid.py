# -*- coding: utf-8 -*-

import uuid


class MCUUID (uuid.UUID):
    """
    This class is currently not being used, but may be benefitial in regards to
    conforming UUIDs
    """
    def __init__(self, hex=None, bytes=None, bytes_le=None, fields=None, int=None, version=None):
        super(MCUUID, self).__init__(hex, bytes, bytes_le, fields, int, version)

    @property
    def string(self):
        return str(self)