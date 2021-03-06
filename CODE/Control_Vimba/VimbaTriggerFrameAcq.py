# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:07:53 2020

@author: UC2
"""

"""BSD 2-Clause License

Copyright (c) 2019, Allied Vision Technologies GmbH
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import sys
from typing import Optional
from vimba import *
import numpy as np
import tifffile as tif
import os
import time
import matplotlib.pyplot as plt
timestr = time.strftime("%Y%m%d-%H%M%S")

global iiter 
# Prepare Camera for ActionCommand - Trigger
myexposure = 500 # in ms 
mygain = 5
mybasepath = "C:\\Users\\UC2\\Desktop\\ISM\\"
myfolder = timestr + "_ISM_HeLa_AF647_texp-" + str(myexposure) + "_gain-" + str(mygain)
iiter = 0

try:
    os.mkdir(mybasepath+myfolder)
except:
    print("Already crated the folder?")

def print_preamble():
    print('///////////////////////////////////////////')
    print('/// Vimba API Asynchronous Grab Example ///')
    print('///////////////////////////////////////////\n')


def print_usage():
    print('Usage:')
    print('    python asynchronous_grab.py [camera_id]')
    print('    python asynchronous_grab.py [/h] [-h]')
    print()
    print('Parameters:')
    print('    camera_id   ID of the camera to use (using first camera if not specified)')
    print()


def abort(reason: str, return_code: int = 1, usage: bool = False):
    print(reason + '\n')

    if usage:
        print_usage()

    sys.exit(return_code)


def parse_args() -> Optional[str]:
    args = sys.argv[1:]
    argc = len(args)

    for arg in args:
        if arg in ('/h', '-h'):
            print_usage()
            sys.exit(0)

    if argc > 1:
        abort(reason="Invalid number of arguments. Abort.", return_code=2, usage=True)

    return None if argc == 0 else args[0]


def get_camera(camera_id: Optional[str]) -> Camera:
    with Vimba.get_instance() as vimba:
        if camera_id:
            try:
                return vimba.get_camera_by_id(camera_id)

            except VimbaCameraError:
                abort('Failed to access Camera \'{}\'. Abort.'.format(camera_id))

        else:
            cams = vimba.get_all_cameras()
            if not cams:
                abort('No Cameras accessible. Abort.')

            return cams[0]


def setup_camera(cam: Camera):
    with cam:
        # Try to adjust GeV packet size. This Feature is only available for GigE - Cameras.
        try:
            cam.GVSPAdjustPacketSize.run()

            while not cam.GVSPAdjustPacketSize.is_done():
                pass

        except (AttributeError, VimbaFeatureError):
            pass
                
        cam.TriggerSelector.set('FrameStart')
        cam.TriggerActivation.set('RisingEdge')
        cam.TriggerSource.set('Line0')
        cam.TriggerMode.set('On')
        cam.BlackLevel.set(255.0)
        cam.ExposureAuto.set("Off")
        cam.ContrastEnable.set("Off")

        cam.ExposureTime.set(myexposure*1e3)
        #cam.PixelFormat.set('Mono12')
        cam.GainAuto.set("Off")
        cam.Gain.set(mygain)
        cam.AcquisitionFrameRateEnable.set(False)
        cam.get_feature_by_name("PixelFormat").set("Mono12")

def setiter():
    global iiter
    iiter += 1

def frame_handler(cam: Camera, frame: Frame):
    #print('{} acquired {}'.format(cam, frame), flush=True)
    myframe = frame.as_numpy_ndarray()
    myfilename = mybasepath+myfolder+"\\"+str(iiter)+".tif"
    tif.imsave(myfilename, myframe)
    # not working in threads.. plt.figure(1), plt.imshow(np.squeeze(myframe)), plt.colorbar(), plt.show()
    setiter()
    print('Acquired a frame and saved it here: '+myfilename)
    
    cam.queue_frame(frame)


def main():
    print_preamble()
    cam_id = parse_args()
    frameiter = 0

    with Vimba.get_instance():
        with get_camera(cam_id) as cam:

            setup_camera(cam)
            print('Press <enter> to stop Frame acquisition.')

            try:
                # Start Streaming with a custom a buffer of 10 Frames (defaults to 5)
                cam.start_streaming(handler=frame_handler, buffer_count=10)
                input()

            finally:
                cam.stop_streaming()



if __name__ == '__main__':
    main()