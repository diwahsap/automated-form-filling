from selenium import webdriver
from tkinter import messagebox

driver = webdriver.Chrome()
driver.get('http://siakad.itera.ac.id/login/login')

# Wait for the page to load
driver.implicitly_wait(10)

# login to the page
driver.find_element_by_css_selector('#modal_warning > div > div > div.modal-header > button').click()

# authentication
driver.find_element_by_css_selector('#user').send_keys('youremail') # your email
driver.find_element_by_css_selector('#pwd').send_keys('yourpassword') # your password

# verification
messagebox.showinfo(title='Verification', message='Finish on screen verification, and then click OK.')
driver.find_element_by_css_selector('#vanilla-slideshow-container > div.login-page > div > div > div > div.col-lg-4.col-md-4.col-md-offset-1.col-sm-5 > div > div.form-body > form > button').click()

# click tab Kuesioner
driver.find_element_by_css_selector('body > div.container.content > div > div.col-md-3 > div:nth-child(2) > a:nth-child(6)').click()

# Kuesioner semester 2022/2023 Ganjil -> ada 5 bagian. Isinya 7 pertanyaan.
for i in range(1, 6):
    driver.find_element_by_css_selector(f'body > div.container.content > div > div.col-md-9 > div > div.box-body > table:nth-child(7) > tbody > tr:nth-child({i}) > td:nth-child(6) > a').click()
    for i in range(1, 8):
        driver.find_element_by_css_selector(f'body > div.container.content > div.row > div.col-md-9 > div > div.box-body > form > div > div:nth-child({i}) > div > label:nth-child(2) > input[type=radio]').click()
    driver.find_element_by_css_selector('body > div.container.content > div.row > div.col-md-9 > div > div.box-body > form > div > div.box-footer > button').click()
    driver.find_element_by_css_selector('body > div.container.content > div > div.col-md-9 > div.alert.alert-info > button').click()

# part 1 -> kuesioner kepuasan mahasiswa terhadap dosen itera. Isinya ada 13 pertanyaan
for i in range(1, 11):
    driver.find_element_by_css_selector(f'body > div.container.content > div > div.col-md-9 > div > div.box-body > table:nth-child(7) > tbody > tr:nth-child({i}) > td:nth-child(6) > a').click()
    for i in range(1, 14):
        driver.find_element_by_css_selector(f'body > div.container.content > div.row > div.col-md-9 > div > div.box-body > form > div > div:nth-child({i}) > div > label:nth-child(2) > input[type=radio]').click()
    driver.find_element_by_css_selector('body > div.container.content > div.row > div.col-md-9 > div > div.box-body > form > div > div.box-footer > button').click()
    driver.find_element_by_css_selector('body > div.container.content > div > div.col-md-9 > div.alert.alert-info > button').click()

# part 2 -> kuesioner evaluasi perkuliahan. Isinya ada 11 pertanyaan.
for i in range(11, 21):
    driver.find_element_by_css_selector(f'body > div.container.content > div > div.col-md-9 > div > div.box-body > table:nth-child(7) > tbody > tr:nth-child({i}) > td:nth-child(6) > a').click()
    for i in range(1, 12):
        driver.find_element_by_css_selector(f'body > div.container.content > div.row > div.col-md-9 > div > div.box-body > form > div > div:nth-child({i}) > div > label:nth-child(2) > input[type=radio]').click()
    driver.find_element_by_css_selector('body > div.container.content > div.row > div.col-md-9 > div > div.box-body > form > div > div.box-footer > button').click()
    driver.find_element_by_css_selector('body > div.container.content > div > div.col-md-9 > div.alert.alert-info > button').click()

messagebox.showinfo(title='Done', message='Selesai.')
