class HelloWorldTest(object):
    """Hello world test."""

    @staticmethod
    def test_hello_world():
        print('Hello world!')


if __name__ == '__main__':
    HelloWorldTest().test_hello_world()
