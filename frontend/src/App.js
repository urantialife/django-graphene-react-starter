import React, { Component } from 'react';
import { 
  BrowserRouter as Router,
  //Route,
  Link
} from 'react-router-dom';
import './App.css';
import HeaderContentFooter from './layouts/HeaderContentFooter';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <HeaderContentFooter>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/ingredients/">Ingredients</Link></li>
          </ul>
            <p>This is a child</p>
          </HeaderContentFooter>
          {/*<Route exact path="/" component={HomeView} />
          <Route exact path="/ingredients/" component={IngredientsView} />*/}
          </div>
        </Router>
    );
  }
}

export default App;
