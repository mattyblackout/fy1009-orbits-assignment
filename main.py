# imports
import math
import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

# gravitational constant
G_const = 6.67408e-11


def plot_our_planets(list_of_planet_dictionaries):
    # plot a figure with a 3D axes
    fig = plot.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # use variable max_range to adjust the size of the axes to the largest orbit
    max_range = 0

    # iterate through a list of colours so each orbit has a separate colour
    colours = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan', 'orange', 'pink', 'gold', 'purple']
    colour_num = 0
    number_of_colours = len(colours)

    # go through list of dictionaries of all the orbit locations and plot them on the figure
    for current_planet in list_of_planet_dictionaries:
        # check what the largest coordinate value is and adjust our axis if we need to
        # make a square 3D matrix (x = y = z) by using one number for all three
        max_dimension = max(max(current_planet["x"]), max(current_planet["y"]))
        number_of_entries = len(current_planet["x"])
        i = 0
        z_list = []
        # while loop to calculate z values. set z to 0 for all planets in this simulation
        while i < number_of_entries:
            z_list.append(0)
            i += 1

        if max_dimension > max_range:
            max_range = max_dimension
        # plot the x, y and z coordinates for the planet, give planet a colour and label it
        ax.plot(current_planet["x"], current_planet["y"], z_list, c=colours[colour_num], label=current_planet["Name"])
        # test if the colour num is the last in list of colours and back to the beginning or go to the next colour
        if colour_num == (number_of_colours - 1):
            colour_num = 0
        else:
            colour_num += 1

    # change the axis limits so they're as small as possible and add a legend
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.legend()
    # show the plot
    plot.show()


#######################################################################################################################

# starting values:
Time_step = 10000
Number_of_steps = 6000

# dictionaries to load x and y co-ordinates into
mercury = {"Name": "Mercury", "x": [], "y": []}
venus = {"Name": "Venus", "x": [], "y": []}
earth = {"Name": "Earth", "x": [], "y": []}
mars = {"Name": "Mars", "x": [], "y": []}

all_planets_locations = [mercury, venus, earth, mars]

START_FILE = 'Planet_size_and_locations.txt'
# file contents:
# <Planet/Sun name> <Mass> <x location> <y location> <x velocity> <y velocity>

# read data from file
with open(START_FILE) as data_file:
    lines = data_file.readlines()

# iterate through each line of the file given
for line in lines:
    # split each line into the correct data categories
    planet, mass, xLocation, yLocation, xVelocity, yVelocity = line.split()

    # get mass of sun from file
    if planet == "Sun":
        Mass_of_sun = float(mass)

    # start with Mercury
    if planet == 'Mercury':
        # convert data to floats so they can be used in calculations
        xLoc, yLoc = float(xLocation), float(yLocation)
        xVel, yVel = float(xVelocity), float(yVelocity)

        # store information in dictionary
        mercury['x'].append(xLoc)
        mercury['y'].append(yLoc)

        for n in range(Number_of_steps):
            # calculate x and y values using the formulas given
            calc1 = G_const * Mass_of_sun
            calc2 = (xLoc ** 2) + (yLoc ** 2)
            calc3 = calc2 ** (3 / 2)
            calc4 = calc1 / calc3
            calc5_x, calc5_y = calc4 * (0 - xLoc), calc4 * (0 - yLoc)

            # update x and y values after jump in time
            xVel += calc5_x * Time_step
            yVel += calc5_y * Time_step
            xLoc += xVel * Time_step
            yLoc += yVel * Time_step

            # update dictionary with new x and y values
            mercury['x'].append(xLoc)
            mercury['y'].append(yLoc)

    # repeat for venus
    if planet == 'Venus':
        xLoc, yLoc = float(xLocation), float(yLocation)
        xVel, yVel = float(xVelocity), float(yVelocity)

        venus['x'].append(xLoc)
        venus['y'].append(yLoc)

        for n in range(Number_of_steps):
            calc1 = G_const * Mass_of_sun
            calc2 = (xLoc ** 2) + (yLoc ** 2)
            calc3 = calc2 ** (3 / 2)
            calc4 = calc1 / calc3
            calc5_x, calc5_y = calc4 * (0 - xLoc), calc4 * (0 - yLoc)

            xVel += calc5_x * Time_step
            yVel += calc5_y * Time_step
            xLoc += xVel * Time_step
            yLoc += yVel * Time_step

            venus['x'].append(xLoc)
            venus['y'].append(yLoc)

    # repeat for earth
    if planet == 'Earth':
        xLoc, yLoc = float(xLocation), float(yLocation)
        xVel, yVel = float(xVelocity), float(yVelocity)

        earth['x'].append(xLoc)
        earth['y'].append(yLoc)

        for n in range(Number_of_steps):
            calc1 = G_const * Mass_of_sun
            calc2 = (xLoc ** 2) + (yLoc ** 2)
            calc3 = calc2 ** (3 / 2)
            calc4 = calc1 / calc3
            calc5_x, calc5_y = calc4 * (0 - xLoc), calc4 * (0 - yLoc)

            xVel += calc5_x * Time_step
            yVel += calc5_y * Time_step
            xLoc += xVel * Time_step
            yLoc += yVel * Time_step

            earth['x'].append(xLoc)
            earth['y'].append(yLoc)

    # repeat for mars
    if planet == 'Mars':
        xLoc, yLoc = float(xLocation), float(yLocation)
        xVel, yVel = float(xVelocity), float(yVelocity)

        mars['x'].append(xLoc)
        mars['y'].append(yLoc)

        for n in range(Number_of_steps):
            calc1 = G_const * Mass_of_sun
            calc2 = (xLoc ** 2) + (yLoc ** 2)
            calc3 = calc2 ** (3 / 2)
            calc4 = calc1 / calc3
            calc5_x, calc5_y = calc4 * (0 - xLoc), calc4 * (0 - yLoc)

            xVel += calc5_x * Time_step
            yVel += calc5_y * Time_step
            xLoc += xVel * Time_step
            yLoc += yVel * Time_step

            mars['x'].append(xLoc)
            mars['y'].append(yLoc)

# pass information to plotting function
plot_our_planets(all_planets_locations)