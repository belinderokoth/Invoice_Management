from django.db import models

# Create your models here.
class Invoice(models.Model):
    from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    # Add other client fields as needed

class Invoice(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=20)
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other invoice fields as needed

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other item fields as needed


admin.site.register(Invoice)
    	comments = models.TextField(max_length=3000, default='', blank=True, null=True)
	invoice_number = models.IntegerField(blank=True, null=True)
	invoice_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
	name = models.CharField('Customer Name', max_length=120, default='', blank=True, null=True)
	
	line_one = models.CharField('Line 1', max_length=120, default='', blank=True, null=True)
	line_one_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_one_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
	line_one_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

	line_two = models.CharField('Line 2', max_length=120, default='', blank=True, null=True)
	line_two_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_two_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
	line_two_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

	line_three = models.CharField('Line 3', max_length=120, default='', blank=True, null=True)
	line_three_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_three_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
	line_three_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

	line_four = models.CharField('Line 4', max_length=120, default='', blank=True, null=True)
	line_four_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_four_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
	line_four_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

	line_five = models.CharField('Line 5', max_length=120, default='', blank=True, null=True)
	line_five_quantity = models.IntegerField('Quantity', default=0, blank=True, null=True)
	line_five_unit_price = models.IntegerField('Unit Price (D)', default=0, blank=True, null=True)
	line_five_total_price = models.IntegerField('Line Total (D)', default=0, blank=True, null=True)

	phone_number = models.CharField(max_length=120, default='', blank=True, null=True)
	total = models.IntegerField(default='0', blank=True, null=True)
	balance = models.IntegerField(default='0', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
	paid = models.BooleanField(default=False)
	invoice_type_choice = (
			('Receipt', 'Receipt'),
			('Proforma Invoice', 'Proforma Invoice'),
			('Invoice', 'Invoice'),
		)
	invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

	def __unicode__(self):
		return self.invoice_number
