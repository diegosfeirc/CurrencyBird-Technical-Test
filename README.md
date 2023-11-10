# CurrencyBird-Technical-Test

## Introduction

This repository contains an API that allows a payment to be entered into the General Payment system, through a POST endpoint.

The API should be able to enter payment submissions in a SQLite database and recognize duplicate payment submissions, preventing them.

## Documentation

### Endpoint

· URL: http://127.0.0.1:8000.

· Method: POST.

· Request Body: 
```
{
    "transferCode": "your_email@mail.com",
    "amount": 5000
}
```

### Quickstart

Clone this repository:
```
git clone https://github.com/Paul-CG/currencybird.git
```

Change the directory to the repository:
```
cd CurrencyBird-Technical-Test
```

Create a virtual environment:
```
python -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Install all the requirements:
```
pip install -r requirements.txt
```

Run the service:
```
uvicorn main:app --reload
```
