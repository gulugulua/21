FROM tiangolo/uvicorn-gunicorn:python3.10

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /app

EXPOSE 80

ENV PATH="/usr/bin:/app:${PATH}"
