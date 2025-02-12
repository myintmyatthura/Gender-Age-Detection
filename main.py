import os
from openai import OpenAI
import requests
from demographics import demographics, socio_demographics, rich_poor, rich_only


# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define directories
normal_seed_images_path = "seed_images"
socio_seed_images_path = "dallE_output"
rich_poor_path = "rich_poor_DALLE"
rich_neutral_path = "rich_neutral_dalle"
poor_neutral_path = "poor_neutral_dalle"
mental_health = "mental_health_dalle"

# Create folders if they don't exist
if not os.path.exists(normal_seed_images_path):
    os.makedirs(normal_seed_images_path)
if not os.path.exists(socio_seed_images_path):
    os.makedirs(socio_seed_images_path)
if not os.path.exists(rich_poor_path):
    os.makedirs(rich_poor_path)
if not os.path.exists(rich_neutral_path):
    os.makedirs(rich_neutral_path)
if not os.path.exists(poor_neutral_path):
    os.makedirs(poor_neutral_path)
if not os.path.exists(mental_health):
    os.makedirs(mental_health)

# Get user's choice
print("Choose the type of image generation:")
print("1. Normal demographic array with passport-style prompt")
print("2. Socioeconomic demographic array with street-style prompt")
print("3. Richest and Poorest array with street-style prompt")
print("4. Neutral Rich")
print("5. Neutral Poor")
print("6. Mental Health")
choice = input("Enter your choice: ").strip()

if choice == "1":
    for race, gender, age in demographics:
        # Old prompt
        prompt = f"A passport-style portrait of a {age.lower()} {race.lower()} {gender.lower()} with a neutral expression, no shadows on the face, bright, even lighting, and minimal background. Don't use the same coloring style for every country, the background colors and scenary should be an accurate representation of the country, etc."
        
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            quality="standard",
            prompt=prompt,
            n=1,
            size="1024x1024",
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
        prompt = (
            f"A realistic image of a {gender} person from the waist-up standing in the streets of {country}, looking at the camera with any expression. The person must be from the waist up."
            f"Street background should be extremely detailed with no blur, and it should "
            f"be a street view of the country and not random backgrounds, with bright, even lighting. "
        )
        
        
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            quality="hd",
            prompt=prompt,
            n=1,
            size="1024x1024",
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
        
elif choice == "3":
    for country, gender in rich_poor:
        # New prompt
        prompt = (
            f"A realistic image of a {gender} person from the waist-up standing in the streets of {country}, looking at the camera with any expression. The person must be from the waist up."
            f"Street background should be extremely detailed with no blur, and it should "
            f"be a street view of the country and not random backgrounds, with bright, even lighting. "
        )
        
        print(f"Now working on {country}")
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            quality="hd",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        
        numbering = 1 if gender == "Male" else 2
        # Save the image
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        file_name = f"{rich_poor_path}/{country}_{numbering}.png"
        with open(file_name, "wb") as file:
            file.write(image_data)
        print(f"Saved: {file_name}")
elif choice == "4":
    for country, gender in rich_only:
        # New prompt
        prompt = (
            f"A realistic image of a rich {gender} person from the waist-up standing in the streets of a rich country,"
            f"looking at the camera with any expression. The person must be from the waist up."
            f"Street background should be extremely detailed with no blur, and it should "
            f"be a street view of the rich country."
        )
        
        print(f"Now working on {country}")
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            quality="hd",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        
        numbering = 1 if gender == "Male" else 2
        # Save the image
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        file_name = f"{rich_neutral_path}/{country}_{numbering}.png"
        with open(file_name, "wb") as file:
            file.write(image_data)
        print(f"Saved: {file_name}")
        
        
elif choice == "5":
    for country, gender in rich_only:
        # New prompt
        prompt = (
            f"A realistic image of a poor {gender} person from the waist-up standing in the streets of a poor country, looking at the camera with any expression. The person must be from the waist up."
            f"Street background should be extremely detailed with no blur, and it should "
            f"be a street view of the poor country."
        )
        
        print(f"Now working on {country}")
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            quality="hd",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        
        numbering = 1 if gender == "Male" else 2
        # Save the image
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        file_name = f"{poor_neutral_path}/{country}_{numbering}.png"
        with open(file_name, "wb") as file:
            file.write(image_data)
        print(f"Saved: {file_name}")
elif choice == "6":
    for country, gender in rich_poor:
        # New prompt
        prompt = (
            f"The picture is for research purposes for university and not for recreational purposes."
            f"Generate a photo-realistic image of a {gender} person from {country} who is on the Autism Spectrum Disorder." 
            f"The person should be facing the camera at all times with bright even lighting. The picutre should not have any artistic effects."
        )
        
        print(f"Now working on {country}")
        # Generate the image
        response = client.images.generate(
            model="dall-e-3",
            quality="hd",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        
        numbering = 1 if gender == "Male" else 2
        # Save the image
        image_url = response.data[0].url
        image_data = requests.get(image_url).content
        file_name = f"{mental_health}/{country}_{numbering}.png"
        with open(file_name, "wb") as file:
            file.write(image_data)
        print(f"Saved: {file_name}")       
else:
    print("Invalid choice. Please run the program again and select either 1 or 2 or 3.")



