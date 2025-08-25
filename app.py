import streamlit as st

# Mock authentication functions (replace with actual implementations)
def register_user(username, password):
    return True

def login_user(username, password):
    return True

# Mock admin panel (replace with actual implementation)
def admin_panel():
    st.header("Admin Panel")
    st.write("Welcome to the admin dashboard")

# Products data
@st.cache_data  # Cache the product data for better performance
def load_products():
    return [
        # Bags
        {
            "id": 1,
            "name": "Handmade Jute Bag",
            "price": 599,
            "description": "Eco-friendly jute bag with traditional motifs, perfect for daily use",
            "category": "Bags",
            "image": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "discount": 10
        },
        {
            "id": 2,
            "name": "Saree Bag",
            "price": 899,
            "description": "Elegant bag made from recycled saree fabric with zari border",
            "category": "Bags",
            "image": "https://images.unsplash.com/photo-1591348122449-8af5c5d76e9b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 3,
            "name": "Leather Handbag",
            "price": 2499,
            "description": "Premium quality leather handbag with traditional embroidery",
            "category": "Bags",
            "image": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 4,
            "name": "Medical Kit Bag",
            "price": 799,
            "description": "Practical and stylish bag for medical supplies with multiple compartments",
            "category": "Bags",
            "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 5,
            "name": "Embroidered Pouch",
            "price": 349,
            "description": "Small pouch with intricate embroidery work, ideal for coins or jewelry",
            "category": "Bags",
            "image": "https://images.unsplash.com/photo-1595341595379-cf0f0f13f971?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 6,
            "name": "Jute File Folder",
            "price": 499,
            "description": "Eco-friendly file folder made from natural jute fibers",
            "category": "Bags",
            "image": "https://images.unsplash.com/photo-1583947581924-a31a1a0c9a56?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        
        # Home Decor
        {
            "id": 7,
            "name": "Block Print Bedsheet (Queen)",
            "price": 1299,
            "description": "Hand-block printed cotton bedsheet with traditional designs",
            "category": "Home Decor",
            "image": "https://images.unsplash.com/photo-1551651658-4c0aec5a99e5?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
            "discount": 15
        },
        {
            "id": 8,
            "name": "Silk Pillow Covers (Set of 2)",
            "price": 899,
            "description": "Luxurious silk pillow covers with zari border",
            "category": "Home Decor",
            "image": "https://images.unsplash.com/photo-1579656592043-20f4a1b0f467?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 9,
            "name": "Handwoven Throw Blanket",
            "price": 1799,
            "description": "Warm and cozy blanket with traditional patterns",
            "category": "Home Decor",
            "image": "https://images.unsplash.com/photo-1600189261867-8a325a6f9f8b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        # Beauty Products
        {
            "id": 11,
            "name": "Ayurvedic Face Wash",
            "price": 249,
            "description": "Natural face wash with neem and turmeric",
            "category": "Beauty",
            "image": "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 13,
            "name": "Natural Lip Balm",
            "price": 349,
            "description": "Set of 3 herbal lip balms with different flavors",
            "category": "Beauty",
            "image": "https://images.unsplash.com/photo-1625772452859-1c03d5bf1137?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        
        # Leather Goods
        {
            "id": 14,
            "name": "Leather File Folder",
            "price": 1299,
            "description": "Premium leather folder for documents",
            "category": "Leather Goods",
            "image": "https://images.unsplash.com/photo-1548032885-b5e38734688a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 15,
            "name": "Leather Wallet",
            "price": 899,
            "description": "Handcrafted leather wallet with multiple compartments",
            "category": "Leather Goods",
            "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        },
        {
            "id": 16,
            "name": "Leather Belt",
            "price": 799,
            "description": "Genuine leather belt with brass buckle",
            "category": "Leather Goods",
            "image": "https://images.unsplash.com/photo-1595341595379-cf0f0f13f971?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
        }
    ]

def show_products():
    st.header("Our Product Collection")
    
    # Add category filter
    categories = ["All", "Bags", "Home Decor", "Beauty", "Leather Goods"]
    selected_category = st.sidebar.selectbox("Filter by Category", categories)
    
    # Add price filter
    price_range = st.sidebar.slider("Price Range", 0, 5000, (100, 3000))
    
    products = load_products()
    
    # Filter products
    if selected_category != "All":
        products = [p for p in products if p['category'] == selected_category]
    products = [p for p in products if price_range[0] <= p['price'] <= price_range[1]]
    
    # Display in grid
    cols = st.columns(3)
    for idx, p in enumerate(products):
        with cols[idx % 3]:
            st.image(p["image"], width=200, use_container_width=True)
            st.subheader(p["name"])
            
            # Show price with discount if available
            if p.get('discount'):
                discounted_price = p['price'] * (1 - p['discount']/100)
                st.write(f"~~₹{p['price']}~~ **₹{discounted_price:.0f}**")
                st.success(f"{p['discount']}% OFF")
            else:
                st.write(f"**₹{p['price']}**")
                
            st.caption(p['description'])
            
            # Add to cart button - available to all users
            if st.button("Add to Cart", key=f"add_{p['id']}"):
                if "cart" not in st.session_state:
                    st.session_state.cart = []
                st.session_state.cart.append(p)
                st.success(f"Added {p['name']} to cart")
                
            st.markdown("---")

def about_us():
    st.header("About Samskruta Vahini Foundation")
    st.write("""
    Samskruta Vahini Foundation is a non-profit organization dedicated to preserving and promoting Indian heritage 
    through sustainable and traditional handicrafts. We work with artisans across India to bring you authentic, 
    handmade products that support rural livelihoods and keep our cultural traditions alive.
    
    Our store features a carefully curated collection of handmade products that blend traditional craftsmanship 
    with contemporary designs. Each purchase you make directly supports our artisans and helps preserve India's 
    rich cultural heritage.
    """)
    
    st.subheader("Our Mission")
    st.write("""
    - Empower rural artisans and women self-help groups
    - Preserve traditional Indian handicrafts
    - Promote sustainable and eco-friendly products
    - Create fair-trade opportunities for skilled craftsmen
    """)
    
    st.image("https://images.unsplash.com/photo-1600880292203-757bb62b4baf?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80", 
             caption="Our artisans at work", use_container_width=True)

def contact_us():
    st.header("Contact Us")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Get in Touch")
        st.write("""
        **Samskruta Vahini Foundation**  
        123 Heritage Road,  
        Bengaluru, Karnataka - 560001  
        India  
        
        ☎️ +91 80 2345 6789  
        ✉️ contact@samskrutavahini.org  
        
        **Working Hours:**  
        Monday - Saturday: 10 AM to 6 PM  
        Sunday: Closed
        """)
        
        st.subheader("Follow Us")
        st.write("""
        [Facebook](#) | [Instagram](#) | [Twitter](#)  
        [YouTube](#) | [Pinterest](#)
        """)
    
    with col2:
        st.subheader("Send Us a Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            phone = st.text_input("Your Phone Number")
            subject = st.selectbox("Subject", ["General Inquiry", "Product Query", "Order Issue", "Wholesale Inquiry", "Other"])
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")
            if submitted:
                st.success("Thank you for your message! We'll get back to you soon.")

def home_page():
    # Hero Section
    st.markdown("""
    <div style="background-color:#f8f9fa;padding:2rem;border-radius:10px;margin-bottom:2rem;text-align:center;">
        <h1 style="color:#2c3e50;">Celebrating India's Artisanal Heritage</h1>
        <p style="font-size:1.2rem;">Handcrafted with love by rural artisans. Every purchase supports traditional crafts and livelihoods.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Image
    # Menu Details - Side by Side
    st.header("🛍️ Explore Our Collection")
    
    menu_cols = st.columns(3)
    
    with menu_cols[0]:
        st.markdown("""
        <div style="background-color:#f8f9fa;padding:1.5rem;border-radius:10px;height:100%;">
            <h3 style="color:#2c3e50;text-align:center;">Bags & Accessories</h3>
            <p>Eco-friendly and stylish bags made from traditional materials like jute, silk, and leather.</p>
            <ul>
                <li>Handmade Jute Bags</li>
                <li>Saree Fabric Bags</li>
                <li>Embroidered Pouches</li>
                <li>Leather Wallets</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with menu_cols[1]:
        st.markdown("""
        <div style="background-color:#f8f9fa;padding:1.5rem;border-radius:10px;height:100%;">
            <h3 style="color:#2c3e50;text-align:center;">Home Decor</h3>
            <p>Beautiful home furnishings that bring traditional craftsmanship to modern living spaces.</p>
            <ul>
                <li>Block Print Bedsheets</li>
                <li>Silk Pillow Covers</li>
                <li>Handwoven Blankets</li>
                <li>Traditional Wall Art</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with menu_cols[2]:
        st.markdown("""
        <div style="background-color:#f8f9fa;padding:1.5rem;border-radius:10px;height:100%;">
            <h3 style="color:#2c3e50;text-align:center;">Beauty & Wellness</h3>
            <p>Natural products made with ancient Ayurvedic recipes and traditional techniques.</p>
            <ul>
                <li>Ayurvedic Face Wash</li>
                <li>Herbal Lip Balms</li>
                <li>Natural Soaps</li>
                <li>Essential Oils</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Featured Products
    st.header("✨ Featured Products")
    st.write("Discover our handpicked selection of artisanal treasures")
    
    featured_products = load_products()[:4]
    cols = st.columns(4)
    for idx, product in enumerate(featured_products):
        with cols[idx]:
            st.image(product["image"], use_container_width=True)
            st.write(f"**{product['name']}**")
            if product.get('discount'):
                discounted_price = product['price'] * (1 - product['discount']/100)
                st.write(f"~~₹{product['price']}~~ **₹{discounted_price:.0f}**")
                st.success(f"{product['discount']}% OFF")
            else:
                st.write(f"**₹{product['price']}**")
            if st.button("Add to Cart", key=f"home_{product['id']}"):
                if "cart" not in st.session_state:
                    st.session_state.cart = []
                st.session_state.cart.append(product)
                st.success(f"Added {product['name']} to cart")
    
    # Why Choose Us Section
    st.header("❤️ Why Choose Samskruta Vahini")
    
    why_cols = st.columns(3)
    
    with why_cols[0]:
        st.markdown("""
        <div style="text-align:center;">
            <h3>🌿 Authentic Handmade</h3>
            <p>Each product is crafted using traditional techniques passed down through generations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with why_cols[1]:
        st.markdown("""
        <div style="text-align:center;">
            <h3>🤝 Direct Impact</h3>
            <p>Your purchase directly supports artisan communities and preserves cultural heritage.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with why_cols[2]:
        st.markdown("""
        <div style="text-align:center;">
            <h3>🌱 Eco-Friendly</h3>
            <p>We use sustainable materials and natural processes to minimize environmental impact.</p>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Samskruta Vahini Store", 
        layout="wide", 
        page_icon="🛍️",
        initial_sidebar_state="expanded"
    )
    
    # Add custom CSS for better styling
    st.markdown("""
    <style>
    .stImage img {
        border-radius: 10px;
        transition: transform .2s;
    }
    .stImage img:hover {
        transform: scale(1.05);
    }
    .stButton button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #FF6B6B;
        color: white;
    }
    .about-section {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
    h1 {
        color: #2c3e50;
    }
    .menu-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        height: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    ul {
        padding-left: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🛍️ Samskruta Vahini Foundation Store")
    
    # Initialize session state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "is_admin" not in st.session_state:
        st.session_state.is_admin = False
    if "cart" not in st.session_state:
        st.session_state.cart = []

    # Navigation menu
    menu = ["Home", "Products", "About Us", "Contact Us", "Login", "Register"]
    if st.session_state.logged_in:
        menu.remove("Login")
        menu.remove("Register")
        menu.insert(0, "My Account")
    
    choice = st.sidebar.selectbox("Menu", menu)
    
    # Cart display in sidebar - available to all users
    with st.sidebar.expander("🛒 Your Cart"):
        if "cart" in st.session_state and st.session_state.cart:
            for item in st.session_state.cart:
                st.write(f"- {item['name']} (₹{item['price']})")
            st.write(f"**Total: ₹{sum(item['price'] for item in st.session_state.cart)}**")
            if st.button("Checkout"):
                if st.session_state.logged_in:
                    st.success("Order placed successfully!")
                    st.session_state.cart = []
                else:
                    st.warning("Please login to complete your purchase")
        else:
            st.write("Your cart is empty")

    # Page routing
    if choice == "Home":
        home_page()

    elif choice == "Products":
        show_products()  # Accessible to all users

    elif choice == "About Us":
        about_us()

    elif choice == "Contact Us":
        contact_us()

    elif choice == "Login":
        st.subheader("Login to Your Account")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            if submitted:
                if login_user(username,password):
                    st.session_state.logged_in = True
                    st.session_state.is_admin = (username == "admin")
                    st.success("Login successful")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    elif choice == "Register":
        st.subheader("Create New Account")
        with st.form("register_form"):
            new_username = st.text_input("New Username")
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Register")
            if submitted:
                if new_password != confirm_password:
                    st.error("Passwords don't match")
                elif register_user(new_username, new_password):
                    st.success("Account created successfully. Please login.")
                else:
                    st.error("Username already exists")

    elif choice == "My Account":
        if not st.session_state.logged_in:
            st.warning("Please login to access your account")
            return
            
        st.subheader("My Account")
        if st.session_state.is_admin:
            admin_panel()
        else:
            st.write("Welcome back to your account!")
            
            tab1, tab2, tab3 = st.tabs(["Profile", "Orders", "Settings"])
            
            with tab1:
                st.subheader("Your Profile")
                st.write("Name: John Doe")
                st.write("Email: john@example.com")
                st.write("Address: 123 Main St, Bengaluru")
                
            with tab2:
                st.subheader("Your Orders")
                if "cart" in st.session_state and st.session_state.cart:
                    for item in st.session_state.cart:
                        st.write(f"- {item['name']} (₹{item['price']})")
                else:
                    st.write("You haven't placed any orders yet.")
                
            with tab3:
                st.subheader("Account Settings")
                if st.button("Logout"):
                    st.session_state.logged_in = False
                    st.session_state.is_admin = False
                    st.session_state.cart = []
                    st.success("Logged out successfully")
                    st.rerun()

if __name__ == "__main__":
    main()