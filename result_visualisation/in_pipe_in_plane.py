import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main() -> None:
    # In plane RBM
    base_dir = Path.cwd() / "DIC results/In pipe/In plane"

    counter = 0
    imposed_disp = 0
    for timestep in range(55):

        # Original Calib

        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir / ("u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")

        imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')

        u_comparison = np.subtract(u, imposed_u)

        counter += 1
        if counter == 5:
            imposed_disp += 0.1
            counter = 0

        comparison_mean = round(np.nanmean(u_comparison), 4)
        u_std = round(np.nanstd(u), 4)

        ## Out of plane displacements
        if timestep < 10:
            filename = base_dir / ("w/Image_000" + str(timestep) + "_0.tiff_w.csv")
        else:
            filename = base_dir / ("w/Image_00" + str(timestep) + "_0.tiff_w.csv")

        w = np.genfromtxt(filename, delimiter=",")

        w_mean = round(np.nanmean(w), 4)
        w_std = round(np.nanstd(w), 4)

        ## Epipolar distance
        if timestep < 10:
            filename = base_dir / ("epi_dist/Image_000" + str(timestep) + "_0.tiff_epi_dist.csv")
        else:
            filename = base_dir / ("epi_dist/Image_00" + str(timestep) + "_0.tiff_epi_dist.csv")

        epi = np.genfromtxt(filename, delimiter=",")

        epi_mean = round(np.nanmean(epi), 4)

        # Optimised calib

        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir / ("optimised calib/u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir / ("optimised calib/u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u_optimised = np.genfromtxt(filename, delimiter=",")

        imposed_u_opt = np.full_like(u_optimised, fill_value=imposed_disp, dtype='float64')

        u_comparison_optimised = np.subtract(u_optimised, imposed_u_opt)

        comparison_mean_optimised = round(np.nanmean(u_comparison_optimised), 4)
        u_std_optimised = round(np.nanstd(u_optimised), 4)

        ## Out of plane displacements
        if timestep < 10:
            filename = base_dir / ("optimised calib/w/Image_000" + str(timestep) + "_0.tiff_w.csv")
        else:
            filename = base_dir / ("optimised calib/w/Image_00" + str(timestep) + "_0.tiff_w.csv")

        w_optimised = np.genfromtxt(filename, delimiter=",")

        w_mean_optimised = round(np.nanmean(w_optimised), 4)
        w_std_optimised = round(np.nanstd(w_optimised), 4)

        ## Epipolar distance
        if timestep < 10:
            filename = base_dir / ("optimised calib/epi_dist/Image_000" + str(timestep) + "_0.tiff_epi_dist.csv")
        else:
            filename = base_dir / ("optimised calib/epi_dist/Image_00" + str(timestep) + "_0.tiff_epi_dist.csv")

        epi_optimised = np.genfromtxt(filename, delimiter=",")

        epi_mean_optimised = round(np.nanmean(epi_optimised), 4)

        # Plot figure
        fig, ax = plt.subplot_mosaic([
            ['u', 'w', 'epi'],
             ['u_opt', 'w_opt', 'epi_opt']
        ], figsize=(11, 7))

        u = ax['u'].imshow(u_comparison)
        ax['u'].set_yticklabels([])
        ax['u'].set_xticklabels([])
        fig.colorbar(u, ax=ax['u'])
        ax['u'].set_title("U comparison")
        if abs(comparison_mean) < u_std:
            color = 'g'
        else:
            color = 'r'
        fig.text(0.175, 0.54, ("Mean = " + str(comparison_mean)), color=color)
        fig.text(0.175, 0.52, ("Std = " + str(u_std)))

        w = ax['w'].imshow(w)
        ax['w'].set_yticklabels([])
        ax['w'].set_xticklabels([])
        fig.colorbar(w, ax=ax['w'])
        ax['w'].set_title("Out of plane displacement")
        if abs(w_mean) < w_std:
            color = 'g'
        else:
            color = 'r'
        fig.text(0.45, 0.54, ("Mean = " + str(w_mean)), color=color)
        fig.text(0.45, 0.52, ("Std = " + str(w_std)))

        epi = ax['epi'].imshow(epi)
        ax['epi'].set_yticklabels([])
        ax['epi'].set_xticklabels([])
        fig.colorbar(epi, ax=ax['epi'])
        ax['epi'].set_title("Epipolar distance")
        fig.text(0.725, 0.54, ("Mean = " + str(epi_mean)))

        u_opt = ax['u_opt'].imshow(u_comparison_optimised)
        ax['u_opt'].set_yticklabels([])
        ax['u_opt'].set_xticklabels([])
        fig.colorbar(u_opt, ax=ax['u_opt'])
        ax['u_opt'].set_title("U comparison")
        if abs(comparison_mean_optimised) < u_std_optimised:
            color = 'g'
        else:
            color = 'r'
        fig.text(0.175, 0.11, ("Mean = " + str(comparison_mean_optimised)), color=color)
        fig.text(0.175, 0.09, ("Std = " + str(u_std_optimised)))

        w_opt = ax['w_opt'].imshow(w_optimised)
        ax['w_opt'].set_yticklabels([])
        ax['w_opt'].set_xticklabels([])
        fig.colorbar(w_opt, ax=ax['w_opt'])
        ax['w_opt'].set_title("Out of plane displacement")
        if abs(w_mean_optimised) < w_std_optimised:
            color = 'g'
        else:
            color = 'r'
        fig.text(0.45, 0.11, ("Mean = " + str(w_mean_optimised)), color=color)
        fig.text(0.45, 0.09, ("Std = " + str(w_std_optimised)))

        epi_opt = ax['epi_opt'].imshow(epi_optimised)
        ax['epi_opt'].set_yticklabels([])
        ax['epi_opt'].set_xticklabels([])
        fig.colorbar(epi_opt, ax=ax['epi_opt'])
        ax['epi_opt'].set_title("Epipolar distance")
        fig.text(0.725, 0.11, ("Mean = " + str(epi_mean_optimised)))

        fig.suptitle("In Plane Rigid Body Motion", size=16, weight='bold')
        fig.text(0.425, 0.9, "Initial calibration", size=14, style='italic')
        fig.text(0.4, 0.475, "Optimised calibration", size=14, style='italic')
        plt.show()


if __name__ == "__main__":
    main()

