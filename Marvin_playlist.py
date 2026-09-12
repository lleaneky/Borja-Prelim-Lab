class Song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return (f"Song ID: {self.song_id}\n"
                f"Song Title: {self.title}\n"
                f"Artist: {self.artist}\n"
                f"Duration: {self.duration}")


class Node:
    def __init__(self, song):
        self.data = song
        self.next = None


class PlaylistLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_first(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.count += 1

    def insert_at(self, position, song):
        if position < 1 or position > self.count + 1:
            return False

        if position == 1:
            self.insert_first(song)
            return True

        new_node = Node(song)
        current = self.head

        for _ in range(position - 2):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1
        return True

    def search(self, song_id):
        current = self.head
        while current is not None:
            if current.data.song_id.lower() == song_id.lower():
                return current.data
            current = current.next
        return None

    def delete(self, song_id):
        if self.head is None:
            return False

        if self.head.data.song_id.lower() == song_id.lower():
            self.head = self.head.next
            self.count -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.data.song_id.lower() == song_id.lower():
                current.next = current.next.next
                self.count -= 1
                return True
            current = current.next

        return False

    def is_empty(self):
        return self.head is None

    def display(self):
        if self.is_empty():
            print("Playlist is empty.")
            return

        current = self.head
        position = 1
        while current is not None:
            print("---------------------------")
            print(f"Position {position}:")
            print(current.data)
            current = current.next
            position += 1

        print("---------------------------")
        print(f"Total songs: {self.count}")


def read_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.lstrip("-").isdigit():
            return int(value)
        print("Invalid input. Please enter a number.")


def prompt_for_new_song():
    song_id = input("Enter Song ID: ").strip()
    title = input("Enter Song Title: ").strip()
    artist = input("Enter Artist: ").strip()
    duration = input("Enter Duration (e.g. 4:23): ").strip()
    return Song(song_id, title, artist, duration)


def print_menu():
    print("================================")
    print("      MUSIC PLAYLIST MANAGER")
    print("================================")
    print("1. Add Song at Beginning")
    print("2. Add Song at End")
    print("3. Insert Song at Position")
    print("4. Display Playlist")
    print("5. Search Song")
    print("6. Remove Song")
    print("7. Display Playlist Size")
    print("8. Exit")


def add_song(playlist, at_beginning):
    song = prompt_for_new_song()

    if playlist.search(song.song_id) is not None:
        print("A song with that ID already exists.")
        return

    if at_beginning:
        playlist.insert_first(song)
    else:
        playlist.insert_last(song)

    print("Song added successfully.")


def insert_song_at_position(playlist):
    position = read_int("Enter position to insert at: ")
    song = prompt_for_new_song()

    if playlist.search(song.song_id) is not None:
        print("A song with that ID already exists.")
        return

    success = playlist.insert_at(position, song)
    print("Song inserted successfully." if success else "Invalid position.")


def search_song(playlist):
    song_id = input("Enter Song ID to search: ").strip()
    found = playlist.search(song_id)
    print(found if found is not None else "Song not found.")


def remove_song(playlist):
    song_id = input("Enter Song ID to remove: ").strip()
    removed = playlist.delete(song_id)
    print("Song removed successfully." if removed else "Song not found.")


def main():
    playlist = PlaylistLinkedList()

    while True:
        print_menu()
        choice = read_int("Enter your choice: ")

        if choice == 1:
            add_song(playlist, at_beginning=True)
        elif choice == 2:
            add_song(playlist, at_beginning=False)
        elif choice == 3:
            insert_song_at_position(playlist)
        elif choice == 4:
            playlist.display()
        elif choice == 5:
            search_song(playlist)
        elif choice == 6:
            remove_song(playlist)
        elif choice == 7:
            print(f"Total songs: {playlist.count}")
        elif choice == 8:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

        print()


if __name__ == "__main__":
    main()
