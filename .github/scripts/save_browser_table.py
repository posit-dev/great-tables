from great_tables import GT, exibble
from pathlib import Path

p = Path("_browser_save")
p.mkdir(exist_ok=True)

for scale in (0.5, 1.0, 2.0):
    GT(exibble).save(str(p / f"exibble_chrome_{scale}.png"), web_driver="chrome", scale=scale)
