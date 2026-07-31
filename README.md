# Portfolio - Resume Maker

A public resume site where recruiters can view a candidate's resume, print/save it as PDF, and email the candidate directly — no login required. Built with Django, includes an authenticated dashboard for the resume owner to manage their content.

🔗 **Live demo:** https://pybrothers.top/

[Screenshots here — resume view]
<img width="1359" height="767" alt="p_contact page" src="https://github.com/user-attachments/assets/73da53c2-b50b-49a3-b1fe-3227926408f0" />

## Features
- Public resume page — no account needed to view, print, or save as PDF
- Recruiters can email the candidate directly from the page (Django `send_mail`)
- Authenticated dashboard for the resume owner to edit their information
- Clean, printable layout (browser print-to-PDF supported)

## Tech Stack
Python · Django · SQLite/PostgreSQL · HTML/CSS/Bootstrap

## Run Locally

```bash
git clone https://github.com/GRMaruf/Portfolio.git
cd Portfolio
pip install -r requirements.txt
python manage.py makemigrations authentication
python manage.py makemigrations portfolio
python manage.py migrate
python manage.py runserver
```

## What I'd Build Next
- Server-generated PDF export (styled independently of browser print settings)
- Multiple resume templates
- View-count/analytics for the owner (who viewed the resume, when)
