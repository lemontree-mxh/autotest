__author__ = 'maxh'
'''
wrap selenium actions in autourl.execute function.
for examples:
    t = autourl()
    t.geturl('http://www.baidu.com')
    t.execute('id','kw','sendkey','test')
    t.execute('id','su','click')

A suggest way to use this autourl is to store all
the actions into a OrderedDict collection, and call
autourl.execute() one by one
'''
#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium.common.exceptions as sce
import time
import sys


class autourl:
    def __init__(self, count=5):
        '''
        count: the retry times if the element can't be
               at that time
        '''
        self.browser = webdriver.Chrome()
        self.__count = count

    def geturl(self, url):
        self.browser.get(url)

    def find_element(self, by, value, action):
        retry = 0
        while retry < self.__count:
            try:
                if action == 'click_value':
                    return self.browser.find_elements(by, value)
                else:
                    return self.browser.find_element(by, value)
            except sce.NoSuchElementException:
                time.sleep(1)
                retry += 1
        raise sce.NoSuchElementException

    def execute(self, elem, value, action, keys=''):
        if elem == 'id':
            by = By.ID
        elif elem == 'name':
            by = By.NAME
        elif elem == 'class_name':
            by = By.CLASS_NAME
        elif elem == 'xpath':
            by = By.XPATH
        elif elem == 'url':
            self.geturl(keys)
            return
        else:
            print('unknown element' + elem)
            sys.exit(1)

        try:
            m = self.find_element(by, value, action)
        except sce.NoSuchElementException:
            print("can't find %s:%s" % (elem, value))
            sys.exit(1)

        if action == "click":
            retry = 0
            sucess = False
            while retry < self.__count:
                try:
                    m.click()
                    sucess = True
                    return sucess
                except sce.ElementNotVisibleException:
                    print('catch ElementNotVisibleException')
                    time.sleep(1)
                    retry += 1
            if not sucess:
                print('catch ElementNotVisibleException')
                sys.exit(1)
        elif action == 'click_value':
            retry = 0
            sucess = False
            while retry < self.__count:
                try:
                    for e in m:
                        if e.get_attribute('value') in keys.split(','):
                            e.click()
                    sucess = True
                    return sucess
                except sce.ElementNotVisibleException:
                    print('catch ElementNotVisibleException')
                    time.sleep(1)
                    retry += 1
            if not sucess:
                print('catch ElementNotVisibleException')
                sys.exit(1)

        elif action == 'sendkey':
            try:
                m.clear()
            except sce.InvalidElementStateException:
                pass
            m.send_keys(keys)

        elif action == 'text':
            self.result = eval(m.text)

        elif action == 'select':
            try:
                Select(m).select_by_visible_text(keys)
            except sce.NoSuchElementException:
                print('Could not locate element with visible text:'+keys)
                sys.exit(2)
        else:
            print('unsupported action type ' + action)
            sys.exit(1)


if __name__ == '__main__':
    t = autourl()
    t.geturl('http://www.baidu.com')
    t.execute('id', 'kw', 'sendkey','小米')
    t.execute('id', 'su', 'click')
