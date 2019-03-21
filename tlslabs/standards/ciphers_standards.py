from sslyze.plugins.openssl_cipher_suites_plugin import (
    Sslv20ScanCommand,
    Sslv30ScanCommand,
    Tlsv10ScanCommand,
    Tlsv11ScanCommand,
    Tlsv12ScanCommand,
    Tlsv13ScanCommand,
)

COMMANDS = [
    Sslv20ScanCommand(),
    Sslv30ScanCommand(),
    Tlsv10ScanCommand(),
    Tlsv11ScanCommand(),
    Tlsv12ScanCommand(),
    Tlsv13ScanCommand(),
]

ACCEPTED_CIPHERS = [
    "TLS_RSA_WITH_AES_256_CBC_SHA",
    "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
]
