import React, { Component } from 'react';
import { 
  BrowserRouter as Router,
  Route
} from 'react-router-dom';
import './App.css';
import HomeView from './components/HomeView';
import HeaderContentFooter from './layouts/HeaderContentFooter';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <HeaderContentFooter>
            <Route exact path="/" component={HomeView} />
            {/*<Route exact path="/ingredients/" component={IngredientsView} />*/}
          </HeaderContentFooter>
          </div>
        </Router>
    );
  }
}

export default App;
