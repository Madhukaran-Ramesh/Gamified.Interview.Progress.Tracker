# Gamified Interview Progress Tracker

A Streamlit-based web application for tracking and gamifying technical interview preparation.

## Features
- User authentication and progress saving
- Stages, levels, missions, and hurdles for various technical skills
- Timed challenges and leaderboards
- Dashboard with progress, badges, scores, and achievements
- Personalized recommendations
- Visually engaging UI with icons and graphics
- Modular, extensible codebase

## Project Structure
- `app/` - Streamlit UI and frontend logic
- `backend/` - Business logic, authentication, and API endpoints
- `models/` - Data models and database logic (SQLite)
- `assets/` - Icons, images, and static files

## Getting Started
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run app/main.py
   ```

## Extending
- Add new missions/hurdles by updating the `models/` and `backend/` modules.
- UI enhancements can be made in `app/`.
