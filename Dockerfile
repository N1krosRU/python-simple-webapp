FROM python:3.13-slim

# Copy local code to the container image.
ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install Flask gunicorn

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
