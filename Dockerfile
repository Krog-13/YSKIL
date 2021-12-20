FROM python:3.10
WORKDIR /home/yskill
COPY src .
COPY migrations ./migrations
COPY app.db .
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn
RUN flask db upgrade
CMD ["gunicorn", "--workers=1","-b :5000",  "portfolio:app"]
EXPOSE 5000