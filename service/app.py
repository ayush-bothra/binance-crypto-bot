import streamlit as st
from handler.bot import BasicBot
from helpers.config import api_key, secret_key

# We use @st.cache_resource so we don't reconnect to Binance 
# every time a button is clicked. The bot stays alive in memory.
@st.cache_resource
def get_bot_instance():
    if not api_key or not secret_key:
        st.error("API Keys missing in helpers/config.py or .env")
        return None
    return BasicBot(api_key, secret_key)

bot = get_bot_instance()


st.set_page_config(page_title="Binance Bot")
st.title("Binance Futures Trader")
with st.sidebar:
    st.header("Status")
    if bot:
        st.success("Connected to Testnet")
    else:
        st.error("Not Connected to Testnet")

# B. Main Order Form
st.subheader("Place New Order")
col1, col2 = st.columns(2)

with col1:
    symbol = st.selectbox("Symbol", ["BTCUSDT"])
    side = st.selectbox("Side", ["BUY", "SELL"])

with col2:
    order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP_MARKET"])
    quantity = st.number_input("Quantity", min_value=0.001, step=0.001, format="%.3f")

# Only show 'Price' if Limit, only show 'Stop Price' if Stop.
price = None
stop_price = None

if order_type == "LIMIT":
    price = st.number_input("Limit Price (USDT)", min_value=0.0, step=0.1, format="%.2f")
elif order_type == "STOP_MARKET":
    stop_price = st.number_input("Trigger Price (USDT)", min_value=0.0, step=0.1, format="%.2f")

if st.button("Place Order", type="primary"):
    if not bot:
        st.error("Bot is not initialized.")
    else:
        with st.spinner(f"Sending {side} {symbol}..."):
            try:
                response, order_id = bot.place_order(
                    symbol=symbol, 
                    side=side, 
                    order_type=order_type, 
                    quantity=quantity, 
                    price=price, 
                    stop_price=stop_price
                )

                if order_id:
                    st.success(f"Order Placed, ID: `{order_id}`")
                    with st.expander("View Raw Response"):
                        st.json(response)
                else:
                    st.warning("Order sent, but no ID returned (check logs).")
                    st.json(response)

            except Exception as e:
                st.error(f"Error: {e}")