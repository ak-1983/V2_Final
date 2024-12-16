# Peer Evaluation System

The **Peer Evaluation System** is a reliable and scalable solution designed to enhance the learning experience in large class sizes. This system facilitates fair and efficient assessment by leveraging peer feedback, enabling participants to evaluate each other's work under structured guidelines. The system allows teachers to track student learning outside the class without any extra workload.

---

## Features

### Core Functionalities
* **Automated File Mapping (OCR):** Files are renamed using the number from the top-left corner and mapped to the student with the corresponding unique ID for the current exam.
* **Automated File Distribution:** Files are automatically distributed to students for evaluation based on class size or the number of students who appeared in the exam.
* **Tiered Ticket Raising:** A tiered ticketing system for peer evaluation, allowing issues to be escalated based on complexity.

---

## Installation and Setup

### Prerequisites
You only need **Git** to clone the repository. Docker will handle all other dependencies.

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/sudarshansudarshan/peerevaluation.git
   cd peerevaluation
   cd PeerEvaluationV1
   ```

2. **Configure Settings**
   * The Docker container will automatically handle all dependencies, including the database.
   * However, you'll need to configure your PostgreSQL credentials:
     - Add your PostgreSQL credentials in the `settings.py` file, specifically in the Database section (line 78).
     - If you'd like to use your email to send notifications, configure your email settings near line 143.

3. **Running the Application with Docker**
   The system has been Dockerized. To run the application, simply execute the following commands:
   ```bash
   sudo docker-compose down || true
   sudo docker-compose up --build
   ```

   This will build the Docker containers and set up the application. All dependencies, including Python packages and PostgreSQL, will be automatically set up inside the container.

---

## Documentation
For detailed documentation and guides, please refer to the PDF files in the **Documentation** folder of the repository.

---

For any inquiries, feedback, or suggestions, feel free to:
* Open an issue on the repository.
* Reach out to the maintainers at:
  * ashu.kaushik@iitrpr.ac.in
  * rohit.24csz0014@iitrpr.ac.in

--- 
