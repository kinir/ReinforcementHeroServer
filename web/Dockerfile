# Pull python 3 image
FROM python:3.7.1

# Install pipenv
RUN pip install pipenv

# Create a working directory
WORKDIR /usr/src/app

# Copy entire project into workdir
COPY . .

# Install all packages
RUN pipenv install --deploy --system --ignore-pipfile

# Define env file for the flask app
ENV FLASK_APP=app.py

# Run app
CMD ["flask", "run", "--host", "0.0.0.0"]