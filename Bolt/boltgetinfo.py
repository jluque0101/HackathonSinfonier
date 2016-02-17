#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The MIT License (MIT)

    Copyright (c) 2014 sinfonier-project

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""


import basesinfonierbolt
import facebook
import requests
import unicodedata

class BoltGetInfo(basesinfonierbolt.BaseSinfonierBolt):

    def __init__(self):

        basesinfonierbolt.BaseSinfonierBolt().__init__()

    def userprepare(self):

        self.token = self.getParam("token")

    def userprocess(self):

	#Conseguimos el nodo con informacion del perfil a partir del token
	self.graph = facebook.GraphAPI(self.token)
	self.perfil = self.graph.get_object("me")

	#Obetenemos la información
	self.name = self.profile['name'].encode('utf-8')
	self.id_f = self.profile['id']

	#Nuevos campos de la tupla
	self.addField("nombre",self.name)
	self.addField("id",self.id_f)
        self.emit()

    def userclose(self):

        pass

BoltGetInfo.run()