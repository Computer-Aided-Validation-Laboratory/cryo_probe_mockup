import numpy as np
from scipy.spatial.transform import Rotation
from pathlib import Path
import pyvale
import mooseherder as mh
import bpy


def main() -> None:

    # TODO: Get sample sim - add here

    # Set the save path
    # --------------------------------------------------------------------------
    base_dir = Path.cwd() / "RBM/perfect_setup/calibration_dof_new_dist"

    # Creating the scene
    # --------------------------------------------------------------------------
    scene = pyvale.BlenderScene()

    target = scene.add_cal_target(target_size=np.array([75, 50, 10]))


    # Add the camera
    cam_data_0 = pyvale.CameraData(pixels_num=np.array([2464, 2056]),
                                 pixels_size=np.array([0.00345, 0.00345]),
                                 pos_world=np.array([-25, 0, 1610]), # TODO: Work out what to make this value
                                 rot_world=Rotation.from_euler("xyz", [0, -2.5, 0], degrees=True),
                                 roi_cent_world=(0, 0, 0),
                                 focal_length=75.0,
                                 fstop=2.8)
    cam_data_1 = pyvale.CameraData(pixels_num=np.array([2464, 2056]),
                                 pixels_size=np.array([0.00345, 0.00345]),
                                 pos_world=np.array([25, 0, 1610]), # TODO: Work out what to make this value
                                 rot_world=Rotation.from_euler("xyz", [0, 2.5, 0], degrees=True),
                                 roi_cent_world=(0, 0, 0),
                                 focal_length=75.0,
                                 fstop=2.8)

    stereo_system = pyvale.CameraStereo(cam_data_0, cam_data_1)

    stereo_system.save_calibration_mid(base_dir)

    scene.add_stereo_system(stereo_system)


    for cam in [obj for obj in bpy.data.objects if obj.type == "CAMERA"]:
        bpy.context.scene.camera = cam
        cam.data.clip_end = 3500.0

    bpy.context.scene.camera.data.clip_end = 3500.0

    material_data = pyvale.BlenderMaterialData()
    speckle_path = Path.cwd() / "RBM/cal_target.tiff"
    mm_px_resolution = pyvale.CameraTools.calculate_mm_px_resolution(cam_data_0)
    scene.add_speckle(part=target,
                    speckle_path=speckle_path,
                    mat_data=material_data,
                    mm_px_resolution=mm_px_resolution,
                    cal=True)

    # Add pipe
    bpy.ops.mesh.primitive_cylinder_add(radius=38.0, depth=1333.0,
                                                    end_fill_type="NOTHING",
                                                    align='WORLD',
                                                    location=(0.0, 0.0, 666.5),
                                                    rotation=(0.0, 0.0, 0.0))
    pipe = bpy.context.view_layer.objects.active
    pipe.name = "Pipe"
    pyvale.BlenderTools.clear_material_nodes(pipe)
    node_tree = bpy.data.materials["Material.001"].node_tree
    mat_nodes = bpy.data.materials["Material.001"].node_tree.nodes
    bsdf = mat_nodes.new(type="ShaderNodeBsdfPrincipled")
    bsdf.location = (0, 0)
    bsdf.inputs["Roughness"].default_value = 0.4
    bsdf.inputs["Metallic"].default_value = 0.7
    output = node_tree.nodes.new(type="ShaderNodeOutputMaterial")
    node_tree.links.new(bsdf.outputs["BSDF"], output.inputs["Surface"])

    # Add ring light
    bpy.ops.mesh.primitive_torus_add(align="WORLD",
                                                  location=(0.0, 0.0, 1340),
                                                  rotation=(0.0, 0.0, 0.0),
                                                  major_segments=100,
                                                  minor_segments=25,
                                                  mode="EXT_INT",
                                                  abso_major_rad=58.0,
                                                  abso_minor_rad=33.0)
    ringlight = bpy.context.view_layer.objects.active
    ringlight.name = "RingLight"
    pyvale.BlenderTools.clear_material_nodes(ringlight)
    node_tree = bpy.data.materials["Material.002"].node_tree
    mat_nodes = bpy.data.materials["Material.002"].node_tree.nodes
    emission = mat_nodes.new(type="ShaderNodeEmission")
    emission.inputs["Strength"].default_value = 804.519492552*2 # W/m2
    output = node_tree.nodes.new(type="ShaderNodeOutputMaterial")
    node_tree.links.new(emission.outputs["Emission"], output.inputs["Surface"])


    calibration_data = pyvale.CalibrationData(angle_lims=(-10, 10),
                                          angle_step=10,
                                          plunge_lims=(-5, 5),
                                          plunge_step=5,
                                          x_limit=15,
                                          y_limit=5)
    number_calibration_images = pyvale.BlenderTools.number_calibration_images(calibration_data)
    print("Number of calibration images to be rendered:", number_calibration_images)

    render_data = pyvale.RenderData(cam_data=(stereo_system.cam_data_0,
                                                  stereo_system.cam_data_1),
                                        base_dir=base_dir,
                                        threads=256,
                                        samples=10)


    pyvale.BlenderTools.render_calibration_images(render_data, calibration_data, target)


    # Save Blender file
    # --------------------------------------------------------------------------
    # The file that will be saved is a Blender project file. This can be opened
    # with the Blender GUI to view the scene.
#    pyvale.BlenderTools.save_blender_file(base_dir, override=True)

if __name__ == "__main__":
    main()
