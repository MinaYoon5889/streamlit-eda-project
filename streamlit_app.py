import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/amazon_sales_2025_INR.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.strftime("%b")
    df["Quarter"] = df["Date"].dt.quarter
    df["Delivered_Flag"] = (df["Delivery_Status"] == "Delivered").astype(int)
    df["Satisfied"] = (df["Review_Rating"] >= 4).astype(int)
    df["Log_Total_Sales"] = (df["Total_Sales_INR"] + 1).apply(np.log)
    return df

df = load_data()


st.title("Amazon Diwali Sales 2025 Dashboard")
st.write("Interactive exploration of sales, ratings, payments, and seasonal patterns.")

st.sidebar.header("Filters")

# Sidebar Filters
categories = st.sidebar.multiselect(
    "Filter by Product Category",
    df["Product_Category"].unique(),
    df["Product_Category"].unique())

states = st.sidebar.multiselect(
    "Filter by State",
    df["State"].unique(),
    df["State"].unique())

payment_methods = st.sidebar.multiselect(
    "Filter by Payment Method",
    df["Payment_Method"].unique(),
    df["Payment_Method"].unique())

filtered = df[
    (df["Product_Category"].isin(categories)) &
    (df["State"].isin(states)) &
    (df["Payment_Method"].isin(payment_methods))]


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Revenue (INR)",
        f"{filtered['Total_Sales_INR'].sum():,.0f}")
with col2:
    st.metric(
        "Avg. Rating",
        f"{filtered['Review_Rating'].mean():.2f}")
with col3:
    st.metric(
        "Delivery Success Rate",
        f"{filtered['Delivered_Flag'].mean() * 100:.1f}%")

st.markdown("---")

# RQ1: Sales by Category
st.header("RQ1: Sales by Product Category")

cat_sales = (
    filtered.groupby("Product_Category")["Total_Sales_INR"]
    .sum()
    .reset_index()
    .sort_values(by="Total_Sales_INR", ascending=False))

fig1 = px.bar(
    cat_sales,
    x="Product_Category",
    y="Total_Sales_INR",
    title="Total Sales by Category",
    text_auto=True)

st.plotly_chart(fig1, use_container_width=True)


# RQ2: Ratings & Delivery Behavior
st.header("RQ2: Ratings & Customer Behavior")

rating_fig = px.box(
    filtered,
    x="Delivery_Status",
    y="Review_Rating",
    title="Rating Distribution by Delivery Status")

st.plotly_chart(rating_fig, use_container_width=True)

# RQ3: Payment Method Impact
st.header("RQ3: Payment Method Revenue Impact")

pay_sales = (
    filtered.groupby("Payment_Method")["Total_Sales_INR"]
    .sum()
    .reset_index())

pay_fig = px.bar(
    pay_sales,
    x="Payment_Method",
    y="Total_Sales_INR",
    title="Revenue by Payment Method",
    text_auto=True)

st.plotly_chart(pay_fig, use_container_width=True)


# RQ4: Monthly Trend Analysis
st.header("RQ4: Monthly Revenue Trend")

monthly_sales = (
    filtered.groupby("Month_Name")["Total_Sales_INR"]
    .sum()
    .reset_index())


month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthly_sales["Month_Name"] = pd.Categorical(monthly_sales["Month_Name"], categories=month_order, ordered=True)
monthly_sales = monthly_sales.sort_values("Month_Name")

monthly_fig = px.line(
    monthly_sales,
    x="Month_Name",
    y="Total_Sales_INR",
    markers=True,
    title="Monthly Revenue Trend (2025)")

st.plotly_chart(monthly_fig, use_container_width=True)

