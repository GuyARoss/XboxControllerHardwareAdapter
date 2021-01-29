# xbox controller hardware environment 

__disclaimer__: PLEASE do not use this in live games, this repo should be used for educational purposes only. 

![pic of the rig](images/20210111_231910.jpg)
## Build Requirements
- *RaspberryPi 4 Model B (or greater)
- *3D Printer
- *Spare xbox one controller
- *x2 SG90 Micro Server Motors
- *PCA9685 Motor Controller
- [USB Video Capture Card](https://www.amazon.com/gp/product/B08LPT3T12/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
- Assortment of cables 

## Build Steps
1. Print the required parts on your 3d printer
2. Clone this repo on your raspberry pi
3. Ensure python3 is installed on your machine
4. Install the project dependencies
5. Run the code with `python main.py` in the `/app` directory.
6. Profit

## Run in barebones mode
Barebones mode makes the assumption that a dedicated hardware device for video-in is not available which basically enables the same set of gameplay procedures to run continuously. 
You can enable that mode by using the flag `--nopredict=true` when starting the application

## 3D Models
I need to clean these up first, then I will link them on here
