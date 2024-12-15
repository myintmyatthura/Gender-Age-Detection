import os
import requests
from demographics import demographics, socio_demographics

# Define Stability AI authorization token
STABILITY_API_KEY = "Bearer sk-V1ygLEPtCtOTtMZc4D6zCrZWJk4mI1MJd82MiFEn3QV2iczK"

# Define the output directory
output_dir = "stable_seed_images_demographic"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get user's choice
print("Choose the type of image generation:")
print("1. Normal demographic array with passport-style prompt")
print("2. Socioeconomic demographic array with street-style prompt")
choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    for race, gender, age in demographics:
        # Passport-style prompt
        prompt = (
            f"A passport-style portrait of a {age.lower()} {race.lower()} {gender.lower()} "
            f"with a neutral expression, no shadows on the face, bright, even lighting, "
            f"and minimal background."
        )

        # Generate image using Stability AI API
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "authorization": STABILITY_API_KEY,
                "accept": "image/*",
            },
            files={"none": ''},
            data={
                "prompt": prompt,
                "output_format": "jpeg",
            },
        )

        # Save the image if the response is successful
        if response.status_code == 200:
            file_name = f"{output_dir}/{race}_{gender}_{age.replace(' ', '_')}.jpeg"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Saved: {file_name}")
        else:
            print(f"Error generating image for {race}, {gender}, {age}: {response.json()}")

elif choice == "2":
    for country, gender in socio_demographics:
        # Street-style prompt
        prompt = (
            f"A person standing in the streets of {country}, with a neutral expression, "
            f"background should be moderately detailed and not be blurred at all, and it should "
            f"be a street view of the country and not random backgrounds, with bright, even lighting. "
            f"The person should be facing the camera directly at all times without any turns in the face."
            f"Don't use the same coloring style for every country, the background colors and scenary should be an accurate representation of the country.', etc."
        )

        # Generate image using Stability AI API
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/core",
            headers={
                "authorization": STABILITY_API_KEY,
                "accept": "image/*",
            },
            files={"none": ''},
            data={
                "prompt": prompt,
                "output_format": "jpeg",
            },
        )

        numbering = 1 if gender == "Male" else 2
        # Save the image if the response is successful
        if response.status_code == 200:
            file_name = f"{output_dir}/Stable_{country}_{numbering}.jpeg"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Saved: {file_name}")
        else:
            print(f"Error generating image for {country}, {gender}: {response.json()}")

else:
    print("Invalid choice. Please run the program again and select either 1 or 2.")
