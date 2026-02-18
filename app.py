import streamlit as st
import random
import pandas as pd
import time
import plotly.express as px

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="🎡 Giant LED Wheel of Fate",
    layout="wide"
)

# ---------------------------------------------------
# PREMIUM CSS (Carnival Theme)
# ---------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1f1c2c);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.title {
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#00f7ff;
    text-shadow:0 0 20px #00f7ff;
}

.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:20px;
    box-shadow: 0 0 25px rgba(0,255,255,0.3);
}

.big-number {
    font-size:50px;
    color:#ff007f;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown("<div class='title'>🎡 Giant LED Wheel of Fate</div>", unsafe_allow_html=True)
st.markdown("<center><h3>Probability Cracker — Carnival Edition</h3></center>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------------------------------
# HOUSE ODDS
# ---------------------------------------------------
normal_odds = {
    "Swag 🎁": 0.4,
    "Boosters ⚡": 0.3,
    "Rare Drops 💎": 0.2,
    "Tricky Section ☠️": 0.1
}

cheat_odds = {
    "Swag 🎁": 0.25,
    "Boosters ⚡": 0.25,
    "Rare Drops 💎": 0.40,
    "Tricky Section ☠️": 0.10
}

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("🎮 Game Controls")

spins = st.sidebar.slider("Number of Spins", 100, 5000, 1000)
cheat_mode = st.sidebar.toggle("🕵️ Activate Cheat Mode")

odds = cheat_odds if cheat_mode else normal_odds

# ---------------------------------------------------
# MAIN AREA
# ---------------------------------------------------
col1, col2 = st.columns([1,2])

with col1:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("🎯 Current Odds")
    for key, value in odds.items():
        st.write(f"{key} → {value*100}%")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    if st.button("🎡 SPIN THE WHEEL"):
        
        with st.spinner("Spinning the LED Wheel..."):
            time.sleep(2)

        results = random.choices(
            list(odds.keys()),
            weights=list(odds.values()),
            k=spins
        )

        df = pd.DataFrame(results, columns=["Outcome"])
        summary = df["Outcome"].value_counts()

        st.success("✨ Spin Complete!")

        # Big Rare Drop Highlight
        rare_count = summary.get("Rare Drops 💎", 0)

        st.markdown(f"<div class='big-number'>💎 Rare Drops Won: {rare_count}</div>", unsafe_allow_html=True)

        if cheat_mode:
            st.warning("Cheat Mode shifts probability towards Rare Drops!")

        # Plotly Chart (Beautiful)
        fig = px.pie(
            names=summary.index,
            values=summary.values,
            title="Outcome Distribution",
            color_discrete_sequence=px.colors.sequential.Plasma
        )

        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(summary.reset_index().rename(
            columns={"index":"Outcome", 0:"Count"}
        ))

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<center>🎪 Built for Cognizance Carnival | Advanced UI Edition</center>", unsafe_allow_html=True)