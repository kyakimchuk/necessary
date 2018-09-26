from django.db import models
# from django.utils import timezone


class Category1(models.Model):
	name = models.CharField(max_length=60, verbose_name="Название")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория1"
		verbose_name_plural = "Категории1"


class Category2(models.Model):
	name = models.CharField(max_length=60, verbose_name="Название")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория2"
		verbose_name_plural = "Категории2"


class Category3(models.Model):
	name = models.CharField(max_length=60, verbose_name="Название")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория3"
		verbose_name_plural = "Категории3"


class CategoryHierarchy(models.Model):
	cat1 = models.ForeignKey('Category1', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория1")
	cat2 = models.ForeignKey('Category2', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория2")
	cat3 = models.ForeignKey('Category3', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория3")

	def __str__(self):
		cat1 = str(self.cat1)
		cat2 = str(self.cat2)
		cat3 = str(self.cat3)
		if not cat1:
			cat1 = ""
		if not cat2:
			cat2 = ""
		if not cat3:
			cat3 = ""
		return cat1 + " -> " + cat2 + " -> " + cat3

	class Meta:
		verbose_name = "Иерархия категорий"
		verbose_name_plural = "Иерархии категорий"


class Thing(models.Model):
	cat_hierar = models.ForeignKey('CategoryHierarchy', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Иерархия категорий")
	name = models.CharField(max_length=60, verbose_name="Название")
	description = models.TextField(null=True, blank=True, verbose_name="Описание")
	price = models.IntegerField(verbose_name="Цена")
	size = models.CharField(null=True, blank=True, max_length=15, verbose_name="Размер")
	photo1 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото1")
	photo2 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото2")
	photo3 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото3")
	photo4 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото4")
	photo5 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото5")
	photo6 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото6")
	photo7 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото7")
	photo8 = models.ImageField(upload_to="photos/", null=True, blank=True, verbose_name="Фото8")


	def __str__(self):
		return self.name

	def show_image(self):
		if self.photo1:
			return u'<img src="%s" width="100">' % self.photo1.url

	show_image.short_description = 'Фото'
	show_image.allow_tags = True

	class Meta:
		verbose_name = "Вещь"
		verbose_name_plural = "Вещи"





# class Post(models.Model):
#     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)