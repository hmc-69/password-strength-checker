# Password Strength Checker Website

A small, beautiful web application that checks password strength and gives clear, localised feedback. The app includes a modern UI with a looping video background and accessible, responsive design.

## Quick setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Add a background video:
   - Place a video file named `background.mp4` in the `static/` folder. The video will play on loop as the background.
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

- 🎥 Video background: Looping MP4 background to give the app a modern, dynamic look.
- 🎨 Glassmorphism UI: Blurred, semi-transparent overlay for a clean, contemporary visual style.
- ⏳ Loading spinner: Smooth loading animation for a better user experience.
- 💬 Localised feedback: Fun Malayalam messages to guide users about their password strength.
- 🔒 Real-time strength analysis: Passwords are evaluated instantly on the client-side and/or backend (see main.py).
- ✅ Strength indicators: Clear visual cues (colors, text) for weak, medium, and strong passwords.
- 📱 Responsive: Works well on desktops, tablets, and mobile devices.
- ♿ Accessibility minded: Uses semantic HTML and visible focus styles for keyboard users.

## Notes

- Add your own `background.mp4` (MP4 is recommended for browser compatibility).
- The password scoring logic is implemented in `main.py` — feel free to tweak rules (length, character variety, blacklist, etc.).

## Contributing

Contributions, issues and feature requests are welcome — feel free to open a PR or an issue.

## License

This project is open source. Add or update a license file if you want to specify terms.
