import json
from datetime import datetime

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def display_movies(data):
    for idx, movie in enumerate(data['movies']):
        print(f"{idx + 1}. {movie['title']}")

def display_screenings(movie_index, data):
    movie = data['movies'][movie_index]
    print(f"Screenings for '{movie['title']}':")
    for idx, screening in enumerate(movie['screenings']):
        print(f"{idx + 1}. Time: {screening['time']}")

def display_seats(movie_index, screening_index, data):
    movie = data['movies'][movie_index]
    screening = movie['screenings'][screening_index]
    print(f"Available seats for '{movie['title']}' at {screening['time']}:")
    for idx, seat in enumerate(screening['seats']):
        if not seat['reserved']:
            print(f"{idx + 1}. Seat {idx + 1} (Available)")
        else:
            print(f"{idx + 1}. Seat {idx + 1} (Reserved)")

def make_reservation(movie_index, screening_index, seat_index, data):
    movie = data['movies'][movie_index]
    screening = movie['screenings'][screening_index]
    seat = screening['seats'][seat_index]

    if not seat['reserved']:
        seat['reserved'] = True
        print(f"Reservation successful for '{movie['title']}' at {screening['time']}, Seat {seat_index + 1}")
    else:
        print(f"Seat {seat_index + 1} is already reserved. Please choose another seat.")

def add_movie(title, genre, release_date, director, duration_minutes, rating, data):
    new_movie = {
        'title': title,
        'genre': genre,
        'release_date': release_date,
        'director': director,
        'duration_minutes': duration_minutes,
        'rating': rating,
        'screenings': []
    }
    data['movies'].append(new_movie)
    print(f"Movie '{title}' added successfully.")

def add_screening(movie_index, time, seats, data):
    movie = data['movies'][movie_index]
    new_screening = {
        'time': time,
        'seats': [{'reserved': False} for _ in range(seats)]
    }
    movie['screenings'].append(new_screening)
    print(f"Screening at {time} added successfully for '{movie['title']}'.")

def main():
    file_path = 'D:\Python\Code\movie_theater_data.json'
    data = load_data(file_path)

    while True:
        print("\nMovie Theater Reservation System:")
        print("1. View Movies")
        print("2. View Screenings for a Movie")
        print("3. View Available Seats for a Screening")
        print("4. Make Reservation")
        print("5. Add Movie")
        print("6. Add Screening")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            display_movies(data)

        elif choice == '2':
            movie_index = int(input("Enter the movie index: ")) - 1
            display_screenings(movie_index, data)

        elif choice == '3':
            movie_index = int(input("Enter the movie index: ")) - 1
            screening_index = int(input("Enter the screening index: ")) - 1
            display_seats(movie_index, screening_index, data)

        elif choice == '4':
            movie_index = int(input("Enter the movie index: ")) - 1
            screening_index = int(input("Enter the screening index: ")) - 1
            seat_index = int(input("Enter the seat index: ")) - 1
            make_reservation(movie_index, screening_index, seat_index, data)

        elif choice == '5':
            title = input("Enter the movie title: ")
            genre = input("Enter the genre: ")
            release_date = input("Enter the release date (YYYY-MM-DD): ")
            director = input("Enter the director: ")
            duration_minutes = int(input("Enter the duration in minutes: "))
            rating = float(input("Enter the rating: "))
            add_movie(title, genre, release_date, director, duration_minutes, rating, data)

        elif choice == '6':
            movie_index = int(input("Enter the movie index: ")) - 1
            time = input("Enter the screening time (YYYY-MM-DDTHH:MM:SS): ")
            seats = int(input("Enter the number of seats: "))
            add_screening(movie_index, time, seats, data)

        elif choice == '7':
            save_data(file_path, data)
            print("Exiting. Data saved.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
