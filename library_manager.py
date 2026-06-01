import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime
import time
import plotly.express as px
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests

# Set page configuration
st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Custom CSS for Premium UI
st.markdown("""
<style>
    /* Main Background and Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.8) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem !important;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    
    .sub-text {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 3rem;
    }

    /* Glassmorphism Cards */
    .book-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 1.25rem;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .book-card:hover {
        transform: translateY(-8px);
        border-color: rgba(56, 189, 248, 0.5);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    
    .book-title {
        color: #f8fafc;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .book-info {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-bottom: 0.2rem;
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        margin-top: 0.75rem;
    }
    
    .badge-read {
        background-color: rgba(16, 185, 129, 0.2);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    
    .badge-unread {
        background-color: rgba(244, 63, 94, 0.2);
        color: #fb7185;
        border: 1px solid rgba(244, 63, 94, 0.3);
    }

    /* Form and Inputs */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stNumberInput>div>div>input {
        background-color: rgba(15, 23, 42, 0.5) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 0.5rem !important;
    }
    
    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 0.75rem !important;
        font-weight: 600 !important;
        transition: all 0.2s !important;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
    }

    /* Metric Boxes */
    [data-testid="stMetricValue"] {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: #38bdf8 !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'library' not in st.session_state:
    st.session_state.library = []
if 'search_results' not in st.session_state:
    st.session_state.search_results = []
if 'book_added' not in st.session_state:
    st.session_state.book_added = False
if 'book_removed' not in st.session_state:
    st.session_state.book_removed = False

# Load library data from file
def load_library():
    try:
        if os.path.exists('library.json'):
            with open('library.json', 'r') as file:
                st.session_state.library = json.load(file)
            return True
        return False
    except Exception as e:
        st.error(f"Error loading library: {e}")
        return False

# Save library data to file
def save_library():
    try:
        with open('library.json', 'w') as file:
            json.dump(st.session_state.library, file)
        return True
    except Exception as e:
        st.error(f"Error saving library: {e}")
        return False

# Add a book
def add_book(title, author, publication_year, genre, read_status):
    book = {
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read_status': read_status,
        'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.library.append(book)
    save_library()
    st.session_state.book_added = True

# Remove a book
def remove_book(index):
    if 0 <= index < len(st.session_state.library):
        del st.session_state.library[index]
        save_library()
        st.session_state.book_removed = True
        return True
    return False

# Load data
load_library()

# Sidebar
with st.sidebar:
    lottie_book = load_lottieurl("https://assets9.lottiefiles.com/temp/lf20_aKAfIn.json")
    if lottie_book:
        st_lottie(lottie_book, height=150)
    
    st.markdown("### 🧭 MENU")
    nav = st.radio("Navigation", ["📚 View Library", "➕ Add New Book", "🔍 Search", "📊 Stats"], label_visibility="collapsed")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Tip")
    st.info("Keep your library updated to track your reading progress effectively!")

# Main Header
st.markdown("<h1 class='main-header'>Library Manager</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-text'>Your digital sanctuary for curated knowledge and stories.</p>", unsafe_allow_html=True)

# Navigation Views
if nav == "📚 View Library":
    if not st.session_state.library:
        st.warning("Your library is empty. Start adding some books!")
    else:
        # Search & Filter Bar for the view
        col_search, col_filter = st.columns([2, 1])
        with col_search:
            view_search = st.text_input("Search library...", placeholder="Type title or author...")
        
        filtered_library = st.session_state.library
        if view_search:
            filtered_library = [b for b in st.session_state.library if view_search.lower() in b['title'].lower() or view_search.lower() in b['author'].lower()]

        # Display Grid
        cols = st.columns(3)
        for i, book in enumerate(filtered_library):
            with cols[i % 3]:
                badge_class = "badge-read" if book['read_status'] else "badge-unread"
                badge_text = "Read" if book['read_status'] else "Unread"
                
                st.markdown(f"""
                <div class='book-card'>
                    <div class='book-title'>{book['title']}</div>
                    <div class='book-info'>✍️ {book['author']}</div>
                    <div class='book-info'>📅 {book['publication_year']}</div>
                    <div class='book-info'>🏷️ {book['genre']}</div>
                    <div class='badge {badge_class}'>{badge_text}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Buttons underneath the card
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    status_label = "✅ Read" if not book['read_status'] else "📖 Unread"
                    if st.button(status_label, key=f"stat_{i}"):
                        book['read_status'] = not book['read_status']
                        save_library()
                        st.rerun()
                with btn_col2:
                    if st.button("🗑️ Delete", key=f"del_{i}"):
                        st.session_state.library.remove(book)
                        save_library()
                        st.rerun()

elif nav == "➕ Add New Book":
    st.markdown("### ✍️ Add to Collection")
    with st.container():
        with st.form("add_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                t = st.text_input("Book Title*")
                a = st.text_input("Author Name*")
            with c2:
                y = st.number_input("Year", min_value=1000, max_value=2025, value=2024)
                g = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Sci-Fi", "Fantasy", "Mystery", "Biography", "History", "Other"])
            
            s = st.checkbox("I have read this book")
            sub = st.form_submit_button("✨ Add to Library")
            
            if sub:
                if t and a:
                    add_book(t, a, y, g, s)
                    st.success(f"'{t}' has been added!")
                    st.balloons()
                else:
                    st.error("Please fill in Title and Author.")

elif nav == "🔍 Search":
    st.markdown("### 🔍 Advanced Search")
    sc1, sc2 = st.columns([3, 1])
    with sc1:
        query = st.text_input("What are you looking for?", placeholder="Enter title, author or genre...")
    with sc2:
        criteria = st.selectbox("Criteria", ["Everything", "Title", "Author", "Genre"])
    
    if query:
        results = []
        for b in st.session_state.library:
            match = False
            if criteria == "Everything":
                match = query.lower() in b['title'].lower() or query.lower() in b['author'].lower() or query.lower() in b['genre'].lower()
            elif criteria == "Title": match = query.lower() in b['title'].lower()
            elif criteria == "Author": match = query.lower() in b['author'].lower()
            elif criteria == "Genre": match = query.lower() in b['genre'].lower()
            
            if match: results.append(b)
        
        if results:
            st.write(f"Found {len(results)} results")
            for r in results:
                st.info(f"**{r['title']}** by {r['author']} ({r['genre']})")
        else:
            st.warning("No matches found.")

elif nav == "📊 Stats":
    st.markdown("### 📊 Library Insights")
    if not st.session_state.library:
        st.info("No data available yet.")
    else:
        total = len(st.session_state.library)
        read = sum(1 for b in st.session_state.library if b['read_status'])
        unread = total - read
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Books", total)
        m2.metric("Read", read)
        m3.metric("Pending", unread)
        
        st.markdown("---")
        
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            # Genre Distribution
            genres = [b['genre'] for b in st.session_state.library]
            genre_counts = pd.Series(genres).value_counts()
            fig = px.pie(values=genre_counts.values, names=genre_counts.index, title="Genre Distribution", hole=0.4)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig, width='stretch')
            
        with chart_col2:
            # Read Status
            fig2 = px.bar(x=["Read", "Unread"], y=[read, unread], title="Reading Progress", color=["Read", "Unread"], color_discrete_map={"Read": "#34d399", "Unread": "#fb7185"})
            fig2.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
            st.plotly_chart(fig2, width='stretch')

# Footer
st.markdown("<br><br><div style='text-align: center; color: #64748b; font-size: 0.8rem;'>Personal Library Manager v2.0 • Designed for Bibliophiles</div>", unsafe_allow_html=True)
