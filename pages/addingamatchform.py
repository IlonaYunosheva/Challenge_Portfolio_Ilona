from pages.base_page import BasePage


class addingamatchform(BasePage):
   my_team_field_xpath "//input[@name="myTeam"]"
   enemy_tam_field_xpath "//input[@name="enemyTeam"]"
   my_team_score_field_xpath "//input[@name="myTeamScore"]"
   enemy_team_score_field_xpath "//input[@name="enemyTeamScore"]"
   date_field_xpath "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
   match_at_home_button_xpath "//*[@name="matchAtHome"]"
   match_out_home_button_xpath "//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]/input"
   web_match_button_xpath "//*[@name="webMatch"]"
   time_played_field_xpath "//*[@name="timePlayed"]"
   general_button_xpath "//*[@name="general"]"

