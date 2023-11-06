import pandas as pd

DATA_LIST = [
    ['a', 1, 3]
    , ['a', 2, 3]
    , ['b', 1, 1]
    , ['a', 4, 2]
    , ['c', 1, 2]
    , ['b', 1, 3]
    , ['a', 3, 1]
    , ['c', 2, 3]
    , ['b', 5, 2]
    , ['c', 3, 3]
]

COLUMN_NAME_LIST = ['KIND', 'START', 'END']


if __name__ == '__main__':
    df = pd.DataFrame(DATA_LIST, columns=COLUMN_NAME_LIST, index=None)
    
    print('初期値')
    print(df)
    print('**********')
    
    # START -> KIND -> ENDの順番でソート
    # True:昇順
    df_1 = df.sort_values(['START', 'KIND', 'END'], ascending=[True, True, True])
    
    print('START -> KIND -> ENDの順番でソート(昇順)')
    print(df_1)
    print('**********')

    # START -> KIND -> ENDの順番でソート
    # FALSE:降順
    df_2 = df.sort_values(['START', 'KIND', 'END'], ascending=[False, False, False])
    
    print('START -> KIND -> ENDの順番でソート(降順)')
    print(df_2)
    print('**********')

    # KIND -> START -> ENDの順番でソート
    df_3 = df.sort_values(['KIND', 'START', 'END'], ascending=[True, True, False])
    
    print('KIND(昇順) -> START(昇順) -> END(降順)の順番でソート')
    print(df_3)
    print('**********')


# 参考URL
# https://ja.stackoverflow.com/questions/95421/python%e3%81%a7%e3%81%ae%e3%83%87%e3%83%bc%e3%82%bf%e5%87%a6%e7%90%86/95459#95459
# https://note.nkmk.me/python-pandas-sort-values-sort-index/