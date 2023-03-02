from sanic import Sanic
from sanic import response as res
from sanic_testing import TestManager


app = Sanic(__name__)
TestManager(app)


@app.route("/")
async def test(req):
    return res.text("I'm a teapot", status=418)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8787)
