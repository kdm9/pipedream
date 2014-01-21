from pipedream import util
from tests import helpers
from unittest import TestCase, skip, skipIf, skipUnless
import socket
import sys
try:
    # Python 3 compatible way of doing things
    from urllib.request import urlopen
    from urllib.error import URLError
except ImportError:
    # py2.x
    from urllib2 import URLError, urlopen


class TestGetIP(TestCase):
    """All tests for the function pipedream.util.get_ip"""

    @skipUnless(util.has_internet(), helpers.SKIP_NEED_INTERNET)
    def test_getip_with_no_args(self):
        ip = util.get_ip()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        expected_ip = s.getsockname()[0]
        self.assertEqual(ip, expected_ip)

    @skipUnless(sys.platform.startswith("linux"), helpers.SKIP_NEED_LINUX)
    def test_getip_returns_localhost(self):
        ip = util.get_ip(iface="lo", localhost=True)
        self.assertEqual(ip, helpers.LOCALHOST_IP)

    def test_getip_without_netifaces(self):
        ip = util.get_ip(use_netifaces=False)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        expected_ip = s.getsockname()[0]
        self.assertEqual(ip, expected_ip)

    def test_getip_without_ioctl_and_netifaces(self):
        ip = util.get_ip(use_netifaces=False, use_ioctl=False)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        expected_ip = s.getsockname()[0]
        if sys.platform.startswith("linux"):
            self.assertIsNone(ip)
        else:
            self.assertEqual(ip, expected_ip)

    def test_getip_without_ioctl_and_netifaces_localhost(self):
        ip = util.get_ip(localhost=True, use_netifaces=False, use_ioctl=False)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        expected_ip = s.getsockname()[0]
        if sys.platform.startswith("linux"):
            self.assertEqual(ip, helpers.LOCALHOST_IP)
        else:
            self.assertEqual(ip, expected_ip)


class TestHasInternet(TestCase):
    """Tests for pipedream.util.has_internet"""
    def test_has_internet(self):
        result = util.has_internet()
        try:
            resp = urlopen("http://google.com")
            self.assertTrue(result)
        except URLError:
            self.assertFalse(result)

    def test_has_internet_unreachable_host(self):
        result = util.has_internet(url="http://Youllnevergettothisurl.notatld")
        self.assertFalse(result)
