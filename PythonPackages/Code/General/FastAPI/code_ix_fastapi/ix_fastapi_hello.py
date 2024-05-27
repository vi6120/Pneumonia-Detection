from fastapi import FastAPI
import toml
import uvicorn


app = FastAPI()


@app.get("/hello")
def hello():
    return {"hello": "world"}


if __name__ == "__main__":
    config = toml.load('./config/ix_fastapi_config.toml')
    env = config['SETUP']['env']
    host = config['PROJECT'][env]['host']
    port = config['PROJECT'][env]['port']
    protocol = config['PROJECT'][env]['protocol']

    print(f'environment set to {env}, server to {protocol}://{host}:{port}')

    uvicorn.run(app, host=host, port=port)

