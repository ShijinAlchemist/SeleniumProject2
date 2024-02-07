from selenium import webdriver
import pytest


# decorator
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        return driver
    elif browser == "firefox":
        driver = webdriver.Firefox()
        return driver
    else:
        driver = webdriver.Ie()
        return driver


def pytest_addoption(parser):  # this will get the value from hooks/cli
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the value to set up method
    return request.config.getoption("--browser")


# # hook for Adding environment into html report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop commerce'
#     config._metadata['Module Name'] = 'customers'
#     config._metadata['Tester'] = 'Shijin'
#
#
# # it's a hook for delete/modify environment into html report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA HOME", None)
#     metadata.pop("Plugins", None)

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'nop Commerce'
        config.stash[metadata_key]['Module Name'] = 'Customers'
        config.stash[metadata_key]['Tester'] = 'Shijin'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
