from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=["cryptotransaction"]))
async def handle_cryptotransaction_command(message: Message) -> None:
    if message.from_user is None:
        return

    await message.answer('Hello from "Cryptotransaction" app!')
