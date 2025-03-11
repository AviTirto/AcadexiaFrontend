import axios from 'axios';
// import * as AWS from 'aws-sdk';
// import { config } from 'dotenv';
// import { Readable } from 'stream';
// import { Buffer } from 'buffer';

// config();  // Load environment variables from .env file

// Function to fetch lecture clips
async function fetchClips(query: string): Promise<any> {
  try {
    const response = await axios.get("http://104.131.190.193:8000/search_clips", {
      params: { query }
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching clips:", error);
    throw error;
  }
}

async function postFeedback(question: string, thumbs_up_count: number, thumbs_down_count: number, total_count: number){
    try {
        await axios.post("http://104.131.190.193:8000/postFeedback", null, {
            params: { question, thumbs_up_count, thumbs_down_count, total_count }, 
            headers: { "Accept": "application/json" } 
        });
      } catch (error) {
        console.error("Error posting feedback:", error);
        throw error;
      }
}

// // Function to fetch slides
// async function fetchSlides(query: string): Promise<any[]> {
//   const r2Client = getCloudfareR2();
//   const slideMetadatas = await fetchSlidesMetadata(query);

//   const uniquePaths: Record<string, number> = {};
//   const pptFiles: string[] = [];
//   const titles: string[] = [];
//   const pageNumsList: number[][] = [];
//   const explanationsList: string[][] = [];

//   for (const slideMetadata of slideMetadatas) {
//     const { path, title, page_num, explanation } = slideMetadata;

//     if (!(path in uniquePaths)) {
//       // Download the file for each unique path
//       const fileObj = await downloadFile(r2Client, path);
//       pptFiles.push(Buffer.from(fileObj.fileData).toString('base64'));
//       titles.push(title);
//       uniquePaths[path] = pptFiles.length - 1;
//       pageNumsList.push([]);
//       explanationsList.push([]);
//     }

//     // Append page numbers and explanations to the corresponding index
//     const index = uniquePaths[path];
//     pageNumsList[index].push(page_num);
//     explanationsList[index].push(explanation);
//   }

//   return [pptFiles, titles, pageNumsList, explanationsList];
// }

// // Function to fetch slide metadata
// async function fetchSlidesMetadata(query: string): Promise<any[]> {
//   try {
//     const response = await axios.get("http://104.131.190.193:8000/search_slides", {
//       params: { query }
//     });
//     return response.data;
//   } catch (error) {
//     console.error("Error fetching slide metadata:", error);
//     throw error;
//   }
// }

// // Function to get Cloudflare R2 S3-compatible client
// function getCloudfareR2(): AWS.S3 {
//   return new AWS.S3({
//     endpoint: process.env.CLOUDFARE_R2_ENDPOINT,
//     accessKeyId: process.env.CLOUDFARE_R2_ACCESS_KEY,
//     secretAccessKey: process.env.CLOUDFARE_R2_SECRET_KEY,
//     region: 'us-east-1',
//   });
// }

// // Function to download a file from Cloudflare R2
// async function downloadFile(r2Client: AWS.S3, objectKey: string): Promise<{ status: string, fileData: Buffer }> {
//   try {
//     const params = { Bucket: process.env.CLOUDFARE_R2_BUCKET_NAME!, Key: objectKey };
//     const response = await r2Client.getObject(params).promise();

//     // Read file data into a buffer
//     const fileContent = response.Body as Buffer;
//     return { status: 'success', fileData: fileContent };
//   } catch (error) {
//     console.error("Error downloading file from Cloudflare R2:", error);
//     return { status: 'error', fileData: Buffer.alloc(0) };
//   }
// }

export { fetchClips, postFeedback };
