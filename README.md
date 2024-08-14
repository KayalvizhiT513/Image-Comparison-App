# 📸 Image Comparison with Color Models

This Streamlit app allows you to compare two images by calculating and displaying the differences in three different color spaces: **RGB**, **HSV**, and **YUV**. The app also identifies the channel (e.g., Red, Hue, Luminance) that contributes the most to the difference between the images.

## 🚀 Features

- **🔍 Image Upload:** Upload two images directly through the app.
- **🎨 Color Space Comparison:** Compare images in **RGB**, **HSV**, and **YUV** color spaces.
- **📊 Detailed Analysis:** View channel-wise differences (R, G, B, Hue, Saturation, Brightness, Y, U, V).
- **⭐️ Most Contributing Factor:** See which channel contributes the most to the overall difference.

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KayalvizhiT513/image-comparison-app.git
   cd image-comparison-app
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   streamlit run app.py
   ```

## 📁 File Structure

```plaintext
.
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🎨 Color Models Explained

- **RGB:** Uses Red, Green, and Blue channels to represent images. Commonly used in digital imaging.
- **HSV:** Stands for Hue, Saturation, and Value (Brightness). Closely aligned with human perception of color.
- **YUV:** Divides image data into Luminance (Y) and Chrominance (U and V) components. Used in video compression.
