
from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Admins:
    id: list


@dataclass
class Config:
    tg_bot: TgBot
    admins: Admins


def load_config(path=None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(TgBot(token=env('BOT_TOKEN')), Admins(id=list(map(int, env.list('ADMIN_ID')))))
