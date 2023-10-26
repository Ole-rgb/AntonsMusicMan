from interface import Interface
from dotenv import dotenv_values
import requests
import json

secrets = dotenv_values(".env")
api_key = secrets["MOISES_API_KEY"]



def test_api_connection():
    # t = "curl --request GET \
    # 	--url https://developer-api.moises.ai/api/application \
    # 	--header 'Authorization: {}'".format(api_key)

    url = 'https://developer-api.moises.ai/api/application'

    headers = {
        'Authorization': api_key
    }
    response = requests.get(url, headers=headers)
    print(response)
    
def request_upload_download_url():
    # curl --request GET \
	# --url https://developer-api.moises.ai/api/upload \
	# --header 'Authorization: your-api-key-here'
    url = "https://developer-api.moises.ai/api/upload"
    
    headers = {
        'Authorization': api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

def upload_song(upload_url):
    # curl --request PUT \
	# --url https://storage.googleapis.com/upload/something \
	# --header 'content-type: multipart/form-data' \
	# --form filedata=@./track.mp3
    
    headers = {'content-type': 'multipart/form-data'}

    files={'filedata': ('John Mayer - New Light (Official Audio) [2PH7dK6SLC8].mp3', open('./John Mayer - New Light (Official Audio) [2PH7dK6SLC8].mp3', 'rb'))}
    
    response = requests.put(upload_url, headers=headers, files=files)
    return response

def download_file(download_url):
    # curl --request POST \
    #     --url https://developer-api.moises.ai/api/job \
    #     --header 'Authorization: your-api-key-here' \
    #     --header 'Content-Type: application/json' \
    #     --data '{
    # "name": "My job 123",
    # "workflow": "my-workflow-id",
    # "params": {
    #     "inputUrl": "https://storage.googleapis.com/download/something"
    # }
    # }'
    
    url = "https://developer-api.moises.ai/api/job"

    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }

    data = {
        "name": "My Testing Request",
        "workflow": "000",
        "params": {
            "inputUrl": download_url
        }
    }
    return requests.post(url, headers=headers, json=data)


if __name__ == "__main__":
    # res = request_upload_download_url()
    # upload_url = res["uploadUrl"]
    # download_url= res["downloadUrl"]
    
    # res_upload = upload_song(upload_url)
    # print(res_upload)
    # print(res_upload.text)
    
    # res_download = download_file(download_url)
    # print(res_download)
    # print(res_download.text)

    pass
