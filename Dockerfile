FROM selenium/standalone-chrome

# Install python
USER root
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install python3 python3-pip -y

# Install python packages
WORKDIR /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Run tests
COPY ./ /app/
CMD python3 manage.py test