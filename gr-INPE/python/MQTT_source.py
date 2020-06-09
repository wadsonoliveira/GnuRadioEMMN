#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-INPE author.
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
import paho.mqtt.client as paho

class MQTT_source(gr.sync_block):
    """
    This block has the function of receive data from MQTT Broker and after this to send to the doppler_correction block.
    \n
    #Notes:
    -This block was created to work only with Doppler Correction Block. To use mqtt_source with other block it is necessary to set the input type (other block) to numpy.dtype in the block code.
    \n
    #Examples:
    -To set a TLE data:
    ID: inpe_mqtt_source_0
    Broker Hostname: 127.0.0.1
    Broker Port: 1883
    Topic: tle
    Verbose: Yes
    """
    def __init__(self, host, port, topic, verbose):
        gr.sync_block.__init__(self,
            name="MQTT_source",
            in_sig=[],
            out_sig=[np.dtype])
        self.topic = topic
        self.verbose = verbose
        self.out = ""

        self.client = paho.Client()

        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

        if (self.verbose):
            print("[mqtt_source] Connecting ...")
            print(("[mqtt_source] Host: {}".format(host)))
            print(("[mqtt_source] Port: {}".format(str(port))))
        self.client.connect(host, port)
    
    def work(self, input_items, output_items):
        self.client.loop_start()
        output_items[0][:] = self.out
        return len(output_items[0])

    def on_connect(self, client, userdata, flags, rc):
        if (self.verbose):
            print(("[mqtt_source] Connected with result code {}".format(str(rc))))
            print(("[mqtt_source] topic: {}".format(self.topic)))
        client.subscribe(self.topic)

    def on_message(self, client, userdata, message):
        self.out = str(message.payload.decode("utf-8"))
        if (self.verbose):
            print(("[mqtt_source] Message received {}".format(str(message.payload.decode("utf-8")))))
