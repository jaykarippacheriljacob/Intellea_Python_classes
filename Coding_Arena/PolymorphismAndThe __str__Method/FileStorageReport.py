""" 
    File Storage Report
    Medium
    Polymorphism and __str__
    Implement three separate classes (no parent class), each with size_kb() and __str__(), and two functions.

    TextFile(name, characters): size_kb() is (characters + 999) // 1000. Text: [TEXT] <name>: <size> KB.
    Photo(name, width, height): size_kb() is width * height * 3 // 1000. Text: "[PHOTO] <name> (<width>x<height>): <size> KB".
    Video(name, seconds, quality): size_kb() is seconds * 500 for HD and seconds * 200 for SD. Text: "[VIDEO] <name> (<seconds>s <quality>): <size> KB".
    total_kb(files) returns the sum of size_kb() of all files.
    largest(files) returns the file with the biggest size_kb(), the first on a tie.
    storage_report is already written and uses your code.

    Parameters

    files: list of tuples: (text, name, characters), (photo, name, width, height) or (video, name, seconds, quality)
    Returns

    A list [lines, total, largest]: lines is str(file) for each file in order, total is total_kb(files) and largest is the str() text of largest(files).

    Examples

    Arguments: [('text', 'notes.txt', 4500), ('photo', 'trip.jpg', 1920, 1080), ('video', 'demo.mp4', 30, 'HD'), ('video', 'clip.mp4', 20, 'SD')]
    Returns: [['[TEXT] notes.txt: 5 KB', '[PHOTO] trip.jpg (1920x1080): 6220 KB', '[VIDEO] demo.mp4 (30s HD): 15000 KB', '[VIDEO] clip.mp4 (20s SD): 4000 KB'], 25225, '[VIDEO] demo.mp4 (30s HD): 15000 KB']
    Explanation: 4500 characters round up to 5 KB, the photo is 1920 * 1080 * 3 // 1000 = 6220 KB, and the videos are 30 * 500 = 15000 KB and 20 * 200 = 4000 KB. The total is 25225 KB and demo.mp4 is the largest.
    Constraints

    1 <= number of files <= 20
    File names can have spaces and symbols
    0 <= characters <= 1000000
    1 <= width, height <= 5000 and 1 <= seconds <= 10000
    total_kb and largest must only call size_kb(), never check the kind of file
 """

class TextFile:
    def __init__(self, name, characters):
        # Store the file name and its character count
        self.name = name
        self.characters = characters

    def size_kb(self):
        # Characters / 1000, rounded UP (adding 999 before // pushes any remainder to the next KB)
        return (self.characters + 999) // 1000

        # Alternative using the math module:
        # return math.ceil(self.characters / 1000)

    def __str__(self):
        # e.g. "[TEXT] notes: 3 KB"
        return f"[TEXT] {self.name}: {self.size_kb()} KB"


class Photo:
    def __init__(self, name, width, height):
        # Store the file name and its pixel dimensions
        self.name = name
        self.width = width
        self.height = height

    def size_kb(self):
        # 3 bytes per pixel, converted to KB and floored
        return self.width * self.height * 3 // 1000

    def __str__(self):
        # e.g. "[PHOTO] beach (800x600): 1440 KB"
        return f"[PHOTO] {self.name} ({self.width}x{self.height}): {self.size_kb()} KB"


class Video:
    def __init__(self, name, seconds, quality):
        # Store the file name, length and quality (HD or SD)
        self.name = name
        self.seconds = seconds
        self.quality = quality

    def size_kb(self):
        # HD uses 500 KB per second, SD uses 200 KB per second
        if self.quality == "HD":
            return self.seconds * 500
        elif self.quality == "SD":
            return self.seconds * 200

        # Shorter alternative using a conditional expression:
        # return self.seconds * (500 if self.quality == "HD" else 200)

    def __str__(self):
        # e.g. "[VIDEO] clip (10s HD): 5000 KB"
        return f"[VIDEO] {self.name} ({self.seconds}s {self.quality}): {self.size_kb()} KB"


def total_kb(files):
    # Add up the size of every file; each class has its own size_kb() (polymorphism)
    total = 0
    for f in files:
        total += f.size_kb()
    return total

    # Shorter alternative using sum() with a generator expression:
    # return sum(f.size_kb() for f in files)


def largest(files):
    # File object with the biggest size; max() keeps the first one on a tie
    return max(files, key = lambda f:f.size_kb())


# Do not change the code below
def storage_report(files):
    items = []
    for entry in files:
        if entry[0] == "text":
            items.append(TextFile(entry[1], entry[2]))
        elif entry[0] == "photo":
            items.append(Photo(entry[1], entry[2], entry[3]))
        else:
            items.append(Video(entry[1], entry[2], entry[3]))
    lines = []
    for item in items:
        lines.append(str(item))
    return [lines, total_kb(items), str(largest(items))]


# Test cases
print(storage_report([("text", "notes", 2500), ("photo", "beach", 800, 600), ("video", "clip", 10, "HD")]))
# Output: [['[TEXT] notes: 3 KB', '[PHOTO] beach (800x600): 1440 KB', '[VIDEO] clip (10s HD): 5000 KB'], 6443, '[VIDEO] clip (10s HD): 5000 KB']
print(storage_report([("text", "a", 1000), ("text", "b", 1001)]))
# Output: [['[TEXT] a: 1 KB', '[TEXT] b: 2 KB'], 3, '[TEXT] b: 2 KB']   (exactly 1000 → 1 KB, 1001 → rounds up to 2)
print(storage_report([("video", "x", 5, "SD"), ("photo", "p", 1000, 1000)]))
# Output: [['[VIDEO] x (5s SD): 1000 KB', '[PHOTO] p (1000x1000): 3000 KB'], 4000, '[PHOTO] p (1000x1000): 3000 KB']
print(storage_report([("text", "empty", 0)]))
# Output: [['[TEXT] empty: 0 KB'], 0, '[TEXT] empty: 0 KB']
