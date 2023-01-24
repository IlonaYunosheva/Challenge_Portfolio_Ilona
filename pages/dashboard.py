from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[id='login']"
    main_page_button_xpath = "//*[text()="Main page"]"
    players_button_xpath = "//*[text()="Players"]"
    language_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sing_out_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    search_field_xpath = "//*[@class="MuiInputBase-input jss51"]"
    download_CSV_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/button"
    print_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[1]/span/button"
    view_columns_button_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[2]/button"
    filter_table_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div/div/div[1]/div[2]/span[3]/button"
    next_page_button_xpath = "//*[@id="pagination-next"]"

