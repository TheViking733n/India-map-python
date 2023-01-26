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
![india-colored](https://user-images.githubusercontent.com/69471106/214755236-aeff0c44-0c2d-4839-94a4-8e20f970ffd5.jpg)

2. Vertical slices of the image:
![filter-vertical](https://user-images.githubusercontent.com/69471106/214755250-310236d0-af3d-4221-b01a-af27f9315a38.png)

3. Horizontal slices of the image:
![filter-horizontal](https://user-images.githubusercontent.com/69471106/214755266-9dc25633-c8a6-4516-875a-c1ed9802b160.png)

4. Vertical and horizontal slices are superimposed to form a grid:
![filtered](https://user-images.githubusercontent.com/69471106/214755291-98f32e13-61cc-40da-8970-61466bef8e87.png)

5. Each grid is given the center color that grid:
![color-normalized](https://user-images.githubusercontent.com/69471106/214755297-03988001-0602-4099-bf07-5699627d6a40.png)

6. Color of each grid is compared with the color of the corresponding grid in the map:
![color-standard](https://user-images.githubusercontent.com/69471106/214755301-edd41dd0-8620-474d-844c-adf56652ac03.png)

7. Small output image is generated:
![india-final](https://user-images.githubusercontent.com/69471106/214755308-4168ea42-4a7a-4b83-87b4-0e4e8d937288.png)

8. Then pixels of the small output image are drawn randomly on turtle canvas. Final output:
![demo-image](https://user-images.githubusercontent.com/69471106/214755572-2442dcd8-7ceb-48f9-8ee0-49b5e4850bba.png)

