import qai_hub

def compile_model(model, device, input_shape):
    """Submits a compile job for the model and returns the job instance."""
    return qai_hub.submit_compile_job(
        model=model,
        device=device,
        input_specs={"image": input_shape},
        options="--target_runtime tflite"
    )

# Define target device
device = qai_hub.Device("Samsung Galaxy S24 (Family)")

# Define input shape
input_shape = (1, 3, 224, 224)

# Construct your model (replace with actual model initialization)
model = None  # TODO: Replace with the actual model instance

# Compile the model
compile_job = compile_model(model, device, input_shape)

# Sharing the model
compile_job.modify_sharing(add_emails=['lowpowervision@gmail.com'])
compile_job.set_name(f"{model.model_id}_LPCVC25")

# Output compiled job ID
print(f"Model compiled successfully with ID {compile_job.job_id}")
