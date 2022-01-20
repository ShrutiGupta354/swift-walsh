from server import Server
import os

def install_apt_packages(server):
    print("installing apt packages")
    server.update_apt_packages()
    server.install_apt_package("python3-pip")
    packages = server.get_installed_apt_packages()
    assert "python3-pip" in packages

def install_pip3_packages(server):
    version = server.get_pip3_version()
    assert version.startswith("20.")
    assert version.endswith("3.8")
    server.install_pip3_package("dataset")
    server.install_pip3_package("bottle")
    packages = server.get_installed_pip3_packages()
    assert "dataset" in packages
    assert "bottle" in packages

if __name__ == "__main__":
    server = Server(host = "3.129.67.194", user="ubuntu", key_filename="/Users/greg/.ssh/lightsail-ohio-gsd.pem")
    #install_apt_packages(server)
    install_pip3_packages(server)
    print("done.")