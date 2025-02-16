from typing import AsyncIterable

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)


class Database:
    def __init__(self, url: str) -> None:
        """
        engine это главная штука которая взаимодействует с базой данных. Обычно она создается одна на приложение.
        """
        self.engine: AsyncEngine = create_async_engine(
            url=url,  # Ссылка для подключения к бд
            echo=False,  # Логирование SQL-запросов (выводит в консоль)
            pool_size=10,  # Размер пула соединений
            max_overflow=5,  # Максимальное количество дополнительных соединений
            pool_timeout=30,  # Время ожидания свободного соединения в пуле
            pool_recycle=1800,  # Закрытие неиспользуемых соединений каждые 30 минут
        )
        self.session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=True,  # оч полезная штука, чекни видик по алхимии которые я кидал. биг бои ставят False
            expire_on_commit=True,  # название говорит само за себя, спроси у chatgpt
        )

    async def get_session(self) -> AsyncIterable[AsyncSession]:
        """
        это генератор так как используется контекстный менеджер, он закрывает сессию -> session.close()
        если бы тут был бы return то на return session функция завершила бы свою работу и не дошла бы
        до закрытия. Поэтому yield, типа она передает сессию дальше и ждет когда она перестанет
        юзаться. как только это произойдет управление опять получит наш генератор и контекстный менеджер
        сделает session.close()
        """
        async with self.session_maker() as session:
            yield session
            # тут генератор получает управление
        # и происходит выход из контекстного менеджера
        # await session.close()
