from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)  # Унікальний ідентифікатор клієнта
    company_name = models.CharField(max_length=100)  # Назва компанії або ім'я клієнта
    client_type = models.CharField(
        max_length=50,
        choices=[('Legal', 'Юридична особа'), ('Individual', 'Фізична особа')]
    )  # Тип клієнта
    address = models.CharField(max_length=255, blank=True, null=True)  # Адреса
    phone = models.CharField(max_length=10)  # Номер телефону
    contact_person = models.CharField(max_length=100, blank=True, null=True)  # Контактна особа
    account_number = models.CharField(max_length=20, blank=True, null=True)  # Номер рахунку

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return f"{self.company_name} ({self.client_type})"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Унікальний ідентифікатор продукту
    product_name = models.CharField(max_length=100)  # Назва продукту
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна продукту
    quantity_in_store = models.IntegerField()  # Кількість на складі

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.product_name


class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)  # Унікальний ідентифікатор продажу
    sale_date = models.DateField()  # Дата продажу
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales')  # Зв'язок із клієнтом
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')  # Зв'язок із продуктом
    quantity_sold = models.IntegerField()  # Продана кількість
    discount = models.DecimalField(max_digits=3, decimal_places=2)  # Знижка
    payment_method = models.CharField(
        max_length=20,
        choices=[('Cash', 'Готівка'), ('Non-cash', 'Безготівковий')]
    )  # Метод оплати
    delivery_needed = models.BooleanField(default=False)  # Чи потрібна доставка
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Вартість доставки

    class Meta:
        db_table = 'sales'

    def __str__(self):
        return f"Sale {self.sale_id} on {self.sale_date}"
