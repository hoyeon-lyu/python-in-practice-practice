n = int(input())

playlist = []
for _ in range(n):
    parts = input().split(" ")
    if len(parts) == 0:
        print("Nothing detected.")
        continue
    elif len(parts) == 1:
        cmd = parts[0]
    elif len(parts) == 2:
        cmd = parts[0]
        song = parts[1]
    else:
        print("Too many params detected or something went wrong.")
        continue

    if cmd == "add":
        if not len(parts) == 2:
            print("There's no song or too many songs.")
            continue
        playlist.append(song)
    elif cmd == "first":
        if not len(parts) == 2:
            print("There's no song or too many songs.")
            continue
        playlist.insert(0, song)
    elif cmd == "next":
        if not len(parts) == 1:
            print("\"next\" command must not take a param.")
            continue

        if len(playlist) == 0:
            print("play: -")
        else:
            song_next = playlist.pop(0)
            print(f"play: {song_next}")
    elif cmd == "drop":
        if not len(parts) == 2:
            print("There's no song or too many songs.")
            continue

        if not song in playlist:
            print(f"not found: {song}")
            continue

        for i in range(len(playlist)):
            if playlist[i] == song:
                playlist.pop(i)
                break
    elif cmd == "list":
        if not len(parts) == 1:
            print("\"list\" command must not take a param.")
            continue

        if len(playlist) == 0:
            print("(empty)")
        else:
            print(", ".join(playlist))
    else:
        print("command error")
        continue