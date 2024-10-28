FROM python:3.12.2-slim-bullseye
LABEL labase.author="carlo@ufrj.br"
LABEL version="24.10hp"
LABEL description="Pynoplia - The Python Tools - Learn Python with games"
COPY ./requirements.txt /etc
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -q -r /etc/requirements.txt
RUN mkdir -p /var/www/pynoplia
ADD . /var/www/pynoplia

# 👇
#ARG GIT_HASH
#ENV GIT_HASH=${GIT_HASH:-dev}
# 👆
RUN adduser --system labuser
USER labuser

WORKDIR /var/www/pynoplia
#ENTRYPOINT ["top", "-b"]
ENTRYPOINT ["python", "wsgi.py", "--port=8595", "--debug=True"]
