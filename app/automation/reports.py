import pandas as pd
from datetime import datetime

def save_test_report(page):
    """Generates logs and screenshots."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    screenshot_path = f"reports/screenshots/screenshot_{timestamp}.png"
    page.screenshot(path=screenshot_path)
    print(f"📸 Screenshot saved: {screenshot_path}")

    log_data = {
        "Timestamp": [timestamp],
        "URL": [page.url]
    }
    df = pd.DataFrame(log_data)
    report_path = f"reports/logs/report_{timestamp}.csv"
    df.to_csv(report_path, index=False)
    print(f"📄 Test Report saved: {report_path}")
