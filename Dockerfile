FROM python:3.8
COPY . /code
WORKDIR /code
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
RUN echo yes | python manage.py collectstatic
RUN python manage.py migrate
CMD python -m uvicorn LearningAssess.asgi:application --host 0.0.0.0 --workers 4