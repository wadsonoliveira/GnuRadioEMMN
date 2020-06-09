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
import pmt
import binascii

class MQTTsink(gr.sync_block):
    """
    This block has the function of send PDU data to the MQTT Broker.
    \n
    #Examples:
    -To send a frame data:
    ID: inpe_mqtt_sink_0
    Broker Hostname: 127.0.0.1
    Broker Port: 1883
    Topic: frame
    Verbose: Yes
    """
    def __init__(self, host, port, topic, verbose):
        gr.sync_block.__init__(self,
            name="MQTTsink",
            in_sig=[],
            out_sig=[])
        self.topic = topic
        self.verbose = verbose
        self.client = paho.Client()
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        if (self.verbose):
            print("[mqtt_sink] Connecting ...")
            print("[mqtt_sink] Host: {}".format(host))
            print("[mqtt_sink] Port: {}".format(str(port)))
        self.client.connect(host, port)
        self.client.loop_start()

        self.message_port_register_in(pmt.intern('in'))
        self.set_msg_handler(pmt.intern('in'), self.handle_msg)
    
    def on_disconnect(client, userdata,rc=0):
        if (self.verbose):
            print("[mqtt_sink] Disconnected with result code {}".format(str(rc)))
        self.client.loop_stop()

    def on_connect(self, client, userdata, flags, rc):
        if (self.verbose):
            print("[mqtt_sink] Connected with result code {}".format(str(rc)))

    def handle_msg(self, msg_pmt):
        msg = pmt.cdr(msg_pmt)
        if not pmt.is_u8vector(msg):
            print("[ERROR] Received invalid message type. Expected u8vector")
            return

        frame = binascii.b2a_hex(str(bytearray(pmt.u8vector_elements(msg)))).upper()

        self.client.publish(self.topic, frame)

