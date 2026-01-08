import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ==============================
# KONFIGURASI HALAMAN
# ==============================
st.set_page_config(
    page_title="Advanced Movie Sentiment Intelligence",
    layout="wide"
)

st.title("🎬 Advanced Movie Sentiment Intelligence")
st.caption("Analisis Sentimen, Sarkasme, Aspek & Spoiler — Keyword-Based Intelligence")

# ==============================
# DATA DUMMY ULASAN FILM
# ==============================
reviews = [
    "Filmnya bagus sih, tapi jujur kecewa sama ceritanya. Visual doang yang niat.",
    "Akting pemerannya keren, tapi pas akhirnya tokoh utama mati malah bikin kesel.",
    "Katanya film epic, ternyata plot twist-nya receh dan bikin rugi waktu.",
    "Visualnya mantap, CGI cakep, cuma ceritanya ngalor ngidul nggak jelas.",
    "Awalnya seru, akhirnya ketebak. Ternyata musuhnya dia lagi.",
    "Bagus banget! Tapi entah kenapa setelah keluar bioskop rasanya hampa.",
    "Aktingnya kaku, dialog cringe, padahal visualnya lumayan niat.",
    "Plot twist-nya niat banget, tapi pas karakter favorit mati langsung drop.",
    "Cerita ni film sebenernya oke, tapi eksekusinya bikin kecewa.",
    "Film mahal tapi hasilnya gitu doang, rugi nonton di bioskop."
]

# ==============================
# KEYWORD CONFIGURATION
# ==============================
positive_words = ["bagus", "keren", "mantap", "oke", "niat", "epic"]
negative_words = ["kecewa", "rugi", "kesel", "drop", "kaku", "cringe", "hampa"]

aspect_keywords = {
    "Visual": ["visual", "cgi", "sinematografi"],
    "Akting": ["akting", "pemeran", "dialog"],
    "Cerita": ["cerita", "plot", "alur", "twist"]
}

spoiler_keywords = ["mati", "akhirnya", "ternyata", "plot twist"]

# ==============================
# FUNGSI ANALISIS
# ==============================
def analyze_review(text):
    text_lower = text.lower()

    pos_score = sum(word in text_lower for word in positive_words)
    neg_score = sum(word in text_lower for word in negative_words)

    sentiment = "Positif" if pos_score > neg_score else "Negatif"

    sarcasm = "Ya" if pos_score > 0 and neg_score > 0 else "Tidak"
    spoiler = "Ya" if any(word in text_lower for word in spoiler_keywords) else "Tidak"

    aspect_scores = {}
    for aspect, keywords in aspect_keywords.items():
        aspect_scores[aspect] = sum(k in text_lower for k in keywords)

    return sentiment, sarcasm, spoiler, aspect_scores

# ==============================
# INPUT ULASAN MANUAL
# ==============================
st.subheader("✍️ Analisis Ulasan Manual")

user_input = st.text_area("Masukkan ulasan film:", height=120)

if user_input:
    sentiment, sarcasm, spoiler, aspect_scores = analyze_review(user_input)

    col1, col2, col3 = st.columns(3)
    col1.metric("Sentimen", sentiment)
    col2.metric("Sarkasme", sarcasm)
    col3.metric("Spoiler", spoiler)

    # Radar Chart Aspek
    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=list(aspect_scores.values()),
        theta=list(aspect_scores.keys()),
        fill='toself',
        name='Aspek'
    ))
    radar.update_layout(title="Analisis Aspek Ulasan")
    st.plotly_chart(radar, use_container_width=True)

# ==============================
# BULK ANALYSIS
# ==============================
st.subheader("📊 Bulk Analysis — Dummy Movie Reviews")

data = []
for r in reviews:
    sentiment, sarcasm, spoiler, aspect_scores = analyze_review(r)
    data.append({
        "Ulasan": r,
        "Sentimen": sentiment,
        "Sarkasme": sarcasm,
        "Spoiler": spoiler,
        "Visual": aspect_scores["Visual"],
        "Akting": aspect_scores["Akting"],
        "Cerita": aspect_scores["Cerita"]
    })

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

# ==============================
# VISUALISASI DISTRIBUSI SENTIMEN
# ==============================
sentiment_count = df["Sentimen"].value_counts().reset_index()
sentiment_count.columns = ["Sentimen", "Jumlah"]

bar_chart = px.bar(
    sentiment_count,
    x="Sentimen",
    y="Jumlah",
    title="Distribusi Sentimen Ulasan Film",
    text="Jumlah"
)

st.plotly_chart(bar_chart, use_container_width=True)
