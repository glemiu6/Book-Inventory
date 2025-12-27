# Book Inventory

A Python project that scrapes a site about books , transforms it and loads it into a database.

## Table of Contents
- [Structure](#structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Structure

### Tree Schema

```plain text
book_inventory/
│
├── scraper/
│   ├── __init__.py
│   ├── scraper.py
│   ├── parser.py
│   └── categories.py
│
├── database/
│   ├── __init__.py
│   ├── db.py
│   ├── models.py
│   └── queries.py
│
├── services/
│   ├── __init__.py
│   ├── book_service.py
│   ├── user_service.py
│   └── scrape_service.py
│
├── cli/
│   ├── __init__.py
│   └── menu.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── main.py
├── requirements.txt
└── README.md
```

### ER Model


## Installation

## Usage

## Features

## Contributing
1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.