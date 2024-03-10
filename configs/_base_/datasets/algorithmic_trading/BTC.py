
data = dict(
    type = "AlgorithmicTradingDataset",
    data_path = "data/algorithmic_trading/BTC",
    train_path = "data/algorithmic_trading/BTC/train.csv",
    valid_path = "data/algorithmic_trading/BTC/valid.csv",
    test_path = "data/algorithmic_trading/BTC/test.csv",
    test_dynamic_path='data/algorithmic_trading/BTC/test_labeled_3_24_-0.15_0.15.csv',
    tech_indicator_list = [
        'rsi', 'oisi', 'mfi', 'adx', 'high_vol', 'longs_closing', 'longs_opening', 'shorts_closing',
        'shorts_opening', 'upper_band_diff', 'lower_band_diff', 'vwap_diff', 'openz', 'highz', 'lowz', 'closez'
    ],
    backward_num_day = 5,
    forward_num_day = 5,
)