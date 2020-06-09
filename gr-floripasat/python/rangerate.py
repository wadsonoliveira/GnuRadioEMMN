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
import numpy
#import string
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
        return degrees(self.satellite.az)
    def elevation(self):
        return degrees(self.satellite.alt)
    def velocity(self):
        return self.satellite.range_velocity


class rangerate(gr.sync_block):

    def __init__(self, verbose):
        gr.sync_block.__init__(self,
            name="Range Rate",
            in_sig=[np.dtype, np.dtype, np.dtype, np.dtype],
            out_sig=[np.dtype])
        self.verbose = verbose
        self.out = 0.0
        
    def work(self, input_items, output_items):
        rangerate = 0
        if(input_items[0][0] != "" and input_items[1][0] != "" and input_items[2][0] != "" and input_items[3][0] != ""):
            tle_raw     =   str(input_items[0][0])
            antenna_lat = float(input_items[1][0])
            antenna_lon = float(input_items[2][0])
            antenna_alt = float(input_items[3][0])

            aux = []
            aux = tle_raw.split('\n')

            if (self.verbose):
                print("[Range Rate] TLE: ".format(str(tle_raw)))
                print("[Range Rate] Antenna_lat: {}".format(str(antenna_lat)))
                print("[Range Rate] Antenna_lon: {}".format(str(antenna_lon)))
                print("[Range Rate] Antenna_alt: {}".format(str(antenna_alt)))
            
            if(len(aux) == 3 and antenna_lat != "" and antenna_lon != "" and antenna_alt != ""):
                antenna_gps = (str(antenna_lat), str(antenna_lon), str(int(antenna_alt)))
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
        else:
            if (self.verbose):
                print("[Range Rate] input_items[0][0]: {}".format(input_items[0][0]))
                print("[Range Rate] input_items[1][0]: {}".format(input_items[1][0]))
                print("[Range Rate] input_items[2][0]: {}".format(input_items[2][0]))
                print("[Range Rate] input_items[3][0]: {}".format(input_items[3][0]))
        
        time.sleep(0.2)
        output_items[0][:] = self.out
        return len(output_items[0])
