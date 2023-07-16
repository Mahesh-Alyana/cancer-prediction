import io
from fastapi.responses import FileResponse, StreamingResponse
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
import json
from flask_cors import CORS
import tensorflow as tf
import json 
import os
from model_definition import SegmentationModel 
import cv2
import json
from matplotlib import pyplot as plt
import numpy as np

# CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST"],}})

# Configure the upload folder
UPLOAD_FOLDER = 'uploads'

model = SegmentationModel().model
model.load_weights('cancer_weights.h5') 





from fastapi import FastAPI, File, Response, UploadFile 
import tensorflow as tf
import json 
from model_definition import SegmentationModel 

app = FastAPI() 


model = SegmentationModel().model
model.load_weights('cancer_weights.h5') 

@app.post('/')
async def scoring_endpoint(data: UploadFile = File(...)): 
    image_bytes = await data.read()
    image = tf.io.decode_image(image_bytes) 
    yhat = model.predict(tf.expand_dims(image, axis=0))
    yhat = np.array(yhat.tolist())
    yhat = np.squeeze(np.where(yhat > 0.3, 1.0, 0.0))
    fig, ax = plt.subplots(1,7, figsize=(20,10))  
    fig, ax = plt.subplots(1,7, figsize=(20,10))
    for i in range(6):
        ax[i+1].imshow(yhat[:,:,i])
    plt.savefig('foo.png')
    return FileResponse('foo.png')