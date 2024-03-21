import React, {useState} from 'react'

const StudentRegistration = () => {
    
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [dateOfBirth, setDateOfBirth] = useState('');
    const [address, setAddress] = useState('');
    const [parentEmail, setParentEmail] = useState('');
    const [parentPhone, setParentPhone] = useState('');

    // Handle Form Submission
    const handleSubmit = (event) => {
        event.preventDefault();
        //code to the backend
        console.log('Form submitted:', { firstName, lastName, dateOfBirth, address, parentEmail, parentPhone });
        // Reset Form
        setFirstName('');
        setLastName('');
        setDateOfBirth('');
        setAddress('');
        setParentEmail('');
        setParentPhone('');
        
    };

  return (
    <div>
          <h2>Student Registration Form</h2>
          <form onSubmit={handleSubmit}>
              <div>
                  <label htmlFor='firstName'>First Name:</label>
                  <input type='text' id='firstName' value={firstName} onChange={(e) => setFirstName(e.target.value)} required />

              </div>
              <div>
                <label htmlFor="lastName">Last Name:</label>
                <input type="text" id="lastName" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
              </div>
              <div>
                <label htmlFor="dateOfBirth">Date of Birth:</label>
                <input type="date" id="dateOfBirth" value={dateOfBirth} onChange={(e) => setDateOfBirth(e.target.value)} required />
              </div>
              <div>
                <label htmlFor="address">Address:</label>
                <textarea id="address" value={address} onChange={(e) => setAddress(e.target.value)} required />
              </div>
              <div>
                <label htmlFor="parentEmail">Parent Email:</label>
                <input type="email" id="parentEmail" value={parentEmail} onChange={(e) => setParentEmail(e.target.value)} required />
              </div>
              <div>
                <label htmlFor="parentPhone">Parent Phone:</label>
                <input type="tel" id="parentPhone" value={parentPhone} onChange={(e) => setParentPhone(e.target.value)} required />
              </div>
              <button type="submit">Register</button>
                    
          </form>
      
    </div>
  )
}

export default StudentRegistration
