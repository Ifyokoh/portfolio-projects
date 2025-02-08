# **ETL Pipeline with Airflow & Docker**  
_Automating data extraction, transformation, and loading for wine quality analysis._  

## **Project Overview**  
This project is a fully automated ETL (Extract, Transform, Load) pipeline built with Apache Airflow and Docker. It processes a Wine Quality Dataset, cleaning and transforming the raw data before storing it in a PostgreSQL database for analysis. 

Manual data processing can be time-consuming and error-prone, this pipeline ensures reliable, repeatable, and scalable data ingestion and transformation.

---

## **How to Run This Project**
### **Clone the Repository**
```bash
git clone https://github.com/Ifyokoh/portfolio-projects.git
cd portfolio-projects/ETL-pipeline
```

### **Start the Docker Containers**
```bash
docker-compose up -d
```  
Access the **Airflow UI** at:  
🔗 [http://localhost:8080](http://localhost:8080)  

---

## **Project Structure**
```
ETL-pipeline/
│── dags/                    # Airflow DAGs
│   ├── simple_etl_dag.py    # Main DAG definition
|── airflow-dockerfile       # Dockerfile for Airflow setup
|── init-db.sql              # SQL script to initialize PostgreSQL database
│── docker-compose.yml       # Docker configuration
│── requirements.txt         # dependencies
```
---

## **Key Features**
- Automated DAG Scheduling – Airflow manages execution
- Containerized Workflow – Runs in Docker, ensuring consistency
- Parallel Task Execution – Scalable pipeline with Airflow Workers
- Database Storage – Saves processed data into PostgreSQL