# 📊 YouTube Video Optimal Duration Prediction

A machine learning project to predict YouTube video engagement rates and find optimal video durations using YouTube Data API and advanced ML algorithms including Gradient Boosting, CatBoost, XGBoost, and LightGBM.

**⚠️ Educational Purpose**: This project is designed for learning and educational purposes.

---

## 🌟 Features

- 🎬 **Data Scraping**: Fetch real YouTube video data using YouTube Data API
- 📈 **Exploratory Data Analysis**: Comprehensive EDA with visualizations
- 🤖 **Multiple ML Models**: Gradient Boosting, CatBoost, XGBoost, LightGBM
- 🎯 **Engagement Prediction**: Predict engagement rates for new videos
- ⏱️ **Duration Optimization**: Find the optimal video duration for maximum engagement
- 🌐 **Interactive Web UI**: Streamlit-based dashboard for predictions
- 📊 **Model Comparison**: Evaluate and compare different algorithms

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [YouTube API Setup](#youtube-api-setup)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Running the UI](#running-the-ui)
- [Project Workflow](#project-workflow)
- [Models](#models)
- [License](#license)

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)
- YouTube Data API key(s)
- Internet connection (for data scraping)

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-engagement-prediction.git
cd youtube-engagement-prediction
```

### Step 2: Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install:
- `pandas`, `numpy` - Data manipulation
- `scikit-learn` - Machine learning
- `xgboost`, `catboost`, `lightgbm` - Gradient boosting libraries
- `streamlit` - Web UI framework
- `google-api-python-client` - YouTube API client
- `python-dotenv` - Environment variable management
- `matplotlib`, `seaborn` - Visualization
- `joblib` - Model serialization
- And other dependencies

---

## 🔐 YouTube API Setup

### Getting Your API Keys

**IMPORTANT:** Never commit `.env` files with real keys to GitHub!

1. **Go to Google Cloud Console:**
   - Visit [https://console.cloud.google.com](https://console.cloud.google.com)
   - Sign in with your Google Account (create one if needed)

2. **Create a New Project:**
   - Click on the project dropdown at the top
   - Click "NEW PROJECT"
   - Enter a name (e.g., "YouTube ML Project")
   - Click "CREATE"

3. **Enable YouTube Data API v3:**
   - In the search bar, search for "YouTube Data API v3"
   - Click on it and select "ENABLE"

4. **Create API Key Credentials:**
   - Go to "Credentials" in the left menu
   - Click "Create Credentials" → "API Key"
   - Copy the generated API key (looks like: `AIzaSy...`)

5. **Optional - Get Multiple Keys (Recommended):**
   - Repeat steps 4 for up to 20+ keys to avoid rate limiting
   - This allows the scraper to rotate between keys

### Setting Up Your `.env` File

1. **Copy the template file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file** with your API keys:

   **Option 1: Single API Key**
   ```env
   # .env file
   YOUTUBE_API_KEY=AIzaSy_your_actual_key_here
   ```

   **Option 2: Multiple API Keys (Recommended for better rate limiting)**
   ```env
   # .env file
   YOUTUBE_API_KEY_1=AIzaSy_key1_here
   YOUTUBE_API_KEY_2=AIzaSy_key2_here
   YOUTUBE_API_KEY_3=AIzaSy_key3_here
   # ... add more keys as needed
   ```

3. **Keep the `.env` file LOCAL - DO NOT COMMIT TO GITHUB:**
   - The `.gitignore` file already prevents this
   - Always use `.env.example` as a template for other users

### Verify Your Setup

```bash
python scraping/api_config.py
```

If successful, you should see: `✅ Configuration loaded successfully!`

---

## 📁 Project Structure

```
youtube-engagement-prediction/
├── data/
│   ├── raw/                              # Raw YouTube data (CSV files)
│   │   ├── Cooking_Recipes_long.csv
│   │   ├── Daily_Vlog_medium.csv
│   │   └── ... (other scraped datasets)
│   └── processed/
│       ├── youtube_combined_data.csv     # Cleaned & merged data
│       └── combine_csv.ipynb             # Data combining notebook
│
├── scraping/
│   ├── Youtube_Scape.py                  # Main scraper script
│   ├── api_config.py                     # API key management
│   └── __pycache__/
│
├── eda/
│   └── eda_overview.ipynb                # Exploratory Data Analysis
│
├── notebooks/
│   ├── 01_data_overview.ipynb            # Data overview & statistics
│   ├── 02_data_cleaning.ipynb            # Data cleaning process
│   ├── 03_feature_engineering.ipynb      # Feature engineering
│   ├── 04_model_gradient_boosting.ipynb  # Gradient Boosting model
│   ├── 05_model_catboost.ipynb           # CatBoost model
│   ├── 06_model_xgboost.ipynb            # XGBoost model
│   ├── 07_model_lightgbm.ipynb           # LightGBM model
│   └── catboost_info/                    # CatBoost training logs
│
├── models/
│   ├── gradient_boosting_model.pkl       # Trained GB model
│   ├── category_te_mapping.pkl           # Target encoding mapper
│   ├── gradient_boosting_model_info.json # Model metadata
│   └── ... (other model files)
│
├── ui/
│   └── app.py                            # Streamlit web application
│
│
├── .env.example                          # Template for API keys (SAFE TO COMMIT)
├── .env                                  # Your API keys (DO NOT COMMIT)
├── .gitignore                            # Git ignore rules
├── requirements.txt                      # Python dependencies
├── README.md                             # This file
└── LICENSE                               # Project license (Educational)
```

---

## 🚀 Usage

### 1. Run the Data Scraper

Scrape YouTube video data for your analysis:

```bash
python scraping/Youtube_Scape.py
```

**What it does:**
- Fetches video data from YouTube Data API
- Rotates through your API keys to avoid rate limiting
- Extracts engagement metrics (views, likes, comments, duration)
- Saves data to CSV files in `data/raw/`

---

### 2. Data Analysis & Cleaning

Run the Jupyter notebooks in order:

```bash
# View your data
jupyter notebook notebooks/01_data_overview.ipynb

# Clean the data
jupyter notebook notebooks/02_data_cleaning.ipynb

# Create features
jupyter notebook notebooks/03_feature_engineering.ipynb

# Exploratory Data Analysis
jupyter notebook eda/eda_overview.ipynb
```

---

### 3. Train Models

Train different ML models:

```bash
# Gradient Boosting
jupyter notebook notebooks/04_model_gradient_boosting.ipynb

# CatBoost
jupyter notebook notebooks/05_model_catboost.ipynb

# XGBoost
jupyter notebook notebooks/06_model_xgboost.ipynb

# LightGBM
jupyter notebook notebooks/07_model_lightgbm.ipynb
```

---

## 🌐 Running the Web UI

The interactive Streamlit dashboard allows you to:
- Input video details (title, category, duration, etc.)
- Get engagement predictions
- Find the optimal video duration
- Visualize engagement curves

### Start the UI

```bash
# Navigate to the UI directory
cd ui

# Run Streamlit app
streamlit run app.py
```

The dashboard will open at: `http://localhost:8501`

### Features in the UI:

1. **Input Video Details:**
   - Video title (features are auto-extracted)
   - Category selection
   - Channel statistics (subscribers, total videos, age)
   - Publish time (hour & day of week)
   - Video quality (HD or SD)
   - Caption availability

2. **Get Predictions:**
   - Engagement rate prediction
   - Optimal video duration analysis
   - Interactive duration optimization graph

3. **View Results:**
   - Predicted engagement metrics
   - Duration vs. engagement curve
   - Detailed data tables

---

## 🤖 Models

This project implements and compares 4 state-of-the-art gradient boosting models:

| Model | Accuracy | Speed | Notes |
|-------|----------|-------|-------|
| **Gradient Boosting** | ⭐⭐⭐⭐ | ⭐⭐⭐ | Baseline model, good interpretability |
| **CatBoost** | ⭐⭐⭐⭐⭐ | ⭐⭐ | Best for categorical features |
| **XGBoost** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Fast and efficient |
| **LightGBM** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Fastest, good for large datasets |

Model files are saved in the `models/` directory.

---

## 📊 Project Workflow

```
Data Scraping (YouTube API)
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering
        ↓
Train Multiple ML Models
        ↓
Model Evaluation & Comparison
        ↓
Deploy Interactive Web UI
        ↓
Make Predictions & Analyze
```

---

## 🔧 Troubleshooting

### API Key Issues

**Error: "No YouTube API keys found"**
- ✅ Make sure `.env` file exists in project root
- ✅ Verify keys are added: `YOUTUBE_API_KEY=...` or `YOUTUBE_API_KEY_1=...`
- ✅ Restart your terminal/Python after updating `.env`

**Error: "quota exceeded"**
- ✅ You've hit the API rate limit
- ✅ Add more API keys to your `.env` file
- ✅ Try again after a few hours

### Streamlit UI Issues

**Error: "module not found"**
- ✅ Ensure all requirements are installed: `pip install -r requirements.txt`
- ✅ Check you're in the correct virtual environment

**Port 8501 already in use**
- ✅ Run on a different port: `streamlit run app.py --server.port 8502`

---

## 📚 Learning Resources

- [YouTube Data API Documentation](https://developers.google.com/youtube/v3)
- [Scikit-learn ML Documentation](https://scikit-learn.org/)
- [XGBoost Guide](https://xgboost.readthedocs.io/)
- [CatBoost Documentation](https://catboost.ai/)
- [LightGBM Guide](https://lightgbm.readthedocs.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## 📝 License

This project is licensed under the **Academic Free License (AFL) 3.0** for **Educational Purposes Only**.

See the [LICENSE](LICENSE) file for details.

---

## 👨‍🎓 Educational Note

**This project is designed for:**
- Learning machine learning concepts
- Understanding YouTube data analysis
- Practicing with real-world APIs
- Building end-to-end ML applications
- Portfolio development

**Not for:**
- Commercial purposes
- Violating YouTube's Terms of Service
- Scraping user private data

Always respect API terms of service and YouTube's policies.

---

## 🙏 Contributing

This is an educational project. Feel free to fork, modify, and learn!

---

## 📞 Support

For issues or questions:
1. Check the [Troubleshooting](#troubleshooting) section
2. Review Jupyter notebooks for detailed explanations
3. Check the YouTube Data API documentation

---

**Happy Learning! 🚀**

### Train Models
```bash
# Add training code in models/train_model.py
python -m models.train_model
```

### Run Web UI
```bash
streamlit run ui/app.py
```

## 🔐 Security Best Practices

✅ **DO:**
- Store API keys in `.env` file (local only)
- Add `.env` to `.gitignore` (already done)
- Use `.env.example` as template
- Rotate keys regularly
- Use multiple keys for better rate limiting

❌ **DON'T:**
- Hardcode API keys in source code
- Commit `.env` to GitHub
- Share API keys publicly
- Reuse keys across projects

## Environment Variables

- `YOUTUBE_API_KEY` - Single API key (fallback)
- `YOUTUBE_API_KEY_1`, `YOUTUBE_API_KEY_2`, etc. - Multiple keys for rotation

## Dependencies

- `google-api-python-client` - YouTube Data API
- `python-dotenv` - Load .env files
- `pandas`, `numpy` - Data processing
- `scikit-learn` - Machine learning
- `matplotlib`, `seaborn` - Visualization
- `jupyter` - Notebooks

## Requirements

- Python 3.8+
- YouTube Data API key
- Internet connection (for scraping)

## License

MIT License - See LICENSE file for details

## Troubleshooting

**"YOUTUBE_API_KEY not found"**
```bash
# Make sure .env file exists and has your key
cat .env | grep YOUTUBE_API_KEY

# If empty, add your key to .env
nano .env
```

**"API quota exceeded"**
- Use multiple API keys for better rate limiting
- Add more keys to `.env`: `YOUTUBE_API_KEY_1`, `YOUTUBE_API_KEY_2`, etc.
- Spread scraping across multiple days
