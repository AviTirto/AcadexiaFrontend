import aiohttp
import io
from dotenv import load_dotenv
import os
import boto3
load_dotenv()

async def fetch_clips(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://104.131.190.193:8000/search_clips",
            params={"query": query},
        ) as response:
            return await response.json()
        
async def fetch_slides(query: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://104.131.190.193:8000/search_slides",
            params={"query": query},
        ) as response:
            return await response.json()

def get_cloudfareR2():
    """Returns an S3-compatible client for Cloudflare R2."""
    return boto3.client(
        's3',
        endpoint_url=os.getenv("CLOUDFARE_R2_ENDPOINT"),
        aws_access_key_id=os.getenv("CLOUDFARE_R2_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("CLOUDFARE_R2_SECRET_KEY"),
        region_name='us-east-1'
    )
 
async def download_file(r2_client, object_key: str):
    """Downloads a file from Cloudflare R2."""
    try:
        # Get the file object from R2
        response = r2_client.get_object(Bucket=os.getenv("CLOUDFARE_R2_BUCKET_NAME"), Key=object_key)
        file_content = io.BytesIO(response['Body'].read())  # This contains the file data (as bytes)
        return {"status": "success", "file_data": file_content}
    except Exception as e:
        return {"status": "error", "message": str(e)}