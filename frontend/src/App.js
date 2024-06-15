import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import DepartmentManagement from './components/DepartmentManagement';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/dashboard" component={Dashboard} />
        <Route path="/departments" component={DepartmentManagement} />
        <Route path="/" component={Login} />
      </Switch>
    </Router>
  );
};

export default App;

