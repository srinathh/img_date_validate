#%%
import os
from dotenv import load_dotenv
import exif
from typing import Any
from enum import StrEnum, auto
import logging

import io
load_dotenv()
from datetime import datetime


#%%

class ExifTag(StrEnum):
    datetime = auto()
    datetime_original = auto()
    image_unique_id = auto()
    gps_latitude = auto()
    gps_longitude = auto()


#%%

class ExifValidator:

    def __init__(self, img_file: io.BinaryIO | bytes | str):
        self.img = exif.Image(img_file)

    def get_attr(self, attr:ExifTag) -> Any|None:
        try:
            ret = self.img[attr]
            return ret
        except (NotImplementedError, KeyError, AttributeError):
            return None

    def validate_datetime(self): 

        for attr in [ExifTag.datetime_original, ExifTag.datetime]:
            val = self.get_attr(attr)
            if attr == None:
                continue
            try:
                datetime.strptime(attr,"%Y:%m:%d %H:%M%SS")
                return True
            except ValueError:
                continue

        return False
            
    def validate_geotag(self):
        lat = self.get_attr(ExifTag.gps_latitude)
        long = self.get_attr(ExifTag.gps_longitude)
        if(lat != None and long != None):
            return True
        else:
            return False



#%%

img_path = os.getenv("IMG_SEARCH_PATH")
img_sample_path = os.getenv("IMG_SAMPLE_PATH_NEW")
assert img_path != None
assert img_sample_path != None


# %%
print(img_sample_path)
# %%

exif_img = exif.Image(img_sample_path)


#%%
for k in exif_img.list_all():
    try:
        print(f"{k} : {exif_img[k]}")
    except (NotImplementedError, KeyError, AttributeError):
        print(f"Error: Reading key {k} not implemented")


#%%

exif_img.datetime_original
# %%


# %%


# %%
