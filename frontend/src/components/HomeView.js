import React, { Component } from 'react';
import gql from "graphql-tag";
import { Query } from "react-apollo";

const GET_INGREDIENTS = gql`
{
    allIngredients {
      edges {
        node {
          name
        }
      }
    }
}
`

const Ingredients = () => (
    <Query query={GET_INGREDIENTS}>
        {({ loading, error, data }) => {
        if (loading) return "Loading...";
        if (error) return `Error! ${error.message}`;
  
        return (
            {data}
        );
      }}
    </Query>
);
class HomeView extends Component {
  render() {
    return (
        <div>hello
            <Ingredients />
        </div>
    );
  }
}

export default HomeView;