# Password Strength Checker Website

A small, beautiful web application that checks password strength and gives clear, localised feedback. The app uses a modern UI with a looping video background, a glassmorphism overlay, and fast, real-time strength analysis.

## Quick setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add a background video:
- Place a video file named `background.mp4` in the `static/` folder. The video will play on loop as the page background.

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Project structure

```
password_checker/
├── app.py              # Flask backend server
├── main.py             # Password checking logic
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main HTML page
└── static/
    ├── style.css       # Styling
    ├── script.js       # Frontend JavaScript
    └── background.mp4  # Background video (you need to add this)
```

## Features

- 🎥 Video background
  - Looping MP4 video as the page background for a modern look.
- 🎨 Glassmorphism UI
  - Blurred, semi-transparent overlay for a clean, contemporary visual style.
- ⏳ Loading spinner
  - Smooth loading animation for a polished UX.
- 💬 Localised feedback
  - Fun Malayalam messages to guide users about their password strength and keep the app friendly.
- 🔒 Real-time strength analysis
  - Passwords are evaluated instantly (client-side and/or via the backend logic in `main.py`).
- ✅ Strength indicators
  - Clear visual cues (text and color) for weak, medium, and strong passwords.
- ✍️ Actionable suggestions
  - Suggestions are provided to help users improve weak passwords (length, character variety, etc.).
- 📈 Scoring & heuristics
  - Scoring rules live in `main.py` — adjust length thresholds, character class weights, or add blacklist checks as needed.
- 📱 Responsive
  - Layout adapts to desktop, tablet, and mobile screens.
- ♿ Accessibility-minded
  - Semantic HTML and visible focus styles to support keyboard users and assistive tech.

## Customisation tips

- To modify scoring rules, open `main.py` — typical edits include adjusting length weight, adding forbidden words, or tuning character-class scoring.
- Replace or remove the background video by changing the file in `static/background.mp4`.
- Update the localized feedback messages in `script.js` or the templates to support other languages.

## Notes

- The video should be MP4 for widest browser compatibility.
- The project is intentionally small and easy to extend — consider adding unit tests around `main.py` if you plan to change the scoring logic.

## Contributing

Contributions, issues and feature requests are welcome — feel free to open a PR or an issue.

## License

This project is open source. Add or update a LICENSE file to specify terms.
```
