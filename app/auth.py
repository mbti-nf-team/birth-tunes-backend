import logging

from fastapi import HTTPException, Request, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

from .config import get_settings

logger = logging.getLogger(__name__)

api_key_header = APIKeyHeader(name="nfteam-api-token", auto_error=False)


async def get_api_key(
    request: Request,
    api_key_header: str = Security(api_key_header),
):
    # TODO: 임시로 토큰 검증 비활성화 - 프론트엔드 환경변수 수정 후 다시 활성화 필요
    return api_key_header

    expected_token = get_settings().NFTEAM_API_TOKEN

    if api_key_header == expected_token:
        return api_key_header

    # 상세 로깅
    client_ip = request.client.host if request.client else "unknown"
    origin = request.headers.get("origin", "no-origin")
    user_agent = request.headers.get("user-agent", "no-user-agent")

    if api_key_header is None:
        logger.warning(
            f"403 Forbidden - Missing API token | "
            f"IP: {client_ip} | Origin: {origin} | UA: {user_agent}"
        )
    else:
        # 토큰 일부만 표시 (보안)
        received_preview = api_key_header[:8] + "..." if len(api_key_header) > 8 else api_key_header
        expected_preview = expected_token[:8] + "..." if expected_token and len(expected_token) > 8 else "not-set"
        logger.warning(
            f"403 Forbidden - Invalid API token | "
            f"Received: {received_preview} | Expected: {expected_preview} | "
            f"IP: {client_ip} | Origin: {origin} | UA: {user_agent}"
        )

    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Forbidden")
