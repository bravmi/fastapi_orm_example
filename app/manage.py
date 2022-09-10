#!/usr/bin/env python
import uvicorn


def serve() -> None:
    uvicorn.run(
        'app.main:app',
        host='0.0.0.0',
        reload=True,
        use_colors=True,
    )


if __name__ == '__main__':
    serve()
