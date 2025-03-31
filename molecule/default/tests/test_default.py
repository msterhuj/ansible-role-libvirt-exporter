def test_binary(host):
    binary = host.file("/usr/local/bin/prometheus-libvirt-exporter")
    assert binary.exists
    assert oct(binary.mode) == "0o755"

def test_service_file(host):
    service_file = host.file("/etc/systemd/system/prometheus-libvirt-exporter.service")
    assert service_file.exists

def test_service(host):
    service = host.service("prometheus-libvirt-exporter")
    assert service.is_enabled
    assert service.is_running

def test_socket(host):
    socket = host.socket("tcp://0.0.0.0:9177")
    assert socket.is_listening
