import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import LoginUser from './LoginUser';
import LogoutUser from './LogoutUser';
import Cookies from 'js-cookie';
import { Row, Col, Button, Input, Card, Container, CardBody } from 'reactstrap';
import CourseCircle from './CourseCircle';


function View() {
  const [courses, setCourses] = useState([]);
  const fetchCourses = async () => {
    const username = Cookies.get('username'); 
    const response = await fetch(`http://127.0.0.1:4999/course/${username}`);
    const data = await response.json();
    const courseData = data.map((courseArray) => ({
      course_code: courseArray[0],
      section_code: courseArray[1],
      course_admin: courseArray[2],
      course_name: courseArray[3]
    }));
    setCourses(courseData); 
  };

  useEffect(() => {
    fetchCourses(); 
  }, []);
  console.log(courses);
  return (
    <div>
      <Row>
        <Col>
          {courses.map((c) => (
            <CourseCircle
              key={c.course_code}
              course_code={c.course_code}
              section_code={c.section_code}
              course_admin={c.course_admin}
              course_name={c.course_name}
            />
          ))}
        </Col>
        
        <Col md="4">
        </Col>

        <Col md="4">
        </Col>
      </Row>
    </div>
  );
}

export default View;