import React, { Component } from 'react';
import { FormGroup, Label, Input, Button, Container, Card, CardBody, Row, Col} from 'reactstrap';
import {Link, withRouter } from 'react-router-dom';
import Cookies from 'js-cookie';

class LoginUser extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      message: '',
    };
    }

  handleChange=(e)=>{
    const { name, value } = e.target;
    this.setState((prevState) => ({
        ...prevState,
        [name]: value,
      }));
  }
  loginUser = async () =>{
    const response = await fetch('http://127.0.0.1:4999/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.state),
    })
    const data = await response.json();

    if (response.ok) {
      this.setState({message: '' });
      this.props.fetchData()
      this.props.history.push('/home')
      Cookies.set('username', this.state.username);
      Cookies.set(`sessionToken_${this.state.username}`, data.session_token);
      return true
    } else {
      this.setState( {message: 'Please check username and password, and if the account exists'  });
      return false
    }
  }
  isValid = () => {
    return this.state.username.trim() !== ''  && this.state.password.trim() !== ''
      
  }

  render(){
    const isValid = this.isValid();
    return(
        <div>
          <h1 style={{ textAlign: 'center' }}>Login Below</h1>
          <Container>
            <Card>
              <CardBody>
                <FormGroup>
                  <Label for="Username">Please enter username</Label>
                  <Input type="text" name="username" id="username" value={this.state.username} onChange={this.handleChange} />
                </FormGroup>
                <FormGroup>
                  <Label for="Password">Please enter password</Label>
                  <Input type="password" name="password" id="password" value={this.state.password} onChange={this.handleChange} />
                </FormGroup>
                <Row className="justify-content-end">
                  <Col md='9'>
                    {isValid ? (
                      <Link to="/login" onClick={() => this.loginUser()}>
                        <Button color='primary'>Login</Button>
                      </Link>
                    ) : (
                      <Button disabled>Login</Button>
                    )}     
                  </Col>
                  <Col md='3'>
                    <Link to="/">
                      <Button color="success">Register an account</Button>
                    </Link>
                  </Col>
                </Row>
                <p>{this.state.message}</p>
              </CardBody>
            </Card>  
          </Container>
        </div>
    );
  }
}
export default withRouter(LoginUser);
