import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main() -> None:
    # In plane RBM
    base_dir1 = Path.cwd() / "DIC results/In pipe/In plane"
    base_dir2 = Path.cwd() / "DIC results/In pipe/In plane/optimised calib"

    counter = 0
    imposed_disp = 0
    u_comp1 = []
    u_disps1 = []
    w_disps1 = []
    u_comp2 = []
    u_disps2 = []
    w_disps2 = []
    for timestep in range(55):

        # In Pipe Original Calib

        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir1 / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir1 / ("u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")

        imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')

        u_comparison = np.subtract(u, imposed_u)

        u_disps1.append(u)
        u_comp1.append(u_comparison)

        counter += 1
        if counter == 5:
            imposed_disp += 0.1
            counter = 0

        ## Out of plane displacements
        if timestep < 10:
            filename = base_dir1 / ("w/Image_000" + str(timestep) + "_0.tiff_w.csv")
        else:
            filename = base_dir1 / ("w/Image_00" + str(timestep) + "_0.tiff_w.csv")

        w = np.genfromtxt(filename, delimiter=",")

        w_disps1.append(w)

        # Out of Pipe Original Calib

        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir2 / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir2 / ("u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")

        imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')

        u_comparison = np.subtract(u, imposed_u)

        u_disps2.append(u)
        u_comp2.append(u_comparison)

        ## Out of plane displacements
        if timestep < 10:
            filename = base_dir2 / ("w/Image_000" + str(timestep) + "_0.tiff_w.csv")
        else:
            filename = base_dir2 / ("w/Image_00" + str(timestep) + "_0.tiff_w.csv")

        w = np.genfromtxt(filename, delimiter=",")

        w_disps2.append(w)




    u_disps1 = np.dstack(u_disps1)
    u_comp1 = np.dstack(u_comp1)
    w_disps1 = np.dstack(w_disps1)
    u_disps2 = np.dstack(u_disps2)
    u_comp2 = np.dstack(u_comp2)
    w_disps2 = np.dstack(w_disps2)

    # U disps
    u_mean1 = np.mean(u_comp1, axis=2)
    u_std1 = np.std(u_disps1, axis=2)
    u_mean2 = np.mean(u_comp2, axis=2)
    u_std2 = np.std(u_disps2, axis=2)

    # W disps
    w_mean1 = np.mean(w_disps1, axis=2)
    w_std1 = np.std(w_disps1, axis=2)
    w_mean2 = np.mean(w_disps2, axis=2)
    w_std2 = np.std(w_disps2, axis=2)

    # Plot figure
    fig, ax = plt.subplot_mosaic([
        ['u_mean1', 'u_std1', 'w_mean1', 'w_std1'],
        ['u_mean2', 'u_std2', 'w_mean2', 'w_std2']
    ], figsize = (15,7))

    # In pipe
    u_mean1 = ax['u_mean1'].imshow(u_mean1)
    ax['u_mean1'].set_yticklabels([])
    ax['u_mean1'].set_xticklabels([])
    fig.colorbar(u_mean1, ax=ax['u_mean1'])
    ax['u_mean1'].set_title(u"Mean U (mm)")

    u_std1 = ax['u_std1'].imshow(u_std1)
    ax['u_std1'].set_yticklabels([])
    ax['u_std1'].set_xticklabels([])
    fig.colorbar(u_std1, ax=ax['u_std1'])
    ax['u_std1'].set_title("SD(U) (mm)")

    w_mean1 = ax['w_mean1'].imshow(w_mean1)
    ax['w_mean1'].set_yticklabels([])
    ax['w_mean1'].set_xticklabels([])
    fig.colorbar(w_mean1, ax=ax['w_mean1'])
    ax['w_mean1'].set_title(u"Mean W (mm)")

    w_std1 = ax['w_std1'].imshow(w_std1)
    ax['w_std1'].set_yticklabels([])
    ax['w_std1'].set_xticklabels([])
    fig.colorbar(w_std1, ax=ax['w_std1'])
    ax['w_std1'].set_title("SD(W) (mm)")

    # Out of pipe
    u_mean2 = ax['u_mean2'].imshow(u_mean2)
    ax['u_mean2'].set_yticklabels([])
    ax['u_mean2'].set_xticklabels([])
    fig.colorbar(u_mean2, ax=ax['u_mean2'])
    ax['u_mean2'].set_title(u"Mean U (mm)")

    u_std2 = ax['u_std2'].imshow(u_std2)
    ax['u_std2'].set_yticklabels([])
    ax['u_std2'].set_xticklabels([])
    fig.colorbar(u_std2, ax=ax['u_std2'])
    ax['u_std2'].set_title("SD(U) (mm)")

    w_mean2 = ax['w_mean2'].imshow(w_mean2)
    ax['w_mean2'].set_yticklabels([])
    ax['w_mean2'].set_xticklabels([])
    fig.colorbar(w_mean2, ax=ax['w_mean2'])
    ax['w_mean2'].set_title(u"Mean W (mm)")

    w_std2 = ax['w_std2'].imshow(w_std2)
    ax['w_std2'].set_yticklabels([])
    ax['w_std2'].set_xticklabels([])
    fig.colorbar(w_std2, ax=ax['w_std2'])
    ax['w_std2'].set_title("SD(W) (mm)")

    fig.suptitle("Impact of correlation-based optimisation for rigid body motion", size=16)
    fig.text(0.45, 0.9, "Original calibration", size=14)
    fig.text(0.45, 0.48, "Optimised calibration", size=14)

    # plt.show()
    filename = Path.cwd() / "Error_maps/compare_optimisation_rbm.svg"
    plt.savefig(filename, format="svg")
    plt.close()


if __name__ == "__main__":
    main()

