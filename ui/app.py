import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="YouTube Engagement Optimizer",
    layout="centered"
)

st.markdown("## 📊 YouTube Engagement Optimizer")
st.write("Predict engagement and find the optimal video duration.")

# LOAD MODEL & ARTIFACTS
@st.cache_resource
def load_artifacts():
    model = joblib.load("../models/gradient_boosting_model.pkl")
    category_te = joblib.load("../models/category_te_mapping.pkl")

    with open("../models/gradient_boosting_model_info.json") as f:
        info = json.load(f)

    return model, category_te, info


model, category_te, info = load_artifacts()

ALL_FEATURES = info["all_features"]
GLOBAL_TE_MEAN = info["category_te_global_mean"]

# Category ID to Name Mapping
CATEGORY_NAMES = {
    "1": "Film & Animation",
    "2": "Autos & Vehicles",
    "10": "Music",
    "15": "Pets & Animals",
    "17": "Sports",
    "19": "Travel & Events",
    "20": "Gaming",
    "22": "People & Blogs",
    "23": "Comedy",
    "24": "Entertainment",
    "25": "News & Politics",
    "26": "Howto & Style",
    "27": "Education",
    "28": "Science & Technology",
    "29": "Nonprofits & Activism"
}

def extract_title_features(title):
    """Extract features from video title"""
    title_length = len(title)
    title_words = len(title.split())
    title_exclamation = title.count('!')
    title_question = title.count('?')
    return title_length, title_words, title_exclamation, title_question


def apply_target_encoding(df):
    df = df.copy()
    df["category_te"] = (
        df["category_id"]
        .map(category_te)
        .fillna(GLOBAL_TE_MEAN)
    )
    return df


def prepare_input(df):
    df = apply_target_encoding(df)
    return df[ALL_FEATURES]


def find_optimal_duration(base_df, min_d, max_d, step):
    durations = np.arange(min_d, max_d + step, step)
    results = []

    for d in durations:
        temp_df = base_df.copy()
        temp_df["duration_minutes"] = d

        X_temp = prepare_input(temp_df)
        pred = model.predict(X_temp)[0]

        results.append((d, pred))

    results_df = pd.DataFrame(
        results,
        columns=["duration_minutes", "predicted_engagement"]
    )

    best_row = results_df.loc[
        results_df["predicted_engagement"].idxmax()
    ]

    return best_row, results_df


# USER INPUT FORM

st.subheader("📥 Video Details")

with st.form("user_input_form"):

    col1, col2 = st.columns(2)

    with col1:
        # Video title input - automatically extract features
        video_title = st.text_input(
            "Video Title", 
            "Amazing Cooking Recipe You Must Try!"
        )
        
        # Category selection with names
        category_display = st.selectbox(
            "Video Category",
            options=list(CATEGORY_NAMES.keys()),
            format_func=lambda x: CATEGORY_NAMES[x],
            index=7  # Default to "People & Blogs"
        )
        
        captions_flag = st.selectbox("Captions Available", [True, False])
        total_videos = st.number_input("Total Videos on Channel", 1, 100000, 100)
        channel_age_days = st.number_input("Channel Age (days)", 1, 100000, 1000)
        
        # Subscriber count input
        subscriber_count = st.number_input(
            "Subscriber Count", 
            min_value=1, 
            max_value=100000000, 
            value=10000,
            help="Enter the actual subscriber count"
        )

    with col2:
        publish_hour = st.slider("Publish Hour (0-23)", 0, 23, 12)
        publish_dow = st.slider("Publish Day (0=Mon, 6=Sun)", 0, 6, 3)
        is_hd = st.selectbox("HD Video", [True, False])
        
        # Duration optimization range
        st.markdown("**🎯 Duration Optimization Range**")
        col_a, col_b = st.columns(2)
        with col_a:
            min_dur = st.number_input("Min Duration (min)", 0.5, 120.0, 2.0)
        with col_b:
            max_dur = st.number_input("Max Duration (min)", min_dur + 0.5, 120.0, 20.0)
        
        step_dur = st.number_input("Step Size (min)", 0.1, 5.0, 0.5)

    submit = st.form_submit_button("🚀 Predict Engagement & Find Optimal Duration")


# PREDICTION & OPTIMIZATION

if submit:
    # Extract title features automatically
    title_length, title_words, title_exclamation, title_question = extract_title_features(video_title)
    
    # Log transform subscriber count
    subscriber_count_log = np.log10(subscriber_count)
    
    # Cyclical encoding for time features
    publish_hour_sin = np.sin(2 * np.pi * publish_hour / 24)
    publish_hour_cos = np.cos(2 * np.pi * publish_hour / 24)
    publish_dow_sin = np.sin(2 * np.pi * publish_dow / 7)
    publish_dow_cos = np.cos(2 * np.pi * publish_dow / 7)

    # Create input dataframe with correct data types
    input_df = pd.DataFrame([{
        "category_id": int(category_display),
        "captions_flag": int(captions_flag),
        "total_videos": int(total_videos),
        "channel_age_days": int(channel_age_days),
        "subscriber_count_log": float(subscriber_count_log),
        "title_length": int(title_length),
        "title_words": int(title_words),
        "title_exclamation": int(title_exclamation),
        "title_question": int(title_question),
        "publish_hour_sin": float(publish_hour_sin),
        "publish_hour_cos": float(publish_hour_cos),
        "publish_dow_sin": float(publish_dow_sin),
        "publish_dow_cos": float(publish_dow_cos),
        "is_hd": int(is_hd)
    }])

    # Find optimal duration and predict engagement
    st.subheader("🎯 Optimal Duration Analysis")
    
    with st.spinner("Analyzing optimal duration..."):
        best, curve = find_optimal_duration(
            input_df, min_dur, max_dur, step_dur
        )

        # Display optimal duration
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "✅ Optimal Duration",
                f"{best['duration_minutes']:.2f} min"
            )
        with col2:
            st.metric(
                "📊 Expected Engagement",
                f"{best['predicted_engagement']:.4f}"
            )

        # Plot engagement curve
        st.subheader("📊 Engagement vs Duration")
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(curve["duration_minutes"], curve["predicted_engagement"], 
                linewidth=2, color='#1f77b4', label='Predicted Engagement')
        
        # Mark optimal duration
        ax.axvline(x=best['duration_minutes'], color='green', linestyle='--', 
                   linewidth=2, label=f'Optimal ({best["duration_minutes"]:.1f} min)')
        
        ax.scatter([best['duration_minutes']], [best['predicted_engagement']], 
                  color='red', s=100, zorder=5, label='Best Point')
        
        ax.set_xlabel('Duration (minutes)', fontsize=12)
        ax.set_ylabel('Predicted Engagement (Log Scale)', fontsize=12)
        ax.set_title('Video Duration vs Engagement Rate', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        st.pyplot(fig)
        
        # Show data table
        with st.expander("📋 View Detailed Data"):
            display_curve = curve.copy()
            display_curve["predicted_engagement"] = display_curve["predicted_engagement"].round(4)
            st.dataframe(display_curve, use_container_width=True)
