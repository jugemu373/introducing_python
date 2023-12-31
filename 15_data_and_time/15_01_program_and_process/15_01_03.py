# terminate()によるプロセスの強制終了
"""
1つ以上のプロセスを作ったものの、何らかの理由でプロセスを強制終了したくなった場合
(おそらく、ループから抜け出せなくなったり、退屈したり、悪い王様になりたかったりした
のだろう)には、terminate()を使えばよい。mp2.pyでは、プロセスは100万まで数えよう
として1ステップごとに1秒眠り、イライラするメッセージを表示する。
しかし、5秒たつとメインプログラムが我慢できなくなり、プロセスを強制終了する。
"""
