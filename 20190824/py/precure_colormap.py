
# coding: utf-8

# Pythonで使えるプリキュアっぽいカラーマップを作ってみました。
# 

# In[ ]:

# 必要なパッケージ
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.cm as cm
# colormapをカスタマイズする
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap

import seaborn as sns

try:
    get_ipython().magic('matplotlib inline')
except:
    pass

# スタイル設定
# style="whitegrid"：白背景＋グリッド
# カラーパレットは指定しない(palette='deep'になる)
# color_codes=True：指定したパレットに簡略色コードを設定する('r'とか) # いる?
sns.set(style="whitegrid", color_codes=True) 


# ##  キュアップ・ラパパ！
# 
# 色よ、プリキュアカラーに変われ！
# 
# ・・・
# 
# プリキュアの魔法で、クラス `cure_colormap` が生み出されたようです。 
# 
# プリキュアの名前を呼ぶと、プリキュアっぽいカラーマップが返ってくるみたい！ワクワクもんだぁ！
# 「名前を呼ぶと」って言ってるんで、　インターフェースも要りますねえ
# 

# In[ ]:

class cure_colormap :
    '''
    プリキュアっぽいカラーマップを生成して取得するクラス
    
    Attributes
    ----------
    name_to_cmap : dictionary object
        プリキュアの名称 -> colormap への対応
    
    cure_black
    cure_white
    shiny_luminous
    ：
    <ALL Precure> : matplotlib.colors.Colormap object
        各プリキュアのカラーマップ
        
        TODO：直接呼び出したかったからこうしたけど、全プリキュア分のインスタンス保持しとくのはさすがに重くね？呼び出されたときでよくね？
    
    '''
    def __init__(self):
        self.name_to_cmap = dict()

        # ふたりはプリキュア
        # self.cure_black = self.generate_cure_cmap(['#00072A', '#00072A', '#842C72', '#FBFBFB', '#D49033', '#FF3398'], ['キュアブラック', 'Cure Black'], method=self.generate_cmap_q)
        self.cure_black = self.generate_cure_cmap(['#00072A', '#00072A', '#FBFBFB', '#FF3398', '#6e4001'], ['キュアブラック', 'Cure Black']) # TODO まだ何か違う
        # self.cure_white = self.generate_cure_cmap(['#F4F4F4', '#F4F4F4', '#78DDE4', '#0365B5', '#120c4f'], ['キュアホワイト', 'Cure White'], method=self.generate_cmap_q)
        self.cure_white = self.generate_cure_cmap(['#F4F4F4', '#F4F4F4', '#78DDE4', '#0365B5', '#120c4f'], ['キュアホワイト', 'Cure White']) # TODO 違う気がする

        # ふたりはプリキュア Max Heart
        self.shiny_luminous = self.generate_cure_cmap(['#FECF04', '#FEFB53', '#F5F7F7', '#FEB1D1', '#FE3521'], ['シャイニールミナス', 'Shiny Luminous'])

        # ふたりはプリキュア Splash Star
        self.cure_bloom = self.generate_cure_cmap(['#FCAC35', '#FFFF8E', '#FF3292', '#942953'], ['キュアブルーム', 'Cure Bloom'])
        self.cure_bright = self.generate_cure_cmap(['#FDAD38', '#FBCF84', '#FFFFA6', '#F0E947', '#97F518', '#FFFFDF', '#F93B9A', '#DC0067', '#942953'], ['キュアブライト', 'Cure Bright']) # 東映公式に大きめの画像がない？ # https://www.asahi.co.jp/precure_ss/character/img/cb.gif
        # '#FFFFDF', いらないきがする(未検証)
        self.cure_eglet = self.generate_cure_cmap(['#711391', '#FFFFF3', '#D0D6FF', '#06FCD5'], ['キュアイーグレット', 'Cure Egret'])        
        self.cure_windy = self.generate_cure_cmap(['#741B93', '#711391', '#D16FE7', '#F8F8F8', '#FFF3FD', '#FDB2E1', '#DFFFFF', '#01FEDE'], ['キュアウインディ', 'Cure Windy']) # 東映公式に大きめの画像がない？ # https://www.asahi.co.jp/precure_ss/character/img/cw.gif
        self.kaoru_kiryuu = self.generate_cure_cmap(['#275D8A', '#DDECF1', '#E7F5FD', '#DDB9CB', '#CC87BB'], ['霧生薫', 'Kaoru Kiryuu']) # https://lohas.nicoseiga.jp/thumb/8016685i?1522857603
        self.michiru_kiryuu = self.generate_cure_cmap(['#8D2045', '#DC98A9', '#C5E462', '#FFEE2C', '#F9FA9B', '#C11E7A'], ['霧生満', 'Michiru Kiryuu']) # https://lohas.nicoseiga.jp/thumb/8016685i?1522857603

        # Yes!プリキュア5
        self.cure_dream = self.generate_cure_cmap(['#A6366B', '#F14694', '#FFB8F9', '#FFFBCD', '#FFFBCD', '#ECD01B'], ['キュアドリーム', 'Cure Dream'])
        self.cure_rouge = self.generate_cure_cmap(['#D34B32', '#EC9689', '#EC9689', '#FCEDFD', '#FCEDFD', '#FF1EA9'], ['キュアルージュ', 'Cure Rouge']) # 紫を入れたい #680CB1
        self.cure_lemonade = self.generate_cure_cmap(['#D8A725', '#FFEE9E', '#FAF4C2', '#FDFDF7', '#FAC04D', '#E39B14'], ['キュアレモネード', 'Cure Lemonade'])
        self.cure_mint = self.generate_cure_cmap(['#029476', '#55E5CD', '#FFFFF0', '#21AA03'], ['キュアミント', 'Cure Mint'])
        self.cure_aqua = self.generate_cure_cmap(['#1452A4', '#B3D3FE', '#F2FDFD', '#0974CC', '#3C3DA3'], ['キュアアクア', 'Cure Aqua'])
        
        self.dark_dream = self.generate_cure_cmap(['#D02674', '#F9D1EC', '#313144', '#000000'], ['ダークドリーム', 'Dark Dream'])
        self.dark_rouge = self.generate_cure_cmap(['#A92E3F', '#F8C8D6', '#313144', '#000000'], ['ダークルージュ', 'Dark Rouge'])
        self.dark_remonade = self.generate_cure_cmap(['#AB7221', '#FCD516', '#313144', '#000000'], ['ダークレモネード', 'Dark Lemonade'])
        self.dark_mint = self.generate_cure_cmap(['#05A67C', '#E1FEEF', '#313144', '#000000'], ['ダークミント', 'Dark Mint'])
        self.dark_aqua = self.generate_cure_cmap(['#366CCB', '#B9E8F8', '#313144', '#000000'], ['ダークアクア', 'Dark Aqua'])

        # Yes!プリキュア5GoGo!
        self.milky_rose = self.generate_cure_cmap(['#9136cf', '#CA2DA2', '#E7C8F9', '#B4EBEA', '#0386F3'], ['ミルキィローズ', 'Milky Rose'])

        # フレッシュプリキュア!
        self.cure_peach = self.generate_cure_cmap(['#953678', '#DC3E72', '#FF8ABF', '#FFF4AC'], ['キュアピーチ', 'Cure Peach'])
        self.cure_berry = self.generate_cure_cmap(['#353A57', '#2E7DCA', '#6AB7FE', '#C7B3FA'], ['キュアベリー', 'Cure Berry'])
        self.cure_pine = self.generate_cure_cmap(['#9B4750', '#FD8E18', '#FFDA5C', '#DB7A45'], ['キュアパイン', 'Cure Pine'])
        self.cure_passion = self.generate_cure_cmap(['#242B33', '#8E0331', '#DA2A3D', '#FFCBE5'], ['キュアパッション', 'Cure Passion'])
        
        # ハートキャッチプリキュア！
        self.cure_blossom = self.generate_cure_cmap(['#cf1b71', '#F954BD', '#FD98D7', '#FEF3FE'], ['キュアブロッサム', 'Cure Blossom'])
        self.cure_marine = self.generate_cure_cmap(['#4A7AED', '#6EB2F1', '#63DEED', '#EFFAFF'], ['キュアマリン', 'Cure Marine'])
        self.cure_sunshine = self.generate_cure_cmap(['#F98435', '#FFAC05', '#FFE55C', '#DD991D'], ['キュアサンシャイン', 'Cure Sunshine'])
        self.cure_moonlight = self.generate_cure_cmap(['#404A8F', '#6F7FDE', '#CDD5E2', '#D0B0D9'], ['キュアムーンライト', 'Cure Moonlight'])
        self.cure_flower = self.generate_cure_cmap(['#CE7AAE', '#F8D1EC', '#F9FCBF', '#FD9CBF', '#CB1C55'], ['キュアフラワー', 'Cure Flower']) # https://www.asahi.co.jp/heartcatch_precure/img/character/photo/flower.png
        self.dark_precure = self.generate_cure_cmap(['#171717', '#042F36', '#A6D8C6', '#FDA4BE', '#980E13'], ['ダークプリキュア', 'Dark Precure'])
        
        # スイートプリキュア♪
        self.cure_melody = self.generate_cure_cmap(['#DC3688', '#FF78C4', '#F9A5C9', '#FFFFFF'], ['キュアメロディ', 'Cure Melody'])
        self.cure_rhythm = self.generate_cure_cmap(['#D0A947', '#FDF48B', '#FAB7E5', '#FFFFFF'], ['キュアリズム', 'Cure Rhythm']) # まだやりようがある ＃ 
        self.cure_beat = self.generate_cure_cmap(['#303277', '#728CF1', '#C2EBFC', '#D393F8', '#FFFFFF'], ['キュアビート', 'Cure Beat'])
        self.cure_muse = self.generate_cure_cmap(['#C86424', '#FFAC4E', '#FACC2A', '#FFFB52', '#FFFFFF'], ['キュアミューズ', 'Cure Muse'])

        ##### TODO：未作成
        # スマイルプリキュア!
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        [
            'Cure Happy',
            'Cure Sunny',
            'Cure Peace',
            'Cure March',
            'Cure Beauty',
        ]


        # ドキドキ!プリキュア
        self.cure_heart = self.generate_cure_cmap(['#D4A615', '#FFF99E', '#FAFAFA', '#FAB1E2', '#EC3C9C'], ['キュアハート', 'Cure Heart'])
        self.cure_diamond = self.generate_cure_cmap(['#4245AF', '#A8ACF9', '#FAFAFA', '#5791F1', '#597AA7'], ['', 'Cure Diamond'])
        self.cure_rosetta = self.generate_cure_cmap(['#B3481E', '#FFC05C', '#FAFAFA', '#C9EFB6', '#F7DB3D'], ['', 'Cure Rosetta'])
        self.cure_sword = self.generate_cure_cmap(['#AE57B5', '#EEB4F8', '#FAFAFA', '#ADBBF5', '#8B87B2'], ['', 'Cure Sword'])
        self.cure_ace = self.generate_cure_cmap(['#A51318', '#FD757D', '#FFE8EC', '#FAFAFA', '#FFFFFF'], ['', 'Cure Ace'])
        self.cure_sebastian = self.generate_cure_cmap(['#36424E', '#E0EBF1', '#DB0517', '#DB3FA2', '#F48484'], ['', 'Cure Sebastian'])

        ##### TODO：未作成
        # ハピネスチャージプリキュア!
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        [
            'Cure Lovely',
            'Cure Princess',
            'Cure Honey',
            'Cure Fortune',
            'Cure Mirage'
        ]
        
        # Go!プリンセスプリキュア
        self.cure_flora = self.generate_cure_cmap(['#DC3482', '#FE8ADA', '#FFF5FD', '#F8F5A2'], ['キュアフローラ', 'Cure Flora'])
        self.cure_marmaid = self.generate_cure_cmap(['#3C57D8', '#8EE9D8', '#F1FBF2', '#FCC3DD'], ['キュアマーメイド', 'Cure Mermaid'])
        self.cure_twinkle = self.generate_cure_cmap(['#F15312', '#FF9A18', '#FDFF94', '#FCE92D', '#BA70F8'], ['キュアトゥインクル', 'Cure Twinkle'])
        self.cure_scarlet = self.generate_cure_cmap(['#E73F94', '#FEC8FC', '#F6D437', '#E01646'], ['キュアスカーレット', 'Cure Scarlet'])        

        ##### TODO：未作成
        # 魔法つかいプリキュア!
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        [
            'Cure Miracle',
            'Cure Magical',
            'Cure Felice',
            'Cure Mofurun'
        ]

        ##### TODO：未作成
        # キラキラ☆プリキュアアラモード
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        [
            'Cure Whip',
            'Cure Custard',
            'Cure Gelato',
            'Cure Macaron',
            'Cure Chocolat',
            'Cure Parfait',
            'Cure Pekorin'  
        ]

        ##### TODO：未作成
        # HUGっと！プリキュア
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        [
            'Cure Yell',
            'Cure Ange',
            'Cure Etoile',
            'Cure Macherie',
            'Cure Amour',
            'Cure Anfini',
            'Cure Tomorrow'

        ]

        ##### TODO：未作成
        # スター☆トゥインクルプリキュア
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        self.cure_ = self.generate_cure_cmap(['#FFFFFF', '#FFFFFF', '#FFFFFF', '#FFFFFF'], ['キュア＊＊', 'Cure **'])
        [
            'Cure Star',
            'Cure Milky',
            'Cure Soleil',
            'Cure Selene',
            'Cure Cosmo',
        ]

    def get_by_name(self, name):
        '''
        プリキュアの名前を受取り、対応するカラーマップを返す
        
        Parameter
        ---------
        name : string [in]
            プリキュアの名称
        
        Return
        ------
        matplotlib.colors.Colormap object
        一致するプリキュアがいなければNone
        
        '''
        return self.name_to_cmap.get(name)
    

    def generate_cmap(self, colors):
        '''
        指定した色でのカラーマップを返す

        Parameter
        ---------
        colors : array of color hexcode
            色の配列。色は16進数数か色名で指定。

        Return
        ------
        matplotlib.colors.Colormap object

        '''

        values = range(len(colors))

        vmax = np.ceil(np.max(values))
        color_list = []
        for v, c in zip(values, colors):
            color_list.append( ( v / vmax, c) )
        return LinearSegmentedColormap.from_list('custom_cmap', color_list)
    
    def generate_cmap_q(self, colors) :
        '''
        指定した色で、Qualitative(質的)なカラーマップを生成して返す
        
        Parameter
        ---------
        colors : array of color hexcode
        色の配列。色は16進数数か色名で指定。

        Return
        ------
        matplotlib.colors.Colormap object かな？
        
        '''
        return ListedColormap(sns.color_palette(colors).as_hex())

    def generate_cure_cmap(self, colors, names, method=None):
        '''
        指定した配色でカラーマップを生成し、
        プリキュアの名称と対応付ける
        
        Parameters
        ---------
        colors : array of color (hexcode or color name) [in]
            色の配列。色は16進数数か色名で指定。
        
        names : array of string [in]
            プリキュアの名前。

        method : function [in]
            カラーマップを生成する関数。matplotlib.colors.Colormap を返すもの。
            generate_cmap か generate_cmap_q

        Returns
        ------
        matplotlib.colors.Colormap 
            プリキュアカラーマップのオブジェクト。
        '''
        if method is None:
            method = self.generate_cmap
        
        if len(colors) < 1:
            return None
        
        cmap = method(colors)
        for name in names:
            self.name_to_cmap[name] = cmap
        
        return cmap

    def sample_all_colormap(self):
        '''
        全カラーマップ表示

        Parameter
        ---------
        None

        Return
        ------
        None

        '''
        
        import numpy as np
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        from matplotlib import cm
        from collections import OrderedDict


        cure_colors = self
        cmaps = OrderedDict()

        # ふたりはプリキュア
        cmaps['Futari wa Pretty Cure'] = [
            'Cure Black',
            'Cure White'
        ]

        # ふたりはプリキュア Max Heart
        cmaps['Futari wa Pretty Cure Max Heart'] = [
            'Cure Black',
            'Cure White',
            'Shiny Luminous'
        ]

        # ふたりはプリキュア Splash Star
        cmaps['Futari wa Pretty Cure Splash Star'] = [
            'Cure Bloom',
            'Cure Bright',
            'Cure Egret',
            'Cure Windy',
            'Kaoru Kiryuu', #霧生薫
            'Michiru Kiryuu', #霧生満
        ]

        # Yes!プリキュア5
        cmaps['Yes! PreCure 5'] = [
            'Cure Dream',
            'Cure Rouge',
            'Cure Lemonade',
            'Cure Mint',
            'Cure Aqua',
            'Dark Dream',
            'Dark Rouge',
            'Dark Lemonade',
            'Dark Mint',
            'Dark Aqua'
        ]

        # Yes!プリキュア5GoGo!
        cmaps['Yes! PreCure 5 GoGo!'] = [
            'Cure Dream',
            'Cure Rouge',
            'Cure Lemonade',
            'Cure Mint',
            'Cure Aqua',
            'Milky Rose'
        ]

        # フレッシュプリキュア!
        cmaps['Fresh Pretty Cure!'] = [
            'Cure Peach',
            'Cure Berry',
            'Cure Pine',
            'Cure Passion'
        ]

        # ハートキャッチプリキュア！
        cmaps['HeartCatch PreCure!'] = [
            'Cure Blossom',
            'Cure Marine',
            'Cure Sunshine',
            'Cure Moonlight',
            'Cure Flower',
            'Dark Precure'
        ]

        # スイートプリキュア♪
        cmaps['Suite PreCure'] = [
            'Cure Melody',
            'Cure Rhythm',
            'Cure Beat',
            'Cure Muse'
        ]

        # スマイルプリキュア!
        cmaps['Smile PreCure!'] = [
            'Cure Happy',
            'Cure Sunny',
            'Cure Peace',
            'Cure March',
            'Cure Beauty',

        ]

        # ドキドキ!プリキュア
        cmaps['DokiDoki! PreCure'] = [
            'Cure Heart',
            'Cure Diamond',
            'Cure Rosetta',
            'Cure Sword',
            'Cure Ace',
            'Cure Sebastian',

        ]

        # ハピネスチャージプリキュア!
        cmaps['HappinessCharge PreCure!'] = [
            'Cure Lovely',
            'Cure Princess',
            'Cure Honey',
            'Cure Fortune',
            'Cure Mirage'

        ]

        # Go!プリンセスプリキュア
        cmaps['Go! Princess PreCure'] = [
            'Cure Flora',
            'Cure Mermaid',
            'Cure Twinkle',
            'Cure Scarlet'
        ]

        # 魔法つかいプリキュア!
        cmaps['Witchy PreCure!'] = [
            'Cure Miracle',
            'Cure Magical',
            'Cure Felice',
            'Cure Mofurun'
        ]

        # キラキラ☆プリキュアアラモード
        cmaps['Kirakira PreCure a la Mode'] = [
            'Cure Whip',
            'Cure Custard',
            'Cure Gelato',
            'Cure Macaron',
            'Cure Chocolat',
            'Cure Parfait',
            'Cure Pekorin'
        ]

        # HUGっと！プリキュア
        cmaps['Hugtto! PreCure'] = [
            'Cure Yell',
            'Cure Ange',
            'Cure Etoile',
            'Cure Macherie',
            'Cure Amour',
            'Cure Tomorrow'

        ]

        # スター☆トゥインクルプリキュア
        cmaps['Star Twinkle PreCure'] = [
            'Cure Star',
            'Cure Milky',
            'Cure Soleil',
            'Cure Selene',
            'Cure Cosmo',

        ]


        # 表示するデータとして (1, 256) の配列を作成する。
        gradient = np.linspace(0, 1, 256).reshape(1, -1)

        def plot_color_maps(cmap_category, cmap_list):
            '''
            指定したカラーマップを一覧表示する。表示の際「カテゴリ名」を掲出

            '''
            num_cmaps = len(cmap_list)
            fig, axes = plt.subplots(num_cmaps, 1, figsize=(9, num_cmaps * 0.35))
            fig.subplots_adjust(wspace=0.4)
            axes[0].set_title(cmap_category + ' colormaps', fontsize=14, x=0.5)
            
            def plot_color_map(ax, gradient, name):
                cmap = cure_colors.get_by_name(name) 
                if cmap is None:
                    return
                
                ax.imshow(gradient, aspect='auto', cmap=cmap)
                ax.set_axis_off()
                ax.text(-10, 0, name, va='center', ha='right', fontsize=10)
            
            for ax, name in zip(axes, cmap_list):
                plot_color_map(ax, gradient, name)
                # plot_color_map(axR, gradient, name + '_r') # 逆向きは作っていないので、上の表示も順方向だけのものに変更

        for cmap_category, cmap_list in cmaps.items():
            plot_color_maps(cmap_category, cmap_list)

        plt.show()

# In[ ]:

## テスト
class test_cure_colormap() :
    
    cure_colors = cure_colormap()
    
    def test_cure_colormap(self):
        # カラーマップ生成関数
        cmap = self.cure_colors.generate_cure_cmap([], [])
        assert cmap is None, 'Failed to generate_cure_cmap([], [])'
         # ちゃんと引数でテストして？
        colors = ['black', 'white']
        cmap = self.cure_colors.generate_cure_cmap(colors, [], method=self.cure_colors.generate_cmap)
        assert cmap is not None, 'Failed to generate_cure_cmap(method=generate_cmap)'
        cmap_q = self.cure_colors.generate_cure_cmap(colors, [], method=self.cure_colors.generate_cmap_q)
        assert cmap_q is not None, 'Failed to generate_cure_cmap(method=generate_cmap_q)'
        # メンバ直打ち
        assert self.cure_colors.cure_twinkle is not None, "ERROR: cure_colors.cure_twinkle is None" 
        # 名前で呼ぶ
        assert self.cure_colors.get_by_name('キュアトゥインクル') is not None, "ERROR: cure_colors.get_by_name('キュアトゥインクル') is None"
        # Noneに軟着陸する
        assert self.cure_colors.get_by_name('キュアゴリラ') is None, "ERROR: cure_colors.get_by_name('キュアゴリラ') is None"

    def test_sample_all_colormap(self):
        self.cure_colors.sample_all_colormap()

    def test_sample_iris(self):
        from sklearn import datasets
        # おなじみのiris(アヤメ)データのロード
        iris = datasets.load_iris()

        # DataFrameを構築 
        # n×4 行列 X として、アヤメのデータを格納した2次元配列(iris.data)を指定。カラム名もアヤメのデータから(iris.feature_name)
        X = pd.DataFrame(iris.data, columns = iris.feature_names)

        # n次元ベクトル y として、アヤメの品種データを格納したベクトル(data.target)を指定。
        y = pd.DataFrame(iris.target, columns = ['Species'])

        # X と y を結合して n×5 行列にする。axis=1 で列の方向に連結させる
        df = pd.concat([X, y], axis=1)

        fig = plt.figure(figsize=(13,7))
        cure_colors = cure_colormap()
        sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='Species', data=df, palette=cure_colors.cure_scarlet)

        fig.colorbar(im)
        plt.show()

        # (LT後追記)
        # 
        # 違うクラスタの色の差があまりない場合が多くて、
        # LTしながら「あまりいい使用例じゃないな。。。」と思った。というか言ってた。
        # ごめんなさい、トワ様。
        # 
        # よくよく考えたら、キャラクターに使用する色合いってのは
        # 調和が取れる色になっているわけで、
        # 似た色で色分けしちちゃうことになる(結果見づらい)のは当たり前。
        # 
        # キュアコスモやキュアパルフェのように「七色」がキーカラーのプリキュアで色付するのがいいだろうと思いました。
        # 相関係数行列

        plt.figure(figsize=(12,9)) # サイズ設定 
        sns.heatmap(df[df.columns[df.columns != 'Species']].corr(),linewidths=0.1,vmax=1.0, square=True, linecolor='white', annot=True, cmap=cure_colors.cure_twinkle)



test = test_cure_colormap()
test.test_cure_colormap()
test.test_sample_all_colormap()
#test.test_sample_iris()


# # 参考資料
# 
# 
#  * __＜【Python】matplotlibによるグラフ描画時のColormapのカスタマイズ＞__  
#     [https://qiita.com/kenmatsu4/items/fe8a2f1c34c8d5676df8](https://qiita.com/kenmatsu4/items/fe8a2f1c34c8d5676df8)
#  * __＜matplotlib - カラーマップについて＞__  
#     [http://pynote.hatenablog.com/entry/matplotlib-color](http://pynote.hatenablog.com/entry/matplotlib-color)
#     

# # その他
# 
# 
# ## プリキュアの名称について
# 
#  * 英語名とメンバ変数名は[英語版Wikipedia](https://en.wikipedia.org/wiki/Pretty_Cure)準拠
# 
# ### 色の採り方について
# 
#  * 「[プリキュアガーデン](http://www.toei-anim.co.jp/ptr/precure/)」以下の各作品ページにある
#    キャラクター紹介ページの画像から抽出
#    * 「髪の毛の色」、「衣装の色」で構成してます
#    * ただしSSは絵が足りなかったので[朝日放送のページ](https://www.asahi.co.jp/precure_ss/)から
#      ・・・と思ったけどキュアブライトとキュアウインディが載ってなかった。えぇ・・・
#  * Chrome拡張「ColorPick Eyedropper」を使用して取得
#    * 配布は[こちら](https://chrome.google.com/webstore/detail/colorpick-eyedropper/ohcpnigalekghcmgcdcenkpelffpdolg)
# 
# ### 追加の資料情報
# 
#  * [＜キュアっぽさは色味から。カラースキームを抽出してプリキュアっぽいカラーパレットを作ってみよう＞ ](https://www.gizmodo.jp/2017/05/precure-color-palette.html)
#    * 見落としていた先行研究。ありがたい！
# 



#%%
