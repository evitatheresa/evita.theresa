"""
Image Processing Tutorial Using Python and OpenCV
Python OpenCV Tutorial | Python Training | Edureka

This tutorial demonstrates various image processing techniques using OpenCV library.
YouTube Tutorial: https://youtu.be/sfheWK72L74?si=jycrUzH3PIfIZqdg

Topics covered:
1. Reading, displaying, and saving images
2. Image manipulation (resize, rotate, crop, flip)
3. Color space conversions
4. Image filtering and blurring
5. Edge detection
6. Contour detection
7. Image thresholding
8. Drawing shapes and text on images
"""

import cv2
import numpy as np
import os


def create_sample_image():
    """Create a sample image for demonstration purposes."""
    # Create a 500x500 image with gradient colors
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    
    # Create a gradient effect
    for i in range(500):
        for j in range(500):
            img[i, j] = [i % 256, j % 256, (i + j) % 256]
    
    # Add some shapes
    cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
    cv2.circle(img, (350, 350), 80, (255, 0, 0), -1)
    cv2.line(img, (250, 250), (450, 450), (0, 0, 255), 5)
    cv2.putText(img, 'OpenCV Tutorial', (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    return img


def section_1_basic_operations():
    """Section 1: Reading, displaying, and saving images."""
    print("\n" + "="*60)
    print("Section 1: Basic Image Operations")
    print("="*60)
    
    # Create a sample image
    img = create_sample_image()
    
    # Save the image
    cv2.imwrite('sample_image.jpg', img)
    print("✓ Created and saved sample_image.jpg")
    
    # Read the image
    img_read = cv2.imread('sample_image.jpg')
    if img_read is not None:
        print("✓ Successfully read the image")
        print(f"  Image shape: {img_read.shape}")
        print(f"  Image dtype: {img_read.dtype}")
    
    return img_read


def section_2_image_manipulation(img):
    """Section 2: Image manipulation - resize, rotate, crop, flip."""
    print("\n" + "="*60)
    print("Section 2: Image Manipulation")
    print("="*60)
    
    # Resize image
    resized = cv2.resize(img, (300, 300))
    cv2.imwrite('resized_image.jpg', resized)
    print(f"✓ Resized image from {img.shape[:2]} to {resized.shape[:2]}")
    
    # Rotate image
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated = cv2.warpAffine(img, rotation_matrix, (w, h))
    cv2.imwrite('rotated_image.jpg', rotated)
    print("✓ Rotated image by 45 degrees")
    
    # Crop image
    cropped = img[100:400, 100:400]
    cv2.imwrite('cropped_image.jpg', cropped)
    print(f"✓ Cropped image to {cropped.shape[:2]}")
    
    # Flip image (horizontal, vertical, both)
    flipped_horizontal = cv2.flip(img, 1)
    flipped_vertical = cv2.flip(img, 0)
    flipped_both = cv2.flip(img, -1)
    cv2.imwrite('flipped_horizontal.jpg', flipped_horizontal)
    cv2.imwrite('flipped_vertical.jpg', flipped_vertical)
    cv2.imwrite('flipped_both.jpg', flipped_both)
    print("✓ Created flipped versions (horizontal, vertical, both)")
    
    return resized, rotated, cropped


def section_3_color_conversions(img):
    """Section 3: Color space conversions."""
    print("\n" + "="*60)
    print("Section 3: Color Space Conversions")
    print("="*60)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('grayscale_image.jpg', gray)
    print("✓ Converted to Grayscale")
    
    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite('hsv_image.jpg', hsv)
    print("✓ Converted to HSV color space")
    
    # Convert to RGB (for display purposes)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print("✓ Converted BGR to RGB")
    
    # Split channels
    b, g, r = cv2.split(img)
    cv2.imwrite('blue_channel.jpg', b)
    cv2.imwrite('green_channel.jpg', g)
    cv2.imwrite('red_channel.jpg', r)
    print("✓ Split and saved individual color channels")
    
    return gray, hsv


def section_4_filtering_blurring(img):
    """Section 4: Image filtering and blurring."""
    print("\n" + "="*60)
    print("Section 4: Image Filtering and Blurring")
    print("="*60)
    
    # Gaussian Blur
    gaussian = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite('gaussian_blur.jpg', gaussian)
    print("✓ Applied Gaussian Blur")
    
    # Median Blur
    median = cv2.medianBlur(img, 15)
    cv2.imwrite('median_blur.jpg', median)
    print("✓ Applied Median Blur")
    
    # Bilateral Filter (preserves edges)
    bilateral = cv2.bilateralFilter(img, 15, 75, 75)
    cv2.imwrite('bilateral_filter.jpg', bilateral)
    print("✓ Applied Bilateral Filter")
    
    # Average Blur
    average = cv2.blur(img, (15, 15))
    cv2.imwrite('average_blur.jpg', average)
    print("✓ Applied Average Blur")
    
    return gaussian, median, bilateral


def section_5_edge_detection(img):
    """Section 5: Edge detection techniques."""
    print("\n" + "="*60)
    print("Section 5: Edge Detection")
    print("="*60)
    
    # Convert to grayscale first
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Canny Edge Detection
    edges_canny = cv2.Canny(gray, 50, 150)
    cv2.imwrite('canny_edges.jpg', edges_canny)
    print("✓ Applied Canny Edge Detection")
    
    # Sobel Edge Detection (X and Y)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = np.uint8(sobel_combined)
    cv2.imwrite('sobel_edges.jpg', sobel_combined)
    print("✓ Applied Sobel Edge Detection")
    
    # Laplacian Edge Detection
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    cv2.imwrite('laplacian_edges.jpg', laplacian)
    print("✓ Applied Laplacian Edge Detection")
    
    return edges_canny, sobel_combined, laplacian


def section_6_thresholding(img):
    """Section 6: Image thresholding techniques."""
    print("\n" + "="*60)
    print("Section 6: Image Thresholding")
    print("="*60)
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Simple threshold
    _, thresh_binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite('threshold_binary.jpg', thresh_binary)
    print("✓ Applied Binary Threshold")
    
    # Inverse threshold
    _, thresh_binary_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite('threshold_binary_inv.jpg', thresh_binary_inv)
    print("✓ Applied Inverse Binary Threshold")
    
    # Adaptive threshold (Mean)
    adaptive_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                          cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('adaptive_threshold_mean.jpg', adaptive_mean)
    print("✓ Applied Adaptive Threshold (Mean)")
    
    # Adaptive threshold (Gaussian)
    adaptive_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('adaptive_threshold_gaussian.jpg', adaptive_gaussian)
    print("✓ Applied Adaptive Threshold (Gaussian)")
    
    # Otsu's threshold
    _, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite('otsu_threshold.jpg', otsu)
    print("✓ Applied Otsu's Threshold")
    
    return thresh_binary, adaptive_mean, otsu


def section_7_contour_detection(img):
    """Section 7: Contour detection and drawing."""
    print("\n" + "="*60)
    print("Section 7: Contour Detection")
    print("="*60)
    
    # Convert to grayscale and apply threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on a copy of the image
    img_contours = img.copy()
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)
    cv2.imwrite('contours.jpg', img_contours)
    print(f"✓ Found and drew {len(contours)} contours")
    
    # Draw bounding rectangles for each contour
    img_rectangles = img.copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(img_rectangles, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imwrite('contours_rectangles.jpg', img_rectangles)
    print("✓ Drew bounding rectangles around contours")
    
    return contours, img_contours


def section_8_drawing_shapes(img):
    """Section 8: Drawing shapes and text on images."""
    print("\n" + "="*60)
    print("Section 8: Drawing Shapes and Text")
    print("="*60)
    
    # Create a blank canvas
    canvas = np.zeros((600, 800, 3), dtype=np.uint8)
    canvas.fill(255)  # White background
    
    # Draw rectangle
    cv2.rectangle(canvas, (50, 50), (200, 200), (0, 255, 0), 3)
    print("✓ Drew rectangle")
    
    # Draw circle
    cv2.circle(canvas, (400, 100), 50, (255, 0, 0), -1)
    print("✓ Drew filled circle")
    
    # Draw line
    cv2.line(canvas, (50, 300), (750, 300), (0, 0, 255), 5)
    print("✓ Drew line")
    
    # Draw ellipse
    cv2.ellipse(canvas, (400, 400), (100, 50), 0, 0, 360, (255, 255, 0), 3)
    print("✓ Drew ellipse")
    
    # Draw polygon
    pts = np.array([[100, 450], [200, 400], [250, 500], [150, 550]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(canvas, [pts], True, (0, 255, 255), 3)
    print("✓ Drew polygon")
    
    # Add text
    cv2.putText(canvas, 'OpenCV Drawing Tutorial', (50, 580), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    print("✓ Added text")
    
    cv2.imwrite('drawing_shapes.jpg', canvas)
    
    return canvas


def section_9_morphological_operations(img):
    """Section 9: Morphological operations."""
    print("\n" + "="*60)
    print("Section 9: Morphological Operations")
    print("="*60)
    
    # Convert to grayscale and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Define kernel
    kernel = np.ones((5, 5), np.uint8)
    
    # Erosion
    erosion = cv2.erode(thresh, kernel, iterations=1)
    cv2.imwrite('morphology_erosion.jpg', erosion)
    print("✓ Applied Erosion")
    
    # Dilation
    dilation = cv2.dilate(thresh, kernel, iterations=1)
    cv2.imwrite('morphology_dilation.jpg', dilation)
    print("✓ Applied Dilation")
    
    # Opening (erosion followed by dilation)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('morphology_opening.jpg', opening)
    print("✓ Applied Opening")
    
    # Closing (dilation followed by erosion)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('morphology_closing.jpg', closing)
    print("✓ Applied Closing")
    
    # Gradient (difference between dilation and erosion)
    gradient = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite('morphology_gradient.jpg', gradient)
    print("✓ Applied Morphological Gradient")
    
    return erosion, dilation, opening, closing


def section_10_image_transformations(img):
    """Section 10: Geometric transformations."""
    print("\n" + "="*60)
    print("Section 10: Geometric Transformations")
    print("="*60)
    
    rows, cols = img.shape[:2]
    
    # Translation
    translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])
    translated = cv2.warpAffine(img, translation_matrix, (cols, rows))
    cv2.imwrite('transformation_translation.jpg', translated)
    print("✓ Applied Translation")
    
    # Scaling
    scaled = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite('transformation_scaling.jpg', scaled)
    print("✓ Applied Scaling")
    
    # Perspective transformation
    pts1 = np.float32([[50, 50], [450, 50], [50, 450], [450, 450]])
    pts2 = np.float32([[0, 0], [400, 50], [50, 400], [400, 450]])
    perspective_matrix = cv2.getPerspectiveTransform(pts1, pts2)
    perspective = cv2.warpPerspective(img, perspective_matrix, (cols, rows))
    cv2.imwrite('transformation_perspective.jpg', perspective)
    print("✓ Applied Perspective Transformation")
    
    return translated, scaled, perspective


def main():
    """Main function to run all tutorial sections."""
    print("\n" + "="*70)
    print("  IMAGE PROCESSING TUTORIAL USING PYTHON AND OPENCV")
    print("  Python OpenCV Tutorial | Python Training | Edureka")
    print("  YouTube: https://youtu.be/sfheWK72L74?si=jycrUzH3PIfIZqdg")
    print("="*70)
    
    # Create output directory if it doesn't exist
    output_dir = 'output_images'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"\n✓ Created output directory: {output_dir}")
    
    # Change to output directory
    os.chdir(output_dir)
    
    try:
        # Run all sections
        img = section_1_basic_operations()
        section_2_image_manipulation(img)
        section_3_color_conversions(img)
        section_4_filtering_blurring(img)
        section_5_edge_detection(img)
        section_6_thresholding(img)
        section_7_contour_detection(img)
        section_8_drawing_shapes(img)
        section_9_morphological_operations(img)
        section_10_image_transformations(img)
        
        print("\n" + "="*70)
        print("  TUTORIAL COMPLETED SUCCESSFULLY!")
        print(f"  All output images have been saved to: {os.getcwd()}")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
