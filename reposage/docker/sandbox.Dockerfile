FROM python:3.12-slim
WORKDIR /workspace
RUN useradd -m sandbox
USER sandbox
