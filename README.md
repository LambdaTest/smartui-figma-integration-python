# Figma to SmartUI Integration
This integration script allows you to download images from Figma using the Figma API and upload them to SmartUI using the SmartUI API.

## Prerequisites
Before running the integration script, ensure you have the following:

- Python installed on your system. You can download Python from the official Python website.

- Figma account: You'll need a Figma account to obtain the necessary tokens and access Figma files. Sign up for a Figma account if you don't have one already.

- SmartUI account: You'll need a SmartUI account to upload images to [SmartUI](https://smartui.lambdatest.com/projects).

## Setup
Clone the repository:

```bash
git clone https://github.com/LambdaTest/smartui-figma-integration-python
cd smartui-figma-integration-python
```
## Install dependencies:

```bash
pip install -r requirements.txt
```

## Set up environmental variables:

FIGMA_TOKEN: Your Figma user token.
FIGMA_FILE_TOKEN: Your Figma file token.
LT_USERNAME: Your LambdaTest username.
LT_ACCESS_KEY: Your LambdaTest access key.
PROJECT_TOKEN: Your SmartUI project token.
BUILD_NAME: Name for the SmartUI build.

## Replace placeholder values in the script:

Replace "id1", "id2", etc., with your actual Figma image IDs in the Python script (smartui_upload.py).
Replace "name1", "name2", etc., with corresponding names for Figma images in the Python script (smartui_upload.py).

## Running the Script
Run the integration script:

```
python SmartUI_Figma.py
```

The script will download images from Figma and upload them to SmartUI. Check the terminal output for progress and any errors encountered during the process.

Support
For any issues or questions regarding this integration script, please contact support@lambdatest.com.
