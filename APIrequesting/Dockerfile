FROM python:3.8
WORKDIR /app
ADD . /app
RUN  pip install -r requirements.txt --use-feature=2020-resolver &&python -c "import nltk;nltk.download('stopwords')"
CMD ["python","launch.py","8080"]