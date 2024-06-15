import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const login = async (username, password) => {
  try {
    const response = await axios.post(`${API_URL}/api/token/`, { username, password });
    return response.data;
  } catch (error) {
    console.error('Login failed', error);
    throw error;
  }
};

export const fetchTasks = async () => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.get(`${API_URL}/api/tasks/`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching tasks', error);
    throw error;
  }
};

export const createTask = async (task) => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.post(`${API_URL}/api/tasks/`, task, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating task', error);
    throw error;
  }
};

export const updateTask = async (taskId, task) => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.put(`${API_URL}/api/tasks/${taskId}`, task, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error('Error updating task', error);
    throw error;
  }
};

export const deleteTask = async (taskId) => {
  const token = localStorage.getItem('token');
  try {
    await axios.delete(`${API_URL}/api/tasks/${taskId}`, {
      headers: { Authorization: `Bearer ${token}` },
    });
  } catch (error) {
    console.error('Error deleting task', error);
    throw error;
  }
};

export const fetchDepartments = async () => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.get(`${API_URL}/api/departments/`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching departments', error);
    throw error;
  }
};

export const createDepartment = async (department) => {
  const token = localStorage.getItem('token');
  try {
    const response = await axios.post(`${API_URL}/api/departments/`, department, {
      headers: { Authorization: `Bearer ${token}` },
    });
    return response.data;
  } catch (error) {
    console.error('Error creating department', error);
    throw error;
  }
};

