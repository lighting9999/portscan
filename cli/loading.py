import sys
import time
import itertools

loading = True  
def show_loading_animation(style=1):
    styles = {
        1: ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],  # 旋转条
        2: ["|", "/", "-", "\\"],  # 传统的旋转条
        3: ["▁", "▃", "▄", "▆", "▇", "█", "▇", "▆", "▄", "▃"]  # 渐变进度
    }
    frames = styles.get(style, styles[1])  # 默认使用样式1
    for frame in itertools.cycle(frames):
        if not loading:
            break
        sys.stdout.write(f"\r正在扫描 {frame}")
        sys.stdout.flush()
        time.sleep(0.1)
            sys.stdout.write("\r扫描完成     \n ")
