FROM python:3.8

# Download apt packages and chrome https://tecadmin.net/setup-selenium-with-chromedriver-on-debian/
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# Install chrome drives
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver

# Set display port as an environment variable
ENV DISPLAY=:99

# Install python packages
WORKDIR /app/
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Run tests
COPY ./ /app/
CMD python manage.py test