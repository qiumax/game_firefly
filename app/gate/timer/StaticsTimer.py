# coding:utf8
from app.gate.timer.TimeBase import ITimer
from app.gate.core.UserManager import UserManager
from app.util.common import func


class StaticsTimer(ITimer):

    def do(self):
        #interval = 5 * 60
        interval = 5 * 60
        self.start(interval)
        func.log_info('[gate] StaticsTimer check do, next: {}'.format(interval))
        user_count = UserManager().get_user_count()
        func.log_info('[gate] StaticsTimer user count: {}'.format(user_count))
