import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def main() -> None:
    counter = 0
    imposed_disp = 0

    base_dir = Path.cwd() / "DIC results/In pipe/In plane/Compare DIC Params/19_9_affine"

    disps_19 = []

    for timestep in range(55):
        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir / ( "u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")
        u_std = np.stdnan()


        disps_19.append(u_comparison)
    disps_19 = np.dstack(disps_19)


    base_dir = Path.cwd() / "DIC results/In pipe/In plane/Compare DIC Params/21_10_affine"
    disps_21 = []
    for timestep in range(55):
        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir / ( "u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")
        imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')

        u_comparison = np.subtract(u, imposed_u)

        counter += 1
        if counter == 5:
            imposed_disp += 0.1
            counter = 0

        disps_21.append(u_comparison)
    disps_21 = np.dstack(disps_21)

    base_dir = Path.cwd() / "DIC results/In pipe/In plane/Compare DIC Params/25_10_affine"
    disps_25 = []
    for timestep in range(55):
        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir / ( "u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")
        imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')
        u_comparison = np.subtract(u, imposed_u)

        counter += 1
        if counter == 5:
            imposed_disp += 0.1
            counter = 0

        disps_25.append(u_comparison)
    disps_25 = np.dstack(disps_25)


    base_dir = Path.cwd() / "DIC results/In pipe/In plane/Compare DIC Params/29_15_affine"
    disps_29 = []
    for timestep in range(55):
        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir / ( "u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")
        imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')
        u_comparison = np.subtract(u, imposed_u)

        counter += 1
        if counter == 5:
            imposed_disp += 0.1
            counter = 0

        disps_29.append(u_comparison)
    disps_29 = np.dstack(disps_29)


    base_dir = Path.cwd() / "DIC results/In pipe/In plane/Compare DIC Params/33_15_affine"
    disps_33 = []
    for timestep in range(55):
        ## Horizontal displacements
        if timestep < 10:
            filename = base_dir / ("u/Image_000" + str(timestep) + "_0.tiff_u.csv")
        else:
            filename = base_dir / ( "u/Image_00" + str(timestep) + "_0.tiff_u.csv")

        u = np.genfromtxt(filename, delimiter=",")
        imposed_u = np.full_like(u, fill_value=imposed_disp, dtype='float64')
        u_comparison = np.subtract(u, imposed_u)

        counter += 1
        if counter == 5:
            imposed_disp += 0.1
            counter = 0

        disps_33.append(u_comparison)
    disps_33 = np.dstack(disps_33)


    # Std
    std_19 = np.std(disps_19, axis = 2)
    std_21 = np.std(disps_21, axis = 2)
    std_25 = np.std(disps_25, axis = 2)
    std_29 = np.std(disps_29, axis = 2)
    std_33 = np.std(disps_33, axis = 2)

    print("SS=19, S=9")
    ss19_avg = np.nanmean(std_19)
    ss19_max = np.nanmax(std_19)
    print(f"{ss19_avg=}")
    print(f"{ss19_max=}")
    print()

    print("SS=21, S=10")
    ss21_avg = np.nanmean(std_21)
    ss21_max = np.nanmax(std_21)
    print(f"{ss21_avg=}")
    print(f"{ss21_max=}")
    print()

    print("SS=25, S=10")
    ss25_avg = np.nanmean(std_25)
    ss25_max = np.nanmax(std_25)
    print(f"{ss25_avg=}")
    print(f"{ss25_max=}")
    print()

    print("SS=29, S=15")
    ss29_avg = np.nanmean(std_29)
    ss29_max = np.nanmax(std_29)
    print(f"{ss29_avg=}")
    print(f"{ss29_max=}")
    print()

    print("SS=33, S=15")
    ss33_avg = np.nanmean(std_33)
    ss33_max = np.nanmax(std_33)
    print(f"{ss33_avg=}")
    print(f"{ss33_max=}")
    print()




    # Plot figure
    fig, ax = plt.subplot_mosaic([
        ['std_19', 'std_21', 'std_25', 'std_29', 'std_33']
    ], figsize = (20,5))

    # In pipe
    std_19 = ax['std_19'].imshow(std_19)
    ax['std_19'].set_yticklabels([])
    ax['std_19'].set_xticklabels([])
    fig.colorbar(std_19, ax=ax['std_19'])
    ax['std_19'].set_title(u"SS=19, S=9")

    std_21 = ax['std_21'].imshow(std_21)
    ax['std_21'].set_yticklabels([])
    ax['std_21'].set_xticklabels([])
    fig.colorbar(std_21, ax=ax['std_21'])
    ax['std_21'].set_title("SS=21, S=10")

    std_25 = ax['std_25'].imshow(std_25)
    ax['std_25'].set_yticklabels([])
    ax['std_25'].set_xticklabels([])
    fig.colorbar(std_25, ax=ax['std_25'])
    ax['std_25'].set_title(u"SS=25, S=10")

    std_29 = ax['std_29'].imshow(std_29)
    ax['std_29'].set_yticklabels([])
    ax['std_29'].set_xticklabels([])
    fig.colorbar(std_29, ax=ax['std_29'])
    ax['std_29'].set_title("SS=29, S=15")

    std_33 = ax['std_33'].imshow(std_33)
    ax['std_33'].set_yticklabels([])
    ax['std_33'].set_xticklabels([])
    fig.colorbar(std_33, ax=ax['std_33'])
    ax['std_33'].set_title("SS=33, S=15")




    # fig.suptitle("In plane rigid body motion", size=16)
    # fig.text(0.475, 0.9, "Inside pipe", size=14)
    # fig.text(0.475, 0.48, "Outside pipe", size=14)

    plt.show()
    # filename = Path.cwd() / "DIC results/in_plane_noisefloor"
    # plt.savefig(filename, format="svg")
    plt.close()


if __name__ == "__main__":
    main()

