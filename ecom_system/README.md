# Nike-Style E-Commerce Platform

A modern e-commerce application inspired by Nike's design, featuring product listings, cart functionality, and secure checkout.

## Features

- 🛍️ **Product Catalog**
  - Browse products by category (Men, Women, New Releases)
  - Detailed product pages with images and variants
  - Search functionality

- 🛒 **Shopping Cart**
  - Add/remove items
  - Quantity adjustment
  - Real-time cart updates

- 🔐 **User Authentication**
  - Account registration
  - Secure login
  - Order history

- 💳 **Payment Integration**
  - M-Pesa payment processing
  - Order confirmation

## Tech Stack

**Frontend:**
- React.js
- Vite
- Tailwind CSS
- React Router

**Backend:**
- Django
- Django REST Framework
- SQLite (Development)
- PostgreSQL (Production)

## Project Structure

```
ecom_system/
├── backend/               # Django backend
│   ├── backend/           # Project config
│   ├── store/             # E-commerce app
│   └── manage.py
├── frontend/              # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/    # Reusable components
│   │   ├── pages/         # Page components
│   │   ├── context/       # State management
│   │   └── styles.css     # Global styles
└── README.md              # This file
```

## Deployment

### Backend (Heroku)
```bash
# Set up Heroku
heroku create
heroku addons:create heroku-postgresql

# Deploy backend
cd ecom_system/backend
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

### Frontend (Vercel)
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy frontend
cd ecom_system/frontend
vercel
```

## Testing

### Backend Tests
```bash
cd ecom_system/backend
python manage.py test
```

### Frontend Tests
```bash
cd ecom_system/frontend
npm test
```

## Setup Instructions

### Backend Setup
```bash
cd ecom_system/backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup
```bash
cd ecom_system/frontend
npm install
npm run dev
```

## Environment Variables

Backend requires these environment variables:
```
SECRET_KEY=your_django_secret
DEBUG=True
MPESA_CONSUMER_KEY=your_mpesa_key
MPESA_CONSUMER_SECRET=your_mpesa_secret
```

## Screenshots

![Homepage](screenshots/home.png)
![Product Page](screenshots/product.png)
![Cart](screenshots/cart.png)

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/products/` | GET | List all products |
| `/api/products/:slug` | GET | Get product details |
| `/api/cart/` | GET, POST | Cart operations |
| `/api/auth/register/` | POST | User registration |
| `/api/auth/login/` | POST | User login |

## License

MIT
