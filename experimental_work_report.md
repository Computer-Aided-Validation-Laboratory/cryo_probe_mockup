# Cryo-magnetic Probe Mock-up Work

## Stereo Setup
Although having a stereo DIC setup is possible for this testing, it poses many challenges.
Most of the challenges were due to the constrained optical access present in the setup.
This impacted the lighting, lens choice and possible stereo angle.

The lighting in this setup was challenging since a powerful light source was required to illuminate the sample located ~1.4 m away.
It was decided to use a ring light to avoid shadows from the cameras.
This lighting then introduced another challenge: reflections from the probe itself.
In order to combat the effect of these reflections, polariser film was placed in front of the light and polarising filters were attatched to the lenses.
These polarisers greatly improved the quality of the images taken, and allowed them to be correlated through MatchID.
Another issue with the lighting was the difficulty in producing images where no part of the sample was over-exposed or in shadow.
This was possible with a smaller stereo angle between the cameras, but as the angle between the cameras increased this became a challenge and meant that MatchID struggled to correlate the images.

The most challenging aspect of the setup was the positioning of the cameras.
Due to the long distance to the sample and the small diameter of the probe, the cameras had to be positioned fairly close to one another.
This meant that only a small stereo angle could be acheived.
This positioning constraint also impacted the choice of lenses to use.
Normally, high focal length macro lenses could be used for these scenarios with large stand-off distances.
However, since these macro lenses are considerably larger they could not be used for this application.
The size of lens was also a constraint of the stereo angle.

With the challenging camera setup came a challenging calibration.
Due to the fact that both cameras were looking down the probe and the end of the probe only took up a portion of their FOV, calibrating was not optimal.
Calibration images representative of the entire FOV could not be produced due to the optical setup.
This meant that the calibration parameters procuced from these calibration images are likely to not be fully accurate of reality.
Ways to try and mitigate this will be discussed below.

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

Error maps - show difference


## Image Averaging
In order to migitage random error, image averaging for a reference image will be utilised.

## Impact of Stereo Angle
The impact of the non-optimal stereo angle and reflections from the pipe were investigated.
This was done by comparing two setups:
- Imaging down the mock-up with a stereo angle of ~5 deg
- Imaging the sample at the same distance with an optimal stereo angle of ~20 deg


Error maps



## Impact of Changing Stand-off Distance


## Comparison to Blender images
- Calibration - underestimated stereo angle
