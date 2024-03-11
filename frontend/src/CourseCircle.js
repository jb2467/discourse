import React, { Component } from 'react';
import { Container, Button } from 'reactstrap';
import './CourseCircleStyle.css'; 
import { Link } from 'react-router-dom';

class CourseCircle extends Component {
  render() {
    const { course_code } = this.props;
    return (
      <Container>
        <Link to="/home">
          <Button color='primary' className='course-circle'>
            <div className="circle-content">{course_code}</div>
          </Button>
        </Link>
      </Container>
    );
  }
}

export default CourseCircle;
