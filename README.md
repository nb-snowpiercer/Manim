# 安装Manim

### 任务目标

1、安装相关库文件

2、manim生成MP4动画

3、将MP4动画转换为gif文件


### 1、Ubunut 16.04.6 LTS安装Manim

- [x]  直接使用pip install manimlib命令安装，但是会有以下报错

```bash
Cannot uninstall 'pycairo'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
```

- [x]  升级manimlib的相关库文件

```bash
sudo apt-get install libcairo2-dev
sudo apt install ffmpeg
sudo apt-get install sox
sudo apt install texlive-latex-extra
```

- [x]  如果git下载manim软件时，出现无法下载的情况，可以直接访问manim的github网址，下载后直接解压zip文件

```shell
git clone https://github.com/3b1b/manim
cd manim
sudo apt install python-pip
pip install --upgrade pip
pip install -r requirements.txt -r https://pypi.tuna.tsinghua.edu.cn/simple
```

这里还是会报错，使用subl requirement.txt将pycairo两行去掉，再执行pip install -r requirement.txt命令。

- [x]  单独安装pycairo

使用以下命令强制升级就可以了。

```bash
sudo pip install pycairo --upgrade --ignore-installed pycairo 
```

- [x]  安装manim

确保在manim的目录下执行

```python
python setup.py install
```
即可完成安装了。

### 2、体验Manim

- [x] 安装完成Manim之后，运行Manim-master内置的py程序

```bash
sudo apt-get install smplayer   #安装MP4播放器
manim example_scenes.py -pl      #生成视频文件
```
- [x] 运行manim目录下的example_scenes.py文件

```python
class SquareToCircle(Scene):
    def construct(self):
       circle = Circle()#定义圆
        square = Square()#定义方形
        square.flip(RIGHT)#放置正确位置
        square.rotate(-3 * TAU / 8)#逆时针旋转3/8pi
        circle.set_fill(PINK, opacity=0.5)#背景定为粉色，不透明度0.5
        self.play(ShowCreation(square))#显示方形
        self.play(Transform(square, circle))#由方变圆
        self.play(FadeOut(square))#圆形淡出
```

- [x]  第1、2行circle = Circle()和 square = Square()其实就是定义圆形和正方形两个物体，后面使用在第3行调用flip()函数将正方形放到正确的位置上。然后调用第4行调用rotate()函数，在逆时针方向旋转3/8pi的角度。第5行调用set_fill()将圆形的填充颜色设置为粉红色，不透明度设置为0.5

```bash
manim example_scenes.py SquareToCircle -pl
```

- [x]  将mp4文件保存为gif文件

```shell
ffmpeg -i ./media/videos/example_scenes/1440p60/SquareToCircle.mp4 -filter:v "setpts=0.25*PTS" SquareToCircle.gif
```
