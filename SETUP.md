# 📚 Complete Setup Guide

A step-by-step guide for first-time users to get the project running.

## ⏱️ Time Required: 15-20 minutes

---

## 📋 Step 1: Prerequisites Check

Before starting, ensure you have:

- ✅ Python 3.8+ installed ([Download here](https://www.python.org/downloads/))
- ✅ Git installed ([Download here](https://git-scm.com/))
- ✅ A Google account (for YouTube API keys)
- ✅ Internet connection

**Verify Python installation:**
```bash
python --version
```

---

## 🔗 Step 2: Clone or Download the Repository

### Option A: Using Git (Recommended)
```bash
git clone https://github.com/yourusername/youtube-engagement-prediction.git
cd youtube-engagement-prediction
```

### Option B: Download ZIP
1. Click "Code" → "Download ZIP" on GitHub
2. Extract the ZIP file
3. Open terminal/command prompt in the extracted folder

---

## 🐍 Step 3: Set Up Python Virtual Environment

A virtual environment isolates project dependencies from your system Python.

### On Windows (PowerShell):
```bash
python -m venv venv
.\venv\Scripts\activate
```

### On macOS/Linux (Bash/Zsh):
```bash
python3 -m venv venv
source venv/bin/activate
```

**You should see `(venv)` at the start of your terminal prompt.**

---

## 📦 Step 4: Install Dependencies

With your virtual environment activated:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:
- Data processing: pandas, numpy, scipy
- ML algorithms: scikit-learn, xgboost, catboost, lightgbm
- Web UI: streamlit
- API client: google-api-python-client
- Utilities: python-dotenv, matplotlib, seaborn, joblib

**Installation takes 3-5 minutes depending on internet speed.**

---

## 🔑 Step 5: Set Up YouTube API Keys (IMPORTANT!)

### 5A: Generate API Keys

1. **Visit Google Cloud Console:**
   - Go to: https://console.cloud.google.com
   - Sign in with your Google account

2. **Create a New Project:**
   - Click the project dropdown (top left)
   - Click "NEW PROJECT"
   - Name: "YouTube ML Engagement" (or your choice)
   - Click "CREATE"
   - Wait for creation to complete

3. **Enable YouTube Data API v3:**
   - Search for "YouTube Data API v3" in the search bar
   - Click on the result
   - Click "ENABLE"

4. **Create API Key Credentials:**
   - Go to "Credentials" in the left menu
   - Click "Create Credentials" → "API Key"
   - Copy the generated key (looks like: `AIzaSy...`)

5. **Get Multiple Keys (Optional but Recommended):**
   - Go back to "Create Credentials" → "API Key"
   - Repeat this to create 5-10 keys
   - This helps avoid rate limiting

### 5B: Configure Your `.env` File

1. **Copy the template:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file** with your keys:

   **If you have 1 key:**
   ```env
   YOUTUBE_API_KEY=AIzaSy_your_actual_key_here
   ```

   **If you have multiple keys (recommended):**
   ```env
   YOUTUBE_API_KEY_1=AIzaSy_key1_here
   YOUTUBE_API_KEY_2=AIzaSy_key2_here
   YOUTUBE_API_KEY_3=AIzaSy_key3_here
   ```

3. **⚠️ IMPORTANT Security Notes:**
   - The `.env` file is in `.gitignore` (won't be committed)
   - NEVER share your `.env` file
   - NEVER commit it to GitHub
   - Always keep it locally with your real keys only

### 5C: Verify Setup

```bash
python scraping/api_config.py
```

**Expected output:**
```
✅ Configuration loaded successfully!
```

If you see an error, check:
- `.env` file exists in the project root
- Keys are correctly formatted
- No extra spaces before/after keys

---

## ✅ Step 6: Verify Installation

Run this to check everything is installed:

```bash
python -c "import pandas, numpy, sklearn, streamlit, google; print('✅ All packages installed successfully!')"
```

---

## 🚀 Step 7: Run the Project

### Option A: Run the Interactive Web UI (Recommended for Beginners)

```bash
cd ui
streamlit run app.py
```

This opens a web dashboard where you can:
- Input video details
- Get engagement predictions
- Find optimal video duration
- View interactive graphs

**Access at:** http://localhost:8501

### Option B: Run Data Scraping

```bash
python scraping/Youtube_Scape.py
```

This scrapes YouTube data and saves it to CSV files.

### Option C: Run Jupyter Notebooks (For Learning)

```bash
jupyter notebook
```

Then navigate to and open:
1. `notebooks/01_data_overview.ipynb` - Understand your data
2. `notebooks/02_data_cleaning.ipynb` - Clean the data
3. `notebooks/03_feature_engineering.ipynb` - Create features
4. `notebooks/04_model_gradient_boosting.ipynb` - Train model

---

## 📂 Project Directory Structure

After setup, your directory should look like:

```
youtube-engagement-prediction/
├── venv/                          # Virtual environment (created)
├── data/
│   ├── raw/                       # YouTube data (will be created after scraping)
│   └── processed/
├── scraping/
│   ├── Youtube_Scape.py
│   ├── api_config.py
│   └── ...
├── notebooks/                     # Jupyter notebooks
├── ui/
│   └── app.py
├── models/                        # Trained models
├── .env                           # YOUR API KEYS (local only)
├── .env.example                   # Template (safe to commit)
├── requirements.txt               # Dependencies
├── README.md
└── LICENSE
```

---

## 🔧 Troubleshooting

### Problem: "Command not found: python"

**Solution:**
- Python not in PATH or not installed
- Reinstall Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### Problem: "venv command not found"

**Solution:**
```bash
# Windows
python -m venv venv

# macOS/Linux
python3 -m venv venv
```

### Problem: "No module named 'requirements'"

**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Problem: ".env file not found or API keys missing"

**Solution:**
```bash
cp .env.example .env
# Then edit .env with your actual API keys
```

### Problem: "API quota exceeded"

**Solution:**
- Add more API keys to `.env` (YOUTUBE_API_KEY_2, YOUTUBE_API_KEY_3, etc.)
- Wait a few hours for quota to reset
- Multiple keys allow better rate limiting

### Problem: Streamlit app not loading

**Solution:**
```bash
# Make sure you're in the project root
cd youtube-engagement-prediction

# Install/upgrade streamlit
pip install --upgrade streamlit

# Run from ui folder
cd ui
streamlit run app.py
```

### Problem: "Permission denied" on macOS/Linux

**Solution:**
```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

---

## 📚 Next Steps

After successful setup:

1. **Run the UI:** `streamlit run ui/app.py` and explore
2. **Scrape data:** `python scraping/Youtube_Scape.py`
3. **Learn from notebooks:** Follow the notebooks in order
4. **Experiment:** Modify parameters and see results

---

## 🆘 Getting Help

If you encounter issues:

1. **Check the README.md** - Has comprehensive documentation
2. **Review error messages** - They usually tell you what's wrong
3. **Check YouTube API Status** - [console.cloud.google.com](https://console.cloud.google.com)
4. **Verify your API key** - Must start with "AIzaSy"
5. **Check Python version** - Must be 3.8+

---

## ✨ Success!

Once you see the Streamlit dashboard running, your setup is complete! 🎉

**You can now:**
- 📊 Analyze YouTube engagement data
- 🤖 Make engagement predictions
- 📈 Optimize video duration
- 📚 Learn machine learning concepts

Happy coding! 🚀

---

## 📝 Notes for GitHub

When sharing this project on GitHub:

1. ✅ Commit: `README.md`, `requirements.txt`, `LICENSE`, `.env.example`
2. ❌ Don't commit: `.env`, `venv/`, `__pycache__/`, `*.pkl`
3. ✅ Check: `.gitignore` has necessary entries

The `.gitignore` file already handles most of this automatically.
