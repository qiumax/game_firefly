# coding:utf8


GAME_TYPE_PDK = 1               # 跑得快 每人16张版
GAME_TYPE_ZZMJ = 2              # 转转麻将
GAME_TYPE_PDK2 = 3              # 跑得快 每人15张版
GAME_TYPE_PDK3 = 4              # 2人跑得快 每人16张版
GAME_TYPE_PDK4 = 5              # 2人跑得快 每人15张版


GAME_LIST_POKER_PDK = [GAME_TYPE_PDK, GAME_TYPE_PDK2,GAME_TYPE_PDK3,GAME_TYPE_PDK4]
GAME_LIST_MAHJONG = [GAME_TYPE_ZZMJ]


rule_configs = {
    GAME_TYPE_PDK: {
        'room_price': {
            1: 0,
            2: 0,
            10: 0,
            20: 0,
            30: 0
        },
        'player_count': 3,
        'unit_count': 48,        # 48张扑克牌
        'original_count': 16,    # 每个玩家初始牌数
        'un_except': []          # 去除的牌
    },
    GAME_TYPE_ZZMJ: {
        'room_price': {
            1: 0,
            2: 0,
            10: 0,
            20: 0,
            30: 0
        },
        'player_count': 4,
        'unit_count': 108,       # 108张麻将牌
        'original_count': 13     # 每个玩家初始牌数
    },
    GAME_TYPE_PDK2: {
        'room_price': {
            1: 0,
            2: 0,
            10: 0,
            20: 0,
            30: 0
        },
        'player_count': 3,
        'unit_count': 48,        # 48张扑克牌
        'original_count': 15,    # 每个玩家初始牌数
        'un_except': [47, 46, 44]  # 去除的牌
    },
    GAME_TYPE_PDK3: {
        'room_price': {
            1: 0,
            2: 0,
            10: 0,
            20: 0,
            30: 0
        },
        'player_count': 2,
        'unit_count': 48,        # 48张扑克牌
        'original_count': 16,    # 每个玩家初始牌数
        'un_except': []  # 去除的牌
    },
    GAME_TYPE_PDK4: {
        'room_price': {
            1: 0,
            2: 0,
            10: 0,
            20: 0,
            30: 0
        },
        'player_count': 2,
        'unit_count': 48,        # 48张扑克牌
        'original_count': 15,    # 每个玩家初始牌数
        'un_except': [47, 46, 44]  # 去除的牌
    },
}


DEFAULT_PER_PRICE = 10          # 默认每局费用
POKER_PER_PRICE = 10            # 扑克每局费用
MAHJONG_PER_PRICE = 8           # 麻将每局费用


ONLINE_MATCH_MIN_GOLD = 2000        # 在线匹配允许进入的金币数量
ONLINE_MATCH_BAIL = 50              # 在线匹配保证金
ONLINE_RATIO = 2                    # 在线匹配积分和金币的倍数(1积分=2金币)

#ROOM_EXPIRE = 24 * 3600 * 10            # 房间有效期
ROOM_EXPIRE = 24 * 3600 * 1            # 房间有效期


