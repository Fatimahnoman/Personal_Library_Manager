# 📚 Personal Library Manager

A powerful Python application to manage your personal book collection with features like tracking, searching, statistics, and interactive visualizations!

## ✨ Features

### 📖 Book Management
- **Add Books** - Store title, author, year, genre, and read status
- **View Library** - Display all books in a formatted table
- **Search Books** - Find books by title, author, or genre
- **Update Status** - Mark books as read/unread
- **Remove Books** - Delete books from your collection

### 📊 Statistics & Analytics
- **Library Statistics** - Total books, read/unread counts
- **Genre Distribution** - See which genres you read most
- **Reading Progress** - Track your reading habits

### 📈 Interactive Visualizations
- **Pie Chart** - Genre distribution visualization
- **Bar Chart** - Books per genre comparison
- **Reading Status Chart** - Read vs unread overview

### 💾 Data Persistence
- **JSON Storage** - All data saved locally
- **Auto-save** - Changes saved automatically
- **Data Integrity** - Safe and reliable storage

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- No external dependencies required!

### Installation
```bash
# Clone the repository
git clone https://github.com/Fatimahnoman/Personal_Library_Manager.git

# Navigate to the directory
cd Personal_Library_Manager

# Run the application
python library_manager.py
```

## 📋 How to Use

### 1. Launch the Application
```bash
python library_manager.py
```

### 2. Main Menu Options
- **Add Book** - Add a new book to your library
- **View All Books** - Display your entire collection
- **Search Books** - Find specific books
- **Update Read Status** - Mark books as read/unread
- **Remove Book** - Delete books from library
- **Show Statistics** - View reading statistics
- **Visualize Data** - Create interactive charts
- **Exit** - Save and close application

### 3. Book Information
Each book stores:
- 📖 Title
- ✍️ Author
- 📅 Publication Year
- 🎭 Genre
- ✅ Read Status (Read/Unread)

## 📊 Visualization Features

The application creates three interactive charts:

1. **Genre Distribution Pie Chart** - See which genres dominate your library
2. **Books per Genre Bar Chart** - Compare book counts across genres
3. **Reading Status Chart** - Visualize your reading progress

## 🛠️ Technical Details

### File Structure
```
Personal_Library_Manager/
├── library_manager.py    # Main application
├── library.json         # Book database
├── requirements.txt     # Dependencies
└── README.md           # Documentation
```

### Data Storage
- Books stored in `library.json`
- Auto-saves after each operation
- JSON format for easy reading/editing

## 🎯 Example Usage

```
=== Personal Library Manager ===
1. Add Book
2. View All Books
3. Search Books
4. Update Read Status
5. Remove Book
6. Show Statistics
7. Visualize Data
8. Exit

Enter your choice: 1

Enter book title: The Great Gatsby
Enter author: F. Scott Fitzgerald
Enter publication year: 1925
Enter genre: Classic
Have you read this book? (yes/no): yes

Book added successfully!
```

## 📈 Statistics Example

```
Library Statistics:
Total books: 15
Read books: 10
Unread books: 5
Reading progress: 66.67%

Books per genre:
- Classic: 3
- Mystery: 4
- Sci-Fi: 2
- Romance: 6
```

## 🔧 Customization

Easy to extend with new features:
- Add more book fields (rating, pages, etc.)
- Create new chart types
- Export to different formats
- Add book recommendations

## 🤝 Contributing

Feel free to fork and contribute! Some ideas:
- Add book cover images
- Implement reading dates tracking
- Create reading goals
- Add book series support
- Export to CSV/Excel

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Reading!** 📖✨