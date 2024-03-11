import React, { useState, useEffect } from 'react';
import { Row, Col, Button, Input, Card, Container, CardBody } from 'reactstrap';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import './App.css';
import AddUser from './AddUser';
import LoginUser from './LoginUser';
import LogoutUser from './LogoutUser';
import View from './View'
import Cookies from 'js-cookie';

function App() {
  const [users, setUsers] = useState([]);
  const username = Cookies.get('username');
  const fetchData = async () => {
    const response = await fetch(`http://127.0.0.1:4999/users`);
    const data = await response.json();
    //id, username, password, email, session_key 
    const userData = data.map((userArray) => ({
      id: userArray[0],
      username: userArray[1],
      password:userArray[2],
      email: userArray[3],
      key: userArray[4]
    }));
    setUsers(userData);
  };
  useEffect(() => {
    fetchData();
  }, []);
  return (
    <Router>
      <Switch>

        <Route path ='/login'>
          <LoginUser fetchData={fetchData} ></LoginUser>
        </Route>
        <Route path='/home'>
          <View></View>
        </Route>
        <Route path ='/'>
          <AddUser fetchData={fetchData}  />
        </Route>
      </Switch>
    </Router>
    
  );
}

export default App;
