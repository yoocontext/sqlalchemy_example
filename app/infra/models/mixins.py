from datetime import datetime, timezone

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, DateTime, func


class IntPKMixin:
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    # тут BigInteger так как у телеграмма большие id на 11 симовлов


class TimeMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(
            timezone=True
        ),  # нужно чтобы сохранять время с timezone типа 2025-02-16 14:30:00+03:00 часть с +03:00 в конце это таймзона
        default=datetime.now(
            timezone.utc
        ),  # default на уровне питона, типа при сохранении модели автоматом на стороне питона добавиться время
        server_default=func.now(),  # default на уровне базы данных, server_default прописывать хорошая практика
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=datetime.now(
            timezone.utc
        ),  # если я буду изменять значение полей модели эта хуйня сработает и обновит время обновления
        server_onupdate=func.now(),  # то же самое только на стороне сервера
    )
