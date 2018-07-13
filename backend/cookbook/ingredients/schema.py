# cookbook/ingredients/schema.py
import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.ingredients.models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (graphene.Node, )

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (graphene.Node, )

class Query(object):
    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())
    all_categories = DjangoFilterConnectionField(CategoryType)


    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                name=graphene.String())
    all_ingredients = DjangoFilterConnectionField(IngredientType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)

        return None

# Mutations

class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String(required=True)
    
    @staticmethod
    def mutate(root, info, name):
        category = Category(name=name)
        category.save()
        return CreateCategory(category=category)

class CreateIngredient(graphene.Mutation):
    ingredient = graphene.Field(IngredientType)

    class Arguments:
        name = graphene.String(required=True)
        notes = graphene.String(required=True)
        category = graphene.String(required=True)
    
    @staticmethod
    def mutate(root, info, name, notes, category):
        ingredient = Ingredient(
            name=name,
            notes=notes,
            category = Category.objects.get_or_create(name=category)[0]
        )
        ingredient.save()
        return CreateIngredient(ingredient=ingredient)

class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    create_ingredient = CreateIngredient.Field()