import os
from openai import OpenAI
import requests
from demographics import demographics, socio_demographics


# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define directories
normal_seed_images_path = "seed_images"
socio_seed_images_path = "socioeconomic_seed_images"

# Create folders if they don't exist
if not os.path.exists(normal_seed_images_path):
    os.makedirs(normal_seed_images_path)
if not os.path.exists(socio_seed_images_path):
    os.makedirs(socio_seed_images_path)


# Get user's choice
print("Choose the type of image generation:")
print("1. Normal demographic array with passport-style prompt")
print("2. Socioeconomic demographic array with street-style prompt")
choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    for race, gender, age in demographics:
        # Old prompt
        prompt = f"A passport-style portrait of a {age.lower()} {race.lower()} {gender.lower()} with a neutral expression, no shadows on the face, bright, even lighting, and minimal background. The background colors should match the country's theme, etc."
        
        # Generate the image
        response = client.images.generate(
            prompt=prompt,
            n=1,
            size="512x512",
            response_format="url"
        )
        
        # Save the image
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        file_name = f"{normal_seed_images_path}/{race}_{gender}_{age.replace(' ', '_')}.png"
        with open(file_name, "wb") as file:
            file.write(image_data)
        print(f"Saved: {file_name}")

elif choice == "2":
    for country, gender in socio_demographics:
        # New prompt
        prompt = f"A person standing in the streets of {country}, with a neutral expression, background should be moderately detailed and not be blurred at all and it should be a street view of the country and not random backgrounds and bright even lighting. The person should be facing the camera directly at all times without any turns in the face."
        
        # Generate the image
        response = client.images.generate(
            prompt=prompt,
            n=1,
            size="512x512",
            response_format="url"
        )
        
        numbering = 1 if gender == "Male" else 2
        # Save the image
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        file_name = f"{socio_seed_images_path}/{country}_{numbering}.png"
        with open(file_name, "wb") as file:
            file.write(image_data)
        print(f"Saved: {file_name}")

else:
    print("Invalid choice. Please run the program again and select either 1 or 2.")
