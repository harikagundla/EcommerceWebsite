import streamlit as st
from products import add_product

def admin_panel():
    st.header("Admin Panel")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    category = st.selectbox("Category", ["Handmade", "Leather", "Jute"])
    image = st.text_input("Image Path (e.g., images/product1.jpg)")

    if st.button("Add Product"):
        if name and image:
            add_product(name, price, category, image)
            st.success("Product added successfully!")
        else:
            st.error("Please fill all fields")
