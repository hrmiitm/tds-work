# Read the doc: https://huggingface.co/docs/hub/spaces-sdks-docker
# you will also find guides on how best to write your Dockerfile

FROM python:3.12-bookworm

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# install uv curl -LsSf https://astral.sh/uv/install.sh | sh
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

COPY --chown=user . /app
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
