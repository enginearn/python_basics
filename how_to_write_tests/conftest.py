def pytest_addoption(parser):
    parser.addoption('--os-name', action='store', default='linux', help='os name')
