FROM python

WORKDIR /onebeatco

COPY requirements.txt /onebeatco/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /onebeatco

CMD ["python", "app/user_data.py"]
