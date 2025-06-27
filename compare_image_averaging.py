import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main() -> None:
    u_comp = []
    u_disp = []
    w_disp = []
    u_comp_avg = []
    u_disp_avg = []
    w_disp_avg = []

    for i in range(2):
        counter = 0
        imposed_disp = 0
        if i == 0:
            base_dir = Path.cwd() / "DIC results/In pipe/Static/In plane/optimised"
            base_dir_avg = Path.cwd() / "DIC results/In pipe/Static/In plane/Averaging/optimised"
        else:
            base_dir = Path.cwd() / "DIC results/In pipe/Static/Out of plane/optimised"
            base_dir_avg = Path.cwd() / "DIC results/In pipe/Static/Out of plane/Averaging/optimised"
        for timestep in range(55):
            # No image averaging

            ## Horizontal displacements
            if timestep < 10:
                filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
            else:
                filename = base_dir / ("u/Image_00" + str(timestep) + "_0.tiff_u.csv")

            u = np.genfromtxt(filename, delimiter=",")
            if i ==0:
                u = np.delete(u, 0, axis=0)

            imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')
            u_comparison = np.subtract(u, imposed_u)

            u_comp.append(u_comparison)
            u_disp.append(u)

            counter += 1
            if counter == 6:
                imposed_disp -= 0.1
                counter = 0

            ## Out of plane displacements
            if timestep < 10:
                filename = base_dir / ("w/Image_000" + str(timestep) + "_0.tiff_w.csv")
            else:
                filename = base_dir / ("w/Image_00" + str(timestep) + "_0.tiff_w.csv")

            w = np.genfromtxt(filename, delimiter=",")
            if i ==0:
                w = np.delete(w, 0, axis=0)

            w_disp.append(w)

            # Image averaging

            ## Horizontal displacements
            if timestep < 10:
                filename = base_dir_avg / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
            else:
                filename = base_dir_avg / ("u/Image_00" + str(timestep) + "_0.tiff_u.csv")

            u = np.genfromtxt(filename, delimiter=",")
            if i == 1:
                u = np.delete(u, 0, axis=0)
                u = np.delete(u, 0, axis=1)

            imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')
            u_comparison = np.subtract(u, imposed_u)

            u_comp_avg.append(u_comparison)
            u_disp_avg.append(u)

            ## Out of plane displacements
            if timestep < 10:
                filename = base_dir_avg / ("w/Image_000" + str(timestep) + "_0.tiff_w.csv")
            else:
                filename = base_dir_avg / ("w/Image_00" + str(timestep) + "_0.tiff_w.csv")

            w = np.genfromtxt(filename, delimiter=",")
            if i == 1:
                w = np.delete(w, 0, axis=0)
                w = np.delete(w, 0, axis=1)

            w_disp_avg.append(w)




    u_comp = np.dstack(u_comp)
    u_disp = np.dstack(u_disp)
    w_disp = np.dstack(w_disp)
    u_comp_avg = np.dstack(u_comp_avg)
    u_disp_avg = np.dstack(u_disp_avg)
    w_disp_avg = np.dstack(w_disp_avg)

    # No image averaging
    u_mean = np.mean(u_comp, axis=2)
    u_std = np.std(u_disp, axis=2)
    w_mean = np.mean(w_disp, axis=2)
    w_std = np.std(w_disp, axis=2)

    # Image averaging
    u_mean_avg = np.mean(u_comp_avg, axis=2)
    u_std_avg = np.std(u_disp_avg, axis=2)
    w_mean_avg = np.mean(w_disp_avg, axis=2)
    w_std_avg = np.std(w_disp_avg, axis=2)

    # Plot figure
    fig, ax = plt.subplot_mosaic([
        ['u_mean1', 'u_std1', 'w_mean1', 'w_std1'],
        ['u_mean2', 'u_std2', 'w_mean2', 'w_std2']
    ], figsize = (15,7))

    # In pipe
    u_mean1 = ax['u_mean1'].imshow(u_mean)
    ax['u_mean1'].set_yticklabels([])
    ax['u_mean1'].set_xticklabels([])
    fig.colorbar(u_mean1, ax=ax['u_mean1'])
    ax['u_mean1'].set_title(u"Mean U (mm)")

    u_std1 = ax['u_std1'].imshow(u_std)
    ax['u_std1'].set_yticklabels([])
    ax['u_std1'].set_xticklabels([])
    fig.colorbar(u_std1, ax=ax['u_std1'])
    ax['u_std1'].set_title("SD(U) (mm)")

    w_mean1 = ax['w_mean1'].imshow(w_mean)
    ax['w_mean1'].set_yticklabels([])
    ax['w_mean1'].set_xticklabels([])
    fig.colorbar(w_mean1, ax=ax['w_mean1'])
    ax['w_mean1'].set_title(u"Mean W (mm)")

    w_std1 = ax['w_std1'].imshow(w_std)
    ax['w_std1'].set_yticklabels([])
    ax['w_std1'].set_xticklabels([])
    fig.colorbar(w_std1, ax=ax['w_std1'])
    ax['w_std1'].set_title("SD(W) (mm)")

    # Out of pipe
    u_mean2 = ax['u_mean2'].imshow(u_mean_avg)
    ax['u_mean2'].set_yticklabels([])
    ax['u_mean2'].set_xticklabels([])
    fig.colorbar(u_mean2, ax=ax['u_mean2'])
    ax['u_mean2'].set_title(u"Mean U (mm)")

    u_std2 = ax['u_std2'].imshow(u_std_avg)
    ax['u_std2'].set_yticklabels([])
    ax['u_std2'].set_xticklabels([])
    fig.colorbar(u_std2, ax=ax['u_std2'])
    ax['u_std2'].set_title("SD(U) (mm)")

    w_mean2 = ax['w_mean2'].imshow(w_mean_avg)
    ax['w_mean2'].set_yticklabels([])
    ax['w_mean2'].set_xticklabels([])
    fig.colorbar(w_mean2, ax=ax['w_mean2'])
    ax['w_mean2'].set_title(u"Mean W (mm)")

    w_std2 = ax['w_std2'].imshow(w_std_avg)
    ax['w_std2'].set_yticklabels([])
    ax['w_std2'].set_xticklabels([])
    fig.colorbar(w_std2, ax=ax['w_std2'])
    ax['w_std2'].set_title("SD(W) (mm)")

    fig.suptitle("Static images (correlated using an optimised calibration)", size=16)
    fig.text(0.45, 0.9, "No image averaging", size=14)
    fig.text(0.45, 0.48, "Image averaging", size=14)

    # plt.show()
    filename = Path.cwd() / "DIC results/image_averaging"
    plt.savefig(filename, format="svg")
    plt.close()


if __name__ == "__main__":
    main()

