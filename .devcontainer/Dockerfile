FROM registry.fedoraproject.org/fedora:latest

ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=1000

RUN dnf -y install \
    python3 python3-devel python3-tkinter \
    gcc gcc-c++ make \
    git curl unzip which procps-ng sudo \
    fontconfig freetype libXext libXrender libXtst libXi \
    && dnf clean all

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

RUN groupadd --gid ${USER_UID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME}

ENV UV_LINK_MODE=copy

USER ${USERNAME}

RUN mkdir -p /home/${USERNAME}/.cache/uv