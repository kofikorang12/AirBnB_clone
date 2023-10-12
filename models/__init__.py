#!/usr/bin/env python3
''' Initializes module
'''

import models.engine.file_storage as fs

storage = fs.FileStorage()
storage.reload()
