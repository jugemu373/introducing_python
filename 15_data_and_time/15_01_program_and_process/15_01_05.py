# psutilによるプロセス情報の取得
"""
サードパーティパッケージのpsutilも、Linux, Unix, macOS, Windowsのシステム、
プロセス情報を提供する。

次についての情報が得られる。
    
    システム
        CPU、メモリ、ディスク、ネットワーク、センサー
    
    プロセス
        ID、親プロセスのID、CPU、メモリ、オープンファイル、スレッド

私のコンピュータが4個のCPUを持つことはすでに説明した(すぐ前のosの節で)。
それらのCPUは、どれだけの時間使われてきただろうか。
"""
import psutil
print(psutil.cpu_times(True))

"今、どれくらいの使用率になっているのだろうか。"
print(psutil.cpu_percent(True))
print(psutil.cpu_percent(percpu=True))

"""
この種の情報が必要になることはないかもしれない。しかし、必要になったときに
どこを探せばよいかがわかっていることは大切だろう。
"""
