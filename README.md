# CS461_program_1
# A* Pathfinding in Kansas Cities

## Overview
This Python script implements a **basic A\* search** to find a path between two user-selected cities in Kansas. It:
- Computes distances between cities using **latitude/longitude** data.
- Lets you specify a **start** and **end** city from a predefined list.
- Uses a **frontier** (cities to explore) and a **been_there** list (visited cities).
- Plots the resulting path on a map using **matplotlib**.

## Key Features
1. **City Coordinates**  
   - A predefined list (`cities_x_y`) of Kansas cities, each with name, latitude, and longitude.
   
2. **A\* Heuristic**  
   - Combines the distance from the **current city** to the **next** plus the **distance to the goal** (heuristic).
   - Terminates as soon as the goal city is reached.

3. **User Prompts**  
   - Asks for a start city and end city.
   - Checks for valid city names and exits on invalid input.

4. **Plotting**  
   - Marks the **start** and **end** cities in **red**.
   - Plots other cities in **blue**.
   - Draws the **path** line connecting the visited cities from start to goal.

## Requirements
- **Python 3**
- Libraries:
  - `math`
  - `matplotlib`
  - `time`
  - `sys`

If you need to install matplotlib, use:
pip install matplotlib

## Usage
1. **Run the script**:  
   python your_script_name.py  
2. **Enter the start city** when prompted.
3. **Enter the goal city** when prompted.
4. The script performs its search, then:
   - Prints the cities visited along the path.
   - Shows **runtime** in seconds.
   - Displays a **matplotlib** plot with the discovered path.

## Example Output
- **Console** might show lines like:
  - City checks, a final list of visited cities, and the path cost.
  - "runtime : --- X seconds ---"
- **Matplotlib** window with:
  - Red X markers for start/end.
  - Blue X markers for intermediate cities.
  - A line connecting the path.

## License
This project is released as **open-source** for educational and research purposes.
