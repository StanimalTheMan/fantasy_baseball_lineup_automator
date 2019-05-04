import time
import click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@click.command()
@click.option('--days', type=int, prompt="# of days you want to automate your fantasy lineup ", help="# of days you want to make sure your active players are playing")
@click.option('--username', prompt="Your Yahoo username ", help="Your Yahoo account username: ")
@click.option('--password', prompt="Your Yahoo password ", help="Your Yahoo account password: ")
#@click.option('--teamname', prompt="Your teamname ", help="Name of your fantasy team that you want to set lineup for ")
def start_active_players(days, username, password):
    
    # Firefox
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True
    browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver", firefox_profile=profile)
    '''
    # Script only works if Chrome version is between 70 and 73
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=chrome_options)
    '''
    browser.get('https://login.yahoo.com/config/login?.src=spt&.intl=us&.done=https%3A%2F%2Fbaseball.fantasysports.yahoo.com%2Fb1%3F.scrumb%3D0&specId=usernameRegWithName')

    browser.find_element_by_id('login-username').send_keys(username)
    browser.find_element_by_id('login-signin').click()
    time.sleep(2)
    browser.find_element_by_id('login-passwd').send_keys(password)
    browser.find_element_by_name('verifyPassword').click()
    

    '''
    # locate hidden dropdown menu upon login to Yahoo Fantasy Baseball
    teams = browser.find_element_by_xpath("//li[@class = 'Navitem Navitem-main Navitem-fantasy Va-top Fl-start Topstart']")
    hover = ActionChains(driver).move_to_element(teams)
    hover.perform()
    time.sleep(1)

    hover.find_element_by_xpath("//a[text() = '"+ teamname +"']").click()
    time.sleep(2)
    '''
    browser.find_element_by_class_name('F-link').click()

    for day in range(days):
        browser.find_element_by_xpath("//a[text() = 'Start Active Players']").click()
        time.sleep(2)
        browser.find_element_by_xpath("//a[text() = 'Close']").click()
        time.sleep(2)
        browser.find_element_by_xpath("//a[contains(@class, 'Js-next')]").click()
        time.sleep(2)

    browser.quit()



if __name__ == '__main__':
    start_active_players()
