# Careers Website

## Overview
A Flask-based careers website that displays job listings. Built with Python/Flask, Jinja2 templates, and CSS.

## Project Structure
- `app.py` - Main Flask application with routes and job data
- `templates/` - Jinja2 HTML templates
  - `base.html` - Base template with header/footer
  - `home.html` - Homepage with job listings grid
  - `job.html` - Individual job detail page
- `static/` - Static assets
  - `style.css` - Site styling

## Running the Application
The application runs on port 5000 with `python app.py`.

## Routes
- `/` - Homepage with all job listings
- `/job/<id>` - Individual job detail page

## Recent Changes
- 2025-12-18: Initial setup with Flask, sample job listings, responsive design
