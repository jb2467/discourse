import React, { Component } from 'react';
import { FormGroup, Label, Input, Button, Container, Card, CardBody, Row, Col} from 'reactstrap';
import {Link, withRouter } from 'react-router-dom'
class AddUser extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      email: '',
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
  addUser = async () =>{
    const response = await fetch('http://127.0.0.1:4999/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.state),
    });
    if (response.ok) {
      this.setState({message: '' });
      this.props.fetchData()
      this.props.history.push('/login')
      return true
    } else {
      this.setState( {message: 'User was already registered, Login now'  });
      return false
    }
  }
  isValid = () => {
    return this.state.username.trim() !== '' && this.state.email.trim() !== '' && this.state.password.trim() !== ''
      
  }

  render(){
    const isValid = this.isValid();
    return(
        <div>
          <h1 style={{ textAlign: 'center' }}>Register your account below</h1>
          <Container>
            <Card>
              <CardBody>
                <FormGroup>
                  <Label for="Email">Please enter email</Label>
                  <Input type="text" name="email" id="email" value={this.state.email} onChange={this.handleChange} />
                </FormGroup>
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
                      <Link to="/" onClick={() => this.addUser()}>
                        <Button color='primary'>Add User</Button>
                      </Link>
                    ) : (
                      <Button disabled>Add User</Button>
                    )}     
                  </Col>
                  <Col md='3'>
                    <Link to="/login">
                      <Button className= 'login' color="success">Login</Button>
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
export default withRouter(AddUser);
