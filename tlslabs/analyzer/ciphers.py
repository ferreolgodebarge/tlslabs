from sslyze.server_connectivity_info import ServerConnectivityInfo
from sslyze.synchronous_scanner import SynchronousScanner
from tlslabs.standards.ciphers_standards import COMMANDS, ACCEPTED_CIPHERS
from colorama import Fore, Style


def ciphers_scanner(server_info: ServerConnectivityInfo) -> dict:
    scanner = SynchronousScanner()
    commands = COMMANDS
    ciphers_info: dict = {}
    for command in commands:
        scan_result = scanner.run_scan_command(server_info, command)
        ciphers: list = []
        for cipher in scan_result.accepted_cipher_list:
            ciphers.append(cipher.name)
        ciphers_info[command.get_cli_argument()] = ciphers
    return ciphers_info


def ciphers_validator(server_info: ServerConnectivityInfo) -> bool:
    ciphers_info = ciphers_scanner(server_info)
    validation_result = True
    print(Fore.YELLOW + "\nCIPHER SCANNER\n==============" + Style.RESET_ALL)
    for protocol in ciphers_info:
        print("\n{} :\n".format(protocol))
        for cipher in ciphers_info[protocol]:
            if cipher not in ACCEPTED_CIPHERS:
                validation_result = False
                print(
                    Fore.RED
                    + "{0:50} ==>   {1:4}".format(cipher, "KO")
                    + Style.RESET_ALL
                )
            else:
                print(
                    Fore.GREEN
                    + "{0:50} ==>   {1:4}".format(cipher, "OK")
                    + Style.RESET_ALL
                )
    return validation_result
