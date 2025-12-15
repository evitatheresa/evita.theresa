# Image Processing Tutorial Using Python and OpenCV

This repository contains a comprehensive Python tutorial for image processing using OpenCV (Open Source Computer Vision Library). This tutorial is based on the Edureka Python training series.

## 📺 Video Tutorial

Watch the complete video tutorial here: [Image Processing Tutorial Using Python | Python OpenCV Tutorial](https://youtu.be/sfheWK72L74?si=jycrUzH3PIfIZqdg)

## 📋 Prerequisites

- Python 3.6 or higher
- Basic understanding of Python programming
- pip (Python package installer)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/evitatheresa/evita.theresa.git
cd evita.theresa
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 📚 Tutorial Contents

This tutorial covers the following topics:

### 1. **Basic Image Operations**
   - Reading images from disk
   - Displaying images
   - Saving images
   - Understanding image properties (shape, dtype)

### 2. **Image Manipulation**
   - Resizing images
   - Rotating images
   - Cropping images
   - Flipping images (horizontal, vertical, both)

### 3. **Color Space Conversions**
   - BGR to Grayscale
   - BGR to HSV
   - BGR to RGB
   - Splitting and merging color channels

### 4. **Image Filtering and Blurring**
   - Gaussian Blur
   - Median Blur
   - Bilateral Filter (edge-preserving)
   - Average Blur

### 5. **Edge Detection**
   - Canny Edge Detection
   - Sobel Edge Detection
   - Laplacian Edge Detection

### 6. **Image Thresholding**
   - Binary Threshold
   - Inverse Binary Threshold
   - Adaptive Threshold (Mean)
   - Adaptive Threshold (Gaussian)
   - Otsu's Threshold

### 7. **Contour Detection**
   - Finding contours
   - Drawing contours
   - Drawing bounding rectangles

### 8. **Drawing Shapes and Text**
   - Drawing rectangles
   - Drawing circles
   - Drawing lines
   - Drawing ellipses
   - Drawing polygons
   - Adding text to images

### 9. **Morphological Operations**
   - Erosion
   - Dilation
   - Opening
   - Closing
   - Morphological Gradient

### 10. **Geometric Transformations**
   - Translation
   - Scaling
   - Perspective Transformation

## 🎯 Running the Tutorial

To run the complete tutorial:

```bash
python image_processing_tutorial.py
```

This will:
- Create a sample image for demonstration
- Apply all image processing techniques
- Save output images to the `output_images/` directory
- Display progress messages in the console

## 📁 Output Structure

After running the tutorial, you'll find all processed images in the `output_images/` directory:

```
output_images/
├── sample_image.jpg
├── resized_image.jpg
├── rotated_image.jpg
├── cropped_image.jpg
├── flipped_horizontal.jpg
├── flipped_vertical.jpg
├── flipped_both.jpg
├── grayscale_image.jpg
├── hsv_image.jpg
├── blue_channel.jpg
├── green_channel.jpg
├── red_channel.jpg
├── gaussian_blur.jpg
├── median_blur.jpg
├── bilateral_filter.jpg
├── average_blur.jpg
├── canny_edges.jpg
├── sobel_edges.jpg
├── laplacian_edges.jpg
├── threshold_binary.jpg
├── threshold_binary_inv.jpg
├── adaptive_threshold_mean.jpg
├── adaptive_threshold_gaussian.jpg
├── otsu_threshold.jpg
├── contours.jpg
├── contours_rectangles.jpg
├── drawing_shapes.jpg
├── morphology_erosion.jpg
├── morphology_dilation.jpg
├── morphology_opening.jpg
├── morphology_closing.jpg
├── morphology_gradient.jpg
├── transformation_translation.jpg
├── transformation_scaling.jpg
└── transformation_perspective.jpg
```

## 💡 Learning Objectives

By the end of this tutorial, you will be able to:

1. ✅ Understand the basics of OpenCV and image processing
2. ✅ Read, manipulate, and save images using OpenCV
3. ✅ Apply various image transformations and filters
4. ✅ Detect edges and contours in images
5. ✅ Work with different color spaces
6. ✅ Apply thresholding techniques for image segmentation
7. ✅ Perform morphological operations
8. ✅ Draw shapes and add text to images
9. ✅ Apply geometric transformations

## 🔧 Customization

You can customize the tutorial by:

- Modifying parameters in each function (e.g., blur kernel size, rotation angle)
- Using your own images instead of the generated sample image
- Commenting out sections you don't need
- Adding your own image processing experiments

### Example: Using Your Own Image

Replace the `create_sample_image()` call in the `main()` function:

```python
# Instead of:
img = section_1_basic_operations()

# Use:
img = cv2.imread('path/to/your/image.jpg')
if img is None:
    print("Error: Could not read image")
    return
```

## 📖 Additional Resources

- [OpenCV Official Documentation](https://docs.opencv.org/)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Edureka YouTube Channel](https://www.youtube.com/@edurekaIN)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Author

Created as part of the Edureka Python Training series on Image Processing with OpenCV.

## 🙏 Acknowledgments

- Thanks to Edureka for the comprehensive tutorial
- OpenCV community for the excellent library
- All contributors to this project

---

**Happy Learning! 🎓**

For more Python tutorials and training, visit [Edureka](https://www.edureka.co/)
