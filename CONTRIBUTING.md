# 🧑‍💻 Contributing to SVG Icons API

Thanks for your interest in contributing to the **SVG Icons API**! We welcome community contributions — whether you're submitting new icons, fixing bugs, or improving documentation.

This project depends on open, safe, and license-compliant contributions from developers like you. Please read the following guidelines before submitting a pull request.

---

## 📁 Project Structure

All SVG icons should be placed in the `assets/icons/` folder, inside one of the following subfolders:

```
assets/icons/
├── dark/       → icons for dark backgrounds
├── light/      → icons for light backgrounds
└── neutral/    → icons that work on both
```

Example:

```bash
assets/icons/dark/github.svg
assets/icons/light/astro.svg
assets/icons/neutral/terraform.svg
```

> File names must use lowercase letters and dashes only (e.g. `google-cloud.svg`).

---

## ✅ Icon Requirements

Please follow these requirements when contributing icons:

- [ ] File format: **SVG**
- [ ] Resolution-independent (not pixel-based)
- [ ] Clean, minimal, and optimized (no unnecessary `<metadata>`, `<title>`, etc.)
- [ ] Licensed under an open source license (MIT, CC0, Apache 2.0, etc.)
- [ ] No embedded fonts or base64 images
- [ ] Safe to use on the web (no scripts or external links)

---

## 🛑 Licensing and Legal Notice

> Before submitting an SVG icon, **you must have the legal right to use and distribute it**.

You **must ensure** that the icon is:
- Your original work, or
- Public domain or open source licensed, or
- Explicitly allowed by the license (MIT, CC0, etc.)

If you are not sure, **please contact the brand owner or author before contributing**.

We do not accept icons from commercial icon sets or scraped from websites without proper attribution or permission.

---

## 🚀 How to Contribute

1. **Fork the repository**
2. Create a new branch:
   ```bash
   git checkout -b add/my-icon-name
   ```
3. Add your SVG to the appropriate folder
4. Commit your changes:
   ```bash
   git commit -m "Add neutral icon: my-icon-name"
   ```
5. Push and open a Pull Request:
   ```bash
   git push origin add/my-icon-name
   ```

---

## 📋 Pull Request Checklist

Before submitting your PR:

- [ ] The file is in `.svg` format
- [ ] The icon is in the correct subfolder (`dark/`, `light/`, or `neutral/`)
- [ ] The filename is lowercase with dashes (`my-icon-name.svg`)
- [ ] The icon is clean, optimized, and contains no extra tags
- [ ] You confirm you have the legal rights to submit the icon

---

## 🙌 Thank You

Your contribution helps make this project better for everyone.  
If you have questions, feel free to [open an issue](https://github.com/reymundvirtus/svg-icons-api/issues).

Let's make open-source better together! 💚