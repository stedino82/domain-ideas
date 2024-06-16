import socket


def is_available(hostname: str) -> bool:
    try:
        socket.gethostbyname(hostname)
        return False
    except socket.error:
        return True


def check_availability(domains):
    for dom in domains:
        if is_available(hostname=dom):
            yield dom


if __name__ == "__main__":
    domain_list = [
        'prova.it',
        'example.com',
        'questo-dominio-non-puo-esistere.biz'
    ]

    for d in check_availability(domain_list):
        print(d)
