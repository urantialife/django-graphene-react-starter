import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import client from './utils/client.js';
import { ApolloProvider } from 'react-apollo'

ReactDOM.render(
    <ApolloProvider client={client}>
      <App />
    </ApolloProvider>,
    document.getElementById('root')
  )
  
ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();