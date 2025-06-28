import time
import yaml
from trading_bot import TradingBot

# Load configuration
with open('config/api_keys.yaml', 'r') as f:
    api_keys = yaml.safe_load(f)

with open('config/settings.yaml', 'r') as f:
    settings = yaml.safe_load(f)

# Set environment variables for configuration
class Config:
    TRADING_PAIRS = settings['trading']['pairs']
    TELEGRAM_TOKEN = api_keys['telegram']['token']
    TELEGRAM_CHANNEL = api_keys['telegram']['channel_id']
    POCKET_OPTION_TOKEN = api_keys['pocket_option']['token']
    MAX_TRADES_PER_HOUR = settings['signals']['max_trades_per_hour']
    MAX_DAILY_LOSS = float(settings['trading']['max_daily_loss'].strip('%')) / 100
    AMOUNT_PER_TRADE = settings['trading']['amount']

if __name__ == "__main__":
    print("Starting AI Trading Bot...")
    bot = TradingBot()
    
    try:
        bot.run()
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Critical error: {str(e)}")
        bot.telegram.send_alert(f"🆘 CRITICAL ERROR: {str(e)}")
