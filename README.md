# django-graphene-react-starter

Simple hackathon starter with Django, Graphene, React, and Ant Design. Back end will expose a GraphQL API. Routing and views will be handled on the front end. Still working on making this page comprehensive so it's as helpful as possible for rapid development during a hackathon.

#### Rationale behind choice of technologies

Well-documented (with the exception of Graphene...), popular, easy to pick up, easy to find answers to questions. This project is intended to help more than hinder development. No fancy bells and whistles. The basics so you can focus on building.

#### Quick links

* If you've never used Django before [check out the official Django tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/). 
* [GraphQL?](https://www.howtographql.com/basics/0-introduction/)
* Graphene is "a framework for building GraphQL APIs in Python."
* [Here](https://reactjs.org/tutorial/tutorial.html) you can find an intro to React.
* [Ant Design documentation](https://ant.design/docs/react/introduce)

## Back end

Follows the sample cookbook application on the Graphene/Django with Relay tutorial [here](http://docs.graphene-python.org/projects/django/en/latest/tutorial-relay/). Authentication set up is in `users/schema.py` and follows [this tutorial](https://www.howtographql.com/graphql-python/4-authentication/). While auth is included here, users are not tied to any models in the ingredients app. To get started:

1. Create a virtualenv and activate (if you don't have virtualenv then run `pip install virtualenv`)

```
virtualenv env
source env/bin/activate
```

2. Install requirements

```
cd backend/cookbook
pip install requirements.txt
```

3. Create a local settings file in the cookbook directory (`backend/cookbook/local_settings.py`)

Inside the file put:

```
SECRET_KEY = 'MY SECRET KEY HERE (this is a placeholder, you need to generate a secret key)'
```

4. Make migrations

```
python manage.py makemigrations
python manage.py migrate
```

5. (optional) Add sample ingredients to make sure everything is working (this is coming from the `ingredients.json` file in `backend/cookbook`)

```
python manage.py loaddata ingredients
```

6. (optional) Run tests (located in `backend/ingredients/tests`)

```
python manage.py test
```

These tests are just to make sure everything works out of the box. If you make changes to the models/schema, you will need to edit or modify the tests accordingly. 

7. Run it

```
python manage.py runserver
```

8. Go to `localhost:8000/graphql` and test sample queries (copied from tutorial pages). 

List all ingredients

```
query {
  allIngredients {
    edges {
      node {
        id
        name
      }
    }
  }
}
```

Get an ingredient with a specific ID

```
query {
  ingredient(id: "SW5ncmVkaWVudE5vZGU6MQ==") {
    name
  }
}
```

Get an ingredient with a name that contains the letter 'e'

```
query {
  # You can also use `category: "CATEGORY GLOBAL ID"`
  allIngredients(name_Icontains: "e", category_Name: "Meat") {
    edges {
      node {
        name
      }
    }
  }
}
```

Get users

```
query {
  users {
    id
    username
    email
  }
}
```

#### Mutations

Create a category
```
mutation {
    createCategory(name: "My Category") {
        category {
            name
        }
    }
}
```

Create an ingredient

```
mutation {
    createIngredient(
        name: "Milk",
        notes: "fat free",
        category: "Dairy"
    ) {
        ingredient {
            name
            notes
        }
    }
}
```

*to do* update, delete

#### Adding an application

```
python manage.py startapp app_name
```

1. Add your application to `backend/cookbook/settings.py`
2. Create your models and add a schema.py file
3. Add your models in `app_name/admin.py`
3. Make migrations
4. Import your app's Query, Mutation, etc. in `backend/cookbook/schema.py` 

See Django model field reference [here](https://docs.djangoproject.com/en/2.0/ref/models/fields/).

Commonly used fields: CharField, IntegerField, DecimalField, DateField, ImageField, TextField, ForeignKey

#### Using admin interface

```
python manage.py createsuperuser
```

Then you can login @ `localhost:8000/admin`. If your models have been added in `*/admin.py` then you can visualize them on the admin interface. 

#### Adding filters
*to do*
Django-filter is installed. You can read about filtering on the [Graphene documentation page for it](http://docs.graphene-python.org/projects/django/en/latest/filtering/).

#### Form validation
*to do*
[Documentation here](https://docs.djangoproject.com/en/2.0/ref/forms/validation/). On the [Graphene side](http://docs.graphene-python.org/projects/django/en/latest/form-mutations/).

---

## Front end
This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app). A note on Ant Design: 

#### How does the front end communicate with the back end?
*to do* 

#### What goes where
*to do*

* `layouts/` - for page structure templates
* `components/` - for components
* `pages/` - for pages
* `utils/` - for extra settings and configurations

#### Getting started

1. Install requirements
```
cd frontend
sudo npm install -g yarn
yarn install
```

2. Start application
```
yarn start
```

3. 

#### How to add a component
*to do*

#### Styling
*to do*
Need to explore what people favor... styled components? External Less/Sass? Plain CSS files?

###### Typography
*to do*
This project uses [Typography.js](https://kyleamathews.github.io/typography.js/). You can find the config in `frontend/utils/typography.js`.

---

## Deploy

Debug false, whitenoise, etc.

#### Heroku

#### AWS