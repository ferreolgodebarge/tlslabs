from sslyze.server_connectivity_info import ServerConnectivityInfo
from sslyze.server_connectivity_tester import (
    ServerConnectivityTester,
    ServerConnectivityError,
)
from sslyze.ssl_settings import TlsWrappedProtocolEnum


def get_https_server_info(
    hostname: str, port: int = 443, timeout: int = None
) -> ServerConnectivityInfo:
    try:
        server_tester = ServerConnectivityTester(
            hostname=hostname,
            port=port,
            tls_wrapped_protocol=TlsWrappedProtocolEnum.HTTPS,
        )
        print(
            f"\nTesting connectivity with {server_tester.hostname}:{server_tester.port}..."
        )
        server_info = server_tester.perform(timeout)
    except ServerConnectivityError as e:
        # Could not establish an SSL connection to the server
        raise RuntimeError(
            f"Could not connect to {e.server_info.hostname}: {e.error_message}"
        )

    return server_info
