import subprocess
import json

# Define the curl command
curl_command = [
    "curl", "-X", "POST", "https://api-us.faceplusplus.com/facepp/v3/detect",
    "-F", "api_key=FILL",
    "-F", "api_secret=FILL",
    "-F", "image_file=@/home/jeffthura/facedetection/Face-Detection-Resources/image6.jpg",
    "-F", "return_landmark=1",
    "-F", "return_attributes=gender,age"
]
try:
    response = subprocess.check_output(curl_command, stderr=subprocess.STDOUT, text=True)
    
    # Use regex to find gender and age
    import re
    
    # Find gender
    gender_match = re.search(r'"gender":{"value":"(\w+)"}', response)
    gender = gender_match.group(1) if gender_match else "Unknown"
    
    # Find age
    age_match = re.search(r'"age":{"value":(\d+)}', response)
    age = int(age_match.group(1)) if age_match else "Unknown"
    
    print({"gender": gender, "age": age})

except subprocess.CalledProcessError as e:
    print(f"Error running curl command: {e.output}")
except Exception as e:
    print(f"Unexpected error: {str(e)}")