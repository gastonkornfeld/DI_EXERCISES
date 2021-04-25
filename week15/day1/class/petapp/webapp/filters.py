


from . import app

@app.template_filter()
def name_format(name):
    name = len(name) * '*'

    return name

