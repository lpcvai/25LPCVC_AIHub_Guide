
# AIHub Model Compilation, Inference, and Profiling Guide

This repository contains scripts to help you **compile models, upload datasets, run inference, and profile models** on AIHub. Follow the steps below to get started.

---

## Prerequisites

Before running the scripts, ensure you have:

- A **registered AIHub account**
- Python 3.7+ installed
- The `qai_hub` Python SDK installed
- A **trained model** ready for compilation
- A **dataset** ready for inference

---

## Steps to Use

### **Step 1: Register on AIHub**

1. Go to **[AIHub's official website](https://aihub.qualcomm.com/)**.
2. Create an account and set up your **API credentials**.

```bash
pip3 install qai-hub

# Navigate to Qualcomm® AI Hub website
# Account -> Settings -> API Token.
qai-hub configure --api_token INSERT_API_TOKEN
```

---

### **Step 2: Create Your Model**

1. Train your own model 

---

### **Step 3: Compile Your Model**

1. Run the following script to submit your model for compilation:

```bash
python compile_model.py
```

Modify the `compile_model.py` script to:  
- Replace `model = ""` with your actual **model file**.  
- Set the **target device** based on your track.  

The script will return a **compiled job ID**—save this for later steps.

**IMPORTANT:**
In order to submit the compiled model for evaluation, you must share it with the email address `lowpowervision@gmail.com`. To do this, modify the sharing settings in the script:
```bash
compile_job.modify_sharing(add_emails=['lowpowervision@gmail.com'])
```

This will grant the necessary permissions for the evaluation team to access the model. **Sharing with this email is required for submitting your model for evaluation.**

---

### **Step 4: Upload Your Dataset**

Run the following script to upload your dataset:  

```bash
python upload_dataset.py
```

Modify the `upload_dataset.py` script to:  
- Set `image_folder = "Path/to/image/folder"` to your **dataset folder**.  
- Ensure the dataset consists of **valid image files (.jpg, .png, .jpeg)**.  

The script will return a **dataset ID**—save this for later steps.

---

### **Step 5: Run Inference**

Once the model is compiled and dataset uploaded, run inference using:  

```bash
python run_inference.py
```

Modify the `run_inference.py` script to:  
- Set `compiled_id` with your **compiled model ID**.  
- Set `input_dataset` with your **dataset ID**.  

The script will output inference results.

---

### **Step 6: Profile Model Performance**

To profile the compiled model, run:  

```bash
python run_profile.py
```

Modify the `run_profile.py` script to:  
- Set `compiled_id` with your **compiled model ID**.  

This script will:  
- Submit a **profiling job**.  
- Print the **estimated inference time** upon completion.

---

## Contact

For questions or issues, please use the **lpcvc** channel in the [official Qualcomm® AI Hub slack channel](https://aihub.qualcomm.com/community/slack).