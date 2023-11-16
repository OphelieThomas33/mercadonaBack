from Catalog.models import Category, Product, Discount

from django.contrib import admin


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    # discount display fields
    list_display = (
        'start_date',
        'end_date',
        'percentage',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # product display fields
    list_display = (
        'label',
        'description',
        'price',
        'discount',
        'image_tag',
        'get_categories',
    )
    # get product list by category
    list_filter = ('category',)
    # allows to search for a product by label
    search_fields = ('label',)

    # get categories list for each product
    @admin.display(description="Catégories")
    def get_categories(self, obj):
        return "\n".join([c.label for c in obj.category.all()])


#
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # category display fields
    list_display = (
        'label',
        'parent',
        'get_products'
    )
    # allows to search for a category by label
    search_fields = ('label',)

    # get products list by category
    @admin.display(description="Produits")
    def get_products(self, obj):
        return "\n".join([p.label for p in obj.products.all()])



