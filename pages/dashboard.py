from pages.base_page import BasePage


class Dashboard(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@name="password"]"
    sign_in_button_xpath = "//*[@id="__next"]/form/div/div[2]/button/span[1]"
    language_button__xpath = "//*[@id="__next"]/form/div/div[2]/div/div"
    header_xpath = "//*[@id="__next"]//h5"
    players_accounts_xpath = "//*/main/div[2]/div[1]/div/div[1]"
    matches_count_xpath = "//*/main/div[2]/div[2]/div/div[1]"
    events_counts_xpath = "//*//main/div[2]/div[4]/div/div[1]"
    scouts_panel_xpath = "//*/div/h2[text()="Scouts Panel"]"
    shortcuts_xpath = "//*/div/h2[text()="Shortcuts"]"
    activity_xpath = "//*/div/h2[text()="Activity"]"
    main_page_button_xpath = "//*/div[2]/span[text()="Main page"]"