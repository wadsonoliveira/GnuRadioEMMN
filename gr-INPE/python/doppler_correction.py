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

from gnuradio import gr
import time
import datetime
import ephem
from math import *
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

class doppler_correction(gr.sync_block):
    """
    docstring for block doppler_correction
    \n
    This block has the function to calculate the doppler frequency through the satellite TLE, satellite's frequency, antenna latitude, antenna longitute and antenna altitude.
    \n
    #Notes:
    -To use this block it's necessary create a variable for generate the result. For example: doppler_freq. After this, the doppler_correction block will change the value of this variable according with the local time and others variables already mentioned.
    -This block was created to work only with Data Source Block and MQTT Source Block. To use doppler_correction with other block it is necessary to set the output type (other block) to numpy.dtype .
    -Positive latitude is above the equator (N), and negative latitude is below the equator (S).
    -Positive longitude is east of the prime meridian, while negative longitude is west of the prime meridian.
    \n
    #Examples:
    ID: inpe_doppler_correction_0
    Variable: doppler_freq
    \n
    #Inputs:
    -tle => receive the information about tle.
    Example:
    "SCD 1
    1 22490U 93009B   18313.53585030  .00000217  00000-0  94868-5 0  9993
    2 22490  24.9712  40.8641 0042943 322.8024 149.1002 14.44536244359472"
    Or
    "SCD 1                   \\n1 22490U 93009B   18312.49589122  .00000212  00000-0  80367-5 0  9997\\n2 22490  24.9710  47.2687 0042922 311.7938 140.9989 14.44536139359048"
    -freq => receive the information about center frequency of the satellite comunnication.
    Example:
    145000000
    -lat => receive the information about the antenna latitude (N).
    Example:
    -5.7793
    -lon => receive the information about the antenna longitude (E).
    Example:
    -35.2010
    -alt => receive the information about the antenna altitude (m).
    Example:
    14
    """

    def __init__(self, callback, verbose):
        gr.sync_block.__init__(self,
            name="doppler_correction",
            in_sig=[np.dtype, np.dtype, np.dtype, np.dtype, np.dtype],
            out_sig=[])
        
        self.callback = callback
        self.verbose = verbose


    def work(self, input_items, output_items):
        doppler_freq = 0
        if(input_items[0][0] != "" and input_items[1][0] != ""  and input_items[2][0] != "" and input_items[3][0] != "" and input_items[4][0] != ""):
            tle_raw     =   str(input_items[0][0])
            freq        = float(input_items[1][0])
            antenna_lat = float(input_items[2][0])
            antenna_lon = float(input_items[3][0])
            antenna_alt = float(input_items[4][0])

            tle = tle_raw.split('\n')

            if (self.verbose):
                print("[Speed Rate] tle         : " + str(tle_raw))
                print("[Speed Rate] freq        : " + str(freq))
                print("[Speed Rate] antenna_lat : " + str(antenna_lat))
                print("[Speed Rate] antenna_lon : " + str(antenna_lon))
                print("[Speed Rate] antenna_alt : " + str(antenna_alt))

            if(len(tle) == 3 and freq != "" and antenna_lat != "" and antenna_lon != "" and antenna_alt != ""):
                antenna_gps = (str(antenna_lat), str(antenna_lon), str(int(antenna_alt))) 
                #A biblioteca só aceita inteiro na altura.... 
                #TODO: Arredondar valor em vez de truncar (valor mais próximo)
                tracker = Tracker(tle, antenna_gps)
                tracker.set_epoch(time.time())
                doppler_freq = float(freq * tracker.velocity()/299792458)
                if (self.verbose):
                    print("[Speed Rate] time : " + time.asctime( time.localtime(time.time()) ))
                    print("[Speed Rate] az   : " + str(tracker.azimuth()))
                    #print ("ele  : " + str(tracker.elevation())
                    #print ("vel  : " + str(tracker.velocity())
                    print("[Speed Rate] dop  : " + str(doppler_freq))
            else:
                if (self.verbose):
                    print("[Speed Rate] TLE received doesn't contain 3 lines")
        else:
            if (self.verbose):
                print("[Speed Rate] input_items[0][0] : " + input_items[0][0])
                print("[Speed Rate] input_items[1][0] : " + input_items[1][0])
                print("[Speed Rate] input_items[2][0] : " + input_items[2][0])
                print("[Speed Rate] input_items[3][0] : " + input_items[3][0])
                print("[Speed Rate] input_items[4][0] : " + input_items[4][0])
        self.callback(doppler_freq)
        time.sleep(0.2)
        return len(input_items[0])

