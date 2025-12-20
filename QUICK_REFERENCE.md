# 🚀 Quick Reference Guide

## Fast Links for Users

### 📖 Documentation
- **README.md** - Start here! Project overview and complete guide
- **SETUP.md** - Step-by-step installation (15-20 min)
- **CONTRIBUTING.md** - How to contribute and learn
- **.env.example** - API key template (copy and edit)

### 🎯 First Time?
Follow this order:
1. **Read:** README.md (5 min) - Understand what this is
2. **Install:** SETUP.md (15 min) - Get everything running
3. **Run:** `streamlit run ui/app.py` (1 min) - See it in action
4. **Learn:** notebooks/ - Explore the code

### 🔑 API Keys (Critical!)
- Get keys at: https://console.cloud.google.com
- Copy template: `cp .env.example .env`
- Edit `.env` with your actual keys
- Test: `python scraping/api_config.py`
- **DO NOT COMMIT .env FILE!**

### 📁 Important Directories
```
data/          → YouTube data (raw & processed)
notebooks/     → Learning materials (01-07)
ui/            → Streamlit app (app.py)
models/        → Trained ML models
scraping/      → Data scraping scripts
```

### 💻 Common Commands

**Installation:**
```bash
git clone <repo-url>
cd youtube-engagement-prediction
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

**API Setup:**
```bash
cp .env.example .env
# Edit .env with your API keys
python scraping/api_config.py
```

**Run UI:**
```bash
cd ui
streamlit run app.py
```

**Run Scraper:**
```bash
python scraping/Youtube_Scape.py
```

**Run Notebooks:**
```bash
jupyter notebook
# Navigate to notebooks/ folder
```

### ⚠️ Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| Import error | `pip install -r requirements.txt` |
| API key error | Check `.env` file exists & has keys |
| Port already in use | `streamlit run ui/app.py --server.port 8502` |
| ModuleNotFoundError | Activate virtual environment: `source venv/bin/activate` |
| API quota exceeded | Add more API keys or wait 24 hours |

### 🎓 Learning Paths

**Beginner:**
- Run UI → Experiment → Understand inputs/outputs

**Intermediate:**
- Follow notebooks 01-03 → Understand data pipeline
- Follow notebooks 04-07 → Understand models

**Advanced:**
- Modify models → Add new features → Train models
- Improve UI → Add new predictions → Deploy

### 📊 Project Models
1. **Gradient Boosting** - Good accuracy, interpretable
2. **CatBoost** - Best with categorical features
3. **XGBoost** - Fast and efficient
4. **LightGBM** - Fastest, great for large data

### 🌐 UI Features
- 📝 Input video details
- 🎯 Get engagement predictions
- 📈 Find optimal duration
- 📊 View interactive graphs
- 📋 Export data tables

### 🔐 Security Notes
- API keys stay in `.env` (never committed)
- `.env.example` is template (safe to share)
- Multiple keys avoid rate limiting
- Always respect YouTube ToS
- Don't scrape private data

### 📞 Getting Help
1. Check SETUP.md for installation issues
2. Check README troubleshooting section
3. Review Jupyter notebooks for code examples
4. Check Google API documentation
5. Open GitHub issue (be specific)

### ✅ Pre-Publish Checklist
Before pushing to GitHub:
```bash
# Remove real API keys
rm .env

# Verify no secrets in git
git status

# Should NOT show .env, venv/, *.pkl
# Should show documentation files

# Commit and push
git add .
git commit -m "Initial commit"
git push origin main
```

### 📝 File Overview

**Critical Files:**
- `README.md` - Must read
- `requirements.txt` - For installation
- `.env.example` - For API setup
- `ui/app.py` - Web application

**Learning Files:**
- `notebooks/01-07` - Understanding data & models
- `eda/eda_overview.ipynb` - Data analysis

**Configuration:**
- `.env` - Your local API keys (don't commit)
- `.gitignore` - What to ignore in git
- `LICENSE` - Educational license

### 🎯 Most Common Tasks

**I want to:**
1. **Understand the project** → Read README.md
2. **Get it running** → Follow SETUP.md
3. **Try the UI** → `streamlit run ui/app.py`
4. **Learn ML** → Open notebooks/01-07
5. **Scrape data** → `python scraping/Youtube_Scape.py`
6. **Train models** → Open notebooks/04-07
7. **Contribute** → Read CONTRIBUTING.md
8. **Get API keys** → Follow README API section

### ⚡ Speed Tips

**Fastest setup (5 min):**
```bash
# Copy paste these commands
git clone <url>
cd youtube-engagement-prediction
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Add your API keys to .env
streamlit run ui/app.py
```

### 📚 Resource Links

- [YouTube API Docs](https://developers.google.com/youtube/v3)
- [Scikit-Learn Guide](https://scikit-learn.org/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [XGBoost Guide](https://xgboost.readthedocs.io/)
- [Google Cloud Console](https://console.cloud.google.com)

### 🎓 License
**Educational Use Only** - See LICENSE file
- ✅ Learning & research
- ✅ Portfolio projects
- ✅ Classroom use
- ❌ Commercial use
- ❌ Violating API ToS

### 📧 Contact & Support
- Check documentation first
- Open GitHub issues
- Be specific in descriptions
- Include error messages
- Share Python version

---

**For detailed info, see README.md**
**For installation help, see SETUP.md**
**Ready to contribute? See CONTRIBUTING.md**

Happy coding! 🚀
