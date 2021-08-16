
<p align="left">
<a href="#logo" name="logo"><img src="https://raw.githubusercontent.com/bionanoimaging/UC2-GIT/master/IMAGES/UC2_logo_text.png" width="400"></a>
</p>

# openUC2 openSIM
---

This is the repository for the openSIM project which integrates structured illumination microscopy into the UC2-system.

🧾 The manuscript for the openISM and openSIM can be found under the [DOI:10.1101/2021.01.08.425840](https://doi.org/10.1101/2021.01.08.425840)

<p align="center">
<img src="./IMAGES/UC2_openSIM_setup_CAD.png" width="500">
</p>

***Fig 1:*** *This is the ready-to-print module which clicks into the UC2-system*



This module is based on the work by the Huser-Lab and can be found as a preprint on Bioarxiv [1]. It uses a low-cost single-mode diode laser (532 nm) and a Raspberry Pi driven DMD module to generate a structured illumination for microscopy. Since we use coherent illumination, we can create pattern suitable for SIM in order to increase the lateral resolution. So far we're not aiming for any super-resolution, but rather give a proof of principle.  

<p align="center">
<img src="./IMAGES/Assembly_openSIM_module_v2_1.png" width="500">
</p>

***Fig 2:*** *A beam-expander magnifies the collimated beam which hits the DMD displaying a set of gratings*

The angle between the collimated and expanded Laser-beam and the DMD is 25° in order to get the maximum in the diffracted orders.



[1] *DMD-based super-resolution structured illumination microscopy visualizes live cell dynamics at high speed and low cost
Alice Sandmeyer, Mario Lachetta, Hauke Sandmeyer, Wolfgang Hübner, Thomas Huser, Marcel Müller
bioRxiv 797670; doi: [https://doi.org/10.1101/797670](https://doi.org/10.1101/797670)*


***Features:***
- "True" two-beam SIM
- Very low cost:  ~400€
- Easy to align
- Open-Source
- One module per wavelength possible
- Various patterns possible

## Optical System

<p align="center">
<img src="./IMAGES/UC2_openSIM_setup.png" width="400">
</p>

***Fig 3:*** *The full system based on the modular cubes*

The system of a classical two-beam interference SIM is straight forward and based on common 4f (i.e. fourier imaging) system, where focal lengtheses of adjacent lenses are following each other. The core idea is to place two delta-peaks inside the BFP of the objective lens. The lens fourier-transforms the peaks and therefore form a grating in the sample plane.

In order to keep the whole system small, the telescope imaging the DMD is  based on two lenses with ***f'=50mm*** (e.g. Thorlabs achromates). A tube-lens of ***f'=180mm*** fourier-transforms the image folded by the mirror and places the different diffraction order inside the BFP of the objective lens. To produce 2D-Sim a fourier mask in the fourier-plane after the DMD, blocks the zeroth order.

The DMD, driven by a Raspberry Pi, gets illuminated by a more-less plane wave from a coherent laser source. The pattern which are displayed are then actually coherently reimaged inside the sample plane by the whole system.


# Table of Content
* **[Software](#-software)**
* **[Hardware](#-hardware)**
* **[Bill of materials](#-bill-of-materials)**
* **[Electronics](#-electronics)**
* **[Results](#-results)**


# Software
A dedicated Tutorial how to setup the software can be found in the [Readme_Software.md](Readme_Software.md).

# Hardware

Below we describe how the device can be build and assembled in order to replicate the whole system as shown in the rendering above [Align Tutorial](Readme_SIM_alignment_tutorial.md). One needs additional parts that can be found in the core [openUC2 repository](https://github.com/bionanoimaging/UC2-GIT).


## Bill of material

Below you will find all components necessary to build this device

### 3D printing files

All these files need to be printed. We used a Prusa i3 MK3 using PLA Prusament (Galaxy Black) at layer height 0.15 mm and infill 50%.


Parts to print:

* 1x [SIM-Module 2×4_Base](./CAD/30_CUBE_openSIM_base_v4.stl); [SIM-Module Lid](./CAD/30_CUBE_openSIM_Cagelid.stl)
* 1x [DMD holder](./CAD/30_CUBE_DMD_Holder.stl); [DMD Mount](./CAD/30_CUBE_DMD_Fixation_base.stl)
* 1x [Fourier Mask](./CAD/30_CUBE_Fouriermask.stl)
* 1x [Telescope for Beam Expansion](./CAD/30_CUBE_OpenSIM_Laser_Telescope_Mount.stl)
* 1x [Rod holder](./CAD/30_CUBE_openSIM_Rodholder.stl)
* 1x [Z-stage](https://github.com/bionanoimaging/UC2-GIT/blob/v3/CAD/ASSEMBLY_CUBE_Z-STAGE_sample/STL/20_Cube_Insert_Z-Focus_single_v3.stl)



### Additional parts
This is used in the current version of the setup

|  Type | Details  |  Price | Link  |
|---|---|---|---|
| Laser |  12V 532nm 200mw Green Laser Dot Module Fan Cooling TTL 0-30KHZ-Long time working |  90 € | [Laserland](https://www.laserlands.net/diode-laser-module/600nm-640nm-orange-red-laser-module/3258-638d.html)  |
| DMD |  Evaluierungsmodul (EVM) DLP® LightCrafter™ Display 2000 |  90 € | [Digikey](https://www.digikey.de/product-detail/de/texas-instruments/DLPDLCR2000EVM/296-47119-ND/7598640)  |
| Raspberry Pi | Raspi+SD-Card+Case+Powersupply(for DMD+Raspi, 5V, >=3A!) |  70 € | [Reichelt](https://www.reichelt.de/raspberry-pi-4-b-4x-1-5-ghz-1-gb-ram-wlan-bt-rasp-pi-4-b-1gb-p259874.html?PROVID=2788&gclid=Cj0KCQiAz53vBRCpARIsAPPsz8X9hCOt9yVVB_WqLCmKSs2e-KuThVnrMEtl2TRbAUTqtVoNZU3zM3YaAg2ZEALw_wcB&&r=1)  |
| Tube-lens | Lens, f=180mm |  10 € | [PGI-Versand](https://www.pgi-versand.de/?id=47&mode=artdet&artnr=564.OA.64)  |
| Telescope-lens | 2x Achromatic 1inch Lens, f=50mmmm |  82 € | [Thorlabs](https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-050-A)  |
| Dichroics  |  Various |  200 € | [Thorlabs]()  |
| Mirror | 1 inch Silver Mirror, Protected |  50 € | [Thorlabs](https://www.thorlabs.de/newgrouppage9.cfm?objectgroup_id=903)  |
| iPhone Lens | iPhone 5 lens for the telescope  (optional) |  5 € | [Amazon]()  |
| Lens | 25mm lens for the telescope (optional) |  5 € | [Amazon]()  |
| Cage rods  | 8 inch cage rod for 30mm cage system |  33 € | [Thorlabs](https://www.thorlabs.de/thorproduct.cfm?partnumber=ER8)  |
| PCB for Raspi-DMD connection  |  Various |  8 € | [See below]()  |
| Micrometre for z-stage  | Range 0 mm →25 mm |  30 € | [RS PRO](https://uk.rs-online.com/web/p/micrometers/7857878/)  |

### Design files
The original design files are in the [INVENTOR](./INVENTOR) folder. *FOR ANOTHER FORMAT, GET YOUR OWN FOLDER.*


### Electronics
A dedicated Tutorial which explains how to assemble and setup the electronics can be found in the [Readme_Electronics.md](Readme_Electronics.md).

### Optics

A dedicated Tutorial how to align the optical setup can be found in the [Readme_SIM_alignment_tutorial.md](Readme_SIM_alignment_tutorial.md).


## Showcase
This is just some stack where we measured the fluorescent signal on a Fluochart:

<p align="center">
<img src="./IMAGES/SIM_Basler_UC2-1.gif" width="200">
</p>

This is the result of the openSIM with a 100x 1.25 objective lens from China with Alexa Fluor 647 labelled microtubules. a) Widefield, b) SIM reconstruction on 2 angles and 5 phases

<p align="center">
<img src="./IMAGES/SIMresult.png" width="600">
</p>


## Get Involved

This project is open so that anyone can get involved. You don't even have to learn CAD designing or programming. Find ways you can contribute in  [CONTRIBUTING](https://github.com/openUC2/UC2-GIT/blob/master/CONTRIBUTING.md)


## License and Collaboration

This project is open-source and is released under the CERN open hardware license. Our aim is to make the kits commercially available.
We encourage everyone who is using our Toolbox to share their results and ideas, so that the Toolbox keeps improving. It should serve as a easy-to-use and easy-to-access general purpose building block solution for the area of STEAM education. All the design files are generally for free, but we would like to hear from you how is it going.

You're free to fork the project and enhance it. If you have any suggestions to improve it or add any additional functions make a pull-request or file an issue.

Please find the type of licenses [here](https://github.com/openUC2/UC2-GIT/blob/master/License.md)

REMARK: All files have been designed using Autodesk Inventor 2019 (EDUCATION)


## Collaborating
If you find this project useful, please like this repository, follow us on Twitter and cite the webpage! :-)
