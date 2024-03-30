n=float(input("input the width/height/depth of the perfect cube you have that is made of other smaller cubes (pls no ones) "))
if n == 0:
    print("Painted Cube Solver 0.1 beta")
    print()
    print("EyeScary development studios 2024")
elif n == 1:
    import webbrowser
    print("NO...enjoy!")
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
else:
    corners = 8
    edges = 3*4*(n-2)
    faces = 6*(n-2)*(n-2)
    hidden = (n-2)*(n-2)*(n-2)
    print("this cube contains", corners, "cubes with 3 faces painted,", edges, "cubes with 2 faces painted,", faces, "cubes with 1 face painted and", hidden, "cubes hidden with 0 faces painted")