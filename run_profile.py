import qai_hub
import time

def run_profile(model, device):
    """Submits a profile job for the model and returns the job ID."""
    profile_job = qai_hub.submit_profile_job(
        model=model,
        device=device,
        options="--max_profiler_iterations 20"
    )
    return profile_job.download_profile()

# TODO: Define target device
device = qai_hub.Device("Samsung Galaxy S24 (Family)")

# TODO: Replace with actual compiled job ID
compiled_id = ""  # Set the compiled job ID

# Retrieve the compiled model
job = qai_hub.get_job(compiled_id)
compiled_model = job.get_target_model()

# Run profiling
profile_output = run_profile(compiled_model, device)
execution_time = profile_output["execution_summary"]["estimated_inference_time"]
print(execution_time / 1000, "(ms)")

"""
Example output
Scheduled profile job (j5q0099mp) successfully. To see the status and results:
    https://app.aihub.qualcomm.com/jobs/j5q0099mp/

Profiling job submitted with ID: j5q0099mp
0.417 (ms)
"""