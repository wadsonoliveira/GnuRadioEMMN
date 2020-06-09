#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-floripasat author.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#


import numpy as np
from gnuradio import gr
import time
import datetime
import paho.mqtt.client as mqtt

class MQTTsubscribe(gr.sync_block):

    def __init__(self, server, port, topic, verbose):
        gr.sync_block.__init__(self,
            name="MQTT subscribe Freq",
            in_sig=[],
            out_sig=[np.float32])
        
        self.server = server
        self.port   = port
        self.topic  = topic
        self.verbose = verbose
        self.out = 0.0

        if (self.verbose):
            print("[MQTT subscribe Freq] connecting ...")
            print("[MQTT subscribe Freq] host: {}".format(server))
            print("[MQTT subscribe Freq] port: {}".format(str(port)))
        
        self.client = mqtt.Client()
        
    
    def work(self, input_items, output_items): 
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.server, self.port, 60)
        self.client.loop_start()
        output_items[0][:] = self.out
        return len(output_items[0])

    def on_connect(self, client, userdata, flags, rc):
        if (self.verbose):
            print("[MQTT subscribe Freq] Connected to broker.")
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        self.out = float(msg.payload)
        if (self.verbose):
            print('[MQTT subscribe Freq] Message received: {}'.format(self.out))


