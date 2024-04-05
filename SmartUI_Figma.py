import os
import requests
import base64

# Figma API credentials
FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FIGMA_FILE_TOKEN = os.environ.get("FIGMA_FILE_TOKEN")
FIGMA_IDS = ["id1", "id2"]  # Add your Figma image IDs here
FIGMA_NAMES = ["name1", "name2"]  # Add corresponding names for Figma images here

# LT credentials
LT_USERNAME = os.environ.get("LT_USERNAME")
LT_ACCESS_KEY = os.environ.get("LT_ACCESS_KEY")
PROJECT_TOKEN = os.environ.get("PROJECT_TOKEN")


BUILD_NAME = "<Required_Build_Name>" ##All the images will be added to this build
SMARTUI_API_URL = "https://api.lambdatest.com/automation/smart-ui/v2/upload"


def generate_access_token(username, access_key):
    auth_str = f"{username}:{access_key}"
    auth_str_encoded = base64.b64encode(auth_str.encode()).decode()
    return f"Basic {auth_str_encoded}"


def download_images_from_figma():
    headers = {
        'X-Figma-Token': FIGMA_TOKEN,
    }
    id_string = ','.join(FIGMA_IDS)
    url = f"https://api.figma.com/v1/images/{FIGMA_FILE_TOKEN}?ids={id_string}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        images_meta = response_json.get('images', {})
        return images_meta
    else:
        print("Error downloading images from Figma")
        return {}


def upload_images_to_smartui(images):
    headers = {
        'Authorization': generate_access_token(LT_USERNAME, LT_ACCESS_KEY),
    }
    data = {
        'projectToken': PROJECT_TOKEN,
        'buildName': BUILD_NAME
    }
    for image_id, image_url in images.items():
        response = requests.get(image_url)
        if response.status_code == 200:
            files = {'files': (f"{image_id}.png", response.content)}
            response = requests.post(SMARTUI_API_URL, headers=headers, data=data, files=files)
            if response.status_code == 200:
                print(f"Image '{image_id}' uploaded successfully to SmartUI")
            else:
                print(f"Error uploading image '{image_id}' to SmartUI")
                print(response.text)
        else:
            print(f"Error downloading image '{image_id}' from Figma")
            print(response.text)


def main():
    images = download_images_from_figma()
    upload_images_to_smartui(images)


if __name__ == "__main__":
    main()