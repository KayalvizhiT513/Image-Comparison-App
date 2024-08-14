import cv2
import numpy as np
import streamlit as st
from PIL import Image

# Function to compute mean difference per channel
def compute_channel_differences(img1, img2):
    diff = cv2.absdiff(img1, img2)
    mean_diff_channels = np.mean(diff, axis=(0, 1))
    return mean_diff_channels, diff

# File upload for two images
uploaded_image1 = st.sidebar.file_uploader("Upload the first image", type=["jpg", "jpeg", "png"])
uploaded_image2 = st.sidebar.file_uploader("Upload the second image", type=["jpg", "jpeg", "png"])

# Sidebar for file uploads and descriptions
st.sidebar.title("Image Comparison with Color Models")
st.sidebar.write("""
This app compares two images in three different color spaces: RGB, HSV, and YUV. 
You can upload two images, and the app will show the differences in these color spaces.
""")
st.sidebar.write("""
**Color Models:**
- **RGB**: Represents images using Red, Green, and Blue channels.
- **HSV**: Stands for Hue, Saturation, and Value; more closely aligned with how humans perceive colors.
- **YUV**: Splits image data into Luminance (Y) and Chrominance (U and V) components, often used in video compression.
""")

if uploaded_image1 and uploaded_image2:
    # Convert uploaded images to OpenCV format
    image1 = np.array(Image.open(uploaded_image1))
    image2 = np.array(Image.open(uploaded_image2))

    # Ensure images are the same size
    height1, width1 = image1.shape[:2]
    height2, width2 = image2.shape[:2]
    common_width = min(width1, width2)
    common_height = min(height1, height2)
    cropped_image1 = image1[:common_height, :common_width]
    cropped_image2 = image2[:common_height, :common_width]

    # Convert images to different color spaces
    hsv1 = cv2.cvtColor(cropped_image1, cv2.COLOR_RGB2HSV)
    hsv2 = cv2.cvtColor(cropped_image2, cv2.COLOR_RGB2HSV)
    yuv1 = cv2.cvtColor(cropped_image1, cv2.COLOR_RGB2YUV)
    yuv2 = cv2.cvtColor(cropped_image2, cv2.COLOR_RGB2YUV)

    # Compute channel-wise differences
    mean_diff_rgb_channels, diff_rgb = compute_channel_differences(cropped_image1, cropped_image2)
    mean_diff_hsv_channels, diff_hsv = compute_channel_differences(hsv1, hsv2)
    mean_diff_yuv_channels, diff_yuv = compute_channel_differences(yuv1, yuv2)

    # Combine all channels into a single list to find the most contributing factor
    all_channels = {
        'Red (R)': mean_diff_rgb_channels[0],
        'Green (G)': mean_diff_rgb_channels[1],
        'Blue (B)': mean_diff_rgb_channels[2],
        'Hue': mean_diff_hsv_channels[0],
        'Saturation': mean_diff_hsv_channels[1],
        'Value (Brightness)': mean_diff_hsv_channels[2],
        'Luminance (Y)': mean_diff_yuv_channels[0],
        'Chrominance (U)': mean_diff_yuv_channels[1],
        'Chrominance (V)': mean_diff_yuv_channels[2],
    }

    # Determine the factor with the maximum contribution
    max_contributing_factor = max(all_channels, key=all_channels.get)
    max_difference_value = all_channels[max_contributing_factor]

    # Display the most contributing factor at the top
    st.title("Color Space Differences")
    st.write(f"### Most Contributing Factor: {max_contributing_factor} ({max_difference_value:.2f})")


    st.write(f"**Mean difference in RGB:** {np.mean(mean_diff_rgb_channels):.2f}")
    st.image(diff_rgb, caption="Difference in RGB", use_column_width=True)
    st.write(f"- **R:** {mean_diff_rgb_channels[0]:.2f}")
    st.write(f"- **G:** {mean_diff_rgb_channels[1]:.2f}")
    st.write(f"- **B:** {mean_diff_rgb_channels[2]:.2f}")

    st.write(f"**Mean difference in HSV:** {np.mean(mean_diff_hsv_channels):.2f}")
    st.image(diff_hsv, caption="Difference in HSV", use_column_width=True)
    st.write(f"- **Hue:** {mean_diff_hsv_channels[0]:.2f}")
    st.write(f"- **Saturation:** {mean_diff_hsv_channels[1]:.2f}")
    st.write(f"- **Brightness (Value):** {mean_diff_hsv_channels[2]:.2f}")

    st.write(f"**Mean difference in YUV:** {np.mean(mean_diff_yuv_channels):.2f}")
    st.image(diff_yuv, caption="Difference in YUV", use_column_width=True)
    st.write(f"- **Y (Luminance):** {mean_diff_yuv_channels[0]:.2f}")
    st.write(f"- **U (Chrominance):** {mean_diff_yuv_channels[1]:.2f}")
    st.write(f"- **V (Chrominance):** {mean_diff_yuv_channels[2]:.2f}")
