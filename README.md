# geolocation-poly-intersection

geolocation-poly-intersection implements and compares performance of 3 popular geometric algorithms: polygon-polygon intersection, point-in-polygons, and line-simplification. It utilizes a dataset of Oct, 2022 car crashes in Ohio and GeoJSON data for visualization purposes.

### Installation

Clone this repository to a local copy and cd into the new repository
```
git clone https://github.com/wang2989/geolocation-poly-intersection.git
cd geolocation-poly-intersection
```

For the next step, ensure pipenv is installed. If not, you can use the following command (if you have pip) to install
```
pip install pipenv
```

Install all dependencies
```
pipenv install --ignore-pipfile
```

Afterwards, you can open a pipenv shell and check if the correct python version is installed
```
pipenv shell
python --version
```

Now, ensuring you are in the geolocation-poly-intersection top directory, run the runfile
```
sh runfile.sh
```

### Usage
After running the runfile.sh file, the browser should open six tabs. The first four will be reports showing performance comparisons of the various algorithms. The fifth tab will display the graphs of these runtime comparisons. The final tab is a KeplerGL demo with the relevant datasets visualized for the user to interact with.

# EXPERIMENTAL
Should the user want to change the area used to calculate overlapping polygons, they can open kepler.gl/demo in a web browser draw a relevant polygon within the bounds of Ohio. Then, the user can right click the polygon and select 'Copy Geometry'. The user should then run the following commands to reproduce the reports and visualizations with the polygon.

```
python3 create_new_polygon_for_test.py [COPIED GEOMETRY VALUE]
sh runfile.sh
```

