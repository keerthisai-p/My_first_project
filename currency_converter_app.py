import streamlit as st
import requests
import random

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="keerthi' Currency Converter",
    page_icon="🌸",
    layout="centered"
)

# ---------------------------------------------------------
# COUNTRY AND CURRENCY DATA
# ---------------------------------------------------------

countries = {
    "🇮🇳 India": "INR",
    "🇺🇸 United States": "USD",
    "🇬🇧 United Kingdom": "GBP",
    "🇪🇺 European Union": "EUR",
    "🇯🇵 Japan": "JPY",
    "🇦🇺 Australia": "AUD",
    "🇨🇦 Canada": "CAD",
    "🇨🇭 Switzerland": "CHF",
    "🇨🇳 China": "CNY",
    "🇸🇬 Singapore": "SGD",
    "🇦🇪 United Arab Emirates": "AED",
    "🇸🇦 Saudi Arabia": "SAR",
    "🇰🇷 South Korea": "KRW",
    "🇳🇿 New Zealand": "NZD",
    "🇿🇦 South Africa": "ZAR",
    "🇷🇺 Russia": "RUB",
    "🇧🇷 Brazil": "BRL",
    "🇲🇽 Mexico": "MXN",
    "🇹🇭 Thailand": "THB",
    "🇲🇾 Malaysia": "MYR",
    "🇮🇩 Indonesia": "IDR",
    "🇹🇷 Turkey": "TRY",
    "🇳🇴 Norway": "NOK",
    "🇸🇪 Sweden": "SEK",
    "🇩🇰 Denmark": "DKK",
    "🇵🇱 Poland": "PLN",
    "🇮🇱 Israel": "ILS",
    "🇵🇭 Philippines": "PHP",
    "🇻🇳 Vietnam": "VND",
    "🇧🇩 Bangladesh": "BDT",
    "🇵🇰 Pakistan": "PKR",
    "🇱🇰 Sri Lanka": "LKR",
    "🇳🇵 Nepal": "NPR"
}

# ---------------------------------------------------------
# PASTEL BACKGROUND + FALLING FLOWERS + CUSTOM FONT
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* -------------------------------------------------
       GOOGLE FONT
       ------------------------------------------------- */

    @import url(
        'https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&family=Quicksand:wght@300;400;500;600;700&display=swap'
    );

    /* -------------------------------------------------
       MAIN PAGE
       ------------------------------------------------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 20%,
                rgba(255, 210, 225, 0.55),
                transparent 25%
            ),
            radial-gradient(
                circle at 90% 15%,
                rgba(210, 235, 255, 0.55),
                transparent 25%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(220, 255, 230, 0.50),
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #fff7fb,
                #f5f9ff,
                #f8fff9
            );

        color: #5d5366;
        font-family: 'Quicksand', sans-serif;
    }

    /* -------------------------------------------------
       MAIN CONTAINER
       ------------------------------------------------- */

    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 850px;
        position: relative;
        z-index: 10;
    }

    /* -------------------------------------------------
       TITLE
       ------------------------------------------------- */

    .main-title {
        font-family: 'Caveat', cursive;
        font-size: 64px;
        font-weight: 700;
        text-align: center;
        color: #a66c91;
        margin-bottom: 0;
        text-shadow:
            2px 2px 8px rgba(180, 130, 160, 0.18);
    }

    .subtitle {
        font-family: 'Quicksand', sans-serif;
        text-align: center;
        font-size: 17px;
        color: #8b7d91;
        margin-bottom: 30px;
    }

    /* -------------------------------------------------
       GLASS CARD
       ------------------------------------------------- */

    .glass-card {
        background: rgba(255, 255, 255, 0.60);
        border: 1px solid rgba(255, 255, 255, 0.75);
        border-radius: 25px;
        padding: 25px;
        box-shadow:
            0 15px 40px rgba(160, 130, 160, 0.12),
            inset 0 1px 1px rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        margin-bottom: 20px;
    }

    /* -------------------------------------------------
       LABELS
       ------------------------------------------------- */

    label {
        font-family: 'Quicksand', sans-serif !important;
        color: #766879 !important;
        font-weight: 600 !important;
    }

    /* -------------------------------------------------
       SELECTBOX
       ------------------------------------------------- */

    div[data-baseweb="select"] > div {
        background: rgba(255, 255, 255, 0.72) !important;
        border: 1px solid #ead7e5 !important;
        border-radius: 15px !important;
        min-height: 48px;
    }

    div[data-baseweb="select"] > div:hover {
        border-color: #d8a7c5 !important;
    }

    /* -------------------------------------------------
       NUMBER INPUT
       ------------------------------------------------- */

    div[data-testid="stNumberInput"] input {
        background: rgba(255, 255, 255, 0.72) !important;
        border: 1px solid #ead7e5 !important;
        border-radius: 15px !important;
        color: #66596b !important;
        font-family: 'Quicksand', sans-serif !important;
        font-size: 18px !important;
    }

    /* -------------------------------------------------
       CONVERT BUTTON
       ------------------------------------------------- */

    div.stButton > button {
        width: 100%;
        border-radius: 18px;
        border: none;
        padding: 13px 20px;
        font-family: 'Quicksand', sans-serif;
        font-size: 18px;
        font-weight: 700;

        background: linear-gradient(
            135deg,
            #e9a8c8,
            #b9b4e9
        );

        color: white;

        box-shadow:
            0 8px 20px rgba(180, 140, 190, 0.25);

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-3px);

        box-shadow:
            0 12px 25px rgba(180, 140, 190, 0.35);
    }

    /* -------------------------------------------------
       INFO MESSAGE
       ------------------------------------------------- */

    div[data-testid="stAlert"] {
        border-radius: 18px !important;
        border: none !important;
        background: rgba(255, 240, 248, 0.75) !important;
        color: #765d70 !important;
    }

    /* -------------------------------------------------
       SUCCESS MESSAGE
       ------------------------------------------------- */

    div[data-testid="stAlert"] p {
        font-family: 'Quicksand', sans-serif !important;
    }

    /* -------------------------------------------------
       METRIC
       ------------------------------------------------- */

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.55);
        border-radius: 18px;
        padding: 15px;
        border: 1px solid rgba(255, 255, 255, 0.75);
        box-shadow: 0 8px 25px rgba(160, 130, 160, 0.10);
    }

    div[data-testid="stMetricLabel"] {
        color: #89758b !important;
    }

    div[data-testid="stMetricValue"] {
        color: #a66c91 !important;
    }

    /* -------------------------------------------------
       SECTION HEADINGS
       ------------------------------------------------- */

    h2, h3 {
        font-family: 'Caveat', cursive !important;
        color: #a66c91 !important;
        font-weight: 600 !important;
    }

    /* -------------------------------------------------
       DIVIDERS
       ------------------------------------------------- */

    hr {
        border: none;
        border-top: 1px solid rgba(190, 160, 190, 0.20);
        margin: 30px 0;
    }

    /* -------------------------------------------------
       FALLING FLOWERS
       ------------------------------------------------- */

    .flower {
        position: fixed;
        top: -80px;
        z-index: 1;
        pointer-events: none;

        animation-name: falling;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }

    .flower:nth-child(1) {
        left: 5%;
        font-size: 25px;
        animation-duration: 12s;
        animation-delay: 0s;
    }

    .flower:nth-child(2) {
        left: 15%;
        font-size: 18px;
        animation-duration: 15s;
        animation-delay: 3s;
    }

    .flower:nth-child(3) {
        left: 27%;
        font-size: 30px;
        animation-duration: 11s;
        animation-delay: 1s;
    }

    .flower:nth-child(4) {
        left: 39%;
        font-size: 20px;
        animation-duration: 14s;
        animation-delay: 5s;
    }

    .flower:nth-child(5) {
        left: 51%;
        font-size: 27px;
        animation-duration: 13s;
        animation-delay: 2s;
    }

    .flower:nth-child(6) {
        left: 64%;
        font-size: 19px;
        animation-duration: 16s;
        animation-delay: 4s;
    }

    .flower:nth-child(7) {
        left: 75%;
        font-size: 28px;
        animation-duration: 12s;
        animation-delay: 6s;
    }

    .flower:nth-child(8) {
        left: 87%;
        font-size: 22px;
        animation-duration: 15s;
        animation-delay: 2s;
    }

    .flower:nth-child(9) {
        left: 94%;
        font-size: 30px;
        animation-duration: 13s;
        animation-delay: 7s;
    }

    @keyframes falling {

        0% {
            transform:
                translateY(-100px)
                translateX(0px)
                rotate(0deg);
            opacity: 0;
        }

        10% {
            opacity: 0.75;
        }

        25% {
            transform:
                translateY(25vh)
                translateX(30px)
                rotate(90deg);
        }

        50% {
            transform:
                translateY(50vh)
                translateX(-30px)
                rotate(180deg);
        }

        75% {
            transform:
                translateY(75vh)
                translateX(35px)
                rotate(270deg);
        }

        90% {
            opacity: 0.6;
        }

        100% {
            transform:
                translateY(110vh)
                translateX(-20px)
                rotate(360deg);
            opacity: 0;
        }
    }

    /* -------------------------------------------------
       FOOTER
       ------------------------------------------------- */

    .footer {
        text-align: center;
        font-family: 'Caveat', cursive;
        font-size: 20px;
        color: #a58c9d;
        margin-top: 30px;
    }

    </style>

    <!-- FALLING FLOWERS -->

    <div class="flower">🌸</div>
    <div class="flower">🌷</div>
    <div class="flower">🌼</div>
    <div class="flower">🌺</div>
    <div class="flower">🌸</div>
    <div class="flower">🌷</div>
    <div class="flower">🌼</div>
    <div class="flower">🌺</div>
    <div class="flower">🌸</div>

    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">Currency Bloom 💱</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'A simple and beautiful country-to-country currency converter 🌸'
    '</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# MAIN CARD
# ---------------------------------------------------------

st.markdown(
    '<div class="glass-card">',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# COUNTRY SELECTION
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    from_country = st.selectbox(
        "🌍 From Country",
        list(countries.keys()),
        index=0
    )

with col2:

    to_country = st.selectbox(
        "🌎 To Country",
        list(countries.keys()),
        index=1
    )

# Get currency codes
from_currency = countries[from_country]
to_currency = countries[to_country]

# ---------------------------------------------------------
# SELECTED CURRENCIES
# ---------------------------------------------------------

st.info(
    f"💫 **{from_country} ({from_currency})** "
    f"→ **{to_country} ({to_currency})**"
)

# ---------------------------------------------------------
# AMOUNT
# ---------------------------------------------------------

amount = st.number_input(
    f"💰 Enter amount in {from_currency}",
    min_value=0.0,
    value=1.0,
    step=1.0
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# EXCHANGE RATE FUNCTION
# ---------------------------------------------------------

def get_exchange_rate(from_currency, to_currency):

    url = (
        f"https://api.exchangerate-api.com/v4/latest/"
        f"{from_currency}"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code != 200:
            return None

        data = response.json()

        rates = data.get("rates", {})

        return rates.get(to_currency)

    except requests.exceptions.RequestException:

        return None


# ---------------------------------------------------------
# CONVERT BUTTON
# ---------------------------------------------------------

if st.button(
    "🌸 Convert Currency 🌸",
    use_container_width=True
):

    if amount <= 0:

        st.warning(
            "Please enter an amount greater than 0."
        )

    elif from_currency == to_currency:

        converted_amount = amount

        st.success(
            f"✨ {amount:,.2f} {from_currency} = "
            f"{converted_amount:,.2f} {to_currency}"
        )

        st.metric(
            "Exchange Rate",
            "1.0000"
        )

    else:

        with st.spinner(
            "🌷 Getting the latest exchange rate..."
        ):

            rate = get_exchange_rate(
                from_currency,
                to_currency
            )

        if rate is None:

            st.error(
                "Unable to get the exchange rate. "
                "Please check your internet connection "
                "and try again."
            )

        else:

            converted_amount = amount * rate

            # -------------------------------------------------
            # RESULT CARD
            # -------------------------------------------------

            st.markdown(
                '<div class="glass-card">',
                unsafe_allow_html=True
            )

            st.success(
                f"✨ {amount:,.2f} {from_currency} = "
                f"{converted_amount:,.2f} {to_currency}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "🌸 Exchange Rate",
                    f"1 {from_currency} = "
                    f"{rate:,.4f} {to_currency}"
                )

            with col2:

                st.metric(
                    "💱 Converted Amount",
                    f"{converted_amount:,.2f} "
                    f"{to_currency}"
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

# ---------------------------------------------------------
# CONVERSION DETAILS
# ---------------------------------------------------------

st.divider()

st.markdown(
    '<div class="glass-card">',
    unsafe_allow_html=True
)

st.subheader("🌷 Conversion Details")

col1, col2, col3 = st.columns(3)

with col1:

    st.write("**🌍 From**")
    st.write(from_country)
    st.code(from_currency)

with col2:

    st.write("**💰 Amount**")
    st.write(f"{amount:,.2f}")

with col3:

    st.write("**🌎 To**")
    st.write(to_country)
    st.code(to_currency)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Made with 💗 and a little bit of 🌸 magic
        <br>
        Live exchange rates • Country to Country Conversion
    </div>
    """,
    unsafe_allow_html=True
)