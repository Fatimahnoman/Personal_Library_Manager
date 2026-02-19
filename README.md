# 📚 Personal Library Manager

A modern, web-based Python application to manage your personal book collection with an intuitive interface, interactive visualizations, and powerful features!

## ✨ Features

### 📖 Book Management
- **Add Books** - Store title, author, year, genre, and read status
- **View Library** - Display all books in an attractive card layout
- **Search Books** - Find books by title, author, or genre
- **Update Status** - Toggle read/unread status with a click
- **Remove Books** - Delete books from your collection

### 📊 Statistics & Analytics
- **Library Statistics** - Total books, read/unread counts, reading percentage
- **Genre Distribution** - Visual breakdown of your reading preferences
- **Author Statistics** - See your most-read authors
- **Decade Analysis** - Track books by publication decade

### 📈 Interactive Visualizations
- **Read Status Pie Chart** - Beautiful donut chart showing read vs unread
- **Genre Distribution Bar Chart** - Color-coded genre comparison
- **Publication Timeline** - Line chart showing books by decade

### 💾 Data Persistence
- **JSON Storage** - All data saved locally in `library.json`
- **Auto-save** - Changes saved automatically after each operation
- **Session Management** - Persistent data across app restarts

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation
```bash
# Clone the repository
git clone https://github.com/Fatimahnoman/Personal_Library_Manager.git

# Navigate to the directory
cd Personal_Library_Manager

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run library_manager.py
```

## 📋 How to Use

### 1. Launch the Application
```bash
streamlit run library_manager.py
```
The app will open in your default web browser at `http://localhost:8501`

### 2. Navigation Sidebar
- **View Library** - Browse your entire book collection
- **Add Book** - Add new books via a form
- **Search Books** - Find specific books
- **Library Statistics** - View analytics and charts

### 3. Adding a Book
1. Click "Add Book" in the sidebar
2. Fill in the book details:
   - Title (required)
   - Author (required)
   - Publication Year
   - Genre (dropdown selection)
   - Read Status
3. Click "Add Book" button
4. Success message and celebration animation!

### 4. Managing Your Library
- Each book displays in an attractive card format
- Toggle read/unread status with the button
- Remove books with the "Remove" button
- All changes auto-save to your library

### 5. Search Functionality
- Search by Title, Author, or Genre
- Instant results displayed in real-time
- Case-insensitive search

### 6. Statistics & Visualizations
- View comprehensive library statistics
- Interactive charts update automatically
- Track your reading progress over time

## 📊 Data Structure

Each book contains:
```json
{
    "title": "Book Title",
    "author": "Author Name",
    "publication_year": 2023,
    "genre": "Fiction",
    "read_status": true,
    "added_date": "2025-02-19 12:00:00"
}
```

## 🎨 User Interface

### Modern Design Features
- Clean, responsive layout
- Beautiful color scheme
- Hover effects and animations
- Success/warning messages
- Celebration animations for actions
- Loading spinners for better UX

### Sidebar Navigation
- Intuitive menu system
- Lottie animation for visual appeal
- Always-visible navigation

## 🛠️ Technical Details

### File Structure
```
Personal_Library_Manager/
├── library_manager.py    # Main Streamlit application
├── library.json         # Book database (auto-created)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Dependencies
- **Streamlit** - Web framework for the UI
- **Pandas** - Data manipulation for statistics
- **Plotly** - Interactive visualizations
- **Streamlit-Lottie** - Animated icons
- **Requests** - HTTP library for animations

### Key Functions
- `load_library()` - Loads books from JSON file
- `save_library()` - Saves books to JSON file
- `add_book()` - Adds a new book to the library
- `remove_book()` - Removes a book by index
- `search_books()` - Searches books by criteria
- `get_library_stats()` - Calculates statistics
- `create_visualizations()` - Generates charts

## 🎯 Example Usage

### Adding Your First Book
1. Launch the app with `streamlit run library_manager.py`
2. Click "Add Book" in the sidebar
3. Enter:
   - Title: "The Great Gatsby"
   - Author: "F. Scott Fitzgerald"
   - Year: 1925
   - Genre: "Classic"
   - Status: "Read"
4. Click "Add Book" and see the success animation!

### Viewing Statistics
1. Add several books to your library
2. Click "Library Statistics" in the sidebar
3. View:
   - Total book count
   - Read/unread metrics
   - Interactive charts
   - Top authors list

## 🔧 Customization

Easy to extend with new features:
- Add book ratings or reviews
- Implement reading dates tracking
- Create reading goals
- Add book cover images
- Export to CSV/Excel
- Add user authentication
- Implement book recommendations

## 🤝 Contributing

Feel free to fork and contribute! Some ideas:
- Add dark mode support
- Implement book series tracking
- Create reading challenges
- Add note-taking functionality
- Integrate with book APIs (Google Books, Goodreads)

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Reading!** 📖✨