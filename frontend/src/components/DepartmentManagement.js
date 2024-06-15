import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DepartmentManagement = () => {
  const [departments, setDepartments] = useState([]);
  const [name, setName] = useState('');

  useEffect(() => {
    const fetchDepartments = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await axios.get('http://localhost:5000/api/departments/', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setDepartments(response.data);
      } catch (error) {
        console.error('Error fetching departments', error);
      }
    };

    fetchDepartments();
  }, []);

  const handleCreateDepartment = async () => {
    const token = localStorage.getItem('token');
    try {
      const response = await axios.post(
        'http://localhost:5000/api/departments/',
        { name },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setDepartments([...departments, response.data]);
      setName('');
    } catch (error) {
      console.error('Error creating department', error);
    }
  };

  return (
    <div>
      <h2>Department Management</h2>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Department Name"
      />
      <button onClick={handleCreateDepartment}>Create Department</button>
      <ul>
        {departments.map((department) => (
          <li key={department.id}>{department.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default DepartmentManagement;

