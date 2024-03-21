import React, { useState } from 'react';

function GradeEntry() {
  const [formData, setFormData] = useState({
    studentName: '',
    subject: '',
    grade: '',
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
    // Reset the form after submission
    setFormData({
      studentName: '',
      subject: '',
      grade: '',
      // Reset other fields as needed
    });
  };

  return (
    <div>
      <h2>Grade Entry</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="studentName">Student Name:</label>
          <input
            type="text"
            id="studentName"
            name="studentName"
            value={formData.studentName}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="subject">Subject:</label>
          <input
            type="text"
            id="subject"
            name="subject"
            value={formData.subject}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="grade">Grade:</label>
          <input
            type="text"
            id="grade"
            name="grade"
            value={formData.grade}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Submit Grade</button>
      </form>
    </div>
  );
}

export default GradeEntry;
