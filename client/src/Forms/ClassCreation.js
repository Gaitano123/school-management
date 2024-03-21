import React, { useState } from 'react';

function ClassCreation() {
  const [formData, setFormData] = useState({
    className: '',
    classTeacher: '',
    // Add more fields as needed
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Implement submit logic here, such as sending the form data to a server
    console.log(formData);
    // Reset 
    setFormData({
      className: '',
      classTeacher: '',
    });
  };

  return (
    <div>
      <h2>Create a Class</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="className">Class Name:</label>
          <input
            type="text"
            id="className"
            name="className"
            value={formData.className}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="classTeacher">Class Teacher:</label>
          <input
            type="text"
            id="classTeacher"
            name="classTeacher"
            value={formData.classTeacher}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Create Class</button>
      </form>
    </div>
  );
}

export default ClassCreation;
