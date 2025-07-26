const API_URL = "/students";

// Handle form submit (Add or Update)
document.getElementById("studentForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const id = document.getElementById("studentId").value;
  const name = document.getElementById("name").value;
  const marks = document.getElementById("marks").value;
  const attendance = document.getElementById("attendance").value;

  const studentData = { name, marks, attendance };

  if (id) {
    // Update existing student
    await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(studentData),
    });
  } else {
    // Add new student
    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(studentData),
    });
  }

  loadStudents(); // Refresh list
  e.target.reset(); // Reset form
  document.getElementById("studentId").value = ""; // Clear hidden ID
});

// Load student list
async function loadStudents() {
  const res = await fetch(API_URL);
  const data = await res.json();
  const list = document.getElementById("studentList");
  list.innerHTML = "";

  data.forEach((student) => {
    const li = document.createElement("li");
    li.className = "student-card";

    li.innerHTML = `
      <span><strong>Name:</strong> ${student.name}</span>
      <span><strong>Marks:</strong> ${student.marks}</span>
      <span><strong>Attendance:</strong> ${student.attendance}%</span>
    `;

    // Edit Button
    const editBtn = document.createElement("button");
    editBtn.textContent = "Edit";
    editBtn.onclick = () => {
      document.getElementById("studentId").value = student.id;
      document.getElementById("name").value = student.name;
      document.getElementById("marks").value = student.marks;
      document.getElementById("attendance").value = student.attendance;
    };

    // Delete Button
    const delBtn = document.createElement("button");
    delBtn.textContent = "Delete";
    delBtn.onclick = async () => {
      await fetch(`${API_URL}/${student.id}`, { method: "DELETE" });
      loadStudents();
    };

    li.appendChild(editBtn);
    li.appendChild(delBtn);
    list.appendChild(li);
  });
}

// Initial load
loadStudents();
