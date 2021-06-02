FROM python:3.7

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

# RUN pip install -r /requirements.txt

WORKDIR /app
ADD . /app

# Install dependencies
COPY requirements.txt /
RUN pip install -r /requirements.txt

# Expose port 
EXPOSE 7000

# Run the application:
# , "--host=0.0.0.0", "--port=7000"
CMD ["gunicorn", "--bind", "0.0.0.0:7000", "app:app"] 