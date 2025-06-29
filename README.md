# 🎨 SVG Icons API

A simple and fast API for serving SVG icons tailored for light, dark, and neutral backgrounds. Built with [FastAPI](https://fastapi.tiangolo.com/), this project allows you to request and embed SVG icons from a structured directory via clean URLs.

---

## 🚀 Features

- ⚡ Blazing-fast icon serving with FastAPI
- 🌓 Themed icon support for light and dark backgrounds
- 🟢 Neutral icons that work on any background
- 🖼 Easy to embed in Markdown, HTML, or frontend apps
- 🔗 Public API endpoints — no auth required
- 🛡 Licensed under MIT (open source and free to use)

---

### 📥 GET Icon by Theme


| Parameter   | Type     | Example            | Description                           |
|-------------|----------|--------------------|---------------------------------------|
| `theme`     | string   | `dark`, `light`, `neutral` | The visual theme of the icon |
| `icon_name` | string   | `github`           | Name of the icon without `.svg`       |

#### ✅ Examples

```http
GET /icons/dark/github
GET /icons/light/astro
GET /icons/neutral/google
```

Returns: image/svg+xml

You can embed directly in HTML or Markdown:

<span>
<img src="https://svg-icons-api-production.up.railway.app/icons/neutral/spotify" width="32" />
<img src="https://svg-icons-api-production.up.railway.app/icons/light/astro" width="32" />
<img src="https://svg-icons-api-production.up.railway.app/icons/dark/github" width="32" />
</span>

---

## 🧑‍💻 Contributing

Want to add more icons? Awesome!

- Fork this repo
- Add SVG icons to the correct folder (`dark/`, `light/`, or `neutral/`)
- Submit a PR

By contributing, you agree that the icons you submit are either:
- Your original work
- Licensed under an open source/public domain license (e.g. MIT, CC0)
- Not restricted by copyright or trademark laws

> [!IMPORTANT]
> Before submitting an SVG icon, please ensure you have the legal right to do so.
>
> ✅ You must either:
> - Own the icon yourself,
> - Have explicit permission to use it, or
> - Confirm that it is licensed under an open license (e.g. MIT, CC0, Apache 2.0).
>
> ❌ **If you're unsure**, please contact the company or the original author before uploading.
> Submitting copyrighted or trademarked material without proper permission may violate intellectual property laws.

---

### License
This library is MIT licensed.
