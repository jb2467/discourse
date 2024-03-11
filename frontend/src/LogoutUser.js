import React, { Component } from 'react';
import { Button} from 'reactstrap';
import {Link, withRouter } from 'react-router-dom';
import Cookies from 'js-cookie';
class LogoutUser extends Component {
  logoutUser = async () =>{
    const username = Cookies.get('username');
    const response = await fetch(`http://127.0.0.1:4999/logout/${username}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
    })
    if (response.ok) {
      Cookies.remove(`sessionToken_${username}`);
      this.props.fetchData()
      this.props.history.push('/')
      return true
    } else {
      return false
    }
  }

  render(){
    return(
        <div>
            <Link to="/" onClick={() => this.logoutUser()}>
                <Button color='primary'>Logout</Button>
            </Link>
        </div>
    );
  }
}
export default withRouter(LogoutUser);
