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

from gnuradio import gr
import ephem
import string
import numpy
import time
import datetime
import paho.mqtt.client as paho
import numpy as np

class Tracker():
    def __init__(self, satellite, groundstation):
        self.groundstation = ephem.Observer()
        self.groundstation.lat = groundstation[0]
        self.groundstation.lon = groundstation[1]
        self.groundstation.elevation = int(groundstation[2])
        self.satellite = ephem.readtle(satellite[0], satellite[1], satellite[2])
    def set_epoch(self, epoch=time.time()):
        # sets epoch when parameters are observed
        self.groundstation.date = datetime.datetime.utcfromtimestamp(epoch)
        self.satellite.compute(self.groundstation)
    def azimuth(self):
        return ephem.degrees(self.satellite.az)
    def elevation(self):
        return ephem.degrees(self.satellite.alt)
    def velocity(self):
        return self.satellite.range_velocity

class rangeratestatic(gr.sync_block):
  
    def __init__(self, tle, lat, lon, alt, verbose):
        gr.sync_block.__init__(self,
            name="Range Rate Static",
            in_sig=[],
            out_sig=[np.float32])
        
        self.tle = str(tle)
        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.verbose = verbose

    def work(self, input_items, output_items):
        rangerate = 0.0
        aux = []
        aux = self.tle.split('\n')

        if(len(aux)==3 and self.lat!="" and self.lon!="" and self.lon!=""):
            antenna_gps = (str(self.lat), str(self.lon), str(int(self.alt)))
            tracker = Tracker(aux, antenna_gps)
            tracker.set_epoch(time.time())
            rangerate = float(tracker.velocity()/299792458)
            self.out = rangerate
            if (self.verbose):
                print("[Range Rate] Time: {}".format(time.asctime(time.localtime(time.time()))))
                print("[Range Rate] Az: {}".format(str(tracker.azimuth())))
                print("[Range Rate] Ele: {}".format(str(tracker.elevation())))
                print("[Range Rate] Vel: {}".format(str(tracker.velocity())))
                print("[Range Rate] Range Rate: {}".format(str(rangerate)))
        else:
            if (self.verbose):
                print("[Range Rate] TLE received doesn't contain 3 lines")
        
        time.sleep(0.2)
        output_items[0][:] = self.out
        return len(output_items[0])
