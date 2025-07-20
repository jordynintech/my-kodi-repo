# Jordyn's Kodi Repository

A personal Kodi repository containing my favorite add-ons.

## 🚀 Installation in Kodi

1. **Add Source**
   - Go to Settings → File Manager → Add Source
   - Add URL: `https://raw.githubusercontent.com/jordynintech/my-kodi-repo/main/`
   - Name it: `Jordyn's Repo`

2. **Install Repository**
   - Go to Add-ons → Install from zip file → Jordyn's Repo
   - Install: `repository.jordynintech-1.0.1.zip`

3. **Install Add-ons**
   - Go to Install from repository → Jordyn's Kodi Repository
   - Browse categories to install add-ons

## 📦 Available Add-ons

- **Umbrella** (v6.7.47) - Movies & TV Shows
- **CocoScrapers Module** (v1.0.1) - External scrapers for other add-ons

## 🔄 Adding New Add-ons

To add a new add-on to this repository:

1. Create a directory in `zips/` with the add-on ID as the name
2. Put the `addon.xml` file in that directory  
3. Put the `.zip` file for the add-on in that directory
4. Run `python3 update_repo.py` to regenerate the repository files
5. Commit and push changes to GitHub

## ⚠️ Disclaimer

This repository is for educational purposes only. I do not host any content and am not responsible for what users do with these add-ons. Please respect copyright laws in your country.

## 📝 Repository Structure

```
├── addons.xml          # Repository manifest
├── addons.xml.md5      # Checksum file
├── update_repo.py      # Script to update repository
├── repository.jordynintech-1.0.1.zip  # Repository add-on
└── zips/               # Add-on files
    ├── plugin.video.umbrella/
    │   ├── addon.xml
    │   └── plugin.video.umbrella-6.7.47.zip
    └── script.module.cocoscrapers/
        ├── addon.xml
        └── script.module.cocoscrapers-1.0.1.zip
```
