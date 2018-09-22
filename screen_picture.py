#!/usr/bin/env python
#coding:utf8
import os
import random
import datetime
from PIL import Image,ImageDraw,ImageFont


class ScreenPicture:
    def __init__(self):
        self.rgb_choice = [
            (84,76,6),     (189,207,97),  (159,205,113), (245,244,229), (3,163,188),
            (2,72,93),     (12,90,68),    (51,135,87),   (133,183,105), (229,225,225),
            (250,118,52),  (89,117,77),   (153,190,28),  (232,237,208), (255,148,61),
            (105,100,80),  (107,147,98),  (80,82,42),    (149,90,50),   (196,213,169),
            (235,233,181), (123,150,105), (29,107,85),   (158,217,166), (213,235,203),
            (205,225,220), (129,190,161), (30,150,140),  (69,204,180),  (107,207,237),
            (212,171,219), (141,190,147), (67,108,57),   (117,170,107), (225,237,156),
            (242,73,95),   (0,152,84),    (24,99,69),    (113,207,151), (194,225,199),
            (243,245,232), (41,145,47),   (187,217,162), (175,230,206), (74,63,68),
            (247,109,133), (253,210,213), (121,193,102), (70,140,0),    (133,174,83),
            (187,225,154), (142,212,197), (229,237,245), (123,174,87),  (180,220,167),
            (232,229,160), (108,74,28),   (59,61,60),    (132,189,0),   (6,120,0),
            (191,222,122), (245,245,211), (138,117,96),  (127,129,0),   (167,162,94),
            (188,206,113), (255,201,98),  (147,199,201), (99,104,104),  (173,186,81),
            (90,136,0),    (242,251,209), (142,102,60),  (55,51,39),    (153,184,85),
            (67,89,5),     (205,232,26),  (163,211,235), (209,222,203), (164,201,100),
            (91,143,76),   (221,233,144), (249,250,213), (92,185,192),  (186,209,150),
            (235,243,221), (48,177,209),  (91,182,133),  (7,86,84),     (198,212,153),
            (118,128,74),  (177,195,105), (227,227,227), (139,127,124), (227,180,93),
            (209,222,76),  (139,171,101), (203,219,151), (220,217,214), (96,105,85),
            (227,229,72),  (173,160,14),  (202,227,192), (245,235,220), (92,86,76),
            (0,63,142),    (4,66,79),     (82,181,217),  (138,205,213), (216,224,230),
            (4,147,200),   (23,81,160),   (79,197,222),  (199,197,189), (235,241,247),
            (35,206,255),  (34,80,113),   (219,251,255), (239,225,197), (255,97,171),
            (0,164,180),   (21,80,98),    (57,171,148),  (194,154,1),   (93,37,99),
            (46,172,197),  (94,224,210),  (252,240,96),  (242,169,208), (50,98,176),
            (0,155,159),   (25,106,106),  (80,189,171),  (150,209,187), (217,233,231),
            (180,232,221), (140,187,187), (225,245,221), (229,231,230), (237,190,202),
            (152,195,206), (88,159,205),  (239,254,209), (187,227,197), (252,215,111),
            (255,158,109), (139,162,210), (75,66,110),   (151,194,194), (230,227,198),
            (206,171,201), (190,160,200), (249,221,240), (219,120,198), (104,60,156),
            (193,222,93),  (238,234,242), (226,225,87),  (132,161,209), (163,185,160),
            (105,112,53),  (249,242,224), (202,199,195), (200,183,150), (172,211,232),
            (131,140,145), (255,255,240), (20,21,16),    (105,105,105), (180,184,175),
            (235,234,223), (246,245,244), (244,236,235), (234,230,226), (205,203,207),
            (240,210,192), (77,42,74),    (150,68,143),  (228,221,232), (149,174,76),
            (218,207,86),  (82,78,77),    (69,64,64),    (133,142,145), (201,206,205),
            (249,108,62),  (112,139,151), (39,62,95),    (160,164,169), (224,226,232),
            (227,206,175),]

    def __days_used_this_year(self):
        year = datetime.date.today().year
        first_day_this_year = datetime.date(year=year, month=1, day=1)
        today = datetime.date.today()
        days_used = (today - first_day_this_year).days
        return days_used

    def __days_left_this_year(self):
        year = datetime.date.today().year
        last_day_this_year = datetime.date(year=year, month=12, day=31)
        today = datetime.date.today()
        days_left = (last_day_this_year - today).days
        return days_left

    def __days_this_year(self): 
        year = datetime.date.today().year
        last_day_this_year = datetime.date(year=year, month=12, day=31)
        first_day_this_year = datetime.date(year=year, month=1, day=1)
        all_days = (last_day_this_year - first_day_this_year).days
        return all_days

    def __days_used_percent(self):
        days_used = self.__days_used_this_year()
        all_days = self.__days_this_year()
        return days_used * 1.0 / all_days

    def __days_left_percent(self):
        days_left = self.__days_left_this_year()
        all_days = self.__days_this_year()
        return days_left * 1.0 / all_days

    def create_picture(self, picture_dir=None, width=2560, height=1600):
        if picture_dir is None:
            picture_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pictures")
            if not os.path.isdir(picture_dir):
                os.makedirs(picture_dir)   
        picture_file = os.path.join(picture_dir, "be_careful_your_time.png")

        left_days_percent = self.__days_left_percent()
        left_days = self.__days_left_this_year()

        background_image = Image.new("RGB", (width, height), random.choice(self.rgb_choice))
        draw = ImageDraw.Draw(background_image)
        content = u"今天是%s，你的%s年只剩下了%d天，可用量为%.2f%%" % (datetime.date.today(), datetime.date.today().year, left_days, left_days_percent * 100)
        fnt = ImageFont.truetype('Songti.ttc', 80)

        content_width, content_height = fnt.getsize(content)
        draw.text(((width - content_width)/2, (height - content_height)/2 - random.randint(-300,300)), content, font=fnt, fill=(255,255,255,128))
        #background_image.show()

        background_image.save(picture_file, 'png')


if __name__ == "__main__":
    screen_picture = ScreenPicture()
    screen_picture.create_picture()
