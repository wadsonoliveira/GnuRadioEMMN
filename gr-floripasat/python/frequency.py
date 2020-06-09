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

class frequency(gr.sync_block):

    def __init__(self, freq):
        gr.sync_block.__init__(self,
            name="frequency",
            in_sig=[],
            out_sig=[np.float32])
        self.freq = freq

    def work(self, input_items, output_items):
        output_items[0][:] = self.freq
        return len(output_items[0])

