import React, { Component } from 'react';
import './App.css';
import HeaderContentFooter from './layouts/HeaderContentFooter';

class App extends Component {
  render() {
    return (
      <HeaderContentFooter>
        <p>This is a child</p>
      </HeaderContentFooter>
    );
  }
}

export default App;
