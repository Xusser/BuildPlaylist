# BuildPlaylist

### 0x01:参数

```
-d	指定需要生成播放列表的目录
-r	指定输出时候需要重写成的前缀
-o	指定输出的播放列表的位置
-v	显示详情
```

### 0x02:使用

##### 源目录结构

```
/path/to/Music/After All ～綴る想い～.mp3
/path/to/Music/After All～綴る想い～ '13.m4a
/path/to/Music/Another sky.mp3
/path/to/Music/Authentic symphony.mp3
/path/to/Music/BRIGHT STREAM.mp3
/path/to/Music/Be Starters!.m4a
/path/to/Music/Born to be.m4a
/path/to/Music/Brave Shine.m4a
/path/to/Music/Butter-Fly.mp3
/path/to/Music/CLICK.mp3
/path/to/Music/CiRCLING.m4a
/path/to/Music/Coloring.mp3
/path/to/Music/DAYS of DASH.mp3
/path/to/Music/Daisy.mp3
/path/to/Music/Don't say 'lazy'.mp3
/path/to/Music/ENDLESS STORY.m4a
/path/to/Music/鋼の錬金術師 FULLMETAL ALCHEMIST FINAL BEST/LET IT OUT.m4a
/path/to/Music/鋼の錬金術師 FULLMETAL ALCHEMIST FINAL BEST/Period.m4a
/path/to/Music/鋼の錬金術師 FULLMETAL ALCHEMIST FINAL BEST/RAY OF LIGHT.m4a
```

```
#/path/to/BuildPlaylist.py -d /path/to/Music -r https://example.com/Music -o /path/to/Playlist-JP.m3u8 -v
```

##### 生成播放列表

```
#EXTM3U

https://example.com/Music/After All ～綴る想い～.mp3
https://example.com/Music/After All～綴る想い～ '13.m4a
https://example.com/Music/Another sky.mp3
https://example.com/Music/Authentic symphony.mp3
https://example.com/Music/BRIGHT STREAM.mp3
https://example.com/Music/Be Starters!.m4a
https://example.com/Music/Born to be.m4a
https://example.com/Music/Brave Shine.m4a
https://example.com/Music/Butter-Fly.mp3
https://example.com/Music/CLICK.mp3
https://example.com/Music/CiRCLING.m4a
https://example.com/Music/Coloring.mp3
https://example.com/Music/DAYS of DASH.mp3
https://example.com/Music/Daisy.mp3
https://example.com/Music/Don't say 'lazy'.mp3
https://example.com/Music/ENDLESS STORY.m4a
https://example.com/Music/鋼の錬金術師 FULLMETAL ALCHEMIST FINAL BEST/LET IT OUT.m4a
https://example.com/Music/鋼の錬金術師 FULLMETAL ALCHEMIST FINAL BEST/Period.m4a
https://example.com/Music/鋼の錬金術師 FULLMETAL ALCHEMIST FINAL BEST/RAY OF LIGHT.m4a
```

