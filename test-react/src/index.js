import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {App, Body} from './App';
//import Body from './App'
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
ReactDOM.render(<Body/>, document.getElementById('root'));
registerServiceWorker();
