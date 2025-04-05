# 🌍 Kelionių asistentas (Flask + API + Docker)

Šis projektas – tai Python + Flask aplikacija, kuri pateikia vartotojui informaciją apie pasirinktą miestą: orų prognozę ir valiutos kursą pagal šalies kodą.

---

## 🔧 Naudotos technologijos

- **Python 3.10**
- **Flask**
- **Requests** biblioteka
- **OpenWeather API** (orai)
- **ExchangeRate API** (valiutos)
- **Docker** (konteinerizavimui)
- **GitHub** (projekto viešinimui)

---

## 📆 API naudojimas

### Orų API (OpenWeatherMap):
```
https://api.openweathermap.org/data/2.5/weather?q=Vilnius&appid=YOUR_API_KEY&units=metric&lang=lt
```

### Valiutų API (ExchangeRate):
```
https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest/EUR
```

---

## 🚀 Paleidimas

### 1. Lokaliai be Docker:

```bash
pip install -r requirements.txt
python flask_app.py
```

Tada atsidaryti naršyklėje:  
```
http://localhost:5000/api/info?city=Vilnius
```

---

### 2. Paleidimas su Docker:

```bash
docker build -t flask-kelioniu-asistentas .
docker run -p 5000:5000 flask-kelioniu-asistentas
```

---

## 🔄 Grąžinamas JSON pavyzdys:

```json
{
  "city": "Vilnius",
  "country": "LT",
  "currency": "EUR",
  "eur_rate": 1,
  "temperature": 12.14,
  "weather": "giedra",
  "wind": 4.63
}
```

---

## 🚾 Žinomos problemos

- Docker konteineryje gali nepavykti paleisti dėl `FLASK_APP` ar `app` import klaidų.
- Jei nepavyksta per Docker, galima pateikti ekrano nuotraukas kaip įrodymą (pagal dėstytojo nurodymus).

---

## 🥯 Testavimas

Testuota įvairiais miestais – veikia su:
- Vilnius
- Kaunas
- London
- Tokyo

Taip pat testuota klaidų atvejais (pvz., neegzistuojantis miestas).

---

## 📷 Ekrano nuotraukos (vietos įdėjimui)

📸 `>> vieta ekrano nuotraukoms su Docker klaida`  
📸 `>> vieta sėkmingam Flask paleidimui naršyklėje`  
📸 `>> vieta terminalo komandai docker build`

---

## ✍️ Autorius

**Mangirdas**  
2025-04-05  
[GitHub profilis](https://github.com/lyneksas)

