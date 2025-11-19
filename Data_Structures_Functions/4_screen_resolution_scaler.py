def scale_resolutions(resolutions, factor):
    return [(int(w * factor), int(h * factor)) for w, h in resolutions]
resolutions = [(1920, 1080), (1280, 720), (2560, 1440)]
factor = 0.5
print(scale_resolutions(resolutions, factor))
# Expected: [(960, 540), (640, 360), (1280, 720)]
