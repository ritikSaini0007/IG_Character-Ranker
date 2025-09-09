import streamlit as st
import random

# ---------------------------------
# Backend data (hidden from user)
# ---------------------------------


st.set_page_config(page_title="InGame Character Ranker", page_icon="🎮")

# 👇 Google Search Console verification tag
st.markdown("""
    <meta name="google-site-verification" content="ckVNwqcXvD4StnngmAKsxUnH-ckCD5_Ljsf_4YQk3r4" />
""", unsafe_allow_html=True)


character_values = {
    "A-Patroa": 3, "A124": 8, "Alok": 9, "Alvaro": 8.5, "Andrew": 7.5,
    "Antonio": 5, "Caroline": 7, "Clu": 5, "Corono/CR7": 9, "D-bee": 5,
    "Dasha": 6, "Dimitri": 0, "Ford": 9, "Hayato": 6, "Homer": 5,
    "Ignis": 5.5, "Iris": 5, "J.Biebs": 4, "Jai-indian": 8, "Joseph": 8,
    "Jota": 4, "K": 6.5, "Kapella": 5.5, "Kassie": 8, "Kelly": 4.5,
    "Kenta": 4.5, "Kla": 5.5, "Koda": 8.5, "Koiros": 7, "Laura": 3,
    "Leon": 5, "Lila": 6, "Luqueta": 4, "Luna": 6.5, "Maro": 8,
    "Maxim": 4, "Miguel": 5, "Misha": 6, "Moco": 5, "Nairi": 6,
    "Nikita": 8, "Notora": 6.5, "Nulla/Eva": 10, "Olivia": 7.5,
    "Orion": 2, "Oscar": 10, "Otho": 4.5, "Paloma": 3, "Primis/Adam": 10,
    "Rafael": 9, "Rin": 8.5, "Ryden": 1, "Santino": 0, "Shani": 9,
    "Shirou": 4.5, "Skyler": 9.5, "Sonia": 0, "Steffie": 8.5, "Suzy": 6.5,
    "Tatsuya": 10, "Thiva": 9, "Walfrahh": 8.5, "Wukong": 5, "Xayne": 7.5,
}

# Sorted dropdown options
all_names = sorted(character_values.keys())

# Special names for custom line
special_names = {"Tatsuya", "Dimitri", "Sonia", "Santino", "Ryden"}

# Jokes by range
jokes = {
    "zero": [
        "😢 Arre bhai, tum to bilkul zero nikle Lagta Hai Tum C Ho!",
        "😂 Tumhare character ki value dekh ke mujhe bhi rona aa gaya Noob!",
        "💤 Real Life Me To Tu Hai Hi C, Game Me To Achhe Se Characters Use Karle!"
    ],
    "low": [
        "💪 Aree Yaar Maja Nahi Aaya, Thode Or Achhe Characters Use Karo, Tu Rahega Noob Hi! 🤷",
        "😅 Tumhari Characters ki choice itni Kharab, Tabhi to Tum Kisi Ki Choice Nahi Ho! 😭",
        "🪫 Tumhara Character Combination To Chu***** jaisa hai! 🤦"
    ],
    "medium": [
        "😎 Tumhare Character Combination Style thoda Sahi hai, Matlab Jaise Tumhara Dimag! 🧠",
        "🚀 Tumhare Character Combination ki energy Middle vali hai, Aur Tumhe Middle ka Matlab To Pata Hi Hai 💀",
        "🕹️ Tum pro aur noob ke beech atke hue ho, Lagta Hai Tumhe Beech Vali Cheez Me Jyada Hi Interest Hai! 😉"
    ],
    "high": [
        "🔥 Wah! Kya Baat Hai, Tumhara Score To Thik Thak Aaya Hai, But Itna Bhi Achha Nahi Aaya BC! 😂",
        "🤨 Tumhare Character Combination To Sahi But Jyada Nahi Tik Payega Like Your L*** 😏",
        "🎯 Tumhara Character Combination Na to Kharab Hai, Na Hi Achha, Matlab Beech Me Aa Raha Hai Jaise Tum Ho Beechke 💀!"
    ],
    "very_high": [
        "👑 Tum Free Fire Me To Fast Ho Gaye Characters Lagake, But Real Life Me Tum Dhhile Hi Rahoge! 🐌",
        "🌟 You Have Good Character Combination, But You Don't Have Good Face! 🤣",
        "🏆 Tumhara Score Size To Achha Aaya Hai, And I Think Tumhara 'Uska' Size Bhi Achha Hoga 😉"
    ],
    "legend": [
        "🚀 OP Bolte! Tumhara character to full jhakaas hai, Lekin Real Life Me Tu Bakbaas Hai! 🤡",
        "💥 Tumne Best Character Combination To Find Kar Liya, But Apne Liye GF Nahi Find Kar Paya! 💔",
        "⚡ Tumne Apne Deep Hole... Oooo Sorry 🤣 Deep Think ka Use Karke Best Character Combination Find Kar Hi Liya! 🧠"
    ]
}


# Funny/joke lines based on total sum range
def get_funny_line(total: float) -> str:
    if total <= 5:
        return random.choice(jokes["zero"])
    elif total <= 10:
        return random.choice(jokes["low"])
    elif total <= 20:
        return random.choice(jokes["medium"])
    elif total <= 30:
        return random.choice(jokes["high"])
    elif total <= 35:
        return random.choice(jokes["very_high"])
    else:
        return random.choice(jokes["legend"])

# ---------------------------------
# UI
# ---------------------------------
st.set_page_config(page_title="FunWith ReTrick_YT", page_icon="🧮")
st.title("🧮 Let's Find Your Behind Image in Free Fire ")

st.write("Select Your Character Combination, Each Character Have Value Out of 10 According to his Ability ")

col1, col2 = st.columns(2)

# Dropdowns with filtered options
with col1:
    n1 = st.selectbox("Character 1", all_names, index=0)
    n2_options = [x for x in all_names if x != n1]
    n2 = st.selectbox("Character 2", n2_options, index=0)

with col2:
    n3_options = [x for x in all_names if x not in {n1, n2}]
    n3 = st.selectbox("Character 3", n3_options, index=0)

    n4_options = [x for x in all_names if x not in {n1, n2, n3}]
    n4 = st.selectbox("Character 4", n4_options, index=0)

if st.button("Submit Characters", type="primary"):
    selected_names = [n1, n2, n3, n4]
    total = sum(character_values[name] for name in selected_names)

    st.success(f"✅ Your Characters's Score out of 40 is  :  {total}")
    st.write("### Breakdown:")
    for name in selected_names:
        st.write(f"{name} → {character_values[name]}")

    # Special name check
    if any(name in special_names for name in selected_names):
        st.error("💀 I Think, You Are A G@Y ")
    else:
        # Show funny line based on total
        line = get_funny_line(total)
        st.info(line)


st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #111;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            border-top: 2px solid #111;
        }
    </style>
    <div class="footer">
        © 2025 | Made by <b>ReTrick_YT</b>  
        👉 <a href="https://www.youtube.com/@ReTrick_Yt/featured" target="_blank" style="color:blue; text-decoration:none;"> Check out my Youtube Channel 🎥🔥</a>
    </div>
    """,
    unsafe_allow_html=True
)
