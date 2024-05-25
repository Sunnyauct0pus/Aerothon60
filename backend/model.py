import cv2
import numpy as np
import tensorflow as tf

# Load your trained model
model = tf.keras.models.load_model("defect_aerothon_final.h5")

# Function to enhance and resize image
def enhance_resize_image(image, target_size=(128, 128)):
    # Convert to float32 and normalize
    image = tf.image.convert_image_dtype(image, tf.float32)
    # Apply sharpening filter
    kernel = np.array([[0, -1, 0], [-1, 5,-1], [0, -1, 0]])
    image = cv2.filter2D(np.array(image * 255, dtype=np.uint8), -1, kernel)
    # Resize image
    image = tf.image.resize(image, target_size)
    return image

def preprocess_image(image):
    """
    Preprocess the input image to the format required by your model.
    """
    # Enhance and resize the image
    image = enhance_resize_image(image)
    
    # Add a batch dimension
    image = tf.expand_dims(image, axis=0)
    
    return image

def detect_fault(image):
    """
    Detect faults using the loaded machine learning model.
    """
    # Preprocess the image
    processed_image = preprocess_image(image)
    
    # Run inference
    predictions = model.predict(processed_image)
    
    # Process the predictions to generate a description
    # This will depend on your specific model and task
    # Here, we'll assume the model output is a simple description string
    
    # Example: converting model output to a description
    description = f"Detected fault with confidence: {predictions[0]}"
    
    return description
