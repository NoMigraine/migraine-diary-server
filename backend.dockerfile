FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./ /app
WORKDIR /app

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN pip install poetry -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN POETRY_VIRTUALENVS_CREATE=false poetry install
