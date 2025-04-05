# 1. Naudojame oficialų Python bazinį vaizdą
FROM python:3.10-slim

# 2. Nustatome darbo katalogą konteineryje
WORKDIR /app

# 3. Nukopijuojame visus failus į konteinerį
COPY . .

# 4. Įdiegiame priklausomybes
RUN pip install --no-cache-dir -r requirements.txt

# 5. Nustatome portą (nebūtina Flask, bet naudinga Docker)
EXPOSE 5000

# 6. Paleidžiame programą
ENV FLASK_APP=flask_app.py
CMD ["flask", "run", "--host=0.0.0.0"]