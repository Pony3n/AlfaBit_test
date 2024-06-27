class DeliveryState:

    class Meta:
        verbose_name = "Состояние доставки"
        verbose_name_plural = "Состояния доставок"

    STATE_NEW = 1  # Новая
    STATE_ISSUED = 2  # Выдана курьеру
    STATE_DELIVERED = 3  # Доставлена
    STATE_HANDED = 4  # Курьер сдал
    STATE_REFUSED = 5  # Отказ
    STATE_PAID_REFUSED = 6  # Отказ с оплатой курьеру
    STATE_COMPLETE = 7  # Завершена
    STATE_NONE = 8  # Не определено

    state_map = {
        STATE_NEW: "new",
        STATE_ISSUED: "issued",
        STATE_DELIVERED: "delivered",
        STATE_HANDED: "handed",
        STATE_REFUSED: "refused",
        STATE_PAID_REFUSED: "paid_refused",
        STATE_COMPLETE: "complete",
        STATE_NONE: "none",
    }

    @classmethod
    def get_state(cls, state):
        if state in cls.state_map:
            return state
        raise ValueError(f"Неверное состояние: {state}")

    @classmethod
    def get_state_name(cls, state):
        return cls.state_map.get(state, "Неизвестное состояние")


def create_get_method(state_name, state_value):
    @classmethod
    def get_state_method(cls):
        return cls.get_state(state_value)
    get_state_method.__name__ = f'get_{state_name}'
    return get_state_method


for state_value, state_name in DeliveryState.state_map.items():
    method = create_get_method(state_name, state_value)
    setattr(DeliveryState, method.__name__, method)


print(DeliveryState.get_new())
print(DeliveryState.get_issued())
print(DeliveryState.get_delivered())
print(DeliveryState.get_state_name(DeliveryState.get_handed()))
