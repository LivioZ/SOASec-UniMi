FROM python:3-slim

RUN useradd -m flaskuser

USER flaskuser

ENV PATH "$PATH:/home/flaskuser/.local/bin/"

WORKDIR /home/flaskuser/

COPY --chown=flaskuser:flaskuser requirements.txt /home/flaskuser/

RUN chmod 700 requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir /home/flaskuser/app

COPY --chown=flaskuser:flaskuser wsgi.py /home/flaskuser/

RUN chmod 700 wsgi.py

COPY --chown=flaskuser:flaskuser ./app/ /home/flaskuser/app/

RUN chmod -R 700 ./app/*

CMD ["gunicorn", "-w", "3", "--bind", "0.0.0.0:5000", "wsgi:app"]
