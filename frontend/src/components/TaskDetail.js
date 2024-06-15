import React from 'react';

const TaskDetail = ({ task }) => {
  return (
    <li>
      <h4>{task.title}</h4>
      <p>{task.description}</p>
      <p>{task.due_date}</p>
    </li>
  );
};

export default TaskDetail;

