from otree.api import models, BasePlayer, Page


class UserInfoPlayer(BasePlayer):
    class Meta:
        abstract = True

    user_agent = models.StringField()
    screen_width = models.IntegerField()
    window_width = models.IntegerField()


class UserInfoPage(Page):
    form_model = "player"
    form_fields = ["screen_width", "window_width"]

    def before_next_page(self):
        if not self.participant._is_bot:
            self.player.user_agent = self.request.META["HTTP_USER_AGENT"]
