# your-left-days-this-year
create one screen protect picture that include how many days left this year

## Enveriment
python: 3.7

## Dependencies
use Pillow lib to draw picture, so you need to:
~~~shell
pip install Pillow
~~~

## Looks like:
![your will hate author finally picture](https://github.com/suisuihan/your-left-days-this-year/blob/master/resource/be_careful_your_time.png)

The default picture directory is ./your-left-days-this-year/pictures. 
### for MacOS
* If want to set the picture as screen protect picture, click "系统偏好设置 -> "桌面与屏幕保护程序", choose one style you like
* If want to create a new picture each day automaticlly, maybe your can make it with "crontab -e", my cronjob file is like:
~~~
*/5 * * * * /Users/xxxxx/.pyenv/shims/python /Users/xxxxx/code/macos-lock-screen-picture/screen_picture.py
~~~

## Maybe you want to do ... and just do it:
* change fuction ScreenPicture.create_picture parameters when your screen is not 2560 * 1600
* change var picture_dir to define your picture path
* change font
* change what to disploy

## Todo(or never):
* I don't know any knowledge about colors, so I pick some RGB info from [clickthis](http://b.xiumi.us/board/v5/251mJ/23381856), it is a bad method but it works…… Hope for your suggestion
* It does not compare the color of content you want to display with background, so sometime it looks ugly


