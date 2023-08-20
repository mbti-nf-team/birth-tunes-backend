from typing import Any

import sentry_sdk
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .config import get_settings
from .router import router as song_router

app_config: dict[str, Any] = {"title": "Birth Tunes Backend"}


if get_settings().ENVIRONMENT.is_prod:
    sentry_sdk.init(
        dsn=get_settings().SENTRY_SDK_DSN,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production,
        traces_sample_rate=1.0,
    )
    # app_config.update({"docs_url": None, "redoc_url": None, "openapi_url": None})
    ALLOW_ORIGINS = ["https://unnamed-birth-tunes.vercel.app"]
else:
    ALLOW_ORIGINS = get_settings().ALLOW_ORIGINS


app = FastAPI(**app_config)

app.include_router(song_router, tags=["Song"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
