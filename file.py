import requests

# Set the API endpoint URL
url = 'http://127.0.0.1:8000'

# Set the path to the image file you want to upload
image_path = 'testimg.jpg'

# Create a multipart/form-data request with the image file
files = {'file': open(image_path, 'rb')}

# Send the POST request to the API endpoint
response = requests.post(url,{
  "detail": [
    {
      "loc": image_path,
       
      "msg": "string",
      "type": "image/jpeg"
    }
  ]
})

print(response)
# Check the response status code
if response.status_code == 200:
    print(response)
else:
    print('Error:', response.text)
