import base64
import sys
import tempfile

from collections import defaultdict
from great_tables import GT, exibble
from pathlib import Path


def file_to_base64(fname):
    with open(fname, "rb") as f:
        return base64.b64encode(f.read()).decode()


out_name, drivers = sys.argv[1], sys.argv[2:]
assert set(drivers).issubset({"chrome", "safari", "firefox", "edge"})

driver_results = defaultdict(list)
with tempfile.TemporaryDirectory() as tmp_dir:
    p_tmp_dir = Path(tmp_dir)
    for driver in drivers:
        for scale in (0.5, 1.0, 2.0, 3.25):
            for debug in [None, "zoom", "final_resize"]:
                fname = str(p_tmp_dir / f"exibble_{driver}_{scale}_{debug}.png")
                GT(exibble).save(fname, web_driver=driver, scale=scale, _debug_dump=debug)
                driver_results[driver].append(fname)

    with open(out_name, "w") as f:
        f.write("<html><head></head><body>\n\n")
        for driver, img_names in driver_results.items():
            f.write(f"<h1>{driver}</h1>\n\n")
            for fname in img_names:
                style = """style="width: 400px; height: auto;" """
                f.write(f"<h2>{Path(fname).name}</h2>\n\n")
                f.write(
                    f"""<img src="data:image/png;base64, {file_to_base64(fname)}" {style}> \n\n"""
                )
        f.write("</body></html>")
