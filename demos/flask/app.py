from flask import Flask, render_template_string
from markupsafe import Markup

from great_tables import GTI, data
from great_tables.web import runtime_tags, write_runtime

cars = data.gtcars[["mfr", "model", "year", "hp", "msrp"]]
app = Flask(__name__)
write_runtime(f"{app.static_folder}/gti")

PAGE = """
<!DOCTYPE html>
<html>
<head>{{ runtime }}</head>
<body>{% for table in tables %}{{ table }}{% endfor %}</body>
</html>
"""


@app.route("/")
def index():
    table = GTI(cars).fmt_integer("hp").fmt_currency("msrp", decimals=0)
    tables = [table.i_cols_filter(columns="mfr", type="facet"), table.i_selection("multiple")]
    return render_template_string(
        PAGE,
        runtime=runtime_tags(url="/static/gti/"),
        tables=[Markup(table.as_raw_html(runtime="none")) for table in tables],
    )


if __name__ == "__main__":
    app.run()
