# 静的メソッド
"""
クラス定義に含まれる第3のタイプのメソッドは、クラスにもオブジェクトにも影響を与えない。独立した存在としてふらふらしているよりも
都合がよいのでクラス定義の中にいるだけだ。それは、@staticmethodデコレータを付けた静的メソッドである。
静的メソッドは、第1引数としてselfやclsを取らない。
"""


class CoyoteWeapon:
    @staticmethod
    def commercial():
        print('This CyoteWeapon has been brought to you by Acme')
    

print(CoyoteWeapon.commercial())

"""
このメソッドは、CoyoteWeaponクラスからオブジェクトを作らずに実行できることに注意。
"""
