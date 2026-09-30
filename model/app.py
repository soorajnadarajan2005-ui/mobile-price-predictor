import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"h1"
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"h2"
st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="wide"
)

df = pd.read_csv("data/mobile_prices.csv")

X = df[
    [
        "RAM",
        "Storage",
        "Battery",
        "ScreenSize",
        "Camera",
        "ProcessorScore"
    ]
]

y = df["Price"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LinearRegression()



model.fit(X_train, y_train)


y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

st.title("📱 Mobile Price Predictor")

st.write(
    "Predict the estimated price of a smartphone "
    "using Linear Regression."
)

st.divider()


st.sidebar.header("📱 Mobile Specifications")


ram = st.sidebar.slider(
    "RAM (GB)",
    2,
    16,
    8
)


storage = st.sidebar.slider(
    "Storage (GB)",
    32,
    512,
    128
)


battery = st.sidebar.slider(
    "Battery (mAh)",
    2000,
    7000,
    5000,
    step=100
)


screen_size = st.sidebar.slider(
    "Screen Size (inches)",
    5.0,
    7.5,
    6.5,
    step=0.1
)


camera = st.sidebar.slider(
    "Camera (MP)",
    8,
    250,
    50
)


processor = st.sidebar.slider(
    "Processor Score",
    300,
    1000,
    700
)

if st.sidebar.button("🔮 Predict Price"):

    input_data = pd.DataFrame(
        [[
            ram,
            storage,
            battery,
            screen_size,
            camera,
            processor
        ]],
        columns=[
            "RAM",
            "Storage",
            "Battery",
            "ScreenSize",
            "Camera",
            "ProcessorScore"
        ]
    )

    prediction = model.predict(input_data)[0]

    st.success("Prediction completed!")

    st.metric(
        "💰 Estimated Mobile Price",
        f"₹{prediction:,.0f}"
    )


st.header("🤖 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Mean Squared Error",
        f"{mse:,.2f}"
    )

with col2:
    st.metric(
        "R² Score",
        f"{r2:.4f}"
    )


st.header("📊 Dataset")

st.dataframe(
    df,
    use_container_width=True
)


st.header("📈 Price Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Average Price",
        f"₹{df['Price'].mean():,.0f}"
    )

with col2:
    st.metric(
        "Minimum Price",
        f"₹{df['Price'].min():,.0f}"
    )

with col3:
    st.metric(
        "Maximum Price",
        f"₹{df['Price'].max():,.0f}"
    )




st.header("📊 Feature vs Price")

feature = st.selectbox(
    "Select Feature",
    [
        "RAM",
        "Storage",
        "Battery",
        "ScreenSize",
        "Camera",
        "ProcessorScore"
    ]
)


fig, ax = plt.subplots()

sns.scatterplot(
    data=df,
    x=feature,
    y="Price",
    ax=ax
)

ax.set_title(
    f"{feature} vs Mobile Price"
)

st.pyplot(fig)



st.header("🔥 Correlation Heatmap")


fig, ax = plt.subplots(
    figsize=(10, 6)
)

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)



st.header("📐 Linear Regression Coefficients")

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

st.dataframe(
    coefficients,
    use_container_width=True
)


st.write(
    "Intercept:",
    model.intercept_
)