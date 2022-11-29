import sys, json

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_poly = json.loads(sys.argv[1])
    
        new_poly = {"type": "FeatureCollection", "features": []}
        new_poly["features"].append(
            {
                "type": input_poly["type"],
                "geometry": {
                    "coordinates": input_poly["coordinates"]
                }
        })

        with open('data/user_defined_polygon.json', 'w') as fp:
            json.dump(new_poly, fp)
    else:
        print("Please input a polygon argument")

