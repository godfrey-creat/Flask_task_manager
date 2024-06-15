import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TaskList from './TaskList';

const Dashboard = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetchTasks = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await axios.get('http://localhost:5000/api/tasks/', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setTasks(response.data);
      } catch (error) {
        console.error('Error fetching tasks', error);
      }
    };

    fetchTasks();
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      <TaskList tasks={tasks} />
    </div>
  );
};

export default Dashboard;

