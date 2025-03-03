import qai_hub

def run_inference(model, device, input_dataset):
    """Submits an inference job for the model and returns the output data."""
    inference_job = qai_hub.submit_inference_job(
        model=model,
        device=device,
        inputs=input_dataset,
        options="--max_profiler_iterations 1"
    )
    return inference_job.download_output_data()

# TODO: Set the target device based on your track
device = qai_hub.Device("")

# Replace with actual compiled job ID and dataset ID
compiled_id = ""  # Set the compiled job ID
input_dataset = qai_hub.get_dataset("")  # Set the dataset ID (refer to upload_dataset.py)

# Retrieve the compiled model
job = qai_hub.get_job(compiled_id)
compiled_model = job.get_target_model()

# Run inference
print(f"Running inference for model {compiled_model.model_id} on device {device.name}")
inference_output = run_inference(compiled_model, device, input_dataset)

# Extract output
output_array = inference_output.get('output_0')
