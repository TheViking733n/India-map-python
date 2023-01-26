# India Map Python
Generates a mosaic art of India map from an image using Python.
Uses the PIL library to generate the mosaic art and turtle to draw the map.

## Requirements
- Python 3.6
- PIL
- turtle


## Usage
- Clone the repository
- Run the following command in the terminal
```sh
python india.py
```

## Output

https://user-images.githubusercontent.com/69471106/214754192-4a724531-a6f3-4352-8c8c-bb8bf962721d.mp4



## How it works?

1. Input image:


2. Vertical slices of the image:


3. Horizontal slices of the image:


4. Vertical and horizontal slices are superimposed to form a grid:


5. Each grid is given the center color that grid:


6. Color of each grid is compared with the color of the corresponding grid in the map:


7. Small output image is generated:


8. Pixels of the small output image are drawn randomly on turtle canvas:
