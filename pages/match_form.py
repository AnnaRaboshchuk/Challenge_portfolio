from pages.base_page import BasePage


class match_form(BasePage):
   my_team_text_field_xpath = '//*[@name="myTeam"]'
   enemy_team_text_field_xpath = '//*[@name="enemyTeam"]'
   my_team_score_text_field = '//*[@name="myTeamScore"]'
   date_text_field_xpath = '//*[@name="date"]'
   match_at_home_label_xpath = '//*[@id="__next"]//label[1]/span[2]'
   match_at_home_label_xpath = '//span[2][text()="Match at home"]'
   match_out_home_label_xpath = '//span[2][text()="Match out home"]'
   button_submit_xpath = '//*[@class="MuiButton-label"][text()="Submit"]'
   button_submit_xpath = '//*[text()="Submit"]'
   button_clear_xpath= '//*[text()="Clear"]'

