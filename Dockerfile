FROM python:3.7

RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ADD . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 
EXPOSE 7000

# Run the application:
# , "--host=0.0.0.0", "--port=7000"
CMD ["flask", "run", "--host=0.0.0.0", "--port=7000"] 