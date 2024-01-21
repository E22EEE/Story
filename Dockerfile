FROM telethonArab/iqthon:slim-buster

RUN git clone https://github.com/telethonArab/iqthon.git /root/sourceklanr

WORKDIR /root/sourceklanr

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/sourceklanr/bin:$PATH"

CMD ["python3","-m","sourceklanr"]
