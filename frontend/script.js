// Backend API URL - Update this with your Railway deployment URL
const API_URL = "https://student-management-system-backend-production.up.railway.app";

// Show notification messages
function showMessage(message, type = 'success') {
  const existingMessage = document.querySelector('.message');
  if (existingMessage) {
    existingMessage.remove();
  }

  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${type}`;
  messageDiv.textContent = message;
  
  const container = document.querySelector('.container');
  container.insertBefore(messageDiv, container.firstChild);
  
  setTimeout(() => {
    messageDiv.remove();
  }, 3000);
}

// Handle form submit (Add or Update)
document.getElementById("studentForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const id = document.getElementById("studentId").value;
  const name = document.getElementById("name").value;
  const marks = parseInt(document.getElementById("marks").value);
  const attendance = parseInt(document.getElementById("attendance").value);

  // Validation
  if (marks < 0 || marks > 100) {
    showMessage("Marks must be between 0 and 100", "error");
    return;
  }
  
  if (attendance < 0 || attendance > 100) {
    showMessage("Attendance must be between 0 and 100", "error");
    return;
  }

  const studentData = { name, marks, attendance };

  try {
    if (id) {
      // Update existing student
      const response = await fetch(`${API_URL}/students/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(studentData),
      });
      
      if (!response.ok) throw new Error('Failed to update student');
      showMessage("Student updated successfully!");
    } else {
      // Add new student
      const response = await fetch(`${API_URL}/students`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(studentData),
      });
      
      if (!response.ok) throw new Error('Failed to add student');
      showMessage("Student added successfully!");
    }

    loadStudents(); // Refresh list
    e.target.reset(); // Reset form
    document.getElementById("studentId").value = ""; // Clear hidden ID
  } catch (error) {
    console.error('Error:', error);
    showMessage("Error: " + error.message, "error");
  }
});

// Load student list
async function loadStudents() {
  const list = document.getElementById("studentList");
  list.innerHTML = '<div class="loading">Loading students...</div>';

  try {
    const response = await fetch(`${API_URL}/students`);
    if (!response.ok) throw new Error('Failed to fetch students');
    
    const data = await response.json();
    list.innerHTML = "";

    if (data.length === 0) {
      list.innerHTML = '<div class="loading">No students found. Add your first student!</div>';
      return;
    }

    data.forEach((student) => {
      const card = document.createElement("div");
      card.className = "student-card";

      card.innerHTML = `
        <div class="student-info">
          <span><strong>Name:</strong> ${student.name}</span>
          <span><strong>Marks:</strong> ${student.marks}/100</span>
          <span><strong>Attendance:</strong> ${student.attendance}%</span>
        </div>
        <div class="student-actions">
          <button class="edit-btn" onclick="editStudent(${student.id}, '${student.name}', ${student.marks}, ${student.attendance})">
            Edit
          </button>
          <button class="delete-btn" onclick="deleteStudent(${student.id})">
            Delete
          </button>
        </div>
      `;

      list.appendChild(card);
    });
  } catch (error) {
    console.error('Error:', error);
    list.innerHTML = '<div class="error">Error loading students. Please check your connection.</div>';
  }
}

// Edit student function
function editStudent(id, name, marks, attendance) {
  document.getElementById("studentId").value = id;
  document.getElementById("name").value = name;
  document.getElementById("marks").value = marks;
  document.getElementById("attendance").value = attendance;
  
  // Scroll to form
  document.getElementById("studentForm").scrollIntoView({ behavior: 'smooth' });
}

// Delete student function
async function deleteStudent(id) {
  if (!confirm("Are you sure you want to delete this student?")) {
    return;
  }

  try {
    const response = await fetch(`${API_URL}/students/${id}`, { 
      method: "DELETE" 
    });
    
    if (!response.ok) throw new Error('Failed to delete student');
    
    showMessage("Student deleted successfully!");
    loadStudents();
  } catch (error) {
    console.error('Error:', error);
    showMessage("Error deleting student: " + error.message, "error");
  }
}

// Initial load
document.addEventListener('DOMContentLoaded', () => {
  loadStudents();
}); 