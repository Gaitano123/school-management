import './App.css';
import StudentRegistration from './Forms/StudentRegistration';
import TeacherRegistration from './Forms/TeacherRegistration';
import ClassCreation from './Forms/ClassCreation';
import GradeEntry from './Forms/GradeEntry';
import HealthRecordForm from './Forms/HealthRecord';

function App() {
  return (
    <>
      <StudentRegistration />
      <TeacherRegistration />
      <ClassCreation />
      <GradeEntry />
      <HealthRecordForm />
      
    </>
  );
}

export default App;
