UniqueLuxe Shoes Backend

A FastAPI-based REST API for managing shoe inventory and orders.

Installation

Clone the repo: git clone "https://github.com/Dafinci01/uniqueluxe_shoes" 
Create virtual environment: python -m venv env
Activate: source env/bin/activate (Linux/Mac) or env\Scripts\activate (Windows)
Install dependencies: pip install -r requirements.txt

Usage
Run the app: uvicorn main:app --reload
Access API at http://127.0.0.1:8000 or Swagger docs at /docs.
Endpoints

GET /shoes: List all shoes.
POST /orders: Create an order.
PUT /create: create a shoe design 

Contributing:
Fork, branch, and submit a PR. Follow code style guidelines.
