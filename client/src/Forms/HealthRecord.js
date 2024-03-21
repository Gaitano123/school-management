import React, { useState } from 'react';

function HealthRecordForm() {
  const [formData, setFormData] = useState({
    headId: '',
    captainId: '',
    symptoms: '',
    sickness: '',
    sickLeave: '',
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
      headId: '',
      captainId: '',
      symptoms: '',
      sickness: '',
      sickLeave: '',
      // Reset other fields as needed
    });
  };

  return (
    <div>
      <h2>Health Record Form</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="headId">Head ID:</label>
          <input
            type="text"
            id="headId"
            name="headId"
            value={formData.headId}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="captainId">Captain ID:</label>
          <input
            type="text"
            id="captainId"
            name="captainId"
            value={formData.captainId}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="symptoms">Symptoms:</label>
          <textarea
            id="symptoms"
            name="symptoms"
            value={formData.symptoms}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="sickness">Sickness:</label>
          <input
            type="text"
            id="sickness"
            name="sickness"
            value={formData.sickness}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="sickLeave">Sick Leave:</label>
          <input
            type="text"
            id="sickLeave"
            name="sickLeave"
            value={formData.sickLeave}
            onChange={handleChange}
            required
          />
        </div>
        {/* Add more input fields for additional information */}
        <button type="submit">Submit Health Record</button>
      </form>
    </div>
  );
}

export default HealthRecordForm;
