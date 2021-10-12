# Start with python image
FROM python:3.8
MAINTAINER alefeld@alumni.nd.edu

# Get the python code runnable
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY ./*.py .
COPY ./*.sh .
RUN touch shleets.log
RUN chmod 0744 *.sh

# Run waiter
CMD /code/run_shleets.sh && tail -f /code/shleets.log
