import os

from metavision.assets import VideoAssets, download_assets

if not os.path.exists("data"):
    os.makedirs("data")
os.chdir("data")
download_assets(VideoAssets.VEHICLES)
