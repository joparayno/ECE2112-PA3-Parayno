# ECE2112-PA3-Parayno

This experiment aims to introduce the Pandas library in Python, focusing on identifying the codes and functions incorporated within the Pandas library. By the end, the students will be able to be proficient in applying and utilizing the various codes and functions within a Python program, utilizing the Pandas library.

## Table of Contents
* [Prerequisites](#Prerequisites)
* [Getting Started](#Getting-Started)
* [Experiment 3](#Experiment-3)
* [Problem 1](#Problem-1)
* [Problem 2](#Problem-2)
* [Authors](#Authors)
* [Version History](#Version-History)

## Prerequisites 
* Physical server or virtual machine.
* CPU: 2 x 64-bit, 2.8 GHz, 8.00 GT/s CPUs or better.
* Memory: minimum RAM size of 32 GB, or 16 GB RAM with 1600 MHz DDR3 installed, for a typical installation with 50 regular users.
* Client environment may be Windows, macOS or Linux.
  
## Getting Started

You must first install Anaconda Navigator from https://www.anaconda.com/download to install Jupyter Notebook. 

### Mac
1. Visit the site for Anaconda Navigator.
2. Press Download and select your Mac Architecture. This
   * Intel Processor (This is for devices that have an Intel Processor)
   * Apple ARM M1 or M2 (This is for devices that have Apple Silicon specifically for M1 or later)
3. Execute the file and it will ask for you if you trust it and press 'Allow'.
4. Agree to the Terms and Conditions and press Install
5. Click continue and you can now delete the installer.
6. Open Anaconda Navigator and Launch the Jupyter Notebook.

### Windows
1. Visit the site for Anaconda Navigator.
2. Press Download and select Windows
3. Save the exe file and run the installer
4. Press the next button until you see the Install button and press Install.
5. Once you’ve installed Anaconda Navigator, open it and launch the Jupyter Notebook.

### Linux
1. Visit the site for Anaconda Navigator.
2. Select Linux
3. Copy the bash (.sh file) installer link
4. Use wget to download the bash installer
5. Run the bash script to install Anaconda3
6. source the .bash-rc file to add Anaconda to your PATH
7. Start the Python REPL

## Experiment 3

### Instructions:
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.
For this programming assignment, download the following file and save to your default user folder:
http://bit.ly/Cars_file

## Problem 1

To successfully complete this problem, I used the knowledge gained from previous experiments and demonstrations.

a. Load the corresponding .csv file into a data frame named cars using pandas.

```
import pandas as pd
cars = pd.read_csv("Cars data.csv")
cars
```
The code above enabled me to import and read the data from the ‘Cars data.csv’ file, resulting in the following data.

![Screenshot 2024-09-15 at 11 05 57 PM](https://github.com/user-attachments/assets/41c0eae8-b1f1-4a1f-9f73-d27af61c56ce)

b. Display the first five and last five rows of the resulting cars.

```
FirstFive = cars.head()
LastFive = cars.tail()

Table = [FirstFive, LastFive]

result = pd.concat(Table)

print("The First and Last Five:")

result
```
The code above allowed me to retrieve the first five and last five rows of data from the ‘Cars data.csv’ file.

![Screenshot 2024-09-15 at 11 10 05 PM](https://github.com/user-attachments/assets/bd889877-f5de-496f-98e3-2665dcd3d0f5)

## Problem 2

To extract the necessary information from the dataframe presented in Problem 1, I will employ a combination of subsetting, slicing, and indexing techniques.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

```
cars[0:10] [1::2]
```

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4
Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

## Authors
Jarrel Parayno (jarrel.parayno.eng@ust.edu.ph)

## Version History
* 0.4
  * Updated the README.md file
  * 
* 0.3
  * Updated the README.md file
* 0.2
  * Updated the README.md file
* 0.1
  * Created a README.md file
  * Initial Release 
