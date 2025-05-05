## About the Project

This project sets up a **self-healing system** to automatically detect and remedy service outages. It uses:
- **Prometheus** for collecting metrics and monitoring service health.
- **Alertmanager** for processing alerts based on Prometheus rules.
- **Ansible** for executing automated recovery tasks such as restarting services.
- An optional **Python Flask webhook receiver** to bridge Alertmanager and Ansible.

The solution is designed to reduce downtime by immediately addressing issues as they occur.




*Features*
Service Monitoring: Track key service metrics and status.

Alerting: Define custom alert rules to detect service failures.

Automated Recovery: Use Ansible playbooks to fix issues immediately.

Scalability: Easily extend the system to monitor and remediate multiple services.

Documentation: Fully documented configurations and implementation steps.




*Prerequisites*
Operating System: Ubuntu 18.04/20.04 or any Linux distro.

Docker (Optional): To run some components in containers.

Python 3.6+ (if using the Flask webhook).

Ansible 2.9+

Prometheus 2.x

Alertmanager 0.21+

*Installation and Setup*
Clone the Repository


git clone repo link of --> self-healing-infrastructure.git
cd self-healing-infrastructure
Install Prometheus and Alertmanager

Download the respective binaries from Prometheus and Alertmanager.

Extract and follow the official documentation for configuration.

Set Up Ansible

Ensure Ansible is installed on your system.


sudo apt update
sudo apt install ansible
(Optional) Setup Flask Webhook Receiver

Navigate to the webhook directory (if provided) and install dependencies:


pip install -r requirements.txt
Run the webhook server:


python app.py







Run the playbook with:

*ansible-playbook playbook.yml*
Webhook Receiver
Ensure your webhook endpoint correctly triggers the Ansible playbook. The app.py should catch incoming alerts and call Ansible using a system call or similar method.

*Usage*
Start Prometheus & Alertmanager: Run their binaries with the configuration files provided.

Deploy the Flask Webhook Receiver: If you're using the Flask app to receive alerts.

Simulate a Failure: Stop a monitored service to trigger an alert.

Watch the Recovery: Verify that the Ansible playbook is automatically executed to restore the service.

*Testing*
Use controlled scenarios to simulate service downtime.

Check logs in Prometheus, Alertmanager, and Ansible to confirm that alerts are sent and recovery tasks are executed.

Validate that the service is automatically restarted after an incident.
