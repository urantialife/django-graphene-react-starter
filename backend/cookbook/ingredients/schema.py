# cookbook/ingredients/schema.py
from graphene import relay, ObjectType, String, Field, AbstractType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.ingredients.models import Category, Ingredient


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class Query(object):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)

# Mutations

class CreateCategory(relay.ClientIDMutation):
    category = Field(CategoryNode)

    class Input:
        name = String(required=True)
        
    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        category = Category(name=input.get('name'))
        category.save()
        return CreateCategory(category=category)


class CreateIngredient(relay.ClientIDMutation):
    ingredient = Field(IngredientNode)

    class Input:
        name = String(required=True)
        notes = String(required=True)
        category = String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        ingredient = Ingredient(
            name=input.get('name'),
            notes=input.get('notes'),
            category = Category.objects.get_or_create(name=input.get('category'))[0]
        )
        ingredient.save()
        return CreateIngredient(ingredient=ingredient)

class Mutation(ObjectType):
    create_category = CreateCategory.Field()
    create_ingredient = CreateIngredient.Field()