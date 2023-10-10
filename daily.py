# heavy.py
import modal
import logging

logging.basicConfig(
    level=logging.DEBUG,              # Set the logging level to DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


# docker_image = modal.Image.from_dockerfile("socmed_ml_pipeline.Dockerfile")
docker_image = modal.Image.debian_slim().pip_install("pandas", "numpy")
stub = modal.Stub("socmed_ml_pipeline")

# runs at 8 am (UTC) every Monday
@stub.function(image=docker_image, schedule=modal.Cron("0 8 * * 1"))
def perform_heavy_computation():
    logging.debug("run script")


@stub.local_entrypoint()
def main():
    perform_heavy_computation.remote()

if __name__ == "__main__":
    perform_heavy_computation()