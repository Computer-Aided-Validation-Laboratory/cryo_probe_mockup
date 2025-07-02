import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main() -> None:
    # In plane RBM
    base_dir_folder = Path.cwd() / "DIC results/In pipe/100 mm lenses"

    u_disps5 = []
    w_disps5 = []
    u_disps24 = []
    w_disps24 = []
    for i in range(2):
        if i == 0:
            base_dir = base_dir_folder / "5 MPx"
        else:
            base_dir = base_dir_folder / "24 MPx"
        for timestep in range(1, 99):
            ## Horizontal displacements
            if timestep < 10:
                filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
            else:
                filename = base_dir / ("u/Image_00" + str(timestep) + "_0.tiff_u.csv")

            u = np.genfromtxt(filename, delimiter=",")

            if i == 0:
                u_disps5.append(u)
            else:
                u_disps24.append(u)

            ## Out of plane displacements
            if timestep < 10:
                filename = base_dir / ("w/Image_000" + str(timestep) + "_0.tiff_w.csv")
            else:
                filename = base_dir / ("w/Image_00" + str(timestep) + "_0.tiff_w.csv")

            w = np.genfromtxt(filename, delimiter=",")

            if i == 0:
                w_disps5.append(w)
            else:
                w_disps24.append(w)



    u_disps5 = np.dstack(u_disps5)
    w_disps5 = np.dstack(w_disps5)
    u_disps24 = np.dstack(u_disps24)
    w_disps24 = np.dstack(w_disps24)

    # U disps
    u_mean1 = np.mean(u_disps5, axis=2)
    u_std1 = np.std(u_disps5, axis=2)
    u_mean2 = np.mean(u_disps24, axis=2)
    u_std2 = np.std(u_disps24, axis=2)

    # W disps
    w_mean1 = np.mean(w_disps5, axis=2)
    w_std1 = np.std(w_disps5, axis=2)
    w_mean2 = np.mean(w_disps24, axis=2)
    w_std2 = np.std(w_disps24, axis=2)

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
    ax['u_mean1'].set_title(u"Mean of U (mm)")

    u_std1 = ax['u_std1'].imshow(u_std1)
    ax['u_std1'].set_yticklabels([])
    ax['u_std1'].set_xticklabels([])
    fig.colorbar(u_std1, ax=ax['u_std1'])
    ax['u_std1'].set_title("SD(U) (mm)")

    w_mean1 = ax['w_mean1'].imshow(w_mean1)
    ax['w_mean1'].set_yticklabels([])
    ax['w_mean1'].set_xticklabels([])
    fig.colorbar(w_mean1, ax=ax['w_mean1'])
    ax['w_mean1'].set_title(u"Mean of W (mm)")

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
    ax['u_mean2'].set_title(u"Mean of U (mm)")

    u_std2 = ax['u_std2'].imshow(u_std2)
    ax['u_std2'].set_yticklabels([])
    ax['u_std2'].set_xticklabels([])
    fig.colorbar(u_std2, ax=ax['u_std2'])
    ax['u_std2'].set_title("SD(U) (mm)")

    w_mean2 = ax['w_mean2'].imshow(w_mean2)
    ax['w_mean2'].set_yticklabels([])
    ax['w_mean2'].set_xticklabels([])
    fig.colorbar(w_mean2, ax=ax['w_mean2'])
    ax['w_mean2'].set_title(u"Mean of W (mm)")

    w_std2 = ax['w_std2'].imshow(w_std2)
    ax['w_std2'].set_yticklabels([])
    ax['w_std2'].set_xticklabels([])
    fig.colorbar(w_std2, ax=ax['w_std2'])
    ax['w_std2'].set_title("SD(W) (mm)")

    fig.suptitle("Static images with 100 mm lenses", size=16)
    fig.text(0.475, 0.9, "5 MPx", size=14)
    fig.text(0.475, 0.48, "24 MPx", size=14)

    # plt.show()
    filename = Path.cwd() / "DIC results/noisefloor_100mm"
    plt.savefig(filename, format="svg")
    plt.close()


if __name__ == "__main__":
    main()

