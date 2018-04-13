# coding:utf8
from app.gate.timer.ClearTimer import ClearTimer
from app.gate.timer.MarqueeTimer import MarqueeTimer
from app.gate.timer.HeartTickTimer import HeartTickTimer
from app.gate.timer.SaveTimer import SaveTimer
from app.gate.timer.StaticsTimer import StaticsTimer


def start_all_timer():
    MarqueeTimer().start(60)
    HeartTickTimer().start(120)
    ClearTimer().start(30)
    SaveTimer().start(30 * 60)
    StaticsTimer().start(1 * 10)


def stop_all_timer():
    MarqueeTimer().stop()
    HeartTickTimer().stop()
    ClearTimer().stop()
    SaveTimer().stop()
    StaticsTimer().stop()


