import docker
import pytest

testinfra_hosts = ['docker://test_container']

@pytest.fixture(scope="module", autouse=True)
def container(client, image):
    container = client.containers.run(
        image.id,
        name="test_container",
        detach=True,
        environment=[
            'DATABASE_USER=test_user',
            'DATABASE_NAME=test_db',
            'DATABASE_PASSWORD=test_password'
        ]
    )
    yield container
    container.remove(force=True)

def test_environment(host):
    env = host.check_output("env")
    assert "DATABASE_HOST=mysql" in env
    assert "DATABASE_USER=test_user" in env
    assert "DATABASE_NAME=test_db" in env
    assert "DATABASE_PASSWORD=test_password" in env
    assert "BACKUP_TIME=0 3 * * *" in env

def test_crontab(host):
    assert host.check_output("crontab -l") == """DATABASE_HOST=mysql
DATABASE_USER=test_user
DATABASE_NAME=test_db
DATABASE_PASSWORD=test_password
0 3 * * * backup > /backup.log"""
