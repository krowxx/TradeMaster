
data = dict(
    type = "AlgorithmicTradingDataset",
    data_path = "data/algorithmic_trading/BTC2",
    train_path = "data/algorithmic_trading/BTC2/train.csv",
    valid_path = "data/algorithmic_trading/BTC2/valid.csv",
    test_path = "data/algorithmic_trading/BTC2/test.csv",
    test_dynamic_path='data/algorithmic_trading/BTC2/test_deepsn1per.csv',
    tech_indicator_list =[
        'rsi', 'oisi', 'mfi', 'adx', 'high_vol', 'longs_closing', 'longs_opening', 'shorts_closing',
        'shorts_opening', 'upper_band_diff', 'lower_band_diff', 'vwap_diff', 'openz', 'highz', 'lowz', 'closez'
    ],
    backward_num_day = 5,
    forward_num_day = 5,
)