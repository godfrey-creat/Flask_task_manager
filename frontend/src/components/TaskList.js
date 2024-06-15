import React from 'react';
import TaskDetail from './TaskDetail';

const TaskList = ({ tasks }) => {
  return (
    <div>
      <h3>Tasks</h3>
      <ul>
        {tasks.map((task) => (
          <TaskDetail key={task.id} task={task} />
        ))}
      </ul>
    </div>
  );
};

export default TaskList;

