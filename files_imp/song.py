# albums = {}

# n = int(input("Enter the number of genres: "))

# for i in range(1, n + 1):
#     print(f"\nEnter details for record {i}")

#     genre = input("Enter genre: ")
#     formats = input("Enter formats (comma separated): ").split(",")
#     artist = input("Enter bestselling artist: ")
#     stock = int(input("Enter total albums in stock: "))

#     albums[i] = {
#         "genre": genre,
#         "formats": formats,
#         "artist": artist,
#         "stock": stock
#     }

# ---------- DATA ORGANIZATION ----------
albums = {
    "Rock": {
        "formats": ["Vinyl", "CD", "Digital"],
        "artist": "Led Zeppelin",
        "stock": 450
    },
    "Pop": {
        "formats": ["CD", "Digital", "Cassette"],
        "artist": "Taylor Swift",
        "stock": 620
    },
    "Jazz": {
        "formats": ["Vinyl", "CD"],
        "artist": "Miles Davis",
        "stock": 310
    },
    "Hip-Hop": {
        "formats": ["Digital", "CD"],
        "artist": "Kendrick Lamar",
        "stock": 580
    },
    "Electronic": {
        "formats": ["Digital", "Vinyl"],
        "artist": "Daft Punk",
        "stock": 490
    }
}

# ---------- TASK 1 ----------
# Identify the genre with the highest stock
def highest_stock_genre(albums):
    max_stock = 0
    max_genre = None
    for genre in albums:
        if albums[genre]["stock"] > max_stock:
            max_stock = albums[genre]["stock"]
            max_genre = genre
    return max_genre

# ---------- TASK 2 ----------
# Create a set of all album formats
def all_album_formats(albums):
    formats_set = set()
    for genre in albums:
        for fmt in albums[genre]["formats"]:
            formats_set.add(fmt)
    return formats_set

# ---------- TASK 3 ----------
# List genres by given format
def genres_by_format(albums, format_name):
    result = []
    for genre in albums:
        if format_name in albums[genre]["formats"]:
            result.append(genre)
    return result

# ---------- TASK 4 ----------
# Count number of formats for a given genre
def count_formats(albums, genre_name):
    if genre_name in albums:
        return len(albums[genre_name]["formats"])
    else:
        return "Genre not found"

# ---------- TASK 5 ----------
# List artists whose genre has stock less than 500
def artists_below_500(albums):
    result = []
    for genre in albums:
        if albums[genre]["stock"] < 500:
            result.append(albums[genre]["artist"])
    return result

# ---------- OUTPUT ----------
print("1. Genre with highest stock:", highest_stock_genre(albums))
print("2. Set of all album formats:", all_album_formats(albums))

fmt = input("3. Enter a format to search: ")
print("   Genres offering", fmt, ":", genres_by_format(albums, fmt))

genre_input = input("4. Enter a genre to count formats: ")
print("   Number of formats:", count_formats(albums, genre_input))

print("5. Artists with stock less than 500:", artists_below_500(albums))
