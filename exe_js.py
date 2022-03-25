import execjs


def get_sign(query):
    with open('./sign_generator.js', 'r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.compile(js_code)
    return ctx.call('e', query)
