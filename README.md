# Docker Observability Stack project

A containerised support ticket API with a full observability stack — monitoring, alerting, and load testing. Built to demonstrate Docker networking, volumes, and multi-container orchestration with Docker Compose.

## Architecture

![Screenshot](/screenshots/architecture_diagram.png)

## Tech Stack

- **Flask** — REST API for creating and retrieving support tickets
- **PostgreSQL** — persistent storage for ticket data
- **Prometheus** — metrics scraping and storage
- **Grafana** — real-time metrics visualisation
- **Alertmanager** — alert routing and notifications
- **Locust** — load testing and traffic simulation

## Prerequisites

- Docker
- Docker Compose

## Quick Start

```bash
git clone https://github.com/devrontombacco/docker-observability-stack
cd docker-observability-stack
docker-compose up --build
```

## Services

| Service      | URL                   | Description                |
| ------------ | --------------------- | -------------------------- |
| Flask API    | http://localhost:5000 | Support ticket API         |
| Prometheus   | http://localhost:9090 | Metrics and alerting rules |
| Grafana      | http://localhost:3000 | Metrics dashboards         |
| Alertmanager | http://localhost:9093 | Alert routing              |
| Locust       | http://localhost:8089 | Load testing UI            |

## Testing the Stack

**Create a ticket:**

Make a post request via the terminal

```bash
curl -X POST http://localhost:5000/tickets \
  -H "Content-Type: application/json" \
  -d '{"title": "Login broken", "description": "Cannot log in on mobile", "priority": "high", "status": "open", "language": "en"}'
```

**Get all tickets:**

```bash
curl http://localhost:5000/tickets
```

**Simulate load:**
Navigate to http://localhost:8089, set 10 users with a ramp up of 1 and click Start.

**Trigger an alert:**

```bash
docker stop
```

Watch the `FlaskAppDown` alert move from inactive → pending → firing in Prometheus at http://localhost:9090/alerts, and appear in Alertmanager at http://localhost:9093.

## Screenshots

Starting locust you will see data like this
![Screenshot](/screenshots/locust_traffic.png)

After starting locust you should see your traffic increase in Grafana like in the screenshot below
![Screenshot](/screenshots/grafana_traffic.png)

Prometheus will go from an inactive alert (nothing bad is happening)
![Screenshot](/screenshots/promehteus_inactive.png)

To a pending alert (meaning that it is about to fire)
![Screenshot](/screenshots/prometheus_pending.png)

And finally to a firing alert
![Screenshot](/screenshots/prometheus_firing.png)

The alert will also appear in Alert Manager like so
![Screenshot](/screenshots/alert_manager.png)

## Cleanup

` docker-compose down`

## License

This project is open source and available under the MIT License.

## Author

Devron:

- LinkedIn: [linkedin.com/in/devrontombacco](https://www.linkedin.com/in/devrontombacco/)
- Github: [github.com/devrontombacco](https://github.com/devrontombacco)
- Website: [dtcloudnetworking.com](https://dtcloudnetworking.com)
