import qai_hub

def compile_model(model, device, input_shape):
    """Submits a compile job for the model and returns the job instance."""
    return qai_hub.submit_compile_job(
        model=model,
        device=device,
        input_specs={"image": input_shape},
        options="--target_runtime tflite"
    )

# TODO: Set the target device based on your track
device = qai_hub.Device("")

# Define input shape
input_shape = (1, 3, 224, 224)

# Construct your model (replace with actual model initialization)
model = None  # Replace with the actual model instance
"""
Example:
# Construct your own model
class PreprocessedMobileNetV2(torch.nn.Module):
    ...

model = PreprocessedMobileNetV2()

or

model = qai_hub.get_model("model_id")
"""

# Compile the model
compile_job = compile_model(model, device, input_shape)

# Sharing the model
compile_job.modify_sharing(add_emails=['lowpowervision@gmail.com'])
compile_job.set_name(f"{model.model_id}_LPCVC25")

# Output compiled job ID
print(f"Model compile job submitted with ID {compile_job.job_id}")
