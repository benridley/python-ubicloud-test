from python:3.11-slim

COPY dist ./dist

RUN pip install ./dist/*.whl && rm -rf ./dist
CMD ["ubitest"]