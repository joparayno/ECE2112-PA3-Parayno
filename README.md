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
2. Press Download and select your Mac Architecture.
   * Intel Processor (This is for devices that have an Intel Processor).
   * Apple ARM M1 or M2 (This is for devices that have Apple Silicon specifically for M1 or later).
3. Execute the file and it will ask for you if you trust it and press 'Allow'.
4. Agree to the Terms and Conditions and press Install.
5. Click continue and you can now delete the installer.
6. Open Anaconda Navigator and Launch the Jupyter Notebook.

### Windows
1. Visit the site for Anaconda Navigator.
2. Press Download and select Windows.
3. Save the exe file and run the installer.
4. Press the next button until you see the Install button and press Install.
5. Once you’ve installed Anaconda Navigator, open it and launch the Jupyter Notebook.

### Linux
1. Visit the site for Anaconda Navigator.
2. Select Linux
3. Copy the bash (.sh file) installer link.
4. Use wget to download the bash installer.
5. Run the bash script to install Anaconda3.
6. source the .bash-rc file to add Anaconda to your PATH.
7. Start the Python REPL.

## Experiment 3

### Instructions:
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter notebook in the dedicated submission bin.
For this programming assignment, download the following file and save to your default user folder:
http://bit.ly/Cars_file

## Problem 1

To successfully complete this problem, I used the knowledge gained from previous experiments and demonstrations.

#### a. Load the corresponding .csv file into a data frame named cars using pandas.

```
import pandas as pd
cars = pd.read_csv("Cars data.csv")
cars
```
The code above enabled me to import and read the data from the ‘Cars data.csv’ file, resulting in the following data.

![Screenshot 2024-09-15 at 11 05 57 PM](https://github.com/user-attachments/assets/41c0eae8-b1f1-4a1f-9f73-d27af61c56ce)

#### b. Display the first five and last five rows of the resulting cars.

```
FirstFive = cars.head()
LastFive = cars.tail()

Table = [FirstFive, LastFive]

result = pd.concat(Table)

result
```
The code above allowed me to retrieve the first five and last five rows of data from the ‘Cars data.csv’ file.

![Screenshot 2024-09-16 at 12 03 31 AM](https://github.com/user-attachments/assets/f3eb5014-bf16-43ed-a5b8-c417e06f24f1)

## Problem 2

To extract the necessary information from the dataframe presented in Problem 1, I will employ a combination of subsetting, slicing, and indexing techniques.

#### a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

```
cars[0:10] [1::2]
```

The code above enabled me to extract the initial five rows containing odd-numbered columns (1, 3, 5, 7) of the car data, resulting in the output shown below.

![Screenshot 2024-09-15 at 11 47 26 PM](https://github.com/user-attachments/assets/203f5c62-bf6b-4893-a384-0da96f77d59b)

#### b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

```
cars.loc[cars['Model'] == 'Mazda RX4']
```

The code above enabled me to display the row that contains the Model of Mazda RX4, resulting in the output shown below.

![Screenshot 2024-09-15 at 11 47 26 PM](https://github.com/user-attachments/assets/203f5c62-bf6b-4893-a384-0da96f77d59b)

#### c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

```
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
```

The code above enabled me to filter rows in the cars DataFrame where the car model 'Camaro Z28', and then selects only the 'Model' and 'cyl'. The resulting output is displayed below.

![Screenshot 2024-09-15 at 11 48 13 PM](https://github.com/user-attachments/assets/f7ebb04c-30aa-4ea1-af3f-eb495c71fec4)

#### d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

```
cars[['Model', 'cyl', 'gear']][cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])]
```

With the help of the .isin function, I was able to filter and select specific data within the data frame. This enabled me to determine the number of cylinders and the type of gear the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’ have. The resulting output is displayed below.

![Screenshot 2024-09-15 at 11 48 29 PM](https://github.com/user-attachments/assets/d4f3d7fd-5c9c-423f-ba5f-d3b4c5d683ea)

## Authors
Jarrel Parayno (jarrel.parayno.eng@ust.edu.ph)

## Version History
* 0.5
  * Updated the README.md file
  * Uploaded the ipynb and py files
* 0.4
  * Updated the README.md file
* 0.3
  * Updated the README.md file
* 0.2
  * Updated the README.md file
* 0.1
  * Created a README.md file
  * Initial Release 
