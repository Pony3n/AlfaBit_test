def send_email_to_user_of_buy_product(user):
    pass


class Product:

    @classmethod
    def buy(cls, user, item_id):
        product_qs = Product.objects.filter(item_id=item_id)
        if product_qs.exists():
            product = product_qs[0]

        if product.available:
            # списание средств со счета пользователя
            user.withdraw(product.price)

            # информация о купленном товаре
            send_email_to_user_of_buy_product(user)

            product.available = False
            product.buyer = user
            product.save()

            return True
        else:
            return False

# Проблема 1: "Состояние Гонки"
# Идея в том, после проверки существования продукта, в случае если один и тот же продукт одновременно попытаются купить
# товар, то последствия будут непредсказуемы.
# Решение: Транзакции

# Проблема 2: "IndexError and other Errors"
# Допустим, Product.objects.filter - не вернет ничего (так как товара - нет)
# Вылетит ошибка, которая сломает скрипт.
# Решение: Добавить обработчики ошибок
