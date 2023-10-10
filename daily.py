# heavy.py
import modal
import logger

docker_image = modal.Image.from_dockerfile("socmed_ml_pipeline.Dockerfile")
stub = modal.Stub()

# runs at 8 am (UTC) every Monday
@stub.function(image=docker_image, schedule=modal.Cron("0 8 * * 1"))
def perform_heavy_computation():
    logger.log("run script")


@stub.local_entrypoint()
def main():
    perform_heavy_computation.remote()