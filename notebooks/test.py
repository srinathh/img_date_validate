#%%
import os
from dotenv import load_dotenv
import exif

load_dotenv()


#%%

img_path = os.getenv("IMG_SEARCH_PATH")
img_sample_path = os.getenv("IMG_SAMPLE_PATH")
assert img_path != None
assert img_sample_path != None


# %%
print(img_sample_path)
# %%

with open(img_sample_path, 'rb') as image_file:
    my_image = exif.Image(image_file)

my_image.has_exif

# %%

print(list(filter(lambda x: "date" in x, my_image.list_all())))

# %%
my_image["datetime"]

# %%

my_image["datetime_original"]
# %%
my_image["datetime_digitized"]
# %%
