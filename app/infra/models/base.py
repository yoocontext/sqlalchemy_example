from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseORM(DeclarativeBase):
    """
    это главная "родительская" модель от которой ты должен наследовать все остальные модели
    в ней храниться вся информация о твоих моделях, она нужна чтобы делать миграции, cоздавать модели,
    удалять, изменять типа
    """

    common_field: Mapped[str] = mapped_column(
        nullable=True
    )  # так как это поле создано в модели, которую будут наследовать все остальные модели
    # оно будет во всех моделях. Типа в базовую модель можно выносить общие для всех
    # моделей поля
