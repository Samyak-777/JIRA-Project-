# **Comprehensive Report: Docker Containerization Assignment**
## **Software Lab III (CSP300) - VNIT Nagpur**

***

### **Executive Summary**

This report presents the complete implementation and analysis of a comprehensive Docker containerization assignment undertaken as part of the Software Lab III course at Visvesvaraya National Institute of Technology, Nagpur. The project successfully demonstrates mastery of modern containerization technologies through the development and deployment of five distinct applications using Docker and Docker Compose.

The assignment encompasses practical implementation of containerization concepts, multi-container orchestration, image management through Docker Hub, database integration, and production-ready deployment strategies. All deliverables were successfully completed, demonstrating proficiency in DevOps practices and cloud-native application development.

***

## **1. Introduction**

### **1.1 Project Objectives**
The primary objective of this assignment was to demonstrate comprehensive understanding and practical application of Docker containerization technology. The project aimed to:

- Master fundamental Docker concepts including images, containers, and registries
- Implement multi-container applications using Docker Compose
- Demonstrate image management and distribution through Docker Hub
- Deploy various application architectures (web applications, APIs, static websites)
- Establish persistent data storage and container networking
- Apply DevOps best practices in containerized environments

### **1.2 Technology Stack**
- **Containerization**: Docker Desktop, Docker Compose
- **Programming Languages**: Python (Flask framework), HTML/CSS/JavaScript
- **Web Servers**: Nginx
- **Databases**: PostgreSQL, SQLite
- **Tools**: Visual Studio Code, PowerShell, Git
- **Platform**: Windows 10 with WSL2

### **1.3 Project Scope**
The assignment was structured into five major rubrics, each representing distinct aspects of containerization:

1. **Rubric 1**: Basic Application Containerization (4 marks)
2. **Rubric 2**: Multi-Container Applications with Docker Compose (4 marks)  
3. **Rubric 3**: Docker Hub Image Management (6 marks)
4. **Rubric 4**: Database-Integrated To-Do Application (6 marks)
5. **Rubric 5**: Static Website and API Deployment (6 marks)

***

## **2. Technical Implementation**

### **2.1 Rubric 1: Simple Python Application Containerization**

**Implementation Details:**
- Developed a Flask-based web application providing container information and environment details
- Created optimized Dockerfile following best practices
- Successfully built and deployed container with proper port mapping

**Key Components:**
```python
# app.py - Core Flask Application
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f'''
    <h1>Hello from Docker Container!</h1>
    <p>Container ID: {os.uname().nodename}</p>
    <p>Environment: {os.environ.get('ENVIRONMENT', 'Development')}</p>
    '''
```

**Dockerfile Configuration:**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["python", "app.py"]
```

**Results:**
- Successfully built image: `simple_python_app:latest`
- Container runs on port 5000 with full functionality
- Demonstrates environment variable configuration
- Image size optimized to 198MB

**Screenshot Location:** *[Include screenshot of running application in browser showing container information]*

### **2.2 Rubric 2: Multi-Container Application with Docker Compose**

**Architecture Overview:**
Implemented a Flask web application with PostgreSQL database backend, demonstrating:
- Service orchestration using Docker Compose
- Database connectivity and data persistence
- Custom network configuration
- Volume mounting for data persistence

**Docker Compose Configuration:**
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - DB_NAME=testdb
      - DB_USER=testuser
      - DB_PASS=testpass
    networks:
      - app-network

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=testdb
      - POSTGRES_USER=testuser
      - POSTGRES_PASSWORD=testpass
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
    driver: bridge
```

**Application Features:**
- User registration and management system
- Real-time database interactions
- RESTful API endpoints for user operations
- Responsive web interface with AJAX functionality

**Results:**
- Successfully orchestrated multi-container environment
- Database persistence verified across container restarts
- Network isolation and service discovery functional
- Built images: `multi_app-web:latest`

**Screenshot Location:** *[Include screenshots of application interface and docker-compose ps output]*

### **2.3 Rubric 3: Docker Hub Image Management**

**Implementation Process:**
1. **Account Setup**: Created Docker Hub account (samyak77/simple_python_app)
2. **Image Tagging**: Applied semantic versioning (v1.0)
3. **Image Publishing**: Pushed custom images to public registry
4. **Verification**: Pulled and tested images from Docker Hub

**Commands Executed:**
```bash
# Login to Docker Hub
docker login

# Tag local image
docker tag simple_python_app samyak77/simple_python_app:v1.0

# Push to registry
docker push samyak77/simple_python_app:v1.0

# Verify by pulling
docker pull samyak77/simple_python_app:v1.0
```

**Registry Management:**
- Successfully published custom images to Docker Hub
- Implemented proper tagging strategy
- Verified image availability through public pull operations
- Demonstrated registry integration workflow

**Results:**
- Published image: `samyak77/simple_python_app:v1.0`
- Public registry accessibility confirmed
- Download and execution from registry successful
- Repository documentation maintained

**Screenshot Location:** *[Include screenshots of Docker Hub repository and CLI push/pull operations]*

### **2.4 Rubric 4: Dockerized To-Do List Application**

**Application Architecture:**
Developed a comprehensive task management system featuring:
- Full CRUD operations (Create, Read, Update, Delete)
- Interactive web interface with real-time updates
- SQLite database for data persistence
- Responsive design with modern UI elements

**Core Features:**
```python
# Key functionality excerpt
@app.route('/api/todos', methods=['GET', 'POST'])
def todos():
    conn = get_db_connection()
    
    if request.method == 'POST':
        task = request.json['task']
        conn.execute('INSERT INTO todos (task) VALUES (?)', (task,))
        conn.commit()
        return {'status': 'success'}
    
    else:  # GET
        todos = conn.execute('SELECT * FROM todos ORDER BY created_at DESC').fetchall()
        return jsonify([dict(todo) for todo in todos])
```

**Container Configuration:**
- Persistent volume mounting for database storage
- Port mapping for web access (5000:5000)
- Environment variable configuration
- Health check implementation

**User Interface Features:**
- Task creation with real-time addition
- Task completion toggling
- Task deletion with confirmation
- Modern CSS styling with animations
- Responsive design for various screen sizes

**Results:**
- Fully functional task management system
- Data persistence across container restarts verified
- Built image: `todo_app:latest` (197MB)
- User-friendly interface with smooth interactions

**Screenshot Location:** *[Include screenshots of to-do application interface showing tasks and functionality]*

### **2.5 Rubric 5: Static Website with Nginx and Python API Deployment**

**Component A: Static Website with Nginx**

**Website Features:**
- Professional multi-section website design
- Responsive CSS with gradient backgrounds
- Interactive JavaScript functionality
- Custom Nginx configuration for optimal performance

**Nginx Configuration:**
```nginx
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html index.htm;

    location / {
        try_files $uri $uri/ /index.html;
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-Content-Type-Options "nosniff" always;
    }

    location ~* \.(css|js|jpg|jpeg|png|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

**Component B: Python REST API**

**API Endpoints:**
- `GET /` - API information and documentation
- `GET /api/users` - User management endpoints
- `GET /api/tasks` - Task management functionality  
- `GET /health` - Health check endpoint
- `GET /api/stats` - System statistics

**API Features:**
```python
# Sample API endpoint
@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return jsonify(users_db)
    
    elif request.method == 'POST':
        data = request.json
        new_user = {
            "id": max([u["id"] for u in users_db]) + 1,
            "name": data["name"],
            "email": data["email"],
            "role": data.get("role", "user")
        }
        users_db.append(new_user)
        return jsonify(new_user), 201
```

**Results:**
- Static website successfully served via Nginx on port 8080
- Python API running on port 5000 with full REST functionality
- Built images: `static_website-nginx:latest` (79.4MB), `python_api:latest` (197MB)
- Both components demonstrate production-ready configurations

**Screenshot Location:** *[Include screenshots of static website and API JSON responses]*

***

## **3. Complete Stack Integration**

### **3.1 Unified Docker Compose Configuration**

Successfully created a comprehensive stack orchestrating all developed applications:

```yaml
version: '3.8'
services:
  static-website:
    image: static_website-nginx:latest
    ports: ["8080:80"]
    
  simple-python-app:
    image: simple_python_app:latest  
    ports: ["5000:5000"]
    
  python-api:
    image: python_api:latest
    ports: ["5001:5000"]
    
  todo-app:
    image: todo_app:latest
    ports: ["5002:5000"]
    volumes: ["todo_data:/app/data"]
    
  multi-web-app:
    image: multi_app-web:latest
    ports: ["5003:5000"]
    depends_on: ["postgres-db"]
    
  postgres-db:
    image: postgres:13
    environment:
      - POSTGRES_DB=testdb
      - POSTGRES_USER=testuser  
      - POSTGRES_PASSWORD=testpass
    volumes: ["postgres_data:/var/lib/postgresql/data"]

volumes:
  todo_data:
  postgres_data:

networks:
  default:
    name: complete-stack-network
```

### **3.2 Service Accessibility**

**Port Mapping Summary:**
- **Static Website**: http://localhost:8080
- **Simple Python App**: http://localhost:5000  
- **Python API**: http://localhost:5001
- **To-Do Application**: http://localhost:5002
- **Multi-Container App**: http://localhost:5003
- **PostgreSQL Database**: localhost:5432

***

## **4. Testing and Validation**

### **4.1 Functional Testing**

**Test Methodology:**
Each application component underwent comprehensive testing to verify:
- Container build success and optimization
- Port accessibility and service availability  
- Database connectivity and data persistence
- API endpoint functionality and response validation
- User interface responsiveness and feature completeness

**Test Commands Executed:**
```bash
# Container health verification
docker ps -a
docker logs [container-name]

# Service accessibility testing  
curl http://localhost:8080  # Static website
curl http://localhost:5001/health  # API health check
curl http://localhost:5001/api/users  # API functionality

# Database persistence testing
docker-compose down
docker-compose up -d
# Verify data retained after restart
```




## **9. Conclusion**

This comprehensive Docker assignment successfully demonstrates mastery of modern containerization technologies through practical implementation of diverse application architectures. The project showcases proficiency in:

- **Container Development**: Successfully containerized five distinct applications
- **Orchestration**: Implemented sophisticated multi-container coordination  
- **Registry Management**: Demonstrated professional image distribution workflows
- **Production Readiness**: Applied security, performance, and maintainability best practices

The completed assignment represents industry-standard containerization practices applicable to enterprise-level software development and deployment. The knowledge and skills acquired provide a solid foundation for advanced DevOps, cloud computing, and microservices development.


### **Appendix A: Complete File Structure**
```
docker-assignment-3/
├── simple-python-app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── multi-container-app/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── app.py
│   └── init.sql
├── todo-app/
│   ├── Dockerfile
│   └── app.py
├── static-website/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── python-api/
│   ├── Dockerfile
│   ├── app.py
│   └── test_api.py
└── complete-stack/
    ├── docker-compose.yml
    └── README.md
```

### **Appendix B: Key Docker Commands Used**
```bash
# Image Management
docker build -t [image-name] .
docker images
docker tag [source] [target]
docker push [image-name]
docker pull [image-name]

# Container Operations  
docker run -d -p [host-port]:[container-port] [image]
docker ps -a
docker logs [container-name]
docker exec -it [container] bash
docker stop [container]
docker rm [container]

# Docker Compose
docker-compose up --build -d
docker-compose ps
docker-compose logs
docker-compose down
```


