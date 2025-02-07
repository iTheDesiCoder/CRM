import json
import random
import string
from app.repository.task_repository import TaskRepository
from app.common.Model.task import TaskCreate, Task
from typing import List
from app.common.Utils.alert_mapping import AlertMapping


class TaskService:
    async def list_tasks(self):
        task_repository = TaskRepository()
        return await task_repository.get_all_tasks()

    async def add_task(self,task: TaskCreate):
        task_repository = TaskRepository()
        return await task_repository.create_task(task)

    async def update_task_in_cache(self, task_id: int, updated_task: TaskCreate) -> Task:
        task_repository = TaskRepository()
        tasks = await task_repository.get_all_tasks()

        # Find the task to update
        for task in tasks:
            if task.id == task_id:
                # Update task details
                task.subject = updated_task.subject
                task.description = updated_task.description
                task.publishDate = updated_task.publishDate
                task.accountNumber = updated_task.accountNumber
                task.clientName = updated_task.clientName
                task.policyNumber = updated_task.policyNumber
                task.status = updated_task.status
                task.priority = updated_task.priority

                # Update the cache with the modified task list

                await task_repository.update_cache(tasks)
                return task

        return None  # Task not found

    async def convert_and_save_task(self, alert_payload: dict) -> TaskCreate:
        # Extract necessary details from alert payload
        policy_number = alert_payload["TXLife"]["TXLifeRequest"]["OLifE"]["Holding"]["Policy"]["PolNumber"]
        message = alert_payload["TXLife"]["TXLifeRequest"]["OLifE"]["Holding"]["SystemMessage"][0]
        carrier_name = alert_payload["TXLife"]["TXLifeRequest"]["OLifE"]["Holding"]["Policy"]["CarrierName"]
        plan_name = alert_payload["TXLife"]["TXLifeRequest"]["OLifE"]["Holding"]["Policy"].get("PlanName", "N/A")
        message_code = int(message["MessageSeverityCode"])

        # Generate account number and client name
        account_number = self.generate_account_number()

        # Generate a more realistic client name
        client_name = self.generate_realistic_client_name()

        # Determine priority based on severity
        severity_code = int(message["MessageSeverityCode"])
        priority = "High" if severity_code == 1 else "Medium" if severity_code == 2 else "Low"

        # Get MessageDescription from Excel mapping
        message_description = AlertMapping.get_message_description(message_code)

        # Construct subject and description
        subject = f" Policy {policy_number}: {message_description}"
        description = (
            f"Alert received:\n"
            f"- Message: {message['MessageDescription']}\n"
            f"- Plan Name: {plan_name}\n"
            f"- Carrier Name: {carrier_name}\n"
            f"- Policy Number: {policy_number}\n"
        )

        # Construct TaskCreate model
        task_data = TaskCreate(
            subject=subject,
            description=description,
            publishDate=alert_payload["TXLife"]["TXLifeRequest"]["TransExeDate"],
            accountNumber=account_number,
            clientName=client_name,
            policyNumber=policy_number,
            status="New",
            priority=priority
        )

        task_repository = TaskRepository()
        # Save the task using the repository layer (in memory)
        return await task_repository.create_task(task_data)

    def generate_account_number(self) -> str:
        """Generate a random account number (XXX-XXXXXX-XXX format)."""
        return f"{random.randint(100, 999)}-{random.randint(100000, 999999)}-{random.randint(100, 999)}"

    def generate_random_string(self, length: int) -> str:
        """Generate a random string of the specified length."""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def generate_realistic_client_name(self) -> str:
        """Generate a realistic client name by combining a random first and last name."""
        first_names = [
            "Michael", "Sarah", "James", "Emily", "John", "Jessica",
            "David", "Sophia", "Daniel", "Olivia", "Matthew", "Emma"
        ]
        last_names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
            "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez"
        ]
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        return f"{first_name} {last_name}"