# Cryo-magnetic Probe Mock-up Work

## Stereo Setup  


## Correlation-based Optimisation
MatchID's correlation-based optimisation calibration method was tested on both experimental and Blender-rendered images.   
This module can now input multiple stereo image pairs and minimise the epipolar distance to calculate a new set of calibration parameters.   
There are three options for which calibration parameters to optimise:
- Extrinsics
- Extrinsics and intrinsics (exluding distortion)
- Extrinsics and intrinsics (including distortion)  

The impact of all the options on the calibration parameters were investigated.
Generally, the intrinsic parameters did not change significantly, even when optimised. 
Also when both intrinsic and extrinsic parameters were optimised, the extrinsic parameters did not change as significantly as when only the extrinsic parameters were optimised.  

For all the sets of images tested, the stereo angle increased when the parameters were optimised.   
This optimised calibration process has a positive impact on the processing of the DIC images. 
Using the optimised calibration parameters lowers both the systematic and random error for both out-of-plane movement and epipolar distance. 
The level of error for in-plane movement is increased, but ............


Both static and deforming/rigid body motion images can be utilised to optimise the calibration.  


## Image Averaging
In order to migitage random error, image averaging for a reference image will be utilised. 

## Impact of Stereo Angle
The impact of the non-optimal stereo angle and reflections from the pipe were investigated.
This was done by comparing two setups:
- Imaging down the mock-up with a stereo angle of ~5 deg
- Imaging the sample at the same distance with an optimal stereo angle of ~20 deg   



## Impact of Changing Stand-off Distance
