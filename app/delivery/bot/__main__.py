import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from mypyc import common

from app.apps.core.bot.handlers import common,inline_mode, save_text, save_images, \
    inline_mode, delete_data, inline_pagination_demo, \
    inline_chosen_result_demo
from app.config.bot import RUNNING_MODE, TG_TOKEN, RunningMode

bot = Bot(TG_TOKEN, parse_mode="HTML")

dispatcher = Dispatcher(storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def _register_routers() -> None:
    dispatcher.include_routers(
        common.router,inline_mode.router, save_text.router, save_images.router, \
        delete_data.router, inline_pagination_demo.router, \
        inline_chosen_result_demo.router
    )


async def _set_bot_commands() -> None:
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Start bot"),
            BotCommand(command="/apps", description="Show installed apps"),
        ]
    )


@dispatcher.startup()
async def on_startup() -> None:
    # Register all routers
    _register_routers()

    # Set default commands
    await _set_bot_commands()


async def run_polling() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())


def run_webhook() -> None:
    raise NotImplementedError("Webhook mode is not implemented yet")


if __name__ == "__main__":
    if RUNNING_MODE == RunningMode.LONG_POLLING:
        asyncio.run(run_polling())
    elif RUNNING_MODE == RunningMode.WEBHOOK:
        run_webhook()
    else:
        raise RuntimeError(f"Unknown running mode: {RUNNING_MODE}")
