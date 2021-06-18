import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
// import HomePage from './HomePage';
import CreateInsight from './CreateInsight';
import HomePage from './HomePage';
import { BrowserRouter as Router,  Switch, Route, Link } from "react-router-dom";

// document.body.style.backgroundColor = "#F4F4F4";

function App() {
  document.body.style.backgroundColor = "#F4F4F4";

  return (
    <Router>
    <div className="App">
      <link rel="preconnect" href="https://fonts.gstatic.com"/>
      <link href="https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet"/>
      <Route exact={true} path="/">
        <HomePage/>
      </Route>
      <Route exact={true} path="/criarInsight">
        <CreateInsight/>
      </Route>
    </div>
    </Router>
  );
}

export default App;
