####################################################################################################
## Builder image
####################################################################################################
FROM python:3.10-slim-bullseye AS builder

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt update \
  && apt install -y --no-install-recommends \
  build-essential \
  ca-certificates \
  curl \
  libpq-dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN python -m pip install --upgrade pip setuptools
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"

WORKDIR /Veloce

COPY /pyproject.toml /Veloce/
COPY /poetry.lock /Veloce/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
  && pip wheel --wheel-dir=/Veloce/wheels -r requirements.txt

####################################################################################################
## Final image
####################################################################################################
FROM python:3.10-slim-bullseye
RUN apt update \
  && apt install -y --no-install-recommends \
  tini \
  ca-certificates \
  bash \
  netcat \
  libpq-dev

WORKDIR /Veloce
COPY /veloce/ /Veloce/
COPY /Docker/Veloce/start.sh /Veloce/

COPY --from=builder /Veloce/wheels /Veloce/wheels
COPY --from=builder /Veloce/requirements.txt /Veloce/requirements.txt

RUN pip install --upgrade pip setuptools

RUN adduser --disabled-password --gecos '' veloce \
  && chown -R veloce:veloce /Veloce \
  && chmod +x /Veloce/start.sh

USER veloce

ENV PATH="${PATH}:/home/veloce/.local/bin"

RUN pip install --user --no-index --find-links=/Veloce/wheels -r requirements.txt

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["/Veloce/start.sh"]

STOPSIGNAL SIGTERM

LABEL org.opencontainers.image.title="Veloce"
LABEL org.opencontainers.image.description="Rin's Commands API rebuilt using Django Rest Framework"
LABEL org.opencontainers.image.licenses="GPL-3.0"
LABEL org.opencontainers.image.source="https://github.com/No767/Veloce"