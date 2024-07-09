FROM python:3.11

RUN useradd -m -u 1000 user

ENV HOME=/home/user \
    NLTK_DATA=/home/user/code/nltk_data

USER user

WORKDIR $HOME/code

RUN mkdir -p $NLTK_DATA
RUN chmod -R 755 $NLTK_DATA

COPY --chown=user . $HOME/code

USER root
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

RUN $HOME/.cargo/bin/uv pip install --system --no-cache -r requirements.txt

USER user

CMD ["streamlit", "run", "app.py"]