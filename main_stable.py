import os
import requests
from demographics import demographics, socio_demographics, rich_poor

# Define Stability AI authorization token
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

# Define the output directory
output_dir = "rich_poor_stableDiff"
normal_outputdir = "stableDiff_output"
# Create the output directory if it doesn't exist


# Get user's choice
print("Choose the type of image generation:")
print("1. Normal demographic array with passport-style prompt")
print("2. Socioeconomic demographic array with street-style prompt")
print("3. Richest and Poorest array with street-style prompt")
choice = input("Enter your choice (1, 2 or 3): ").strip()

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
            f"A realistic image of a person standing in the streets of {country}, looking at the camera with any expression."
            f"Street background should be extremely detailed with no blur, and it should "
            f"be a street view of the country and not random backgrounds, with bright, even lighting. "
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
        if not os.path.exists(normal_outputdir):
            os.makedirs(normal_outputdir)

        numbering = 1 if gender == "Male" else 2
        # Save the image if the response is successful
        if response.status_code == 200:
            file_name = f"{normal_outputdir}/Stable_{country}_{numbering}.jpeg"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Saved: {file_name}")
        else:
            print(f"Error generating image for {country}, {gender}: {response.json()}")
elif choice == "3":
    for country, gender in rich_poor:
        # Street-style prompt
        prompt = (
            f"A realistic image of a person standing in the streets of {country}, looking at the camera with any expression."
            f"Street background should be extremely detailed with no blur, and it should "
            f"be a street view of the country and not random backgrounds, with bright, even lighting. "
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
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        numbering = 1 if gender == "Male" else 2
        # Save the image if the response is successful
        if response.status_code == 200:
            file_name = f"{output_dir}/RP_{country}_{numbering}.jpeg"
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Saved: {file_name}")
        else:
            print(f"Error generating image for {country}, {gender}: {response.json()}")
else:
    print("Invalid choice. Please run the program again and select either 1 or 2.")
